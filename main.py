# Import math module for pi constant
import math

# Define a function that takes radius as an argument and returns area
def calculate_area(radius):
    # Use the formula area = pi * r^2
    area = math.pi * radius ** 2
    return area

# Define a function that takes square meters as an argument and returns acres
def convert_to_acres(square_meters):
    # Use the formula acres = square meters x 0.000247
    acres = square_meters * 0.000247
    return acres

# Ask the user for input radius
radius = float(input("Enter the radius: "))

# Call the functions and print the result
area = calculate_area(radius)
acres = convert_to_acres(area)
print(f"The area of a circle with radius {radius} is {area} square meters or {acres} acres.")
