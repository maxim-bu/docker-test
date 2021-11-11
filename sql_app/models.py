from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer, String
)


Base = declarative_base()


class Person(Base):
    __tablename__ = 'Persons'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
