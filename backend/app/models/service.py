from sqlalchemy import Column, Integer, String, Text, Numeric, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class Service(Base):
    __tablename__ = "service"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Numeric(10, 2), nullable=False)

    completed_services = relationship("CompletedService", back_populates="service")


class CompletedService(Base):
    __tablename__ = "completed_service"

    id = Column(Integer, primary_key=True)
    id_order = Column(Integer, ForeignKey("order.id"), nullable=False)
    id_service = Column(Integer, ForeignKey("service.id"), nullable=False)

    order = relationship("Order", back_populates="completed_services")
    service = relationship("Service", back_populates="completed_services")