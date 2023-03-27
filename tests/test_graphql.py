from fastapi.testclient import TestClient
from server import app


client = TestClient(app)


def test_graphql_fields():
    pass
