# Q7. String representation
#
# Task:
# Add `__str__` and `__repr__` magic methods to `BankAccount`.
# - `__str__`: Friendly text for users -> `"Account holder: <name> | Balance: <balance>"`
# - `__repr__`: Unambiguous text for developers -> `"BankAccount(name='<name>', balance=<balance>)"`
# - Never expose more than name and balance.
#
# Explanation:
# - `__str__(self)`:
#   * Called by `str(obj)` and `print(obj)`. It should be readable and user-friendly.
# - `__repr__(self)`:
#   * Called by `repr(obj)` and inside the interactive console / debugger.
#   * It should ideally look like valid Python code that could recreate the object: `BankAccount(name='Parth', balance=1000)`.
#
# Example / Test Case:
# acc = BankAccount("Parth", 1000)
# assert str(acc) == "Account holder: Parth | Balance: 1000"
# assert repr(acc) == "BankAccount(name='Parth', balance=1000)"

# Write your BankAccount class here:

class BankAccount : 
    def __init__(self , name , balance) : 
        self.__name = name 
        self.__balance = balance 

    def __str__(self) : 
        return f"Account holder : {self.__name} | Balance : {self.__balance}" 
    
    def __repr__(self) : 
        return f"BankAccount(name : {self.__name} , balance : {self.__balance})"



# ==================== TEST CASES ====================
# if __name__ == "__main__":
#     acc = BankAccount("Parth", 1000)
#     assert str(acc) == "Account holder: Parth | Balance: 1000"
#     assert repr(acc) == "BankAccount(name='Parth', balance=1000)"
#     print("Q7 passed successfully!")
