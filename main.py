import math

def calculate_area_circle(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    area = math.pi * radius ** 2
    return area

def calculate_area_rectangle(length, breadth):
    if length < 0 or breadth < 0:
        raise ValueError("Length and breadth cannot be negative")
    area = length * breadth
    return area

def calculate_area_square(side):
    if side < 0:
        raise ValueError("Side cannot be negative")
    area = side ** 2
    return area

def calculate_area_trapezoid(base1, base2, height):
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError("Bases and height cannot be negative")
    area = (base1 + base2) / 2 * height
    return area

def calculate_area_triangle(base, height):
    if base < 0 or height < 0:
        raise ValueError("Base and height cannot be negative")
    area = 0.5 * base * height
    return area

def calculate_area_parallelogram(base, height):
    if base < 0 or height < 0:
        raise ValueError("Base and height cannot be negative")
    area = base * height
    return area

shape_name = input("Enter the shape name: ")

if shape_name == "circle":
    try:
        radius = float(input("Enter the radius: "))
        area = calculate_area_circle(radius)
        print(f"The area of circle is {area}")
    except ValueError:
        print("Invalid input")
elif shape_name == "rectangle":
    try:
        length = float(input("Enter the length: "))
        breadth = float(input("Enter the breadth: "))
        area = calculate_area_rectangle(length, breadth)
        print(f"The area of rectangle is {area}")
    except ValueError:
        print("Invalid input")
elif shape_name == "square":
    try:
        side = float(input("Enter the side: "))
        area = calculate_area_square(side)
        print(f"The area of square is {area}")
    except ValueError:
        print("Invalid input")
elif shape_name == "trapezoid":
    try:
        base1 = float(input("Enter the first base: "))
        base2 = float(input("Enter the second base: "))
        height = float(input("Enter the height: "))
        area = calculate_area_trapezoid(base1, base2, height)
        print(f"The area of trapezoid is {area}")
    except ValueError:
        print("Invalid input")
elif shape_name == "triangle":
    try:
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        area = calculate_area_triangle(base, height)
        print(f"The area of triangle is {area}")
    except ValueError:
        print("Invalid input")
elif shape_name == "parallelogram":
    try:
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        area = calculate_area_parallelogram(base, height)
        print(f"The area of parallelogram is {area}")
    except ValueError:
        print("Invalid input")
else:
    print(f"Sorry, I don't know how to calculate {shape_name}.")
