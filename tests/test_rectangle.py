import pytest
from source.shapes import Rectangle
import math


class TestRectangle:

    def test_rectangle_area(self, my_rectangle):
        assert my_rectangle.area() == my_rectangle.width * my_rectangle.height

    def test_rectangle_perimeter(self, my_rectangle):
        assert my_rectangle.perimeter() == 2 * (my_rectangle.width + my_rectangle.height)

    def test_rectangle_equality(self, my_rectangle, invalid_rectangle):
        assert my_rectangle == Rectangle(10, 5)
        assert my_rectangle != invalid_rectangle
        assert my_rectangle != "Not a rectangle"
        assert my_rectangle != Rectangle(5, 10)