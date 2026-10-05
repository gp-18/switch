# Product of Digits
# Find the product of all digits of an integer n.
#
# Example 1:
# Input: n = 1234
# Output: 24
#
# Example 2:
# Input: n = 56
# Output: 30
#
# Example 3 (Edge Case - Contains Zero):
# Input: n = 1045
# Output: 0  # 1 * 0 * 4 * 5 = 0

number = abs(int(input("Enter the number : ")))

if number == 0:
    print(0)
else:
    product = 1

    while number > 0:
        last_digit = number % 10
        product *= last_digit
        number = number // 10

    print(product)