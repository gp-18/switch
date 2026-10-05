# Given a list of Boolean values, determine whether at least one value is True and whether all values are True.

# Example 1:
# Input: flags = [True, False, True]
# Output: Any True: True, All True: False

# Example 2:
# Input: flags = [True, True, True]
# Output: Any True: True, All True: True

flags = [True, False, True]
print(f"Any True: {any(flags)}, All True: {all(flags)}")
