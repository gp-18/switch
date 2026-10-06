# Count Words in a String
# Given a string `s`, count the total number of words separated by one or more spaces.
#
# Example 1:
# Input: s = 'The quick brown fox'
# Output: 4
#
# Example 2:
# Input: s = '   hello   world   '
# Output: 2  # Handles leading/trailing and consecutive spaces
#
# Example 3 (Edge Case - String with Only Spaces):
# Input: s = '    '
# Output: 0

s = input("Enter the string : ")

print(f"Your string is : '{s}' and now doing the operations on it.")

word_count = 0
in_word = False

for char in s:
    if char != " ":
        if not in_word:
            word_count += 1
            in_word = True
    else:
        in_word = False

print(f"Number of words : {word_count}")