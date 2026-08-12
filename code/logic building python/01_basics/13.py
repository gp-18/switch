# Check whether a given integer is single-digit, double-digit, or multi-digit.


number = int(input("Enter an integer: "))

if -9 <= number <= 9:
    print("Single-digit")
elif -99 <= number <= 99:
    print("Double-digit")
else:
    print("Multi-digit")