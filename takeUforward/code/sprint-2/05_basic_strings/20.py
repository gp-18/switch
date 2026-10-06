# Rotate String
# Given two strings `s` and `goal`, return True if and only if `s` can become `goal` after some number of cyclic shifts.
#
# Example 1:
# Input: s = 'abcde', goal = 'cdeab'
# Output: True
#
# Example 2:
# Input: s = 'abcde', goal = 'abced'
# Output: False
#
# Example 3 (Edge Case - Different Lengths):
# Input: s = 'aa', goal = 'a'
# Output: False

s = input("Enter the first string : ")
goal = input("Enter the goal string : ")

print(f"Your string is : '{s}', goal is : '{goal}' and now doing the operations on it.")

if len(s) != len(goal):
    print("False")
elif goal in s + s:
    print("True")
else:
    print("False")