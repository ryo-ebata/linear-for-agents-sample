"""
Script to collect JRA (Japan Racing Association) data.

This script demonstrates how to use the JRADataCollector class to collect
horse racing data from JRA's database or API, covering data from 1986 to the present.
"""
import argparse
import logging
from datetime import datetime

from data_collection.jra_collector import JRADataCollector

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

def main():
    """
    Main function to run the JRA data collection script.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Collect JRA horse racing data")
    parser.add_argument(
        "--start-year", 
        type=int, 
        default=1986, 
        help="Starting year for data collection (default: 1986)"
    )
    parser.add_argument(
        "--end-year", 
        type=int, 
        default=datetime.now().year, 
        help="Ending year for data collection (default: current year)"
    )
    parser.add_argument(
        "--data-types", 
        nargs="+", 
        choices=["race_calendar", "race_results", "horse_data", "track_condition"],
        default=["race_calendar", "race_results", "horse_data", "track_condition"],
        help="Data types to collect (default: all)"
    )
    args = parser.parse_args()
    
    logger.info(f"Starting JRA data collection from {args.start_year} to {args.end_year}")
    logger.info(f"Data types to collect: {args.data_types}")
    
    # Initialize the JRA data collector
    collector = JRADataCollector(start_year=args.start_year, end_year=args.end_year)
    
    # Collect the data
    collector.collect_all_data(data_types=args.data_types)
    
    # Export data summary
    collector.export_data_summary()
    
    logger.info("JRA data collection completed successfully")

if __name__ == "__main__":
    main()

