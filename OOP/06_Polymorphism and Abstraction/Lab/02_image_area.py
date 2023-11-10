class ImageArea:
    def __init__(self, width: int, height: int) -> None:
        """Initialize ImageArea with width and height."""
        self.width = width
        self.height = height

    def get_area(self) -> int:
        """Calculate and return the area of the image."""
        return self.width * self.height

    def __gt__(self, other: 'ImageArea') -> bool:
        """Implement '>' operator based on area comparison."""
        return self.get_area() > other.get_area()

    def __ge__(self, other: 'ImageArea') -> bool:
        """Implement '>=' operator based on area comparison."""
        return self.get_area() >= other.get_area()

    def __eq__(self, other: 'ImageArea') -> bool:
        """Implement '==' operator based on area comparison."""
        return self.get_area() == other.get_area()

# a1 = ImageArea(7, 10)
# a2 = ImageArea(35, 2)
# a3 = ImageArea(8, 9)
# print(a1 == a2)
# print(a1 != a3)
# a1 = ImageArea(7, 10)
# a2 = ImageArea(35, 2)
# a3 = ImageArea(8, 9)
# print(a1 != a2)
# print(a1 >= a3)
# a1 = ImageArea(7, 10)
# a2 = ImageArea(35, 2)
# a3 = ImageArea(8, 9)
# print(a1 <= a2)
# print(a1 < a3)
