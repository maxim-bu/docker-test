from sql_app.database import Session, SessionLocal

def get_db() -> Session:
    "Функция для получеиния сессии для работы с БД"
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()