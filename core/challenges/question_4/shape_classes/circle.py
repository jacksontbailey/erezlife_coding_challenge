import math
from core.challenges.question_4.shape_classes.shape import Shape

class Circle(Shape):
    def __init__(self, radius):
        super().__init__('circle', radius)
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.side_length
    
    def calculate_area(self):
        return math.pi * self.side_length ** 2