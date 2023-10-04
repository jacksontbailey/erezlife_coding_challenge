import math
from shape_classes.shape import Shape

class Pentagon(Shape):
    def __init__(self, side_length):
        super().__init__('pentagon', side_length)
    
    def calculate_perimeter(self):
        return 5 * self.side_length
    
    def calculate_area(self):
        return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.side_length ** 2