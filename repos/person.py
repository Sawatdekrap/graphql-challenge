from models.person import Person
from models.address import Address
from constants.state import State


def get_people() -> list[Person]:
    return [
        Person(
            email="abc123@gmail.com",
            name="abc123 gmail",
            address=Address(
                number=1,
                street="Street St",
                city="Sydney",
                state=State.NSW,
            ),
        ),
        Person(
            email="persontwo@gmail.com",
            name="person two",
            address=Address(
                number=2,
                street="Second Road",
                city="Brisbane",
                state=State.QLD,
            ),
        ),
        Person(
            email="bigboss@hotmail.com",
            name="Big Boss",
            address=Address(
                number=99,
                street="Zzz Parade",
                city="Perth",
                state=State.WA,
            ),
        ),
    ]
