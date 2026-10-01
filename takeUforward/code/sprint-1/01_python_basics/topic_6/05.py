# Calculate the sum of the digits of a non-negative integer using a loop and % / //.

# Example 1:
# Input: 1234
# Output: 10 (1 + 2 + 3 + 4 = 10)

# Example 2:
# Input: 505
# Output: 10 (5 + 0 + 5 = 10)

# Get user input for a non-negative integer
number = int(input("Enter a non-negative integer: "))
# Initialize a variable to store the sum of digits
sum_of_digits = 0
# Use a loop to extract each digit and add it to the sum
while number > 0:
    digit = number % 10  # Get the last digit
    sum_of_digits += digit  # Add the digit to the sum
    number //= 10  # Remove the last digit from the number
# Print the result
print(f"Sum of digits: {sum_of_digits}")