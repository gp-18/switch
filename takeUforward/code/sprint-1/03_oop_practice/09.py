# ============================================================
# Problem: Payment Processing System
# Difficulty: Hard
# ============================================================
#
# PROBLEM STATEMENT:
# Design a payment system with a common payment interface and
# separate CardPayment, UPIPayment, and WalletPayment implementations.
# Each payment validates its amount, rejects invalid payments,
# and returns a status.
# Process multiple payments polymorphically through the common interface.
#
# INPUT:
# - payments_data: list of tuples (payment_type, amount)
#
# OUTPUT:
# - List of status strings in format "<type>: success" or "<type>: failure"
#
# EXAMPLE:
# Input:  [("card", 500), ("upi", 0), ("wallet", 250)]
# Output: ["card: success", "upi: failure", "wallet: success"]
#
# CONSTRAINTS:
# - Card valid if amount > 0 and amount <= 50000
# - UPI valid if amount > 0 and amount <= 100000
# - Wallet valid if amount > 0 and amount <= 1000 (default balance)
# ============================================================

from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount):
        pass

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def process_payment(self):
        pass


class CardPayment(Payment):
    def validate(self):
        pass

    def process_payment(self):
        pass


class UPIPayment(Payment):
    def validate(self):
        pass

    def process_payment(self):
        pass


class WalletPayment(Payment):
    def __init__(self, amount, wallet_balance=1000):
        pass

    def validate(self):
        pass

    def process_payment(self):
        pass


def solution(payments_data):
    # Process payments polymorphically and return status list
    pass


# ---- TEST CASES ----
assert solution([("card", 500), ("upi", 0), ("wallet", 250)]) == [
    "card: success",
    "upi: failure",
    "wallet: success"
], "Test 1 Failed"

assert solution([("wallet", -50), ("card", 1200), ("upi", 450), ("card", -100)]) == [
    "wallet: failure",
    "card: success",
    "upi: success",
    "card: failure"
], "Test 2 Failed"

assert solution([("upi", 5000), ("wallet", 1500), ("card", 0)]) == [
    "upi: success",
    "wallet: failure",
    "card: failure"
], "Test 3 Failed"

print("All test cases passed!")
