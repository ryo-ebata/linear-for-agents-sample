from setuptools import setup, find_packages

setup(
    name="linear-for-agents-sample",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dotenv",
    ],
    python_requires=">=3.8",
)

