class Square:
    def __init__(self, square_side):
        self.side = square_side

    def area(self):
        area_square = round((self.side * self.side), 2)
        return area_square

    def perimeter(self):
        perimeter_square =round((4 * self.side), 2)
        return perimeter_square
