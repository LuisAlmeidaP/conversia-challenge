
import os
from dotenv import load_dotenv

load_dotenv()

class Envs:
    PORT = int(os.environ.get('PORT', 3000))
    DATABASE_URL = os.environ.get('DATABASE_URL')
    TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')

    @classmethod
    def validate(cls):
        envs_requirement = [
            cls.PORT,
            cls.DATABASE_URL,
            cls.TWILIO_ACCOUNT_SID,
            cls.TWILIO_AUTH_TOKEN
        ]

        if any( var is None for var in envs_requirement ):
            raise ValueError('Environment variables must not be None')