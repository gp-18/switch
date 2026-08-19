# Remove all vowels from a string.

if (string := input("Enter the string: ")) and len(string) >= 2:

    new_string = ""

    for char in string : 
        if char.lower() not in "aeiou" :
            new_string += char 

    print(new_string)

else:
    print("Enter a valid string with at least 2 characters")