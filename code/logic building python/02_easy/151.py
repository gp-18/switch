# Remove all vowels from a string.
# Example 1: Input: 'a' -> Output: Vowel
# Example 2: Input: 'b' -> Output: Consonant

if (string := input("Enter the string: ")) and len(string) >= 2:

    new_string = ""

    for char in string : 
        if char.lower() not in "aeiou" :
            new_string += char 

    print(new_string)

else:
    print("Enter a valid string with at least 2 characters")
