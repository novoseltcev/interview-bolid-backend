from sqlalchemy import Column, Float, Integer, String

from .mixins import BaseModelMixin


class Event(BaseModelMixin):
    """Model for a country."""

    __tablename__ = "events"

    sensor_type = Column(Integer, nullable=False)
    name = Column(String, nullable=True)
    temperature = Column(Float, nullable=True)
    humidity = Column(Float, nullable=True)
