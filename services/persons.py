from sqlalchemy.orm import Session

from api import schemas
from sql_app import models

def get_persons(db: Session):
    return db.query(models.Person).all()

def create_person(db: Session, params: schemas.PersonCreate):
    new_person = models.Person(**params.dict())
    db.add(new_person)
    db.commit()
    return new_person