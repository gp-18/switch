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
