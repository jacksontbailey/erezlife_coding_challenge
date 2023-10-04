import math
from core.challenges.question_4.shape_classes.shape import Shape

class Triangle(Shape):
    """
    Class representing a triangle shape derived from the Shape class.

    Methods:
        calculate_perimeter(): Calculates the perimeter of the triangle.
        calculate_area(): Calculates the area of the triangle.
    """
    
    def __init__(self, side_length):
        """
        Initializes a Triangle object with a given side length.

        Args:
            side_length (float): Length of the triangle's side.
        """
        super().__init__('triangle', side_length)
    

    def calculate_perimeter(self):
        """
        Calculates the perimeter of the triangle.

        Returns:
            float: Perimeter of the triangle.
        """
        return 3 * self.side_length
    

    def calculate_area(self):
        """
        Calculates the area of the triangle.

        Returns:
            float: Area of the triangle.
        """
        return 0.5 * self.side_length * math.sqrt(3)