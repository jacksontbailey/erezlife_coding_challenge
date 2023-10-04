import math
from core.challenges.question_4.shape_classes.shape import Shape

class Triangle(Shape):
    def __init__(self, side_length):
        super().__init__('triangle', side_length)
    
    def calculate_perimeter(self):
        return 3 * self.side_length
    
    def calculate_area(self):
        return 0.5 * self.side_length * math.sqrt(3)