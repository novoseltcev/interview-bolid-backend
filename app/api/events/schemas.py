from typing import Optional

from app.api.base_schemas import BaseModel


class EventSchema(BaseModel):
    sensor_type: int
    num: int
    name: Optional[str]
    temperature: Optional[float]
    humidity: Optional[float]
