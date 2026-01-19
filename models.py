from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    address: str
    dob: str
    gender: str
    email: str
    password: str
