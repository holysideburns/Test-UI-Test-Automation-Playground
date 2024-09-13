import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    BASE_URL = os.getenv('BASE_URL')    
    TEST_USERNAME = os.getenv('TEST_USERNAME')
    TEST_PASSWORD = os.getenv('TEST_PASSWORD')

    @classmethod
    def validate(cls):
        if not cls.BASE_URL:
            raise ValueError("BASE_URL must be set in .env file")
        if not cls.TEST_USERNAME or not cls.TEST_PASSWORD:
            raise ValueError("TEST_USERNAME and TEST_PASSWORD must be set in .env file")
        
        