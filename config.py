import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
    DB_FILE = "database/company_db.json"

APP_TITLE = " AI Fire Mart "
API_URL = "http://127.0.0.1:8080/llm"