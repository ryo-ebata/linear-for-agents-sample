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
│   └── __init__.py
├── tests/                # Test files
│   └── __init__.py
├── .env.example          # Example environment variables
├── .gitignore            # Git ignore file
├── README.md             # This file
└── requirements.txt      # Project dependencies
```

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

