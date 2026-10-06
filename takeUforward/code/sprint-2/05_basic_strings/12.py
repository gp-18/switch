# Reverse Words in a String
# Given an input string `s`, reverse the order of the words. Return a string of the words in reverse order joined by a single space, removing leading, trailing, and multiple spaces between words.
#
# Example 1:
# Input: s = 'the sky is blue'
# Output: 'blue is sky the'
#
# Example 2:
# Input: s = '  hello world  '
# Output: 'world hello'
#
# Example 3 (Edge Case - Multiple Spaces Between Words):
# Input: s = 'a good   example'
# Output: 'example good a'

s = input("Enter the string : ")

print(f"Your string is : '{s}' and now doing the operations on it.")

result = ""
word = ""

for char in s:
    if char != " ":
        word += char
    else:
        if word:
            result += word[::-1] + " "
            word = ""

if word:
    result += word[::-1]

result = result[::-1]

print(f"String after reversing the words : {result}")