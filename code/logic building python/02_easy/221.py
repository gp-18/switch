# Compute the volume of a cone given height and radius.
# Example 1: Input: r=2, h=3 -> Output: 12.57
# Example 2: Input: r=3, h=5 -> Output: 47.12

import math

radius = float(input("Enter cone radius: "))
height = float(input("Enter cone height: "))

if radius > 0 and height > 0:
    volume = (1 / 3) * math.pi * (radius ** 2) * height
    print("Cone volume:", round(volume, 2))
else:
    print("Radius and height must be positive")
