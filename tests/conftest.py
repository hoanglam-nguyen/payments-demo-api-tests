import pytest

def pytest_addoption(parser):
    parser.addoption("--containerized", action="store_true", help="Flag indicating whether tests are running inside a container")
