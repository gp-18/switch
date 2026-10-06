# Swap First and Last Character
# Given a string `s`, swap its first and last characters and return the modified string.
#
# Example 1:
# Input: s = 'hello'
# Output: 'oellh'
#
# Example 2:
# Input: s = 'python'
# Output: 'nythop'
#
# Example 3 (Edge Case - Single Character String):
# Input: s = 'a'
# Output: 'a'

s = input("Enter the string : ")

print(f"Your string is : '{s}' and now doing the operations on it.")

if len(s) <= 1:
    new_string = s
else:
    new_string = s[-1] + s[1:len(s)-1] + s[0]

print(f"New string : {new_string}")