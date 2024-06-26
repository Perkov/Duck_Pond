from setuptools import find_packages, setup

setup(
    name="jaffle",
    packages=find_packages(exclude=["jaffle_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "pandas",
        "sqlescapy",
        "lxml",
        "html5lib"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest", "localstack", "awscli", "awscli-local"]},
)
