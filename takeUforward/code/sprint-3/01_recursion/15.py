# Length of a string using recursion
# Given a string `s`, find and return its length using recursion without using the built-in len() function.
#
# Example 1:
# Input: s = "hello"
# Output: 5
#
# Example 2:
# Input: s = ""
# Output: 0
#
# Example 3 (Edge Case):
# Input: s = "recursion"
# Output: 9
#

s = input("Enter the string : ")

print(f"Your string is : '{s}' and now doing the operations on it.")
def string_length(s):
    if s == "":
        return 0
    return 1 + string_length(s[1:])

print(string_length(s))
