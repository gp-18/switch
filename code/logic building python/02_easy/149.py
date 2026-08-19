# Print the middle character(s) of a string.

if (string1 := input("Enter the string: ")) and len(string1) >= 1:

    mid = len(string1) // 2

    if len(string1) % 2 != 0:
        print(string1[mid])

    else:
        print(string1[mid - 1], string1[mid])

else:
    print("Enter the correct string1")