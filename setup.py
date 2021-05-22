import os
from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="testcode",
    version="0.1.0",
    py_modules=["testcode"],
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "testcode = testcode.main:cli",
        ],
    },
)
