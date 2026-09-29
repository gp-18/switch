# Pattern 8: Inverted Star Pyramid
# Given an integer N, print an inverted centered star pyramid of height N.

# Example 1:
# Input: N = 3
# Output:
# *****
#  ***
#   *

# Example 2:
# Input: N = 4
# Output:
# *******
#  *****
#   ***
#    *

number = int(input("Enter the number: "))

for i in range(1, number + 1):

    for j in range(i - 1):
        print(" ", end="")

    for k in range(2 * (number - i) + 1):
        print("*", end="")

    for l in range(i - 1):
        print(" ", end="")

    print()
        