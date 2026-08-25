# Check whether a number is a perfect square (without using the square root function).
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

if (number := int(input("Enter the number: "))) >= 0:
    is_perfect_square = False

    for i in range(number + 1):
        if i * i == number:
            is_perfect_square = True
            break

    print("Yes") if is_perfect_square else print("No")
else:
    print("Negative numbers are not perfect squares")
