from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from app.database import Base

class Employee(Base):
    __tablename__ = "employee"

    id_employee = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    middle_name = Column(String(100), nullable=True)
    phone = Column(String(20), nullable=False)
    role = Column(String(100), nullable=False)

    work_schedules = relationship("WorkSchedule", back_populates="employee")
    employee_positions = relationship("EmployeePosition", back_populates="employee")
    orders = relationship("Order", back_populates="employee")


class WorkSchedule(Base):
    __tablename__ = "work_schedule"

    id_work_schedule = Column(Integer, primary_key=True)
    id_employee = Column(Integer, ForeignKey("employee.id_employee"), nullable=False)
    id_shift = Column(Integer, ForeignKey("shift.id_shift"), nullable=False)
    scheduled_date = Column(Date, nullable=False)

    employee = relationship("Employee", back_populates="work_schedules")
    shift = relationship("Shift", back_populates="work_schedules")


class EmployeePosition(Base):
    __tablename__ = "employee_position"

    id_employee_position = Column(Integer, primary_key=True)
    id_positions = Column(Integer, ForeignKey("positions.id_positions"), nullable=False)
    id_employee = Column(Integer, ForeignKey("employee.id_employee"), nullable=False)

    position = relationship("Position", back_populates="employee_positions")
    employee = relationship("Employee", back_populates="employee_positions")