# Convert angle in radians to degrees.
# Example 1: Input: 1 (radians) -> Output: 57.3 degrees
# Example 2: Input: 3.14159 (radians) -> Output: 180.0 degrees

import math

radians = float(input("Enter angle in radians: "))
degrees = radians * (180 / math.pi)
print(f"{radians} radians = {round(degrees, 2)} degrees")
