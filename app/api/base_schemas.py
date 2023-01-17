from typing import Any, Generic, TypeVar

from fastapi import Query
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, ValidationError
from pydantic.error_wrappers import ErrorWrapper
from pydantic.generics import GenericModel
from pydantic.utils import to_lower_camel

DataT = TypeVar("DataT")
MetaT = TypeVar("MetaT")


class BaseSchema(BaseModel):
    class Config:
        alias_generator = to_lower_camel
        allow_population_by_field_name = True
        orm_mode = True

    @classmethod
    def from_orm_list(cls, entities: list[DataT]) -> list:
        return [cls.from_orm(entity) for entity in entities]  # type: ignore


class Error(BaseSchema):
    type: str
    msg: str
    body: dict | None = None


class PageMeta(BaseSchema):
    page: int
    total: int
    per_page: int


class Response(GenericModel, Generic[DataT]):
    data: DataT


class ResponseWithMeta(GenericModel, Generic[DataT, MetaT]):
    data: DataT
    meta: MetaT


class ResponseList(GenericModel, Generic[DataT]):
    data: list[DataT]
    meta: PageMeta


class FailureResponse(BaseModel):
    errors: list[Error]


class QueryModel(BaseSchema):
    def __init__(self, **kwargs: Any) -> None:
        try:
            super().__init__(**kwargs)
        except ValidationError as e:
            raise RequestValidationError(
                [
                    ErrorWrapper(
                        exc=e,
                        loc=("query",) + error["loc"],
                    )
                    for error in e.errors()
                ]
            ) from e


class Pagination(QueryModel):
    page: int = Query(ge=1, example=1)
    per_page: int = Query(ge=2, le=100, example=10)
