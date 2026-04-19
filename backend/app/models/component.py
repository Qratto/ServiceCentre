from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class Component(Base):
    __tablename__ = "component"

    id_component = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    count = Column(Integer, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)

    characteristics_assoc = relationship("CharacteristicLink", back_populates="component")
    used_in_orders = relationship("UsedComponent", back_populates="component")


class UsedComponent(Base):
    __tablename__ = "used_component"

    id_used_component = Column(Integer, primary_key=True)
    id_order = Column(Integer, ForeignKey("order.id_order"), nullable=False)
    id_component = Column(Integer, ForeignKey("component.id_component"), nullable=False)
    used_count = Column(Integer, nullable=False)

    order = relationship("Order", back_populates="used_components")
    component = relationship("Component", back_populates="used_in_orders")