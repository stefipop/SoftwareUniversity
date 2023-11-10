from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self._radius = radius

    @property
    def radius(self) -> float:
        """Get the radius of the circle."""
        return self._radius

    def calculate_area(self) -> float:
        """Calculate the area of the circle."""
        return pi * self.radius ** 2

    def calculate_perimeter(self) -> float:
        """Calculate the perimeter of the circle."""
        return 2 * pi * self.radius


class Rectangle(Shape):
    def __init__(self, height: float, width: float) -> None:
        self._height = height
        self._width = width

    @property
    def height(self) -> float:
        """Get the height of the rectangle."""
        return self._height

    @property
    def width(self) -> float:
        """Get the width of the rectangle."""
        return self._width

    def calculate_area(self) -> float:
        """Calculate the area of the rectangle."""
        return self.height * self.width

    def calculate_perimeter(self) -> float:
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
