# GraphQL API Challenge

## Overview

This repo contains an API that exposes a GraphQL query endpoint for mocked data representing people and addresses.

The data (and corresponding GraphQL query) is structured in the following way:

```
people {
    email
    name
    address {
        number
        street
        city
        state
    }
}
```

## Setup

This API uses Python (developed with Python 3.11.0), and can be set up with the following terminal commands:

```bash
$ python --version
Python 3.11.0
$ python -m venv venv
...
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
...
```

## Running the server

```bash
(venv) $ uvicorn server:app
INFO:     Started server process [46202]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
...
```

There are several options for sending queries to the GraphQL API endpoint, some of which are listed below:

### Curl

Users can use the `curl` tool to send a POST HTTP request with a GraphQL query to the API. For example:

```bash
$ curl "http://localhost:8000/graphql" \
    -H "Content-Type: application/json" \
    -d '{"query": "query{people{address{state}}}"}'
{"data": {"people": [{"address": {"state": "NSW"}}, {"address": {"state": "QLD"}}, {"address": {"state": "WA"}}]}}
```

### GraphiQL

The API has an interactive GraphQL query editor webpage that can be accessed via browser at `http://localhost:8000/graphql`

## Tests

Test files are located in the `/tests` directory, and are run using pytest.

```bash
(venv) $ pytest tests
...
```

## Additional Resources

[FastAPI Documentation](https://fastapi.tiangolo.com/)

[Strawberry Documentation](https://strawberry.rocks/)

[GraphQL Documentation](https://graphql.org/)
