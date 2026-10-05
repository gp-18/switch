# Calculate Power
# Calculate base^exponent without using the built-in exponentiation operator **.
#
# Example 1:
# Input: base = 2, exp = 5
# Output: 32
#
# Example 2:
# Input: base = 3, exp = 4
# Output: 81
#
# Example 3 (Edge Case - Exponent Zero):
# Input: base = 5, exp = 0
# Output: 1  # Any non-zero number to power 0 is 1

base = int(input("Enter the base: "))
exp = int(input("Enter the exponent: "))

result = 1
b = base
e = abs(exp)

while e > 0:
    if e % 2 == 1:
        result *= b
    b *= b
    e //= 2

if exp < 0:
    print(1 / result)
else:
    print(result)