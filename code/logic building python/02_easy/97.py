# Print the factorial of each number from 1 to n.

if (number := int(input("Enter the number: "))) >= 1:

    for i in range(1, number + 1):
        factorial = 1

        for j in range(1, i + 1):
            factorial = factorial * j

        print(f"{i}! = {factorial}")

else:
    print("Enter a valid number")