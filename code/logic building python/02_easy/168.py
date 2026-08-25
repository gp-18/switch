# Check if a number is prime.
# Example 1: Input: 7 -> Output: yes
# Example 2: Input: 9 -> Output: no

number = int(input("Enter the number: "))

if number < 2:
    print("no")

else:
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    print("yes") if is_prime else print("no")
