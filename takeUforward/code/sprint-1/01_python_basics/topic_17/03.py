# Fix a string-cleaning program that calls .upper() but discards the returned string.

# Example 1:
# Input (buggy): text = "hello"; text.upper(); print(text)  (prints "hello" because strings are immutable)
# Output (fixed): text = "hello"; text = text.upper(); print(text)  (prints "HELLO")

# Example 2:
# Input: s = "python"; s = s.upper()
# Output: "PYTHON"

# Buggy code:
# text = "hello"
# text.upper()  # String methods do not modify in-place; strings are immutable
# print(text)   # Still prints "hello"

# Fixed code:
text = "hello"
text = text.upper()
print(text)

s = "python"
s = s.upper()
print(s)
