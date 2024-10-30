from datetime import datetime
from http.client import responses

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from src.data.postgres.Integration.model import IntegrationDB
from src.domain.dto.integration.IntegracionDTO import CreateIntegrationDto
from src.domain.dto.SMS.smsDTO import CreateSMSDto
from src.config.envs import Envs

import httpx

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

    def create(self, createintegration: CreateIntegrationDto ) -> IntegrationDB :

        integration = IntegrationDB(
            name=           createintegration.name,
            description=    createintegration.description,
            endpoint=       str(createintegration.endpoint),
            created=        datetime.utcnow(),
            updated=        datetime.utcnow(),
            access_token=   createintegration.access_token
        )

        self.db.add(integration)
        self.db.commit()
        self.db.refresh(integration)

        return integration

    async def sendsms( self, integration_id, create_sms: CreateSMSDto ):

        integration = self.get( integration_id )

        if integration:

            template_body = {
                "to": create_sms.to,
                "From": create_sms.from_number,
                "Body": create_sms.body
            }

            end_point = f"{integration.endpoint}/{ Envs.TWILIO_ACCOUNT_SID }/Messages.json"

            async with httpx.AsyncClient() as client:
                response = await client.post(
                    end_point,
                    headers={"Authorization": f"Bearer {integration.access_token}"},
                    data = template_body
                )
            return response.json()


