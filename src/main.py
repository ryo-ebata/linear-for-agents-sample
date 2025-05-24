"""
Main entry point for the application.
"""
from utils.config import get_config

def main():
    """
    Main function to run the application.
    """
    config = get_config()
    print(f"Starting application with config: {config}")
    
    # Your application logic here
    print("Hello, Linear for Agents!")

if __name__ == "__main__":
    main()

