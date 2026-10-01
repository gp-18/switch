# Check whether a number is between 1 and 100 inclusive using a chained comparison.

# Example 1:
# Input: 50
# Output: True (1 <= 50 <= 100)

# Example 2:
# Input: 105
# Output: False

num = float(input("Enter a number: "))
num_val = int(num) if num.is_integer() else num

# Chained comparison
is_between = 1 <= num_val <= 100
if is_between:
    print(f"{is_between} (1 <= {num_val} <= 100)")
else:
    print(f"{is_between}")
