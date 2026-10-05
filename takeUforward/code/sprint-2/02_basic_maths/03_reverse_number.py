# Reverse a Number
# Reverse the digits of an integer n.
#
# Example 1:
# Input: n = 12345
# Output: 54321
#
# Example 2:
# Input: n = 10400
# Output: 401  # Trailing zeros are dropped
#
# Example 3 (Edge Case - Negative Number):
# Input: n = -123
# Output: -321  # Negative sign preserved

number = int(input("Enter the number: "))

is_negative = number < 0

number = abs(number)

reverse = 0

while number > 0:
    last_digit = number % 10
    reverse = reverse * 10 + last_digit
    number = number // 10

if is_negative:
    reverse = -reverse

print(reverse)
