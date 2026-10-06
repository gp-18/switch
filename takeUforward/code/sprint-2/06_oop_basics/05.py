# Q5. Is private really private?
#
# Task:
# - Try `print(acc.__balance)` and observe the `AttributeError`.
# - Inspect `print(acc.__dict__)` to see the actual mangled name Python created.
# - Access the private balance through the mangled name `acc._BankAccount__balance`.
# - Write 3 lines in a comment explaining what you learned.
#
# Explanation:
# - Name Mangling:
#   * Python transforms any identifier with two leading underscores (like `__balance`) into
#     `_ClassName__balance` (e.g. `_BankAccount__balance`).
#   * This is done primarily to avoid name collisions in inheritance hierarchies, NOT for hardcore security.
#   * Python follows the philosophy: "We are all consenting adults here". Privacy is established by convention.
#
# Example / Test Case:
# acc = BankAccount("Parth", 1000)
# # print(acc.__balance)            -> AttributeError
# print(acc.__dict__)               # see the mangled name
# print(acc._BankAccount__balance)  # works

# Write your BankAccount class and observation comments here:
class BankAccount:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def getName(self):
        return self.__name

    def getBalance(self):
        return self.__balance


# ==================== OBSERVATION ====================

acc = BankAccount("Parth", 1000)

# Direct access does not work because Python changed __balance
# into _BankAccount__balance internally.
# print(acc.__balance)   # AttributeError

# __dict__ shows the actual names Python stored.
print(acc.__dict__)

# We can access the "private" attribute using its mangled name.
print(acc._BankAccount__balance)


# Q5 Observation:
# 1. __balance cannot be accessed directly using acc.__balance.
# 2. Python changes __balance to _BankAccount__balance using name mangling.
# 3. Name mangling is not true security; the attribute can still be accessed using the mangled name.


# ==================== TEST CASES ====================
# if __name__ == "__main__":
#     acc = BankAccount("Parth", 1000)
#     try:
#         _ = acc.__balance
#         assert False, "Direct access should raise AttributeError"
#     except AttributeError:
#         pass
#
#     assert acc._BankAccount__balance == 1000
#     print("Mangled attribute found:", acc.__dict__)
#     print("Q5 passed successfully!")
