import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file if available

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables!")
