import uvicorn
from fastapi import FastAPI, Depends

from src.data.postgres.database import InstanceDataBase


class Server:

    def __init__( self, port: int, routes, database: InstanceDataBase ):
        self.app = FastAPI(title="Integracion con Twilio", version='1.0.0')
        self.routes = routes
        self.port = port
        self.database = database


        self.app.include_router( self.routes )



    async def start_server( self ):
        config = uvicorn.Config(self.app, host="0.0.0.0", port=self.port, reload=True )
        server = uvicorn.Server(config)
        await server.serve()

