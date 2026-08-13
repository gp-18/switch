# Check if a number is prime or not.
if (number := int(input("Enter the number: "))) > 1:
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    print("prime number") if is_prime else print("not a prime number")
else:
    print("Enter a number greater than 1")