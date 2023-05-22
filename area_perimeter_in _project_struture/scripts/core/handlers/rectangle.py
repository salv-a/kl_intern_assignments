class Rectangle:
    def __init__(self, rectangle_side_1, rectangle_side_2):
        self.side_1 = rectangle_side_1
        self.side_2 = rectangle_side_2

    def area(self):
        area_rectangle = round((self.side_1 * self.side_2), 2)
        return area_rectangle

    def perimeter(self):
        perimeter_rectangle = round((2 * (self.side_1 + self.side_2)), 2)
        return perimeter_rectangle
