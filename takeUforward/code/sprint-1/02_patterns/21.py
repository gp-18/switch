# Pattern 21: Hollow Rectangle Pattern
# Given an integer N, print an N x N square filled with stars only on the border and spaces inside.

# Example 1:
# Input: N = 3
# Output:
# ***
# * *
# ***

# Example 2:
# Input: N = 4
# Output:
# ****
# *  *
# *  *
# ****

number = int(input("Enter the number : "))

for i in range(number):
    for j in range(number):
        if i == 0 or i == number - 1 or j == 0 or j == number - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()