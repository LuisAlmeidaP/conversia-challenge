import asyncio
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.envs import Envs
from presentation.server import Server
from presentation.routes import routes
from src.data.postgres.database import InstanceDataBase



async def main():
    Envs.validate()
    db = InstanceDataBase( Envs.DATABASE_URL )
    server = Server( port=Envs.PORT,routes=routes, database=db)
    server.app.state.database = db
    await server.start_server()




if __name__ == '__main__':
    asyncio.run(main())

