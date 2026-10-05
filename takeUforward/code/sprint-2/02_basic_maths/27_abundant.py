# Abundant Number
# A number is abundant if the sum of its proper divisors is greater than the number itself.
#
# Example 1:
# Input: n = 12
# Output: True  # Proper divisors: 1 + 2 + 3 + 4 + 6 = 16 > 12
#
# Example 2:
# Input: n = 15
# Output: False  # Proper divisors: 1 + 3 + 5 = 9 <= 15
#
# Example 3 (Edge Case - Smallest Value N = 1):
# Input: n = 1
# Output: False  # Divisor sum is 0 <= 1

number = int(input("Enter the number: "))

if number <= 1:
    print(False)
else:
    divisors_sum = 1

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            divisors_sum += i
            if i != number // i:
                divisors_sum += number // i

    print(divisors_sum > number)
