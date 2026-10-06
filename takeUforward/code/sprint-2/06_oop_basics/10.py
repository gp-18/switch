# Q10. Class attribute, instance attribute and transfer
#
# Task:
# - Add a class attribute `bank_name = "PyBank"`.
# - Add a class attribute `total_accounts = 0` that increments every time an account is created.
# - Add `transfer(self, other, amount)` that withdraws from `self` and deposits into `other`.
#   If the withdrawal fails, nothing changes anywhere and it returns `False`. If successful, returns `True`.
#
# Explanation:
# - Class Attributes vs Instance Attributes:
#   * Class attributes are shared across all instances of a class (e.g. `BankAccount.total_accounts`, `BankAccount.bank_name`).
#   * Instance attributes (`self.__balance`) are distinct and unique to each object.
# - Atomic Operations:
#   * In financial transfers, either the entire transaction succeeds or nothing happens. If deducting from `self` fails,
#     no money is added to `other`.
#
# Example / Test Case:
# a = BankAccount("A", 1000)
# b = BankAccount("B", 500)
# assert BankAccount.total_accounts >= 2
# assert a.transfer(b, 300) is True
# assert (a.balance, b.balance) == (700, 800)
# assert a.transfer(b, 99999) is False
# assert (a.balance, b.balance) == (700, 800)

# Write your BankAccount class here:



# ==================== TEST CASES ====================
# if __name__ == "__main__":
#     a = BankAccount("A", 1000)
#     b = BankAccount("B", 500)
#     assert BankAccount.total_accounts >= 2
#     assert a.transfer(b, 300) is True
#     assert (a.balance, b.balance) == (700, 800)
#     assert a.transfer(b, 99999) is False
#     assert (a.balance, b.balance) == (700, 800)
#     print("Q10 passed successfully!")
