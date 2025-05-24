"""
Tests for the configuration utilities.
"""
import os
import pytest
from src.utils.config import get_config

def test_get_config():
    """
    Test that get_config returns a dictionary with the expected keys.
    """
    config = get_config()
    assert isinstance(config, dict)
    assert "api_key" in config
    assert "api_url" in config
    assert "debug" in config
    assert "log_level" in config

def test_environment_variables(monkeypatch):
    """
    Test that environment variables are correctly loaded.
    """
    # Set environment variables
    monkeypatch.setenv("API_KEY", "test_key")
    monkeypatch.setenv("API_URL", "https://test.example.com")
    monkeypatch.setenv("DEBUG", "True")
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")
    
    # Reload the module to pick up the new environment variables
    import importlib
    import src.utils.config
    importlib.reload(src.utils.config)
    
    # Get the config
    from src.utils.config import get_config
    config = get_config()
    
    # Check that the environment variables were correctly loaded
    assert config["api_key"] == "test_key"
    assert config["api_url"] == "https://test.example.com"
    assert config["debug"] is True
    assert config["log_level"] == "DEBUG"

