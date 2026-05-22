from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    phone: str
    role: str

class EmployeeResponse(EmployeeCreate):
    id_employee: int

class EmployeeEdit(BaseModel):
    first_name: str | None
    last_name: str | None
    middle_name: str | None
    phone: str | None
    role: str | None