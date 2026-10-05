# Generate All Prime Numbers Up To N
# Generate every prime number from 2 to N.
#
# Example 1:
# Input: n = 20
# Output: [2, 3, 5, 7, 11, 13, 17, 19]
#
# Example 2:
# Input: n = 10
# Output: [2, 3, 5, 7]
#
# Example 3 (Edge Case - Smallest Prime / Boundary):
# Input: n = 2
# Output: [2]

number = int(input("Enter the number: "))

if number < 2:
    print([])
else:
    is_prime = [True] * (number + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(number ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, number + 1, i):
                is_prime[j] = False

    primes = [i for i in range(2, number + 1) if is_prime[i]]
    print(primes)
