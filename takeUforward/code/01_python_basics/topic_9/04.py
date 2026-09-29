# Use a ternary expression to label a number as even or odd.

# Example 1:
# Input: 14
# Output: "even"

# Example 2:
# Input: 9
# Output: "odd"

num = int(input("Enter an integer: "))

# Ternary expression: <val_if_true> if <condition> else <val_if_false>
result = "even" if num % 2 == 0 else "odd"
print(f'"{result}"')
