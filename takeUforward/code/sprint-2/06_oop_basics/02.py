# Q2. Setter with validation
#
# Task:
# Add a `setName(name)` method to `BankAccount`.
# - Reject non-string values by raising a `TypeError`.
# - Strip extra leading and trailing whitespace before storing the name.
# - Reject empty or whitespace-only names by raising a `ValueError`.
#
# Explanation:
# - Encapsulation & Validation:
#   * Directly exposing attributes allows outside code to assign invalid data (e.g. `acc.name = ""` or `acc.name = 123`).
#   * A setter method (`setName`) acts as a gatekeeper, validating and sanitizing data before modifying state.
# - `isinstance(name, str)`: Checks if the incoming argument is indeed a string.
# - `name.strip()`: Removes leading/trailing spaces. If the resulting string is empty, raise `ValueError`.
#
# Example / Test Case:
# acc = BankAccount("Parth", 1000)
# acc.setName("  Rahul  ")
# assert acc.getName() == "Rahul"
# # acc.setName("")   -> ValueError
# # acc.setName(123)  -> TypeError

# Write your BankAccount class here:



# ==================== TEST CASES ====================
# if __name__ == "__main__":
#     acc = BankAccount("Parth", 1000)
#     acc.setName("  Rahul  ")
#     assert acc.getName() == "Rahul"
#
#     try:
#         acc.setName("")
#         assert False, "Should raise ValueError for empty name"
#     except ValueError:
#         pass
#
#     try:
#         acc.setName(123)
#         assert False, "Should raise TypeError for non-string name"
#     except TypeError:
#         pass
#
#     print("Q2 passed successfully!")
