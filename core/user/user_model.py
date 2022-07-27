from ..base_model import BaseModel
from sqlalchemy import Column, Integer, String

class User(BaseModel):
    __tablename__ ="users"
    
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    username = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String, index=True)

    def __repr__(self) -> str:
        return f"User(username={self.username!r})"