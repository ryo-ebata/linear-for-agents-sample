"""
Script to collect JRA (Japan Racing Association) data.

This script demonstrates how to use the JRADataCollector class to collect
horse racing data from JRA's database or API, covering data from 1986 to the present.
"""
import argparse
import logging
import sys
from datetime import datetime
from typing import List, Optional

from data_collection.jra_collector import JRADataCollector

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

def parse_arguments():
    """
    Parse command line arguments.
    
    Returns:
        Parsed arguments
    """
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
    return parser.parse_args()

def validate_arguments(args) -> bool:
    """
    Validate command line arguments.
    
    Args:
        args: Parsed arguments
        
    Returns:
        True if arguments are valid, False otherwise
    """
    if args.start_year < 1986:
        logger.error(f"Start year must be >= 1986, got {args.start_year}")
        return False
    
    if args.end_year < args.start_year:
        logger.error(f"End year must be >= start year, got {args.end_year} < {args.start_year}")
        return False
    
    if args.end_year > datetime.now().year:
        logger.warning(f"End year is in the future: {args.end_year} > {datetime.now().year}")
    
    return True

def main():
    """
    Main function to run the JRA data collection script.
    """
    try:
        # Parse and validate command line arguments
        args = parse_arguments()
        if not validate_arguments(args):
            sys.exit(1)
        
        logger.info(f"Starting JRA data collection from {args.start_year} to {args.end_year}")
        logger.info(f"Data types to collect: {args.data_types}")
        
        # Initialize the JRA data collector
        collector = JRADataCollector(start_year=args.start_year, end_year=args.end_year)
        
        try:
            # Collect the data
            collector.collect_all_data(data_types=args.data_types)
            
            # Export data summary
            collector.export_data_summary()
            
            logger.info("JRA data collection completed successfully")
        except Exception as e:
            logger.error(f"Error during data collection: {e}")
            sys.exit(1)
            
    except KeyboardInterrupt:
        logger.info("Data collection interrupted by user")
        sys.exit(130)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
