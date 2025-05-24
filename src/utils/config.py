"""
Configuration utilities for the application.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Configuration
API_KEY = os.getenv("API_KEY", "")
API_URL = os.getenv("API_URL", "https://api.jra.jp")

# Application Settings
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# JRA Data Collection Settings
JRA_REQUEST_DELAY = float(os.getenv("JRA_REQUEST_DELAY", "1.0"))
JRA_DATA_DIR = os.getenv("JRA_DATA_DIR", "data")

def get_config():
    """
    Returns the current configuration as a dictionary.
    """
    return {
        "api_key": API_KEY,
        "api_url": API_URL,
        "debug": DEBUG,
        "log_level": LOG_LEVEL,
        "jra_request_delay": JRA_REQUEST_DELAY,
        "jra_data_dir": JRA_DATA_DIR,
    }
