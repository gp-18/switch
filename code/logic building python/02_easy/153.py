# Replace all vowels in a string with '*'.
# Example 1: Input: 'a' -> Output: Vowel
# Example 2: Input: 'b' -> Output: Consonant

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
