# Dataclass Inheritance & __post_init__ Constructor Chaining
# In modern Python, @dataclass auto-generates __init__. Use __post_init__ for validation
# and computed fields across inheritance hierarchies.
#
# 1. @dataclass class Account:
#    - account_id: str
#    - holder_name: str
#    - balance: float = 0.0
#    - def __post_init__(self):
#      if self.balance < 0: raise ValueError("Balance cannot be negative")
#
# 2. @dataclass class PremiumAccount(Account):
#    - cashback_rate: float = 0.01
#    - reward_points: int = 0
#    - def __post_init__(self):
#      call super().__post_init__() to trigger base validation!
#      calculate self.reward_points = int(self.balance * 0.1)
#
# Example 1:
# Input:  p = PremiumAccount("A1", "Raj", balance=500.0, cashback_rate=0.02)
# Output: p.account_id == "A1", p.balance == 500.0, p.reward_points == 50
#
# Example 2:
# Input:  PremiumAccount("A2", "Simran", balance=-50.0)
# Output: ValueError: Balance cannot be negative
#

# Write your solution below:


from dataclasses import dataclass


@dataclass
class Account:
    account_id: str
    holder_name: str
    balance: float = 0.0

    def __post_init__(self):
        # Validate the balance after initialization.
        if self.balance < 0:
            raise ValueError("Balance cannot be negative")


@dataclass
class PremiumAccount(Account):
    cashback_rate: float = 0.01
    reward_points: int = 0

    def __post_init__(self):
        # Run the parent class validation first.
        super().__post_init__()

        # Calculate reward points from the balance.
        self.reward_points = int(self.balance * 0.1)


# Example 1: Valid premium account
p = PremiumAccount(
    "A1",
    "Raj",
    balance=500.0,
    cashback_rate=0.02
)

print(p.account_id)
print(p.holder_name)
print(p.balance)
print(p.cashback_rate)
print(p.reward_points)