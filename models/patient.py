from pydantic import BaseModel
from typing import Optional

class PatientModel(BaseModel):
    name: str
    age: int
    gender: str
    condition: Optional[str] = ""
    image_url: Optional[str] = ""

class UpdatePatientModel(BaseModel):
    name: Optional[str]
    age: Optional[int]
    gender: Optional[str]
    condition: Optional[str]
    image_url: Optional[str]