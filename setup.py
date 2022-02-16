from setuptools import setup, find_packages

install_requires = [
    "alembic==1.7.6",
    "flask==1.1.0",
    "orjson==3.6.7",
    "pydantic==1.9.0",
    "sqlalchemy==1.4.31",
    "structlog==21.5.0",
]
dev_requires = ["autoflake==1.4", "black==22.1.0", "isort==5.10.1"]
test_requires = [
    "coverage==6.3.1",
    "pytest==7.0.1",
    "pytest-cov==3.0.0",
    "tox==3.24.5",
]

setup(
    name="gogolook",
    version="0.1.0",
    description="A Restful task list API",
    author="Jacob Chen",
    author_email="chenjr0719@gmail.com",
    packages=find_packages(exclude=["tests"]),
    install_requires=install_requires,
    extras_require={"dev": dev_requires + test_requires, "test": test_requires},
)
