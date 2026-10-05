# Demonstrate the difference between find() and index() when the target is missing.

# Example 1:
# Input: "hello".find("z")
# Output: -1 (safe, returns -1)

# Example 2:
# Input: "hello".index("z")
# Output: Raises ValueError: substring not found

print("hello".find("z"))
try:
    "hello".index("z")
except ValueError as e:
    print(f"Raises ValueError: {e}")
