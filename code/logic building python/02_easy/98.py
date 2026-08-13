# Print the sum of all odd digits and even digits separately in a given number.

if (number := int(input("Enter the number: "))) >= 0:

    odd_sum = 0
    even_sum = 0

    while number > 0:
        last_digit = number % 10

        if last_digit % 2 == 0:
            even_sum += last_digit
        else:
            odd_sum += last_digit

        number = number // 10

    print("Sum of even digits:", even_sum)
    print("Sum of odd digits:", odd_sum)

else:
    print("Enter a valid number")