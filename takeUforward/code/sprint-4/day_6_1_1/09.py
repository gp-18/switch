# Q9. Digital Wallet with Daily Spending Limit (Practice - Encapsulation)
#
# Task:
# Design a `DigitalWallet` class that enforces both account balance checks and regulatory daily spending
# ceilings to protect against fraudulent drains.
#
# Attributes:
# - wallet_id (str) : Wallet account ID (public).
# - owner (str) : Owner name (public).
# - __balance (float) : Available funds (private).
# - __daily_limit (float) : Maximum spending allowed per calendar day (private).
# - __spent_today (float) : Total expenditures accumulated today (private).
#
# Methods:
# - __init__(self, wallet_id: str, owner: str, initial_balance: float, daily_limit: float):
#     Initializes wallet state.
# - top_up(self, amount: float):
#     Adds amount to __balance if amount > 0.
# - pay(self, amount: float) -> bool:
#     If amount <= 0, prints "Invalid payment amount." and returns False.
#     If amount > self.__balance, prints "Insufficient balance." and returns False.
#     If self.__spent_today + amount > self.__daily_limit, prints "Daily spending limit exceeded." and returns False.
#     Otherwise: deducts amount from __balance, adds amount to __spent_today,
#     prints "Payment of ${amount:.2f} successful.", and returns True.
# - reset_daily_spent(self):
#     Simulates the midnight rollover by resetting __spent_today = 0.0.
# - get_balance(self) -> float:
#     Returns current balance.
# - get_remaining_daily_limit(self) -> float:
#     Returns __daily_limit - __spent_today.
#
# Example 1:
# Input:
# wallet = DigitalWallet("W-881", "Priya", 5000.0, 2000.0)
# wallet.pay(1200.0)
# wallet.pay(1000.0)  # Exceeds daily limit (1200 + 1000 = 2200 > 2000)
# print("Balance:", wallet.get_balance())
# print("Remaining Limit Today:", wallet.get_remaining_daily_limit())
# wallet.reset_daily_spent()  # Next day starts
# wallet.pay(1000.0)
# print("Balance after day 2:", wallet.get_balance())
# Output:
# Payment of $1200.00 successful.
# Daily spending limit exceeded.
# Balance: 3800.0
# Remaining Limit Today: 800.0
# Payment of $1000.00 successful.
# Balance after day 2: 2800.0
#
# Example 2:
# Input:
# wallet = DigitalWallet("W-882", "Sam", 500.0, 1000.0)
# wallet.pay(600.0)   # Exceeds balance (insufficient funds)
# Output:
# Insufficient balance.
#
# Example 3 (Edge Case):
# Input:
# wallet = DigitalWallet("W-883", "Alex", 100.0, 500.0)
# wallet.pay(-50.0)   # Negative payment rejected
# wallet.top_up(-20.0) # Negative top up rejected
# print("Balance unchanged:", wallet.get_balance())
# Output:
# Invalid payment amount.
# Balance unchanged: 100.0
#
# Think About:
# - Encapsulation manages two linked constraints (`__balance` and `__spent_today`) in a single atomic transaction.
# - Direct manipulation of either variable would risk out-of-sync invariants.
# - Time Complexity: O(1) per transaction.
# - Space Complexity: O(1) auxiliary space.

# Write your DigitalWallet class below:

class DigitalWallet:
    def __init__(self, wallet_id: str, owner: str, initial_balance: float, daily_limit: float):
        # Write your code here
        pass

    def top_up(self, amount: float):
        # Write your code here
        pass

    def pay(self, amount: float) -> bool:
        # Write your code here
        pass

    def reset_daily_spent(self):
        # Write your code here
        pass

    def get_balance(self) -> float:
        # Write your code here
        pass

    def get_remaining_daily_limit(self) -> float:
        # Write your code here
        pass
