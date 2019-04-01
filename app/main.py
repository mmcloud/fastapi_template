from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request

from api.api_v1.api import api_router
from core import config
from db.session import Session


app = FastAPI(__name__, title=config.PROJECT_NAME, openapi_url="/api/v1/openapi.json")


app.include_router(api_router, prefix=config.API_V1_STR)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = Session()
    response = await call_next(request)
    request.state.db.close()
    return response