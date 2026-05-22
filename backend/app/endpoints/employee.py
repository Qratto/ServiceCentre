from fastapi import APIRouter
from fastapi.params import Depends
from app.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.base import BaseRepository
from app.schemas.employee import EmployeeCreate, EmployeeResponse, EmployeeEdit
from app.models import Employee

router = APIRouter(prefix="/employees", tags=["employee"])


@router.get("/", response_model=list[EmployeeResponse])
async def get_employees(session: AsyncSession = Depends(get_db)):
    base_repository = BaseRepository(Employee, session)
    employees = await base_repository.find_all()
    return employees

@router.get("/{id}", response_model=EmployeeResponse)
async def get_employee(id: int, session: AsyncSession = Depends(get_db)):
    base_repository = BaseRepository(Employee, session)
    employee = await base_repository.find_by(id)
    return employee

@router.post("/", response_model=EmployeeResponse)
async def post_employee(employee_data: EmployeeCreate, session: AsyncSession = Depends(get_db)):
    base_repository = BaseRepository(Employee, session)
    employee = await base_repository.create(employee_data)
    print(employee.__dict__)
    return employee


@router.patch("/")
async def edit_employee(employee_data: EmployeeEdit, id: int, session: AsyncSession = Depends(get_db)):
    base_repository = BaseRepository(Employee, session)
    employee = await base_repository.edit(employee_data, id)
    return employee


@router.delete("/{id}")
async def delete_employee(id: int, session: AsyncSession = Depends(get_db)):
    base_repository = BaseRepository(Employee, session)
    result = await base_repository.delete(id)
    return result



