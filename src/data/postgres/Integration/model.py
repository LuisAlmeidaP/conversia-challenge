import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()

class IntegrationDB( Base ):
    __tablename__ = "integrations"

    id = Column( UUID( as_uuid=True ), primary_key=True, default=uuid.uuid4 )
    name         =                           Column( String, nullable=False )
    description  =                           Column( String )
    endpoint     =                           Column( String )
    created      =                           Column( DateTime )
    updated      =                           Column( DateTime )
    access_token =                           Column( String )