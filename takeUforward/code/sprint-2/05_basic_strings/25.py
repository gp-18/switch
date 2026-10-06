# Remove Outermost Parentheses
# A valid parentheses string is decomposed into primitive parts. Return the string after removing the outermost parentheses of every primitive part.
#
# Example 1:
# Input: s = '(()())(())'
# Output: '()()()'
#
# Example 2:
# Input: s = '(()())(())(()(()))'
# Output: '()()()()(())'
#
# Example 3 (Edge Case - Single Primitive Block):
# Input: s = '()()'
# Output: ''

s = input("Enter the string : ")

print(f"Your string is : '{s}' and now doing the operations on it.")

result = ""
opened = 0

for char in s:
    if char == '(':
        if opened > 0:
            result += char
        opened += 1
    elif char == ')':
        opened -= 1
        if opened > 0:
            result += char

print(f"String after removing outermost parentheses : '{result}'")




