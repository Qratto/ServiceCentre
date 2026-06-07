from pydantic import BaseModel
from datetime import time

class ShiftCreate(BaseModel):
    title: str
    duration: time

class ShiftResponse(ShiftCreate):
    id: int

class ShiftEdit(BaseModel):
    title: str | None = None
    duration: time | None = None