# Remove all spaces from a string.

if (string := input("Enter the string: ")):

    new_string = ""

    for char in string:
        if char != " ":
            new_string += char

    print(new_string)

else:
    print("Enter a valid string")