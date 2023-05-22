import math


class Circle:
    def __init__(self, circle_radius):
        self.radius = circle_radius

    def area(self):
        area_circle = round((math.pi * (self.radius * self.radius)), 2)
        return area_circle

    def perimeter(self):
        perimeter_circle = round((2 * math.pi * self.radius), 2)
        return perimeter_circle
