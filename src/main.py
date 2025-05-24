"""
Main entry point for the application.
"""
from utils.config import get_config
from data_collection.jra_collector import JRADataCollector

def main():
    """
    Main function to run the application.
    """
    config = get_config()
    print(f"Starting application with config: {config}")
    
    # Initialize the JRA data collector
    collector = JRADataCollector()
    
    # Example: Collect race calendar data for 2022
    print("Collecting race calendar data for 2022...")
    race_calendar = collector.collect_race_calendar(2022)
    print(f"Collected {len(race_calendar)} race calendar entries")
    
    # Example: Collect race results data for 2022
    print("Collecting race results data for 2022...")
    race_results = collector.collect_race_results(2022)
    print(f"Collected {len(race_results)} race results")
    
    print("Data collection completed successfully")

if __name__ == "__main__":
    main()
