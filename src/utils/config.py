"""
Configuration utilities for the application.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Configuration
API_KEY = os.getenv("API_KEY", "")
API_URL = os.getenv("API_URL", "https://api.example.com")

# Application Settings
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

def get_config():
    """
    Returns the current configuration as a dictionary.
    """
    return {
        "api_key": API_KEY,
        "api_url": API_URL,
        "debug": DEBUG,
        "log_level": LOG_LEVEL,
    }

