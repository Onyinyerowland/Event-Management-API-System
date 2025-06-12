from pydantic import BaseModel


class SpeakerBase(BaseModel):
    name:str
    topic:str

class Speaker(SpeakerBase):
    id:int
