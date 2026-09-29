# Fix a program that uses = instead of == in a condition.

# Example 1:
# Input (buggy): if x = 5: print("five")  (SyntaxError: invalid syntax)
# Output (fixed): if x == 5: print("five")

# Example 2:
# Input: x = 10; check if x == 10
# Output: True (properly evaluates equality)

# Buggy code:
# if x = 5:  # SyntaxError: invalid syntax (assignment operator '=' used instead of equality '==')
#     print("five")

# Fixed code:
x = 5
if x == 5:
    print("five")

x = 10
print(f"x == 10: {x == 10}")
