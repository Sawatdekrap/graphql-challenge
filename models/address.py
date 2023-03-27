from pydantic import BaseModel
from constants.state import State


class Address(BaseModel):
    number: int
    street: str
    city: str
    state: State
