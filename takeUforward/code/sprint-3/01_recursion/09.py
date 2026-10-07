# Reverse a string using recursion
# Given a string `s`, return the reversed string using recursion.
#
# Example 1:
# Input: s = "takeuforward"
# Output: "drawrofuwkat"
#
# Example 2:
# Input: s = "abcd"
# Output: "dcba"
#
# Example 3 (Edge Case):
# Input: s = ""
# Output: ""
#

s = input("Enter the string : ")

print(f"Your string is : '{s}' and now doing the operations on it.")
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string(s))
