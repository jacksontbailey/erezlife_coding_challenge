import math
from core.challenges.question_4.shape_classes.shape import Shape

class Pentagon(Shape):
    """
    Class representing a pentagon shape derived from the Shape class.

    Methods:
        calculate_perimeter(): Calculates the perimeter of the pentagon.
        calculate_area(): Calculates the area of the pentagon.
    """
    
    def __init__(self, side_length):
        """
        Initializes a Pentagon object with a given side length.

        Args:
            side_length (float): Length of the pentagon's side.
        """
        super().__init__('pentagon', side_length)
    

    def calculate_perimeter(self):
        """
        Calculates the perimeter of the pentagon.

        Returns:
            float: Perimeter of the pentagon.
        """
        return 5 * self.side_length
    

    def calculate_area(self):
        """
        Calculates the area of the pentagon.

        Returns:
            float: Area of the pentagon.
        """
        return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.side_length ** 2