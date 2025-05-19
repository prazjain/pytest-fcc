
#to make test fixtures available to all test files, pytest will look for a file named conftest.py in the test directory or any parent directory.
# This file can contain fixtures, hooks, and other configurations that you want to share across multiple test files.
import pytest
from source.shapes import Rectangle


@pytest.fixture
def my_rectangle():
    """Fixture to create a Rectangle object."""
    rectangle = Rectangle(10, 5)
    yield rectangle
    del rectangle

@pytest.fixture
def invalid_rectangle():
    """Fixture to create an invalid Rectangle object."""
    rectangle = Rectangle(-10, 5)
    yield rectangle
    del rectangle
