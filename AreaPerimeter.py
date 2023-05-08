import math


def input_function(input_from_prompt):
    while True:
        try:
            float_input = float(input(input_from_prompt))
            if float_input == 0:
                print("Dimensions cannot be zero")
                continue
            return float_input
        except:
            print("Invalid input.Enter valid number")
            continue


class AreaPerimeter:
    def circle(self):
        radius = input_function("Enter the radius\n")
        area = round((math.pi * (radius * radius)), 2)
        perimeter = round((2 * math.pi * radius), 2)
        return area, perimeter

    def triangle(self):
        a = input_function("Enter first side\n")
        b = input_function("Enter second side\n")
        c = input_function("Enter third side\n")
        s = (a + b + c) / 2
        area = round((math.sqrt(s * (s - a) * (s - b) * (s - c))), 2)
        perimeter = round((a + b + c), 2)
        return area, perimeter

    def square(self):
        side = input_function("Enter the side\n")
        area = round((side * side), 2)
        perimeter = round((4 * side), 2)
        return area, perimeter

    def rectangle(self):
        length = input_function("Enter length\n")
        breadth= input_function("Enter breadth \n")
        area = round((length * breadth), 2)
        perimeter = round((2 * (length + breadth)), 2)
        return area, perimeter

    def cube(self):
        cube_side = input_function("Enter the side\n")
        area = round((6 * (cube_side * cube_side)), 2)
        perimeter = round((12 * cube_side), 2)
        volume = round((pow(cube_side, 3)), 2)
        return area, perimeter, volume

    def cuboid(self):
        l = input_function("Enter length\n")
        b = input_function("Enter breadth\n")
        h = input_function("Enter height\n")
        area = round((2 * (l * b + b * h + l * h)), 2)
        perimeter = round((4 * (l + b + h)), 2)
        volume = round((l * b * h), 2)
        return area, perimeter, volume

    def sphere(self):
        sphere_radius = input_function("Enter radius\n")
        area = round((4 * math.pi * (sphere_radius * sphere_radius)), 2)
        perimeter = round((2 * math.pi * sphere_radius), 2)
        volume = round(((4 / 3) * math.pi * pow(sphere_radius, 3)), 2)
        return area, perimeter, volume


name_shape = input(
    "Enter the shape\n1.Circle\n2.Triangle\n3.Square\n4.Rectangle\n5.Cube\n6.Cuboid\n7.Sphere\n")
shape_obj = AreaPerimeter()
if name_shape == "1":
    print(shape_obj.circle())
elif name_shape == "2":
    print(shape_obj.triangle())
elif name_shape == "3":
    print(shape_obj.square())
elif name_shape == "4":
    print(shape_obj.rectangle())
elif name_shape == "5":
    print(shape_obj.cube())
elif name_shape == "6":
    print(shape_obj.cuboid())
elif name_shape == "7":
    print(shape_obj.sphere())
else:
    print("This is not supported!!")
