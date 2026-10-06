# Maximum Nesting Depth of the Parentheses
# Given a valid parentheses string `s`, return the maximum nesting depth of parentheses in `s`.
#
# Example 1:
# Input: s = '(1+(2*3)+((8)/4))+1'
# Output: 3
#
# Example 2:
# Input: s = '(1)+((2))+(((3)))'
# Output: 3
#
# Example 3 (Edge Case - No Parentheses):
# Input: s = '1+2+3'
# Output: 0

s = input("Enter the string : ")

print(f"Your string is : '{s}' and now doing the operations on it.")

current_depth = 0
max_depth = 0

for char in s:
    if char == '(':
        current_depth += 1
        if current_depth > max_depth:
            max_depth = current_depth
    elif char == ')':
        current_depth -= 1

print(f"Maximum nesting depth : {max_depth}")

