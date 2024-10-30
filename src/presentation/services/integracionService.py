
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from src.data.postgres.Integration.model import IntegrationDB


class IntegrationService:

    def __init__(self, db: Session):
        self.db = db

    def get(self, integration_id: str) -> IntegrationDB:
        query = select(IntegrationDB).where(IntegrationDB.id == integration_id)
        result = self.db.execute(query)
        integration = result.scalars().first()
        if not integration:
            raise ValueError("Integration not found")
        return integration

    def create(self, integrationDto ) -> IntegrationDB:
        pass


