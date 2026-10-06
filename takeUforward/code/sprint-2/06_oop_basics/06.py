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
class BankAccount:
    def __init__(self, name, balance=0):
        self.setName(name)
        self.setBalance(balance)

    def setBalance(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative.")

        self.__balance = amount

    def getBalance(self):
        return self.__balance

    def setName(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")

        name = name.strip()

        if not name:
            raise ValueError("Name cannot be empty.")

        self.__name = name

    def getName(self):
        return self.__name


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
