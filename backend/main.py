from fastapi import FastAPI
from contextlib import asynccontextmanager

from starlette.responses import RedirectResponse

from app.database import engine, Base
from app.models import *
from app.endpoints.employee import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    print("База данных пересоздана")

    yield

    # async with engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.drop_all)
    #
    # print("Таблицы удалены")
    await engine.dispose()

app = FastAPI(lifespan=lifespan)
app.include_router(router)

@app.get("/")
def root():
    return RedirectResponse("/docs")
