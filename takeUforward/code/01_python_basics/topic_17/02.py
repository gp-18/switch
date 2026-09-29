# Fix a program that tries to add an integer directly to the string returned by input().

# Example 1:
# Input (buggy): age = input("Age: ") ; next_year = age + 1  (TypeError: can only concatenate str to str)
# Output (fixed): age = int(input("Age: ")) ; next_year = age + 1  (e.g., "25" -> 25 + 1 = 26)

# Example 2:
# Input: user enters "10"
# Output: int("10") + 5 = 15

# Buggy code:
# age = input("Age: ")
# next_year = age + 1  # Raises TypeError: can only concatenate str (not "int") to str

# Fixed code:
age_input = "25"  # Simulating input
age = int(age_input)
next_year = age + 1
print(f"Age: {age}, Next year: {next_year}")

# Example 2 demonstration:
user_entry = "10"
print(f"int('{user_entry}') + 5 = {int(user_entry) + 5}")
