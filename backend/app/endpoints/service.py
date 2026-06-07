from fastapi import APIRouter
from fastapi.params import Depends
from app.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.base import BaseRepository
from app.schemas.service import ServiceCreate, ServiceResponse, ServiceEdit
from app.models import Service

service_router = APIRouter(prefix="/services", tags=["service"])


@service_router.get("/", response_model=list[ServiceResponse])
async def get_services(session: AsyncSession = Depends(get_db)):
    base_repository = BaseRepository(Service, session)
    services = await base_repository.find_all()
    return services

@service_router.get("/{id}", response_model=ServiceResponse)
async def get_service(id: int, session: AsyncSession = Depends(get_db)):
    base_repository = BaseRepository(Service, session)
    service = await base_repository.find_by(id)
    return service

@service_router.post("/", response_model=ServiceResponse)
async def post_service(service_data: ServiceCreate, session: AsyncSession = Depends(get_db)):
    base_repository = BaseRepository(Service, session)
    service = await base_repository.create(service_data)
    return service


@service_router.patch("/", response_model=ServiceResponse)
async def edit_service(service_data: ServiceEdit, id: int, session: AsyncSession = Depends(get_db)):
    base_repository = BaseRepository(Service, session)
    service = await base_repository.edit(service_data, id)
    return service


@service_router.delete("/{id}")
async def delete_service(id: int, session: AsyncSession = Depends(get_db)):
    base_repository = BaseRepository(Service, session)
    result = await base_repository.delete(id)
    return result