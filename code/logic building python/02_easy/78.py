# Print the product of digits of a given number.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

if (number := int(input("Enter the number: "))) >= 0:
    product = 1

    while number > 0:
        last_digit = number % 10
        product = product * last_digit
        number = number // 10

    print("Product of digits:", product)

else:
    print("Enter a valid number")
