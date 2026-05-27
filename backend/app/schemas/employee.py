from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    phone: str
    role: str

class EmployeeResponse(EmployeeCreate):
    id: int

class EmployeeEdit(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    middle_name: str | None = None
    phone: str | None = None
    role: str | None = None

class EmployeeAccount(BaseModel):
    username: str
    password_hash: str
