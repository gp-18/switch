# Calculate the natural logarithm of a number.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

import math

number = float(input("Enter the number: "))

if number > 0:

    result = math.log(number)

    print("Natural logarithm:", result)

else:
    print("Logarithm is only defined for positive numbers")
