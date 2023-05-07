from pydantic import BaseModel
from datetime import date

class DiaryDay(BaseModel):
    id: int = None
    date: date
    place: str = None
    plase_on_map: str = None
    previewText: str = None
    text: str