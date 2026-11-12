# Maximum Nesting Depth of the Parentheses
# Given a valid parentheses string s containing digits 0-9, arithmetic operators,
# and parentheses '(' and ')'.
# Return the maximum nesting depth of parentheses in s.
#
# Example 1:
# Input:  s = "(1+(2*3)+((8)/4))+1"
# Output: 3
# Explanation: Deepest nested sub-expression is ((8)/4) with depth 3.
#
# Example 2:
# Input:  s = "(1)+((2))+(((3)))"
# Output: 3
#
# Example 3:
# Input:  s = "()(())((()()))"
# Output: 3
#
# Think About:
# - Use an integer counter `depth` to track currently open parentheses (no stack needed).
# - On '(': increment depth += 1 and update max_depth = max(max_depth, depth).
# - On ')': decrement depth -= 1.
# - Ignore digits and operators.
# - Time Complexity: O(N)
# - Space Complexity: O(1) auxiliary space
#

s = input("Enter a valid parentheses string : ").strip()

print(f"Your input string : '{s}'")

# Write your solution below:
# Optimal Approach: Depth Counter (Single Pass)
# Time Complexity: O(N) | Space Complexity: O(1)

def max_depth(paren_str):
    depth = 0
    best_depth = 0

    for c in paren_str:
        if c == '(':
            depth += 1
            best_depth = max(best_depth, depth)
        elif c == ')':
            depth -= 1

    return best_depth

ans = max_depth(s)

print(f"The maximum nesting depth is : {ans}")
