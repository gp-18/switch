# Check palindrome using recursion
# Given a string `s`, check if it is a palindrome using recursion by comparing characters from both ends. Return True or False.
#
# Example 1:
# Input: s = "racecar"
# Output: True
#
# Example 2:
# Input: s = "hello"
# Output: False
#
# Example 3 (Edge Case):
# Input: s = "a"
# Output: True
#

s = input("Enter the string : ")

print(f"Your string is : '{s}' and now doing the operations on it.")
def is_palindrome(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return is_palindrome(s, left + 1, right - 1)

print(is_palindrome(s, 0, len(s) - 1))
