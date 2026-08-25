# Print all factors of a given number.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

if (number := int(input("Enter the number: "))) >= 1:

    for i in range(1, number + 1):
        if number % i == 0:
            print(i)

else:
    print("Give a correct number")
