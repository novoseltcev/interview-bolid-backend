from uuid import UUID as UUID4
from uuid import uuid4

from sqlalchemy import Column, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UUIDMixin(Base):
    """Single PK as uuid"""

    __abstract__ = True

    uuid: UUID4 = Column(
        UUID(as_uuid=True),
        default=uuid4,
        server_default=text("gen_random_uuid()"),
        primary_key=True,
        index=True,
    )


class BaseModelMixin(UUIDMixin):
    """Combining model system info"""

    __abstract__ = True
