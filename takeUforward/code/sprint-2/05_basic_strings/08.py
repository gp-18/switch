# Remove All Spaces from a String
# Given a string `s`, remove every space character from the string and return the result.
#
# Example 1:
# Input: s = 'take u forward'
# Output: 'takeuforward'
#
# Example 2:
# Input: s = 'hello world'
# Output: 'helloworld'
#
# Example 3 (Edge Case - Multiple Consecutive Spaces):
# Input: s = '  a b  c   '
# Output: 'abc'

s = input("Enter the string : ")

print(f"Your string is : '{s}' and now doing the operations on it.")

without_space = ""
for char in s : 
    if char != " " : 
        without_space += char 

print(f"String without spaces : {without_space}")
