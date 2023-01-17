from __future__ import annotations

from collections.abc import Iterable
from typing import Generic, Type, TypeVar
from uuid import UUID

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.lib.entities.mixins import BaseModelMixin
from app.lib.repository import Repository

ModelT = TypeVar("ModelT", bound=BaseModelMixin)


class ModelRepository(Repository[ModelT], Generic[ModelT]):
    """Base generic repository, that must be inherited in your realization."""

    def __init__(self, session: AsyncSession, model: Type[BaseModelMixin]) -> None:
        super().__init__(session=session)
        self.model = model

    async def select_page(
        self, page: int, page_length: int
    ) -> tuple[Iterable[ModelT], int]:
        return await self._paginate(
            stm=select(self.model),
            page=page,
            page_length=page_length,
        )

    async def select_by_uuid(self, id: int) -> ModelT | None:
        return await self.session.get(entity=self.model, ident=id)  # type: ignore

    async def delete(self, uuid: UUID) -> None:
        await self.session.execute(delete(self.model).where(self.model.id == id))

    async def update(self, entity: ModelT) -> ModelT | None:
        await self.session.execute(
            update(self.model)
            .where(self.model.uuid == entity.id)
            .values(**self._to_dict(entity))
        )
        return await self.select_by_uuid(entity.id)
