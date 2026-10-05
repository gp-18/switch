# LCM
# Find the Least Common Multiple of two numbers a and b.
#
# Example 1:
# Input: a = 12, b = 18
# Output: 36
#
# Example 2:
# Input: a = 4, b = 6
# Output: 12
#
# Example 3 (Edge Case - Coprime Numbers):
# Input: a = 5, b = 7
# Output: 35  # For coprime numbers, LCM = a * b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = abs(a)
b = abs(b)

if a == 0 or b == 0:
    print(0)
else:
    number = max(a, b)

    while True:
        if number % a == 0 and number % b == 0:
            print(number)
            break

        number += 1


# optimze approach 

# formula : lcm * hcf = a * b 