from typing import Union
from ..base_model import Base

class BlogModel(Base):
    title: str
    description: Union[str, None] = None
