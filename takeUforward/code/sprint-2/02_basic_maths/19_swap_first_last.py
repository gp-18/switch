# Swap First and Last Digit
# Swap the first and last digits of a number n.
#
# Example 1:
# Input: n = 12345
# Output: 52341
#
# Example 2:
# Input: n = 9876
# Output: 6879
#
# Example 3 (Edge Case - Single Digit):
# Input: n = 5
# Output: 5  # First and last digits are the same

number = input("Enter the number: ")

if len(number) > 1:
    number = list(number)
    number[0], number[-1] = number[-1], number[0]
    number = "".join(number)

print(number)