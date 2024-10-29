from fastapi import APIRouter
from .integracion.integracionController import IntegrationRouter


routes = APIRouter()
routes.include_router( IntegrationRouter, prefix="/integration", tags=["Integration"] )
