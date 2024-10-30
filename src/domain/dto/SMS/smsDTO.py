from datetime import datetime

from pydantic import BaseModel, HttpUrl, Field, constr
from uuid import UUID

class CreateSMSDto( BaseModel ):
    to: int
    from_number: int
    body: str = Field(..., min_length=3, max_length=50, description="Mensaje de texto")