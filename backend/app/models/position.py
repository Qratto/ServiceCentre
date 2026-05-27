from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from app.database import Base

class Position(Base):
    __tablename__ = "positions"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    payment_ration = Column(Float, nullable=False)

    employee_positions = relationship("EmployeePosition", back_populates="position")