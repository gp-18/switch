# Take a password string and check basic rules
# (length >= 8 and contains at least one digit).

password = input("Enter the string: ")

if len(password) >= 8 and any(character.isdigit() for character in password):
    print("Yes")
else:
    print("No")