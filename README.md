# Linear for Agents Sample

This repository contains a Python environment setup for the Linear for Agents sample project.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setting up the environment

1. Clone the repository:
   ```bash
   git clone https://github.com/ryo-ebata/linear-for-agents-sample.git
   cd linear-for-agents-sample
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Project Structure

```
linear-for-agents-sample/
├── src/                  # Source code
│   ├── data_collection/  # Data collection modules
│   │   ├── __init__.py
│   │   └── jra_collector.py  # JRA data collection module
│   ├── utils/            # Utility modules
│   │   ├── __init__.py
│   │   └── config.py     # Configuration utilities
│   ├── __init__.py
│   ├── main.py           # Main application entry point
│   └── collect_jra_data.py  # Script to collect JRA data
├── tests/                # Test files
│   ├── __init__.py
│   ├── test_config.py
│   └── test_jra_collector.py  # Tests for JRA data collector
├── data/                 # Directory for collected data (created at runtime)
├── .env.example          # Example environment variables
├── .gitignore            # Git ignore file
├── README.md             # This file
└── requirements.txt      # Project dependencies
```

## JRA Data Collection

This project includes a module for collecting horse racing data from JRA (Japan Racing Association) from 1986 to the present. The data collection script extracts the following types of data:

- Race calendar (dates, venues, race names)
- Race results (finishing positions, times, odds)
- Horse data (profiles, pedigree)
- Track condition data (weather, track state)

### Using the JRA Data Collector

To collect JRA data, you can use the provided script:

```bash
python src/collect_jra_data.py --start-year 2000 --end-year 2022 --data-types race_calendar race_results
```

Command-line options:
- `--start-year`: Starting year for data collection (default: 1986)
- `--end-year`: Ending year for data collection (default: current year)
- `--data-types`: Types of data to collect (options: race_calendar, race_results, horse_data, track_condition)

The collected data will be saved to CSV files in the `data/` directory.

## Development

To run the tests:
```bash
pytest
```

To format the code:
```bash
black .
```

To check code style:
```bash
flake8
```
