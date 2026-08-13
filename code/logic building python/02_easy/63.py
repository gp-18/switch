# Take a 4-digit number and check if the first and last digits are equal.

number = list(map(int, input("Enter the 4 digit number :")))

if len(number) != 4 : 
    print("Enter the correct length")

if number[0] == number[len(number) -1 ] :
    print("yes first and last digit is equal")
else : 
    print("no it's not equal")