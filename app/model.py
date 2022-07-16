from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base

class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, nullable=False)
    kazakh = Column(String, nullable=False)
    russian = Column(String, nullable=False)
    who_added = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    identification = Column(String, nullable=False, unique=True)
    username = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))