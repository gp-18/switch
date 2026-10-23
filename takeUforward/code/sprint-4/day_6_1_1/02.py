# Q2. Bank Account with Audit Log (Practice - Encapsulation)
#
# Task:
# Design a `BankAccount` class where the balance and transaction history cannot be
# directly altered from outside, preventing balance tampering and maintaining a reliable audit trail.
#
# Attributes:
# - account_number (str) : Unique account identifier (public).
# - holder_name (str) : Account holder's name (public).
# - __balance (float) : Current monetary balance (private).
# - __transactions (list[str]) : History log of completed deposits & withdrawals (private).
#
# Methods:
# - __init__(self, account_number: str, holder_name: str, initial_balance: float):
#     Initialize attributes. If initial_balance < 0, set __balance = 0.0.
# - deposit(self, amount: float):
#     If amount > 0, adds to __balance and appends "Deposited: ${amount:.2f}" to __transactions.
#     Otherwise prints "Invalid deposit amount.".
# - withdraw(self, amount: float):
#     If 0 < amount <= __balance, deducts amount and appends "Withdrew: ${amount:.2f}" to __transactions.
#     If amount > __balance, prints "Insufficient funds.".
#     If amount <= 0, prints "Invalid withdrawal amount.".
# - get_balance(self) -> float:
#     Returns the current balance.
# - get_statement(self) -> list[str]:
#     Returns a copy of the transaction history list.
#
# Example 1:
# Input:
# account = BankAccount("ACC101", "Alice", 1000.0)
# account.deposit(500.0)
# account.withdraw(200.0)
# account.withdraw(2000.0)
# print(account.get_balance())
# print(account.get_statement())
# Output:
# Insufficient funds.
# 1300.0
# ['Deposited: $500.00', 'Withdrew: $200.00']
#
# Example 2:
# Input:
# account = BankAccount("ACC102", "Bob", 100.0)
# account.deposit(50.0)
# print(account.get_balance())
# Output:
# 150.0
#
# Example 3 (Edge Case):
# Input:
# account = BankAccount("ACC103", "Charlie", -500.0)  # Negative initial balance
# account.deposit(-100.0)                             # Invalid deposit
# account.withdraw(10.0)                              # Insufficient funds (starts at 0.0)
# print(account.get_balance())
# Output:
# Invalid deposit amount.
# Insufficient funds.
# 0.0
#
# Think About:
# - Private attributes `__balance` and `__transactions` prevent arbitrary modification.
# - Always return `self.__transactions.copy()` from `get_statement()` to protect internal state.
# - Time Complexity: O(1) for balance, deposit, and withdraw.
# - Space Complexity: O(T) where T is the number of transactions recorded.

# Write your BankAccount class below:

class BankAccount:
    def __init__(self, account_number: str, holder_name: str, initial_balance: float):
        # Write your code here
        pass

    def deposit(self, amount: float):
        # Write your code here
        pass

    def withdraw(self, amount: float):
        # Write your code here
        pass

    def get_balance(self) -> float:
        # Write your code here
        pass

    def get_statement(self) -> list:
        # Write your code here
        pass
