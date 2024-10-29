from logging import log
from venv import logger

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.data.postgres.Integration.model import IntegrationDB


class IntegrationService:

    def __init__(self, db: AsyncSession):
        self.db = db


    async def get( self, integration_id: str )-> IntegrationDB:
        query = select(IntegrationDB).where( IntegrationDB.id == integration_id )
        result = await self.db.execute(query)
        print(result, 12)
        integration = result.scalars().first()

        if not integration:
            raise ValueError("Integration not found")
        return integration


