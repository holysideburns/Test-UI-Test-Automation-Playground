import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    BASE_URL = "http://www.uitestingplayground.com"
    TIMEOUT = 10000  # milliseconds
    
    # Credentials
    TEST_USERNAME = os.getenv('TEST_USERNAME')
    TEST_PASSWORD = os.getenv('TEST_PASSWORD')

    @classmethod
    def validate(cls):
        if not cls.TEST_USERNAME or not cls.TEST_PASSWORD:
            raise ValueError("TEST_USERNAME and TEST_PASSWORD must be set in .env file")