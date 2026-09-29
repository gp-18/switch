# Check whether an integer is even or odd.

# Example 1:
# Input: 4
# Output: 4 is even

# Example 2:
# Input: 7
# Output: 7 is odd

number = int(input("Enter an integer: "))
# Check if the number is even or odd using the modulus operator
if number % 2 == 0:     
    print(f"{number} is even")
else:
    print(f"{number} is odd")