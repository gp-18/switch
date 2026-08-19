# Count how many characters (excluding spaces) are in a string.
if (string := input("Enter the string: ")) and len(string) >= 1:
    count = 0

    for char in string:
        if char != " ":
            count += 1

    print(count)

else:
    print("Enter a valid string")