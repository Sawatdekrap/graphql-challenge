from fastapi import APIRouter


router = APIRouter(prefix="/graphql")


@router.get("")
async def root():
    return "GraphQL route"
