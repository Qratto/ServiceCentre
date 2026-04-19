from sqlalchemy import Column, Integer, String, Time
from sqlalchemy.orm import relationship

from app.database import Base

class Shift(Base):
    __tablename__ = "shift"

    id_shift = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    duration = Column(Time, nullable=False)

    work_schedules = relationship("WorkSchedule", back_populates="shift")