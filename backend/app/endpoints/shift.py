from fastapi import APIRouter
from fastapi.params import Depends
from app.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.base import BaseRepository
from app.schemas.shift import ShiftCreate, ShiftResponse, ShiftEdit
from app.models import Shift

shift_router = APIRouter(prefix="/shifts", tags=["shift"])


@shift_router.get("/", response_model=list[ShiftResponse])
async def get_shifts(session: AsyncSession = Depends(get_db)):
    base_repository = BaseRepository(Shift, session)
    shifts = await base_repository.find_all()
    return shifts

@shift_router.get("/{id}", response_model=ShiftResponse)
async def get_shift(id: int, session: AsyncSession = Depends(get_db)):
    base_repository = BaseRepository(Shift, session)
    shift = await base_repository.find_by(id)
    return shift

@shift_router.post("/", response_model=ShiftResponse)
async def post_shift(shift_data: ShiftCreate, session: AsyncSession = Depends(get_db)):
    base_repository = BaseRepository(Shift, session)
    shift = await base_repository.create(shift_data)
    return shift


@shift_router.patch("/", response_model=ShiftResponse)
async def edit_shift(shift_data: ShiftEdit, id: int, session: AsyncSession = Depends(get_db)):
    base_repository = BaseRepository(Shift, session)
    shift = await base_repository.edit(shift_data, id)
    return shift


@shift_router.delete("/{id}")
async def delete_shift(id: int, session: AsyncSession = Depends(get_db)):
    base_repository = BaseRepository(Shift, session)
    result = await base_repository.delete(id)
    return result