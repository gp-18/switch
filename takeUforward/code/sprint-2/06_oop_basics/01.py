# Q1. Create the class and getters
#
# Task:
# Create a `BankAccount` class with private attributes `__name` and `__balance`, initialized in `__init__`.
# Add getter methods `getName()` and `getBalance()` to access them.
#
# Explanation:
# - Attributes vs Methods:
#   * Attributes store the data/state of an object (e.g., name, balance).
#   * Methods define the behavior and operations on that data.
# - Private Attributes:
#   * Prefixing an attribute with double underscores (`self.__name`, `self.__balance`) triggers
#     Python's name mangling, keeping the internal representation hidden from casual outside access.
# - Getters:
#   * Public methods like `getName()` and `getBalance()` provide controlled, read-only access to
#     private attributes without exposing them directly.
#
# Example / Test Case:
# acc = BankAccount("Parth", 1000)
# assert acc.getName() == "Parth"
# assert acc.getBalance() == 1000

# Write your BankAccount class here:


class BankAccount:
    def __init__(self , name , balance) :
        self.__name = name 
        self.__balance = balance 

    def getName(self) :
        return self.__name

    def getBalance(self) :
        return self.__balance


# ==================== TEST CASES ====================
# if __name__ == "__main__":
#     acc = BankAccount("Parth", 1000)
#     assert acc.getName() == "Parth"
#     assert acc.getBalance() == 1000
#     print("Q1 passed successfully!")
