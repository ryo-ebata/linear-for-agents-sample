#!/usr/bin/env python3
"""
Script to verify the Python environment setup.
"""
import sys
import pkg_resources
import platform

def check_python_version():
    """Check if Python version is 3.8 or higher."""
    python_version = sys.version_info
    print(f"Python version: {platform.python_version()}")
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        print("WARNING: Python version should be 3.8 or higher.")
        return False
    print("Python version check: OK")
    return True

def check_dependencies():
    """Check if all dependencies are installed."""
    try:
        with open("requirements.txt", "r") as f:
            requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]
        
        missing = []
        for requirement in requirements:
            try:
                pkg_name = requirement.split("==")[0]
                pkg_resources.get_distribution(pkg_name)
                print(f"Found {pkg_name}")
            except pkg_resources.DistributionNotFound:
                missing.append(requirement)
        
        if missing:
            print(f"WARNING: Missing dependencies: {', '.join(missing)}")
            print("Run 'pip install -r requirements.txt' to install them.")
            return False
        
        print("Dependencies check: OK")
        return True
    except Exception as e:
        print(f"Error checking dependencies: {e}")
        return False

def main():
    """Run all checks."""
    print("Verifying Python environment...")
    python_ok = check_python_version()
    deps_ok = check_dependencies()
    
    if python_ok and deps_ok:
        print("\nEnvironment setup is complete and valid!")
        return 0
    else:
        print("\nEnvironment setup has issues that need to be addressed.")
        return 1

if __name__ == "__main__":
    sys.exit(main())

