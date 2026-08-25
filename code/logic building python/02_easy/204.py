# Find the area of a regular hexagon given side length.
# Example 1: Input: 3 -> Output: 23.38
# Example 2: Input: 5 -> Output: 64.95

import math

side = float(input("Enter side length of regular hexagon: "))
if side > 0:
    area = (3 * math.sqrt(3) / 2) * (side ** 2)
    print("Area of hexagon:", round(area, 2))
else:
    print("Please enter a positive side length")
