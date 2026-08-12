# Take two numbers and determine whether both are even, both are odd, or one is even and one is odd.
number1 = int(input("Enter the number 1: "))
number2 = int(input("Enter the number 2: "))

if number1 & 1 == 0 and number2 & 1 == 0:
    print("Both are even")

elif number1 & 1 != 0 and number2 & 1 != 0:
    print("Both are odd")

else:
    print("One is even and another one is odd")