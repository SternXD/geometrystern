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
        raise ValueError("Base1, base2, and height cannot be negative")
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

def calculate_area_trapezium(a, b, c, d, h):
    if a < 0 or b < 0 or c < 0 or d < 0 or h < 0:
        raise ValueError("All sides and height cannot be negative")
    area = 0.5 * (a + b) * h
    return area

def calculate_area_rhombus(diagonal1, diagonal2):
    if diagonal1 < 0 or diagonal2 < 0:
        raise ValueError("Diagonals cannot be negative")
    area = 0.5 * diagonal1 * diagonal2
    return area

def calculate_area_kite(diagonal1, diagonal2):
    if diagonal1 < 0 or diagonal2 < 0:
        raise ValueError("Diagonals cannot be negative")
    area = 0.5 * diagonal1 * diagonal2
    return area

def calculate_area_semicircle(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    area = math.pi * radius ** 2 / 2
    return area

shape_name = input("Enter the shape name: ")

if shape_name == "circle":
    try:
        radius = float(input("Enter the radius: "))
        area = calculate_area_circle(radius)
        print(f"The area of the circle is {area}")
    except ValueError as error:
        print(error)

elif shape_name == "rectangle":
    try:
        length = float(input("Enter the length: "))
        breadth = float(input("Enter the breadth: "))
        area = calculate_area_rectangle(length, breadth)
        print(f"The area of the rectangle is {area}")
    except ValueError as error:
        print(error)

elif shape_name == "square":
    try:
        side = float(input("Enter the side: "))
        area = calculate_area_square(side)
        print(f"The area of the square is {area}")
    except ValueError as error:
        print(error)

elif shape_name == "trapezoid":
    try:
        base1 = float(input("Enter the first base: "))
        base2 = float(input("Enter the second base: "))
        height = float(input("Enter the height: "))
        area = calculate_area_trapezoid(base1, base2, height)
