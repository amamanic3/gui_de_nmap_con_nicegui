from sqlalchemy import create_engine, event
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.config import settings

class Base(DeclarativeBase): pass

engine = create_engine(settings.database_url, connect_args={"check_same_thread": False} if settings.database_url.startswith("sqlite") else {})
if settings.database_url.startswith("sqlite"):
    @event.listens_for(engine, "connect")
    def _foreign_keys(dbapi_connection, _):
        dbapi_connection.execute("PRAGMA foreign_keys=ON")
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

def initialize_database() -> None:
    from pathlib import Path
    if settings.database_url.startswith("sqlite:///"):
        Path(settings.database_url.removeprefix("sqlite:///")).parent.mkdir(parents=True, exist_ok=True)
    from app.database import models
    from app.database.migrations import migrate
    Base.metadata.create_all(engine)
    migrate(engine)
