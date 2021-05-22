from setuptools import setup

setup(
    name="testcode",
    version="0.1.0",
    py_modules=["testcode"],
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "testcode = main:cli",
        ],
    },
)
