# Prime Factorization
# Find all prime factors of a given number n.
#
# Example 1:
# Input: n = 60
# Output: [2, 2, 3, 5]  # 60 = 2 * 2 * 3 * 5
#
# Example 2:
# Input: n = 84
# Output: [2, 2, 3, 7]  # 84 = 2 * 2 * 3 * 7
#
# Example 3 (Edge Case - Prime Number):
# Input: n = 13
# Output: [13]  # A prime number has only itself as its prime factor

number = int(input("Enter the number: "))

number = abs(number)

prime_factors = []

i = 2

while i * i <= number:
    while number % i == 0:
        prime_factors.append(i)
        number = number // i

    i += 1

if number > 1:
    prime_factors.append(number)

print(prime_factors)