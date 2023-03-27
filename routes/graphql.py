import strawberry
from strawberry.fastapi import GraphQLRouter
from repos.person import get_people
from constants.state import State


@strawberry.type
class Address:
    number: int
    street: str
    city: str
    state: strawberry.enum(State)


@strawberry.type
class Person:
    email: str
    name: str
    address: Address


@strawberry.type
class Query:
    people: list[Person] = strawberry.field(resolver=get_people)


schema = strawberry.Schema(query=Query)
router = GraphQLRouter(schema)
