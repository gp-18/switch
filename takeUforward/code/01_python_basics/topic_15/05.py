# Write a function with **kwargs that prints each key-value pair; explain what type kwargs is.

# Example 1:
# Input: display_info(name="Alice", age=25)
# Output:
# name: Alice
# age: 25
# Note: kwargs is of type <class 'dict'>

# Example 2:
# Input: display_info(city="Paris", country="France", role="Developer")
# Output:
# city: Paris
# country: France
# role: Developer

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print(f"Note: kwargs is of type {type(kwargs)}")

display_info(name="Alice", age=25)
print()
display_info(city="Paris", country="France", role="Developer")
