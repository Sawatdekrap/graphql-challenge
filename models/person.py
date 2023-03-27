from pydantic import BaseModel
from .address import Address


class Person(BaseModel):
    email: str
    name: str
    address: Address
