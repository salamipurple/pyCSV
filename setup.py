from setuptools import setup, find_packages

setup(
    name="pyCSV",
    version="0.1.0",
    packages=find_packages(),
    description="Super simple CSV logger",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="quantamecho",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # or whatever license u want
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)