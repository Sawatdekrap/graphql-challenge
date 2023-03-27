from fastapi.testclient import TestClient
import pytest
from http import HTTPStatus
from server import app


client = TestClient(app)


@pytest.mark.parametrize(
    "query,expected_fields",
    [
        # Simple query with person's email
        (r"query{people{email}}", ["email"]),
        # Simple query with person's name
        (r"query{people{name}}", ["name"]),
        # Query with person's address state
        (r"query{people{address{state}}}", ["address.state"]),
        # Full Query
        (
            r"query{people{email,name,address{number,street,city,state}}}",
            [
                "email",
                "name",
                "address.number",
                "address.street",
                "address.city",
                "address.state",
            ],
        ),
    ],
)
def test_graphql_fields(query: str, expected_fields: list[str]):
    response = client.post("/graphql", json={"query": query})

    assert response.status_code == HTTPStatus.OK

    response_data = response.json()
    graphql_data = response_data.get("data")
    assert isinstance(graphql_data, dict)
    people = graphql_data.get("people")
    assert isinstance(people, list)

    for person in people:
        for field in expected_fields:
            assert _is_field_in_data(person, field), f"Field '{field}' not in {person}"


def _is_field_in_data(data: dict, field: str) -> bool:
    field_parts = field.split(".")
    sub_data = data
    for part in field_parts:
        sub_data = sub_data.get(part)
        if sub_data is None:
            return False

    return sub_data is not None
