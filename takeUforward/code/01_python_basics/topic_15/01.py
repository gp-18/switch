# Write a greet(name, greeting="Hello") function and call it with and without the second argument.

# Example 1:
# Input: greet("Alice")
# Output: "Hello, Alice!" (uses default "Hello")

# Example 2:
# Input: greet("Bob", greeting="Welcome")
# Output: "Welcome, Bob!"

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Call without the second argument (uses default)
print(f'"{greet("Alice")}"')

# Call with the second argument
print(f'"{greet("Bob", greeting="Welcome")}"')
