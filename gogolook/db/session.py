from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from gogolook.config import Settings


def get_session(settings: Settings):

    engine = create_engine(settings.DATABASE_URI, pool_pre_ping=True)
    SessionLocal = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )
    return SessionLocal()
