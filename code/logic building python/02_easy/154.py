# Replace all spaces in a string with '_'.

if (string := input("Enter the string: ")):

    new_string = ""

    for char in string:
        if char.lower() == " ":
            new_string += "_"
        else:
            new_string += char

    print(new_string)

else:
    print("Enter a valid string")