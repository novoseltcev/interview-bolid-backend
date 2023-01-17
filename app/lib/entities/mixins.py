from sqlalchemy import Column, Integer, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class IDMixin(Base):
    """Single PK as id"""

    __abstract__ = True

    id = Column(
        Integer,
        primary_key=True,
        server_default=text('1'),
        nullable=False,
        index=True,
    )


class BaseModelMixin(IDMixin):
    """Combining model system info"""

    __abstract__ = True
