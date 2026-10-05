# Remove Duplicate Characters from a String
# Given a string `s`, remove all duplicate characters, keeping only the first occurrence of each character in its original relative order.
#
# Example 1:
# Input: s = 'programming'
# Output: 'progami'
#
# Example 2:
# Input: s = 'banana'
# Output: 'ban'
#
# Example 3 (Edge Case - All Identical Characters):
# Input: s = 'zzzz'
# Output: 'z'

s = input("Enter the string : ")

print(f"Your string is : {s} and now doing the operations on it.")

seen = set()
result = ""

for char in s:
    if char not in seen:
        seen.add(char)
        result += char

print(f"The string after removing duplicates is : {result}")