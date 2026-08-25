# Count how many vowels and consonants are in a string.
# Example 1: Input: 'a' -> Output: Vowel
# Example 2: Input: 'b' -> Output: Consonant

if (string := input("Enter the string: ")):
    vowels = 0
    consonants = 0

    for char in string:
        if char.isalpha():
            if char.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)

else:
    print("Enter a valid string")
