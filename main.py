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

def calculate_volume_cuboid(length, breadth, height):
    if length < 0 or breadth < 0 or height < 0:
        raise ValueError("Length, breadth, and height cannot be negative")
    volume = length * breadth * height
    return volume

def calculate_volume_sphere(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    volume = 4/3 * math.pi * radius ** 3
    return volume

def calculate_volume_cylinder(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height cannot be negative")
    volume = math.pi * radius ** 2 * height
    return volume

def calculate_volume_cone(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height cannot be negative")
    volume = 1/3 * math.pi * radius ** 2 * height
    return volume

def calculate_volume_pyramid(base_area, height):
    if base_area < 0 or height < 0:
        raise ValueError("Base area and height cannot be negative")
    volume = 1/
