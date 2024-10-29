from pydantic import BaseModel, HttpUrl
from uuid import UUID



class CreateIntegrationDto( BaseModel ):
    id: UUID
    name: str
    description: str
    endpoint: HttpUrl


    # @classmethod