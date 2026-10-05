# Normalize a user-entered name using strip(), lower(), and title().

# Example 1:
# Input: name = "   jOhN dOE   "
# Output: "John Doe"

# Example 2:
# Input: name = "  ALICE  "
# Output: "Alice"

name = "   jOhN dOE   "
clean_name = name.strip().title()
print(f'"{clean_name}"')
