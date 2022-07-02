from pydantic import BaseModel

class Base(BaseModel):
    id: int
    created_at: str
    updated_at: str
    is_active: bool = True