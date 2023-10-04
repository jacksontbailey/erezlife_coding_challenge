from shape_classes.shape import Shape

class Square(Shape):
    def __init__(self, side_length):
        super().__init__('square', side_length)
    
    def calculate_perimeter(self):
        return 4 * self.side_length
    
    def calculate_area(self):
        return self.side_length ** 2