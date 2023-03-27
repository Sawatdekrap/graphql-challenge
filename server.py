from typing import Union

from fastapi import FastAPI
from routes.graphql import router as graphql_router

app = FastAPI()

app.include_router(graphql_router, prefix="/graphql")
