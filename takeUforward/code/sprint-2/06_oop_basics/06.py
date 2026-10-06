# Q6. Default values and safe initialisation
#
# Task:
# - In `__init__`, make `balance` default to `0`.
# - Reject a negative starting balance with a `ValueError`.
# - Reuse your `setName` validation inside `__init__` so validation rules live in one place.
#
# Explanation:
# - Default Arguments:
#   * Defining `def __init__(self, name, balance=0):` allows instantiating accounts without specifying initial balance.
# - DRY (Don't Repeat Yourself):
#   * Instead of duplicating type checks and whitespace stripping in `__init__`, call `self.setName(name)`
#     directly inside `__init__`.
#
# Example / Test Case:
# acc = BankAccount("Parth")
# assert acc.getBalance() == 0
# # BankAccount("Parth", -5)  -> ValueError
# # BankAccount("", 100)      -> ValueError

# Write your BankAccount class here:



# ==================== TEST CASES ====================
# if __name__ == "__main__":
#     acc = BankAccount("Parth")
#     assert acc.getBalance() == 0
#
#     try:
#         BankAccount("Parth", -5)
#         assert False, "Should raise ValueError for negative starting balance"
#     except ValueError:
#         pass
#
#     try:
#         BankAccount("", 100)
#         assert False, "Should raise ValueError for empty name"
#     except ValueError:
#         pass
#
#     print("Q6 passed successfully!")
