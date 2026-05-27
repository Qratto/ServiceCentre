from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base

class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    id_client = Column(Integer, ForeignKey("client.id"), nullable=False)
    id_employee = Column(Integer, ForeignKey("employee.id"), nullable=False)
    registration_date = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    price = Column(Numeric(10, 2), nullable=False)
    status = Column(String(100), nullable=False)

    client = relationship("Client", back_populates="orders")
    employee = relationship("Employee", back_populates="orders")

    completed_services = relationship("CompletedService", back_populates="order")
    used_components = relationship("UsedComponent", back_populates="order")