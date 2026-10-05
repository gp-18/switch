# Check Power of Two
# Determine whether an integer n is a power of 2.
#
# Example 1:
# Input: n = 16
# Output: True
#
# Example 2:
# Input: n = 10
# Output: False
#
# Example 3 (Edge Case - Zero or Negative Number):
# Input: n = 0
# Output: False  # 0 and negative integers are not powers of two

number = int(input("Enter the number: "))

if number <= 0:
    print(False)
else:
    print((number & (number - 1)) == 0)