import math
from source.shapes import Circle

class TestCircle:
    def setup_method(self, method):
        self.circle = Circle(10)
        print("Setup for test method:", method.__name__)

    def teardown_method(self, method):
        print("Teardown for test method:", method.__name__)
        del self.circle 

    def test_circle_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_circle_perimeter(self):
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius
    