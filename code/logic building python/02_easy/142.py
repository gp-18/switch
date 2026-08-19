# Count the number of digits, letters, and special characters in a string.


if (string := input("Enter the string: ")):
    digits = 0
    letters = 0
    special_characters = 0

    for char in string:
        if ('0' <= char <= '9'):
            digits += 1

        elif ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            letters += 1

        else:
            special_characters += 1

    print("Digits:", digits)
    print("Letters:", letters)
    print("Special characters:", special_characters)

else:
    print("Enter a valid string")