# Read an integer and print whether it is positive, negative, or zero.

# Example 1:
# Input: -15
# Output: -15 is negative

# Example 2:
# Input: 0
# Output: The number is zero

number = int(input("Enter an integer: "))

if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print("The number is zero")
