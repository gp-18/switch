# ============================================================
# Problem: Bank Account Operations
# Difficulty: Easy
# ============================================================
#
# PROBLEM STATEMENT:
# Create a BankAccount class initialized with an account holder
# and starting balance. Implement deposit(amount) and withdraw(amount)
# methods. Reject non-positive amounts and withdrawals greater than
# the available balance.
# Implement solution() to execute operations and return the final balance.
#
# INPUT:
# - account_holder: string
# - initial_balance: non-negative integer
# - operations: list of tuples (operation_type, amount)
#
# OUTPUT:
# - Final balance as integer
#
# EXAMPLE:
# Input:  ("Asha", 1000, [("deposit", 500), ("withdraw", 200), ("withdraw", 2000)])
# Output: 1300
#
# CONSTRAINTS:
# - initial_balance >= 0
# - operations contains valid operation strings: "deposit" or "withdraw"
# ============================================================

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder 
        self.balance = balance 

    def deposit(self, amount):
        if amount > 0 : 
            self.balance += amount 
        else : 
            return None 

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance :
            self.balance -= amount 
        else :
            return None

    def get_balance(self):
        return self.balance


def solution(account_holder, initial_balance, operations):
    # Execute operations and return final balance
    s = BankAccount(account_holder, initial_balance) 
    for i in operations :
        if i[0] == "deposit" : 
            s.deposit(i[1])
        elif i[0] == "withdraw" : 
            s.withdraw(i[1])
    return s.get_balance() 


# ---- TEST CASES ----
assert solution("Asha", 1000, [("deposit", 500), ("withdraw", 200), ("withdraw", 2000)]) == 1300, "Test 1 Failed"
assert solution("Raj", 500, [("deposit", -100), ("deposit", 300), ("withdraw", 900), ("withdraw", 200)]) == 600, "Test 2 Failed"
assert solution("Rahul", 100, [("withdraw", 100), ("deposit", 50)]) == 50, "Test 3 Failed"
assert solution("Sneha", 200, [("withdraw", 0), ("deposit", 0)]) == 200, "Test 4 Failed"

print("All test cases passed!")
