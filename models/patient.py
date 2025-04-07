from sqlalchemy import Column, Integer, String, ForeignKey
from database.database import Base

class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))
