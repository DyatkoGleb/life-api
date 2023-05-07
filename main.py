from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import DiaryDay
import json
import os


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


pathDiary = 'diary.json'


def is_file_exist(path) -> bool:
    return False if not os.path.exists(path) else True

def is_file_empty(path) -> bool:
    return True if os.stat(path).st_size == 0 else False

def get_file_data(path) -> dict:
    with open(path, 'r') as file:
        return json.load(file)


@app.post('/adddiaryday')
def add_diary_day(item: DiaryDay):
    try:
        if not is_file_exist(pathDiary) or is_file_empty(pathDiary):
            with open(pathDiary, 'w') as write_file:
                json.dump({}, write_file)

        data = get_file_data(pathDiary)

        item.id = field_id = int(max(list(data.keys())))+1 if data else 1
        data[field_id] = item.dict()

        with open(pathDiary, 'w') as write_file:
            json_str = json.dumps(data, default=str)
            write_file.write(json_str)

        return data[field_id]
    except Exception as err:
        return err

@app.get('/getdiaryday')
def get_diary_day(id: str):
    try:
        if not is_file_exist(pathDiary) or is_file_empty(pathDiary):
            return {}
        else:
            return get_file_data(pathDiary)[id]
    except Exception as err:
        return err

@app.get('/getalldiarydays')
def get_all_diary_days():
    try:
        if not is_file_exist(pathDiary) or is_file_empty(pathDiary):
            return {}
        else:
            return get_file_data(pathDiary)
    except Exception as err:
        return err