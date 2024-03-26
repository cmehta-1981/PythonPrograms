import pytest


@pytest.fixture()           # called decorator & execute before every test method called
def setup():
    print("Launching browser")
    print("Open Browser")
    yield                   # called after each test method executed
    print("Close Browser")
