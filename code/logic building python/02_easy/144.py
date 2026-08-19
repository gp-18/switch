# Count how many times a given character appears in a string.

if (string := input("Enter the string: ")) and len(string) >= 1:

    keyword = input("Enter the character to search: ")

    if len(keyword) == 1:

        count = 0

        for char in string:
            if char == keyword:
                count += 1

        print("Count:", count)

    else:
        print("Enter only one character")

else:
    print("Enter a valid string")