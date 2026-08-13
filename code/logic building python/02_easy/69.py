character = input("Enter the character: ")

if len(character) != 1:
    print("Only one character is allowed")
elif character.isdigit():
    print("Yes, it's a digit")
elif character.isalpha():
    print("Yes, it's a letter")
else:
    print("Neither")