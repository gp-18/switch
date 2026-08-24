# Print the string after removing all digit characters.

if (string := input("Enter the string: ")) and len(string) >= 1:

    new_string = ""

    for char in string:
        if not char.isdigit():
            new_string += char

    print(new_string)

else:
    print("Give correct string")