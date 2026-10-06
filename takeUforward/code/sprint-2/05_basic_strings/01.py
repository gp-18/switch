# Reverse a String
# Given a string `s`, return a new string with its characters reversed.
#
# Example 1:
# Input: s = 'hello'
# Output: 'olleh'
#
# Example 2:
# Input: s = 'Python'
# Output: 'nohtyP'
#
# Example 3 (Edge Case - Single Character / Palindrome):
# Input: s = 'a'
# Output: 'a'

s = input("Enter the string : ")

print(f"Your string is : '{s}' and now doing the operations on it.")

reverse_string = s[::-1]

print(reverse_string)