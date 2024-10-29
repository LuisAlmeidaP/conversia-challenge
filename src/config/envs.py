
import os
from dotenv import load_dotenv

load_dotenv()

class Envs:
    PORT = int(os.environ.get('PORT', 3000))
    DATABASE_URL = os.environ.get('DATABASE_URL')

    @classmethod
    def validate(cls):
        envs_requirement = [
            cls.PORT,
            cls.DATABASE_URL,
        ]

        if any(var is None for var in envs_requirement):
            raise ValueError('Environment variables must not be None')