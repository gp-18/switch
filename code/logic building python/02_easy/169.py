# Print all prime numbers in the interval 1 to 10.
# Example 1: Input: 7 -> Output: yes
# Example 2: Input: 9 -> Output: no

for i in range(2, 11):

    is_prime = True

    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        print(i)
