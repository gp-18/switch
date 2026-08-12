# Take an alphabet character and check if it lies between 'a' and 'm' or 'n' and 'z'.

character = input("Enter the character: ")

if 97 <= ord(character) <= 109:
    print("Lies between a to m")
elif 110 <= ord(character) <= 122:
    print("Lies between n to z")
else:
    print("Not a lowercase alphabet character")