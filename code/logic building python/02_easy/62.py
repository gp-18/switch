# Take a 3-digit number and determine if the middle digit is the largest, smallest, or neither.
number = list(map(int, input("Enter the 3 digit number: ")))

if len(number) != 3:
    print("Enter a valid 3 digit number")
else:
    if number[1] > number[0] and number[1] > number[2]:
        print("Middle number is the greatest")
    elif number[1] < number[0] and number[1] < number[2]:
        print("Middle number is the smallest")
    else:
        print("Neither")
