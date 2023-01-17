from typing import Optional

from pydantic import Field

from app.api.base_schemas import BaseSchema


class EventSchema(BaseSchema):
    sensor_type: int = Field(alias="Sensor_type")
    id: int = Field(alias="num")
    name: Optional[str]
    temperature: Optional[float]
    humidity: Optional[float]
