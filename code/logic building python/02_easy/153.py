# Replace all vowels in a string with '*'.

if (string := input("Enter the string: ")):

    new_string = ""

    for char in string:
        if char.lower() in "aeiou":
            new_string += "*"
        else:
            new_string += char

    print(new_string)

else:
    print("Enter a valid string")