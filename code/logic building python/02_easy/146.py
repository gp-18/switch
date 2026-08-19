# Reverse a string without using built-in reverse.

if (string := input("Enter the string: ")) and len(string) >= 1:

    reverse = ""
    for char in string : 
        reverse = char + reverse

    print(reverse)

else:
    print("Enter a valid string")