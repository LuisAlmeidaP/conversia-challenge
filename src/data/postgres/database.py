from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.data.postgres.Integration.model import IntegrationDB

class InstanceDataBase:
    def __init__(self, DATABASE_URL: str):
        self.DATABASE_URL = DATABASE_URL
        self._engine = create_engine(self.DATABASE_URL, echo=False)  # Cambia a create_engine
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self._engine)
        self.Base = declarative_base()

        self.Base.metadata.create_all(bind=self._engine)

        IntegrationDB.metadata.create_all(bind=self._engine)


    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()
