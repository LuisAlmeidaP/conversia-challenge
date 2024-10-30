from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from src.domain.dto.SMS.smsDTO import CreateSMSDto
from src.domain.helpers.get_bearer_token import get_bearer_token
from src.data.postgres.database import InstanceDataBase
from sqlalchemy.ext.asyncio import AsyncSession
from src.domain.dto.integration.IntegracionDTO import CreateIntegrationDto
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
async def get_integration( integration_id: str, db: Session = Depends(get_db), token: str = Depends( get_bearer_token ) ):
    service = IntegrationService(db)
    try:
        integration_get = service.get( integration_id )
        return integration_get
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str( error ))


@IntegrationRouter.post('/create')
async def create_integration( createintegration: CreateIntegrationDto, request: Request, db: Session = Depends(get_db), token: str = Depends(get_bearer_token) ) :

    service = IntegrationService(db)
    try:
        response = service.create( createintegration )
        return response
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to create")


@IntegrationRouter.post('/sendSMS/{integration_id}')
async def send( integration_id: str, create_sms: CreateSMSDto, request: Request, db: Session = Depends(get_db), token: str = Depends( get_bearer_token ) ):

    service = IntegrationService( db )
    try:
        response = await service.sendsms( integration_id, create_sms )
        return response
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str( e ))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

