# Find HCF (GCD) of two numbers using loops.

if (number1 := int(input("Enter the number 1: "))) >= 1 and (number2 := int(input("Enter the number 2: "))) >= 1:

    max_number = 1

    for i in range(1, min(number1, number2) + 1):
        if number1 % i == 0 and number2 % i == 0:
            if i > max_number:
                max_number = i

    print(max_number)

else:
    print("Enter valid positive numbers")