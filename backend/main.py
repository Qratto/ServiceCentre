from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.endpoints.client import client_router
from seed_database import seed_database
from starlette.responses import RedirectResponse

from app.database import engine, Base
from app.models import *
from app.endpoints.employee import employee_router
from app.endpoints.shift import shift_router
from app.endpoints.auth import auth_router
from app.endpoints.service import service_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    await seed_database()

    print("База данных пересоздана")

    yield

    await engine.dispose()

app = FastAPI(lifespan=lifespan)

app.include_router(employee_router)
app.include_router(shift_router)
app.include_router(auth_router)
app.include_router(service_router)
app.include_router(client_router)

@app.get("/")
def root():
    return RedirectResponse("/docs")