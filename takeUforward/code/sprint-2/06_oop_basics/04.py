# Q4. Withdraw
#
# Task:
# Add a `withdraw(amount)` method to `BankAccount`.
# - Reject zero or negative amounts with a `ValueError`.
# - If `amount` exceeds the current balance, print "Insufficient amount" and return `False` (balance remains unchanged).
# - Otherwise, subtract `amount` from `__balance` and return `True`.
#
# Explanation:
# - Exceptions vs Return Values:
#   * Invalid input arguments (e.g. negative numbers) represent programming or client errors, so raise `ValueError`.
#   * Legitimate operational failures (e.g. insufficient funds) are often handled by returning status codes or booleans (`False`),
#     leaving the object state intact.
#
# Example / Test Case:
# acc = BankAccount("Parth", 1000)
# assert acc.withdraw(300) is True
# assert acc.getBalance() == 700
# assert acc.withdraw(5000) is False
# assert acc.getBalance() == 700   # unchanged

# Write your BankAccount class here:
class BankAccount : 
    def __init__(self , name , balance) :
        self.__balance = balance 
        self.__name = name 

    def withdraw(self , amount) :

        if amount <= 0 :
            raise ValueError("Amount must be greater than 0.")
        
        if amount > self.__balance :
            print("Insufficient amount")
            return False
        
        self.__balance -= amount 
        
        return True


# ==================== TEST CASES ====================
# if __name__ == "__main__":
#     acc = BankAccount("Parth", 1000)
#     assert acc.withdraw(300) is True
#     assert acc.getBalance() == 700
#     assert acc.withdraw(5000) is False
#     assert acc.getBalance() == 700
#
#     try:
#         acc.withdraw(0)
#         assert False, "Should raise ValueError for zero withdrawal"
#     except ValueError:
#         pass
#
#     try:
#         acc.withdraw(-10)
#         assert False, "Should raise ValueError for negative withdrawal"
#     except ValueError:
#         pass
#
#     print("Q4 passed successfully!")
