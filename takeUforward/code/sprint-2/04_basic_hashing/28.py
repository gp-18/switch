# Count Vowels and Consonants
# Given a string `s`, count the number of vowels (a, e, i, o, u, case-insensitive) and consonants (alphabetic characters that are not vowels). Ignore spaces, digits, and punctuation.
#
# Example 1:
# Input: s = 'takeuforward'
# Output: {'vowels': 5, 'consonants': 7}
#
# Example 2:
# Input: s = 'hello world'
# Output: {'vowels': 3, 'consonants': 7}
#
# Example 3 (Edge Case - No Vowels and Has Digits):
# Input: s = 'rhythm 123'
# Output: {'vowels': 0, 'consonants': 6}


s = input("Enter the string : ").lower()

print(f"Your string is : {s} and now doing the operations on it.")

freq = {
    'vowels': 0,
    'consonants': 0
}

for char in s:
    char = char.lower()

    if char in "aeiou":
        freq["vowels"] += 1
    elif char in "bcdfghjklmnpqrstvwxyz":
        freq["consonants"] += 1

print(freq)
