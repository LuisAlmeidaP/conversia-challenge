import fastapi
from fastapi import APIRouter, Depends, HTTPException,Request
from src.data.postgres.database import InstanceDataBase
from sqlalchemy.ext.asyncio import AsyncSession

from src.presentation.services.integracionService import IntegrationService

IntegrationRouter = APIRouter()

async def get_db(request: Request) -> AsyncSession:
    database: InstanceDataBase = request.app.state.database
    async with database.Session() as session:
        yield session

@IntegrationRouter.get('/{integration_id}')
async def get_integration(integration_id: str, db: AsyncSession = Depends(get_db)):
    service = IntegrationService(db)

    try:
        integration_get = await service.get(integration_id)
        return integration_get
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
