from pydantic import BaseModel
from datetime import date


class EventBase(BaseModel):
    title:str
    location:str
    date: date


class EventCreate(EventBase):
    pass

class Event(EventBase):
    id:int
    is_open:bool=True

class Config:
    orm_mode =True
