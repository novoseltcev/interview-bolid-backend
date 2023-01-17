from __future__ import annotations

from abc import ABC
from collections.abc import Iterable
from typing import Any, Generic, Type, TypeVar

from sqlalchemy import func, literal, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import Select

from app.lib.entities.mixins import Base

BaseT = TypeVar("BaseT", bound=Base)


class Repository(ABC, Generic[BaseT]):
    """Base generic repository, that must be inherited in your realization."""

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def __aenter__(self) -> Repository:
        """Async context manager for transaction"""
        await self.session.begin()
        return self

    async def __aexit__(
        self, exc_type: Type[Exception], exc_val: Any, exc_tb: Any
    ) -> None:
        if exc_type:
            await self.rollback()

        await self.session.close()

    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        await self.session.rollback()

    async def _paginate(
        self, *, stm: Select, page: int, page_length: int
    ) -> tuple[Iterable[BaseT], int]:
        result = await self.session.execute(
            stm.offset((page - 1) * page_length).limit(page_length)
        )
        count = await self.session.execute(
            select(func.count(literal("*"))).select_from(stm)
        )
        return (
            result.unique().scalars().all(),
            int(count.scalar()),
        )

    async def insert(self, entity: BaseT) -> None:
        self.session.add(entity)

    async def merge(self, entity: BaseT) -> BaseT | None:
        return await self.session.merge(entity)

    async def refresh(self, entity: BaseT) -> None:
        await self.session.refresh(entity)

    @staticmethod
    def _to_dict(entity: BaseT) -> dict[str, Any]:
        return {
            key: value for key, value in entity.__dict__.items() if key[:4] != "_sa_"
        }
