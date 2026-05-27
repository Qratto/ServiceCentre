from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class Characteristic(Base):
    __tablename__ = "characteristic"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    value = Column(String(255), nullable=False)

    component_links = relationship("CharacteristicLink", back_populates="characteristic")


class CharacteristicLink(Base):
    __tablename__ = "characteristics"

    id = Column(Integer, primary_key=True)
    id_component = Column(Integer, ForeignKey("component.id"), nullable=False)
    id_characteristic = Column(Integer, ForeignKey("characteristic.id"), nullable=False)

    component = relationship("Component", back_populates="characteristics_assoc")
    characteristic = relationship("Characteristic", back_populates="component_links")