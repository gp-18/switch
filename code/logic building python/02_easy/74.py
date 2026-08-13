# Take two numbers and check if both are positive and their sum is less than 100.

if (number1 := int(input("Enter the number 1: "))) > 0 and (number2 := int(input("Enter the number 2: "))) > 0:
    print("Yes") if number1 + number2 < 100 else print("No")
else:
    print("Invalid input")