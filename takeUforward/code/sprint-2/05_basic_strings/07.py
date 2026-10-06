# Palindrome Check
# Given a string `s`, return True if the string reads the same backward as forward, otherwise False (exact match, case-sensitive).
#
# Example 1:
# Input: s = 'racecar'
# Output: True
#
# Example 2:
# Input: s = 'hello'
# Output: False
#
# Example 3 (Edge Case - Case Sensitivity):
# Input: s = 'Racecar'
# Output: False  # 'R' != 'r'

s = input("Enter the string : ")

print(f"Your string is : '{s}' and now doing the operations on it.")

if s == s[::-1] : 
    print("True")
else : 
    print("False")
