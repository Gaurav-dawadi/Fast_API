# from pydantic import BaseModel
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy import Column, Integer, Boolean, DateTime
from .database import Base


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    is_active = Column(Boolean)



