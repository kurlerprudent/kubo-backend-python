
from pydantic import BaseModel
from typing import List

class Patient(BaseModel):
    id: int
    name: str
    age: int
    user_id: int
    class Config:
        orm_mode = True

class PatientList(BaseModel):
    patients: List[Patient]
