# Import math module for pi constant and square root function
import math

# Define a function that takes radius as an argument and returns area of circle
def calculate_area_circle(radius):
    # Use the formula area = pi * r^2
    area = math.pi * radius ** 2
    return area

# Define a function that takes length and breadth as arguments and returns area of rectangle
def calculate_area_rectangle(length, breadth):
    # Use the formula area = l * b
    area = length * breadth
    return area

# Define a function that takes side as an argument and returns area of square
def calculate_area_square(side):
    # Use the formula area = s^2
    area = side ** 2
    return area

# Define a function that takes base1, base2 and height as arguments and returns area of trapezoid
def calculate_area_trapezoid(base1, base2, height):
    # Use the formula area = (b1 + b2) / 2 * h
    area = (base1 + base2) / 2 * height
    return area

# Define a function that takes base and height as arguments and returns area of triangle 
def calculate_area_triangle(base, height):
    # Use the formula area = 0.5 * b * h 
    # Alternatively use Heron's formula if three sides are given 
    # See [^1^][1] [^2^][4]  for more details 
    area = 0.5 * base * height 
    return area 

# Define a function that takes base and height as arguments and returns area of parallelogram 
def calculate_area_parallelogram(base, height):
   # Use the formula Area=base*height 
   # See [^1^][1] [^3^][3] for more details 
   Area=base*height 
   return Area 

# Ask the user for input shape name
shape_name = input("Enter the shape name: ")

# Check which shape is entered and ask for corresponding inputs 
if shape_name == "circle":
   radius=float(input("Enter The Radius: "))
elif shape_name == "rectangle":
   length=float(input("Enter The Length: "))
   breadth=float(input("Enter The Breadth: "))
elif shape_name == "square":
   side=float(input("Enter The Side: "))
elif shape_name == "trapezoid":
   base1=float(input("Enter The First Base: "))
   base2=float(input("Enter The Second Base: "))
   height=float(input("Enter The Height: "))
elif shape_name == "triangle":
   base=float(input("Enter The Base: "))
   height=float(input("Enter The Height: "))   
elif shape_name == "parallelogram":
   base=float(input("Enter The Base: ")) 
   height=float(input("Enter The Height: "))  
else:
   print(f"Sorry, I don't know how to calculate {shape_name}.")

# Call the corresponding function and print the result 
if shape_name == "circle":
   Area_circle=calculate_area_circle(radius)
   print(f"The Area Of Circle Is {Area_circle}")
elif shape_name == "rectangle":
   Area_rectangle=calculate_area_rectangle(length,breadth)
   print(f"The Area Of Rectangle Is {Area_rectangle}")
elif shape_name == "square":
   Area_square=calculate_area_square(side)
   print(f"The Area Of Square Is {Area_square}")
elif shape_name == "trapezoid":
   Area_trapezoid=calculate_area_trapezoid(base1,base2,height)
   print(f"The Area Of Trapezoid Is {Area_trapezoid}")
elif shape_name == "triangle":
   Area_triangle=calculate_area_triangle(base,height)
   print(f"The Area Of Triangle Is {Area_triangle}")   
elif shape_name == "parallelogram":  
  Area_parallelogram=calculate_area_parallelogram(base,height)  
  print(f"The Area Of Parallelogram Is {Area_parallelogram}")  
