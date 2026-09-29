# Check whether a character is a vowel using in and a case-insensitive comparison.

# Example 1:
# Input: 'E'
# Output: 'E' is a vowel

# Example 2:
# Input: 'b'
# Output: 'b' is not a vowel

char = input("Enter a character: ").strip()

vowels = "aeiou"
if len(char) == 1 and char.isalpha():
    if char.lower() in vowels:
        print(f"'{char}' is a vowel")
    else:
        print(f"'{char}' is not a vowel")
else:
    print("Please enter a single alphabet character.")
