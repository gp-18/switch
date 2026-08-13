# Find LCM of two numbers using loops.

if (number1 := int(input("Enter the number 1: "))) > 0 and \
   (number2 := int(input("Enter the number 2: "))) > 0:

    max_number = max(number1, number2)

    for i in range(max_number, number1 * number2 + 1):
        if i % number1 == 0 and i % number2 == 0:
            print("LCM:", i)
            break

else:
    print("Enter valid positive numbers")