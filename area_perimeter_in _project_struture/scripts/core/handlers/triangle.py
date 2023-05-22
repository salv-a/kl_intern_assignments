import math


class Triangle:
    def __init__(self, triangle_side_1, triangle_side_2, triangle_side_3):
        self.side_1 = triangle_side_1
        self.side_2 = triangle_side_2
        self.side_3 = triangle_side_3

    def area(self):
        semi_perimeter = (self.side_1 + self.side_2 + self.side_3) / 2
        area_triangle = round((math.sqrt(
            semi_perimeter * (semi_perimeter - self.side_1) * (semi_perimeter - self.side_2) * (
                    semi_perimeter - self.side_3))), 2)
        return area_triangle

    def perimeter(self):
        perimeter_triangle = round((self.side_1 + self.side_2 + self.side_3), 2)
        return perimeter_triangle
