# Call a function using keyword arguments in a different order from its parameter list.

# Example 1:
# Input: def describe_person(name, age): ... -> describe_person(age=25, name="Alice")
# Output: "Name: Alice, Age: 25"

# Example 2:
# Input: def order(item, qty): ... -> order(qty=3, item="Coffee")
# Output: "Order: 3 x Coffee"

def describe_person(name: str, age: int) -> str:
    return f"Name: {name}, Age: {age}"

def order(item: str, qty: int) -> str:
    return f"Order: {qty} x {item}"

# Calling with keyword arguments out of order
print(f'"{describe_person(age=25, name="Alice")}"')
print(f'"{order(qty=3, item="Coffee")}"')
