# Check whether every character in a string belongs to a chosen allowed character set.

# Example 1:
# Input: s = "abc123", allowed = string.ascii_lowercase + string.digits
# Output: True

# Example 2:
# Input: s = "abc-123", allowed = string.ascii_lowercase + string.digits
# Output: False (contains '-')

import string

allowed = set(string.ascii_lowercase + string.digits)
s = "abc123"
print(all(c in allowed for c in s))
