from setuptools import setup, find_packages

setup(
    name="linear-for-agents-sample",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
        "pandas>=2.0.3",
        "beautifulsoup4>=4.12.2",
        "lxml>=4.9.3",
        "tqdm>=4.66.1",
        "aiohttp>=3.8.5",
    ],
    python_requires=">=3.8",
)
