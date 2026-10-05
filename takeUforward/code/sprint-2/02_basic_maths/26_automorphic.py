# Automorphic Number
# Check whether the square of a number ends with the number itself.
#
# Example 1:
# Input: n = 5
# Output: True  # 5^2 = 25 ends with 5
#
# Example 2:
# Input: n = 25
# Output: True  # 25^2 = 625 ends with 25
#
# Example 3 (Edge Case - Single Digit Non-Automorphic):
# Input: n = 7
# Output: False  # 7^2 = 49 does not end with 7

number = int(input("Enter the number: "))

if number < 0:
    print(False)
elif number == 0:
    print(True)
else:
    square = number * number
    temp = number
    is_automorphic = True

    while temp > 0:
        if temp % 10 != square % 10:
            is_automorphic = False
            break
        temp //= 10
        square //= 10

    print(is_automorphic)
