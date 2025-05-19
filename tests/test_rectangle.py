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

    @pytest.mark.slow
    def test_slow_test(self, my_rectangle):
        # Simulate a slow test
        import time
        time.sleep(2)
        assert my_rectangle.area() == my_rectangle.width * my_rectangle.height

    @pytest.mark.parametrize("width, height, expected_area", [
        (2, 3, 6),
        (4, 5, 20),
        (0, 5, 0),
        (1.5, 2.5, 3.75)
    ])
    def test_rectangle_area_parametrized(self, width, height, expected_area):
        rectangle = Rectangle(width, height)
        assert rectangle.area() == expected_area