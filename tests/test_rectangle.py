import pytest
from source.shapes import Rectangle
import math

class TestRectangle:
    def setup_method(self, method):
        self.rectangle = Rectangle(10, 5)
        print("Setup for test method:", method.__name__)

    def teardown_method(self, method):
        print("Teardown for test method:", method.__name__)
        del self.rectangle 

    def test_rectangle_area(self):
        assert self.rectangle.area() == self.rectangle.width * self.rectangle.height

    def test_rectangle_perimeter(self):
        assert self.rectangle.perimeter() == 2 * (self.rectangle.width + self.rectangle.height)