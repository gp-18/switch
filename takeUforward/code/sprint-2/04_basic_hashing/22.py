# Check if a String is a Pangram
# A pangram is a sentence where every letter of the English alphabet appears at least once. Return True if the given string `s` is a pangram, otherwise False (ignore case).
#
# Example 1:
# Input: s = 'thequickbrownfoxjumpsoverthelazydog'
# Output: True
#
# Example 2:
# Input: s = 'takeuforward'
# Output: False  # Missing several alphabet letters
#
# Example 3 (Edge Case - Uppercase Letters and Punctuation):
# Input: s = 'The quick brown fox jumps over the lazy dog!'
# Output: True

s = input("Enter the string : ")

print(f"Your string is : {s} and now doing the operations on it.")

s = s.lower()

seen = set()

for char in s:
    if 'a' <= char <= 'z':
        seen.add(char)

if len(seen) == 26:
    print("True")
else:
    print("False")