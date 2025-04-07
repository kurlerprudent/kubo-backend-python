from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    password: str

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    class Config:
        orm_mode = True
