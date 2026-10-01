# Given a non-negative integer, print its last digit and the number after removing its last digit.

# Example 1:
# Input: 1234
# Output: Last digit: 4, Remaining number: 123

# Example 2:
# Input: 9
# Output: Last digit: 9, Remaining number: 0

# Get user input for a non-negative integer
number = int(input("Enter a non-negative integer: "))
# Calculate the last digit and the remaining number
last_digit = number % 10
remaining_number = number // 10 
# Print the results
print(f"Last digit: {last_digit}, Remaining number: {remaining_number}")
