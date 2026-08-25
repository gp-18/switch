# Print the factorial of each number from 1 to n.
# Example 1: Input: 5 -> Output: 120
# Example 2: Input: 3 -> Output: 6

if (number := int(input("Enter the number: "))) >= 1:

    for i in range(1, number + 1):
        factorial = 1

        for j in range(1, i + 1):
            factorial = factorial * j

        print(f"{i}! = {factorial}")

else:
    print("Enter a valid number")
