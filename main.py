# Import math module for pi constant
import math

# Define a function that takes radius as an argument and returns area
def calculate_area(radius):
    # Use the formula area = pi * r^2
    area = math.pi * radius ** 2
    return area

# Ask the user for input radius
radius = float(input("Enter the radius: "))

# Call the function and print the result
area = calculate_area(radius)
print(f"The area of a circle with radius {radius} is {area} square meters.")