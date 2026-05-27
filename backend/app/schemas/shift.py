from pydantic import BaseModel
from datetime import time

class ShiftCreate(BaseModel):
    title: str
    duration: time

class ShiftResponse(ShiftCreate):
    id_shift: int

class ShiftEdit(BaseModel):
    title: str | None = None
    duration: str | None = None