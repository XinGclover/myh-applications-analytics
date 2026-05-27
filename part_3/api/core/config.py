# api/core/config.py

from dotenv import load_dotenv
import os

load_dotenv()

REFRESH_API_KEY = os.getenv("REFRESH_API_KEY")