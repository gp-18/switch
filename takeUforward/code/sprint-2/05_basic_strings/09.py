# Length of Last Word
# Given a string `s` consisting of words and spaces, return the length of the last word in the string.
#
# Example 1:
# Input: s = 'Hello World'
# Output: 5  # Last word is 'World'
#
# Example 2:
# Input: s = '   fly me   to   the moon  '
# Output: 4  # Last word is 'moon'
#
# Example 3 (Edge Case - Single Word with Trailing Spaces):
# Input: s = 'a '
# Output: 1

s = input("Enter the string : ")

print(f"Your string is : '{s}' and now doing the operations on it.")

length_of_last_word = 0
current_word_length = 0

for char in s:
    if char != " ":
        current_word_length += 1
    elif current_word_length > 0:
        length_of_last_word = current_word_length
        current_word_length = 0

if current_word_length > 0:
    length_of_last_word = current_word_length

print(f"Length of last word : {length_of_last_word}")