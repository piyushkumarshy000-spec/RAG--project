import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    TOP_K = 3
    MAX_QUERY_LENGTH = 300

settings = Settings()