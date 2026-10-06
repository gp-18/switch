# Q9. Replace getters and setters with @property
#
# Task:
# Rewrite the class the Pythonic way using `@property`:
# - `name`: Has a getter `@property` and a validating setter `@name.setter`.
# - `balance`: Has a getter `@property` only (read-only, no setter).
#
# Explanation:
# - Why `@property`?
#   * In languages like Java, `getName()` and `setName()` are standard.
#   * In Python, `@property` allows accessing methods using attribute syntax (`acc.name`, `acc.balance`) while
#     still retaining the power to validate on assignment or compute values dynamically.
#   * If you don't define a setter for `balance`, attempting `acc.balance = 5000` automatically raises an `AttributeError`.
#
# Example / Test Case:
# acc = BankAccount("Parth", 1000)
# acc.name = "Rahul"            # uses the setter
# assert acc.name == "Rahul"
# assert acc.balance == 1000
# # acc.balance = 5000          -> AttributeError (no setter)

# Write your BankAccount class here:

class BankAccount:
    def __init__(self, name, balance=0):
        self.setName(name)
        self.setBalance(balance)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        value = value.strip()
        if not value:
            raise ValueError("Name cannot be empty.")
        self.__name = value

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self , value) : 
        if value < 0 :
            raise ValueError("Amount cannot be negative.")
        self.__balance = value
    
    @property
    def withdraw(self , amount) : 
        if amount < 0 :
            raise ValueError("Amount cannot be negative.")
        if amount > self.__balance :
            return False
        self.__balance -= amount
        return True

    @property
    def deposit(self , amount) : 
        if amount < 0 :
            raise ValueError("Amount cannot be negative.")
        self.__balance += amount
        return self.__balance
    



# ==================== TEST CASES ====================
# if __name__ == "__main__":
#     acc = BankAccount("Parth", 1000)
#     acc.name = "Rahul"
#     assert acc.name == "Rahul"
#     assert acc.balance == 1000
#
#     try:
#         acc.balance = 5000
#         assert False, "Direct assignment to balance should raise AttributeError"
#     except AttributeError:
#         pass
#
#     print("Q9 passed successfully!")
