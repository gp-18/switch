# Sum of Digits
# Find the sum of all digits of an integer n.
#
# Example 1:
# Input: n = 12345
# Output: 15
#
# Example 2:
# Input: n = 902
# Output: 11
#
# Example 3 (Edge Case - Negative Number):
# Input: n = -456
# Output: 15  # Digits: 4 + 5 + 6

number = abs(int(input("Enter the number : ")))

digit_sum = 0

while number > 0:
    last_digit = number % 10
    digit_sum += last_digit
    number = number // 10

print(digit_sum)