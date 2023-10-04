from core.challenges.question_4.shape_classes.shape import Shape

class Square(Shape):
    """
    Class representing a square shape derived from the Shape class.

    Methods:
        calculate_perimeter(): Calculates the perimeter of the square.
        calculate_area(): Calculates the area of the square.
    """
    def __init__(self, side_length):
        """
        Initializes a Square object with a given side length.

        Args:
            side_length (float): Length of the square's side.
        """
        super().__init__('square', side_length)
    
    def calculate_perimeter(self):
        """
        Calculates the perimeter of the square.

        Returns:
            float: Perimeter of the square.
        """
        return 4 * self.side_length
    
    def calculate_area(self):
        """
        Calculates the area of the square.

        Returns:
            float: Area of the square.
        """
        return self.side_length ** 2