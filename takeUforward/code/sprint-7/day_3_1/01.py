# Remove Outermost Parentheses
# Given a valid parentheses string s, consider its primitive decomposition:
# s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
# Return s after removing the outermost parentheses of every primitive string.
#
# Example 1:
# Input:  s = "((()))"
# Output: "(())"
#
# Example 2:
# Input:  s = "()(()())(())"
# Output: "()()()"
#
# Example 3:
# Input:  s = "()(())((()))"
# Output: "()(())"
#
# Think About:
# - Use an integer balance counter to track nesting depth without needing a stack.
# - For '(': append to result only if balance > 0 (not outermost opener), then increment balance.
# - For ')': decrement balance first, then append to result only if balance > 0 (not outermost closer).
# - Collect characters in a list and join at the end to guarantee O(N) string construction.
# - Time Complexity: O(N)
# - Space Complexity: O(N) for the result string (O(1) extra space)
#

s = input("Enter a valid parentheses string : ").strip()

print(f"Your input string : '{s}'")

# Write your solution below:
# Optimal Approach: Balance Counter (Single Pass)
# Time Complexity: O(N) | Space Complexity: O(N)

def remove_outer_parentheses(paren_str):
    res = []
    balance = 0

    for ch in paren_str:
        if ch == '(':
            # Append '(' only if we are already inside a primitive (depth > 0)
            if balance > 0:
                res.append(ch)
            balance += 1
        else:
            # Decrement depth first; if it stays > 0, it's an inner closing bracket
            balance -= 1
            if balance > 0:
                res.append(ch)

    return ''.join(res)

ans = remove_outer_parentheses(s)

print(f"After removing outermost parentheses : '{ans}'")
