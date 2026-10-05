# Prime Number
# Check whether a number is prime (has exactly two distinct positive divisors: 1 and itself).
#
# Example 1:
# Input: n = 7
# Output: True
#
# Example 2:
# Input: n = 12
# Output: False
#
# Example 3 (Edge Case - Non-Prime Boundary):
# Input: n = 1
# Output: False  # 1 is neither prime nor composite


number = int(input("Enter the number: "))

if number < 2:
    print(False)
else:
    is_prime = True

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    print(is_prime)