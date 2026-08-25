# Check if a string contains any special character.
# Example 1: Input: 'hello@world' -> Output: Contains special characters
# Example 2: Input: 'python123' -> Output: No special characters

import string

text = input("Enter a string: ")

special_chars = set(string.punctuation)
has_special = any(char in special_chars for char in text)

if has_special:
    print("Contains special characters")
else:
    print("No special characters")
