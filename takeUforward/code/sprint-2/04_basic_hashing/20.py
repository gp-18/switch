# First Repeating Character in a String
# Given a string `s`, find and return the first character that appears more than once (the one whose second occurrence comes earliest). If no character repeats, return -1.
#
# Example 1:
# Input: s = 'geeksforgeeks'
# Output: 'e'  # 'e' repeats earliest at index 2
#
# Example 2:
# Input: s = 'abcdef'
# Output: -1  # No repeating character
#
# Example 3 (Edge Case - Consecutive Identical Characters):
# Input: s = 'abbc'
# Output: 'b'  # 'b' repeats at index 2

s = input("Enter the string : ")

print(f"Your string is : {s} and now doing the operations on it.")

seen = set()

for char in s:
    if char in seen:
        print(char)
        break
    seen.add(char)
else:
    print("-1")

