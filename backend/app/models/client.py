from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

class Client(Base):
    __tablename__ = "client"

    id_client = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    middle_name = Column(String(100), nullable=True)
    phone = Column(String(20), nullable=False)
    email = Column(String(255), nullable=False)

    orders = relationship("Order", back_populates="client")