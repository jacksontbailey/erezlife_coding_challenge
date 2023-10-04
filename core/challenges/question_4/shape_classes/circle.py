import math
from core.challenges.question_4.shape_classes.shape import Shape

class Circle(Shape):
    """
    Class representing a circle shape derived from the Shape class.

    Methods:
        calculate_perimeter(): Calculates the perimeter of the circle.
        calculate_area(): Calculates the area of the circle.
    """
    
    def __init__(self, radius):
        """
        Initializes a Circle object with a given radius.

        Args:
            radius (float): Radius of the circle.
        """
        super().__init__('circle', radius)
    

    def calculate_perimeter(self):
        """
        Calculates the perimeter of the circle.

        Returns:
            float: Perimeter of the circle.
        """
        return 2 * math.pi * self.side_length
    

    def calculate_area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: Area of the circle.
        """
        return math.pi * self.side_length ** 2