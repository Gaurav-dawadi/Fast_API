# from pydantic import BaseModel
from sqlalchemy.ext.declarative import as_declarative


@as_declarative()
class Base:
    id: int
    created_at: str
    updated_at: str
    is_active: bool = True
    
    # __name__: str
    # Generate __tablename__ automatically
    # @declared_attr
    # def __tablename__(cls) -> str:
    #     return cls.__name__.lower()


