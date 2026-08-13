# Check whether a number is a perfect square (without using the square root function).
if (number := int(input("Enter the number: "))) >= 0:
    is_perfect_square = False

    for i in range(number + 1):
        if i * i == number:
            is_perfect_square = True
            break

    print("Yes") if is_perfect_square else print("No")
else:
    print("Negative numbers are not perfect squares")