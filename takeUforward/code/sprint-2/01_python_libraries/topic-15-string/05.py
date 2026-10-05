# Create a simple character-validation function using ascii_letters and digits.

# Example 1:
# Input: is_valid_username("user_99")
# Output: True (letters, digits, underscore allowed)

# Example 2:
# Input: is_valid_username("user#1")
# Output: False

import string

allowed = set(string.ascii_letters + string.digits + "_")

def is_valid_username(name):
    return len(name) > 0 and all(c in allowed for c in name)

print(is_valid_username("user_99"))
print(is_valid_username("user#1"))
