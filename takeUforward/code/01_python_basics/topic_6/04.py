# Calculate the area of a circle from a radius supplied by the user.

# Example 1:
# Input: radius = 5
# Output: Area: 78.53981633974483

# Example 2:
# Input: radius = 7
# Output: Area: 153.93804002589985

# Import the math module to access the value of pi
import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print(f"Area: {area}")
