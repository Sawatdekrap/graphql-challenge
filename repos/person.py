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
        )
    ]
