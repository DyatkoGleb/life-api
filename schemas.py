from pydantic import BaseModel
from datetime import date

class DiaryDay(BaseModel):
    id: int = None
    date: date
    location: str = None
    location_on_map: str = None
    preview_text: str = None
    text: str