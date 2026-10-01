# Use an f-string to show two numbers and their sum in one sentence.

# Example 1:
# Input: a = 5, b = 7
# Output: "The sum of 5 and 7 is 12."

# Example 2:
# Input: a = 12.5, b = 7.5
# Output: "The sum of 12.5 and 7.5 is 20.0."

a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
# Calculate the sum of a and b
sum_ab = a + b      
# Print the result using an f-string
print(f"The sum of {a} and {b} is {sum_ab}.")