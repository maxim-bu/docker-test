from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from config import DATABASE_URL

engine = create_engine(DATABASE_URL, pool_recycle=3600, echo=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    from .models import Base
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    db = SessionLocal()