from pydantic import BaseModel
from datetime import date

class DiaryDay(BaseModel):
    date: date
    place: str = None
    plase_on_map: str = None
    text: str