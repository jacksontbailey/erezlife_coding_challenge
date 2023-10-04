class Shape:
    """
    Base class representing a geometric shape.

    Attributes:
        name (str): Name of the shape.
        side_length (float): Length of the shape's side or radius.

    Methods:
        calculate_perimeter(): Abstract method to calculate the perimeter of the shape.
        calculate_area(): Abstract method to calculate the area of the shape.
    """
    def __init__(self, name, side_length):
        """
        Initializes a Shape object with a given name and side length.

        Args:
            name (str): Name of the shape.
            side_length (float): Length of the shape's side or radius.
        """
        self.name = name
        self.side_length = float(side_length)
    
    def calculate_perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.

        Returns:
            float: Perimeter of the shape.
        """
        pass
    
    def calculate_area(self):
        """
        Abstract method to calculate the area of the shape.

        Returns:
            float: Area of the shape.
        """
        pass