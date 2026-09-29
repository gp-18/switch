# Given a word, print its first and last characters safely; handle an empty string.

# Example 1:
# Input: word = "Python"
# Output: First: P, Last: n

# Example 2:
# Input: word = ""
# Output: String is empty


word = str(input("Enter a word: ")) 


if len(word) == 0:
    print("String is empty")
else:
    first_char = word[0]
    last_char = word[-1]
    print(f"First: {first_char}, Last: {last_char}")