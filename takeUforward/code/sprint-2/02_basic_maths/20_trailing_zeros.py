# Count Trailing Zeros
# Count the number of zeros at the end of a number n.
#
# Example 1:
# Input: n = 12000
# Output: 3
#
# Example 2:
# Input: n = 1040
# Output: 1
#
# Example 3 (Edge Case - No Trailing Zeros / Negative):
# Input: n = -500
# Output: 2  # Trailing zeros count is 2

number = int(input("Enter the number: "))

number = abs(number)

count = 0

while number > 0 and number % 10 == 0:
    count += 1
    number = number // 10

print(count)