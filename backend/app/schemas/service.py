from pydantic import BaseModel

class ServiceCreate(BaseModel):
    name: str
    description: str
    price: int

class ServiceResponse(ServiceCreate):
    id: int

class ServiceEdit(BaseModel):
    name: str | None = None
    description: str | None = None
    price: int | None = None
