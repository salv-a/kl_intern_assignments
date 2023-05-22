from scripts.core.handlers.circle import Circle
from scripts.core.handlers.triangle import Triangle
from scripts.core.handlers.square import Square
from scripts.core.handlers.rectangle import Rectangle
from scripts.core.handlers.data_validation import input_function

name_shape = input("Enter the shape\n1.Circle\n2.Triangle\n3.Square\n4.Rectangle\n")

if name_shape == "1":
    try:
        circle_radius = input_function("Enter the radius\n")
        circle_obj = Circle(circle_radius)
        print("Area",circle_obj.area())
        print("Perimeter",circle_obj.perimeter())
    except ValueError:
        print("---Exception---")
elif name_shape == "2":
    try:
        triangle_side_1 = input_function("Enter first side\n")
        triangle_side_2 = input_function("Enter second side\n")
        triangle_side_3 = input_function("Enter third side\n")
        triangle_obj = Triangle(triangle_side_1, triangle_side_2, triangle_side_3)
        print("Area",triangle_obj.area())
        print("Perimeter",triangle_obj.perimeter())
    except ValueError:
        print("---Exception---")
elif name_shape == "3":
    try:
        square_side = input_function("Enter the side\n")
        square_obj = Square(square_side)
        print("Area",square_obj.area())
        print("Perimeter",square_obj.perimeter())
    except ValueError:
        print("---Exception---")
elif name_shape == "4":
    try:
        rectangle_side_1 = input_function("Enter length\n")
        rectangle_side_2 = input_function("Enter breadth \n")
        rectangle_obj = Rectangle(rectangle_side_1, rectangle_side_2)
        print("Area",rectangle_obj.area())
        print("Perimeter",rectangle_obj.perimeter())
    except ValueError:
        print("---Exception---")
else:
    print("This is not supported!!")
