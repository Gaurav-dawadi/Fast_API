from ..base_model import Base
from typing import Union
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ ="users"
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    username = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String, index=True)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r})"