from pydantic import BaseModel

class ClientCreate(BaseModel):
    first_name: str
    last_name: str
    middle_name: str | None = None
    phone: str
    email: str

class ClientResponse(ClientCreate):
    id: int

class ClientEdit(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    middle_name: str | None = None
    phone: str | None = None
    email: str | None = None