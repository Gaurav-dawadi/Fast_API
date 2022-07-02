from ..base_model import Base
from typing import Union

class User(Base):
    first_name: Union[str, None] = None
    last_name: Union[str, None] = None
    username: str
    email: str
    password: str