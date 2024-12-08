import uuid

from sqlalchemy import BIGINT, Column, VARCHAR
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_tg = Column(BIGINT, nullable=False, unique=True)
    education_id = Column(BIGINT, nullable=True)
    group_id = Column(BIGINT, nullable=True)
    jwt_token = Column(VARCHAR, nullable=True)
