from app.db.session import AsyncSession
from app.lib.entities.event import Event
from app.lib.model_repository import ModelRepository


class EventRepository(ModelRepository[Event]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session=session, model=Event)
        self.session = session
        self.model = Event
