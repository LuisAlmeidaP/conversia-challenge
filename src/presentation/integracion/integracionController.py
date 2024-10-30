import fastapi
from fastapi import APIRouter, Depends, HTTPException,Request
from sqlalchemy.orm import Session

from src.data.postgres.database import InstanceDataBase
from sqlalchemy.ext.asyncio import AsyncSession

from src.presentation.services.integracionService import IntegrationService

IntegrationRouter = APIRouter()

async def get_db(request: Request) -> AsyncSession:
    database: InstanceDataBase = request.app.state.database
    db = next(database.get_db())
    try:
        yield db
    finally:
        db.close()

@IntegrationRouter.get('/{integration_id}')
async def get_integration( integration_id: str, db: Session = Depends(get_db) ):
    service = IntegrationService(db)

    try:
        integration_get = service.get( integration_id )
        return integration_get
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str( error ))
