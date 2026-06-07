from fastapi import APIRouter
from fastapi.params import Depends
from app.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.base import BaseRepository
from app.schemas.client import ClientCreate, ClientEdit, ClientResponse
from app.models import Client

client_router = APIRouter(prefix="/clients", tags=["client"])


@client_router.get("/", response_model=list[ClientResponse])
async def get_clients(session: AsyncSession = Depends(get_db)):
    base_repository = BaseRepository(Client, session)
    clients = await base_repository.find_all()
    return clients

@client_router.get("/{id}", response_model=ClientResponse)
async def get_client(id: int, session: AsyncSession = Depends(get_db)):
    base_repository = BaseRepository(Client, session)
    client = await base_repository.find_by(id)
    return client

@client_router.post("/", response_model=ClientResponse)
async def post_client(client_data: ClientCreate, session: AsyncSession = Depends(get_db)):
    base_repository = BaseRepository(Client, session)
    client = await base_repository.create(client_data)
    return client


@client_router.patch("/", response_model=ClientResponse)
async def edit_client(client_data: ClientEdit, id: int, session: AsyncSession = Depends(get_db)):
    base_repository = BaseRepository(Client, session)
    client = await base_repository.edit(client_data, id)
    return client


@client_router.delete("/{id}")
async def delete_client(id: int, session: AsyncSession = Depends(get_db)):
    base_repository = BaseRepository(Client, session)
    result = await base_repository.delete(id)
    return result