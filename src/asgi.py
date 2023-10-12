from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from src.api.urls import add_routes
from src.db import database


def create_app(init_db: bool = True) -> FastAPI:
    _app = FastAPI()

    if init_db:
        database.init_db()

        @asynccontextmanager
        async def lifespan(_app: FastAPI):
            yield
            if database._engine is not None:
                await database.close()

    add_routes(_app)

    return _app


app = create_app()

if __name__ == '__main__':
    uvicorn.run(app)
