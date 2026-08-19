# Count uppercase and lowercase letters in a string.

if (string := input("Enter the string: ")):
    uppercase = 0
    lowercase = 0

    for char in string:
        if 'A' <= char <= 'Z':
            uppercase += 1

        elif 'a' <= char <= 'z':
            lowercase += 1

    print("Uppercase letters:", uppercase)
    print("Lowercase letters:", lowercase)

else:
    print("Enter a valid string")