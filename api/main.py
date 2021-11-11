from typing import Optional, List

from fastapi import FastAPI, Depends
from sqlalchemy.orm.session import Session

from config import API_PATH, DATABASE_URL
from .dependences import get_db
from . import schemas
from services import persons
from sql_app import database


app = FastAPI(title="DockerTest", openapi_prefix=API_PATH)


@app.get('/ping/', tags=['Debug'])
def ping():
    return "pong"

@app.post('/initdb/')
def init_db():
    database.init_db()
    return True

@app.get('/env/')
def test_env():
    return DATABASE_URL

@app.get(
    '/persons/',
    tags=['Persons'],
    response_model=List[schemas.Person]
)
def get_persons_list(
    db: Session = Depends(get_db)
):
    return persons.get_persons(db)

@app.post(
    '/persons/',
    tags=['Persons'],
    response_model=schemas.Person
)
def create_person(
    params: schemas.PersonCreate,
    db: Session = Depends(get_db)
):
    return persons.create_person(db, params)

@app.get('/new/')
def new_test():
    return 'HELLO'