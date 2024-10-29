

import os
from collections.abc import Callable
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


class InstanceDataBase:
    def __init__( self, database_url: str ):
        print(database_url,1)

        self.DATABASE_URL = database_url
        self._engine = create_async_engine(self.DATABASE_URL, echo=False)
        self.Session: Callable[[], AsyncSession] = async_sessionmaker(self._engine)

    async def get_db( self ) -> AsyncSession:
        async with self.Session() as session:
            yield session

