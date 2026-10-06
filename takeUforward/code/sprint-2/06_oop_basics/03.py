# Q3. Deposit
#
# Task:
# Add a `deposit(amount)` method to `BankAccount`.
# - `amount` must be a strictly positive number (> 0).
# - If `amount` is zero or negative, raise a `ValueError`.
# - Otherwise, add the amount to `__balance` and return the new balance.
#
# Explanation:
# - State Mutation via Business Logic:
#   * Encapsulating balance changes inside a method ensures invariants are upheld (e.g., you cannot deposit negative money).
#   * Returning the updated state allows callers to immediately inspect the result of the operation.
#
# Example / Test Case:
# acc = BankAccount("Parth", 1000)
# assert acc.deposit(500) == 1500
# # acc.deposit(0)    -> ValueError
# # acc.deposit(-10)  -> ValueError

# Write your BankAccount class here:

class BankAccount : 
    def __init__(self , name , balance) :
        self.__balance = balance 
        self.__name = name 

    def deposit(self , amount) :

        if amount <= 0 :
            raise ValueError("Amount must be greater than 0.")
        
        self.__balance += amount 
        
        return self.__balance





# ==================== TEST CASES ====================
# if __name__ == "__main__":
#     acc = BankAccount("Parth", 1000)
#     assert acc.deposit(500) == 1500
#
#     try:
#         acc.deposit(0)
#         assert False, "Should raise ValueError for zero deposit"
#     except ValueError:
#         pass
#
#     try:
#         acc.deposit(-10)
#         assert False, "Should raise ValueError for negative deposit"
#     except ValueError:
#         pass
#
#     print("Q3 passed successfully!")
