from datetime import datetime

from pydantic import BaseModel, HttpUrl, Field
from uuid import UUID



class CreateIntegrationDto( BaseModel ):
    name: str = Field(..., min_length=3, max_length=50, description="Nombre de la integración")
    description: str = Field(..., max_length=200, description="Descripción breve de la integración")
    endpoint: HttpUrl = Field(..., description="URL del endpoint de la integración")
    created: datetime = Field(default_factory=datetime.utcnow, description="Fecha de creación")
    updated: datetime = Field(default_factory=datetime.utcnow, description="Fecha de última actualización")
    access_token: str = Field(..., min_length=10, description="Token de acceso para la integración")