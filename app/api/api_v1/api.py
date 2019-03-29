from fastapi import APIRouter

from api.api_v1.endpoints import user, token

api_router = APIRouter()
api_router.include_router(user.router)
api_router.include_router(token.router)