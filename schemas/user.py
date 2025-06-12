from pydantic import BaseModel

class UserBase(BaseModel):
    name:str
    email:str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id:int
    is_active:bool=True


class Config:
    orm_mode= True
