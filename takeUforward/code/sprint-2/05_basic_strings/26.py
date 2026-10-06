# Longest Word in a Sentence
# Given a sentence string `s`, find and return the word with the maximum length. If there is a tie, return the first occurring longest word.
#
# Example 1:
# Input: s = 'The quick brown fox jumped over the lazy dog'
# Output: 'jumped'
#
# Example 2:
# Input: s = 'I love programming in Python'
# Output: 'programming'
#
# Example 3 (Edge Case - Tie in Word Length):
# Input: s = 'cat dog fox'
# Output: 'cat'  # First longest word

s = input("Enter the sentence : ")

print(f"Your sentence is : '{s}' and now doing the operations on it.")

current_word = ""
longest_word = ""

for char in s:
    if char != " ":
        current_word += char
    else:
        if len(current_word) > len(longest_word):
            longest_word = current_word

        current_word = ""

if len(current_word) > len(longest_word):
    longest_word = current_word

print(f"Longest word : '{longest_word}'")
print(f"Length of longest word : {len(longest_word)}")