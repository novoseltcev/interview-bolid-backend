from typing import Iterable

from fastapi import Depends

from app.api.base_schemas import PageMeta
from app.api.events.repository import Event, EventRepository
from app.api.events.schemas import EventSchema
from app.db.session import AsyncSession, get_session


def get_repository(
    session: AsyncSession = Depends(get_session),
) -> EventRepository:
    return EventRepository(session=session)


class EventService:
    def __init__(
        self,
        repository: EventRepository = Depends(get_repository),
    ) -> None:
        self.repository = repository

    async def get_all(
        self, *, page: int, per_page: int
    ) -> tuple[Iterable[Event], PageMeta]:
        async with self.repository:
            data, total = await self.repository.select_page(
                page=page, page_length=per_page
            )
            await self.repository.commit()
            return data, PageMeta(page=page, per_page=per_page, total=total)

    async def create(self, data: EventSchema) -> None:
        async with self.repository:
            await self.repository.insert(Event(**data.dict()))
            await self.repository.commit()
