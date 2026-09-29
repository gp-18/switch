# Write greet(name) that returns a greeting string; print the returned value in the caller.

# Example 1:
# Input: greet("Alice")
# Output: "Hello, Alice!"

# Example 2:
# Input: greet("Bob")
# Output: "Hello, Bob!"

def greet(name: str) -> str:
    return f"Hello, {name}!"

# Caller demonstration
greeting1 = greet("Alice")
print(f'"{greeting1}"')

greeting2 = greet("Bob")
print(f'"{greeting2}"')
