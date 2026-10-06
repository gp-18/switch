# Q8. Transaction history
#
# Task:
# - Add a private list `__history` to record transactions.
# - Every successful deposit or withdrawal appends a tuple like `("deposit", 500)` or `("withdraw", 200)`.
# - Add `getHistory()` that returns a COPY of the list so outside code cannot alter the internal history.
#
# Explanation:
# - Defensive Copying:
#   * Python lists are mutable references. If you return `self.__history` directly, any external caller
#     can execute `acc.getHistory().append(...)` or `acc.getHistory().clear()`, modifying the account's internal state.
#   * Returning `self.__history.copy()` or `list(self.__history)` ensures external modifications don't affect the internal object.
#
# Example / Test Case:
# acc = BankAccount("Parth", 1000)
# acc.deposit(500)
# acc.withdraw(200)
# h = acc.getHistory()
# assert h == [("deposit", 500), ("withdraw", 200)]
# h.append(("hack", 999999))
# assert len(acc.getHistory()) == 2   # original not affected

# Write your BankAccount class here:



# ==================== TEST CASES ====================
# if __name__ == "__main__":
#     acc = BankAccount("Parth", 1000)
#     acc.deposit(500)
#     acc.withdraw(200)
#     h = acc.getHistory()
#     assert h == [("deposit", 500), ("withdraw", 200)]
#     h.append(("hack", 999999))
#     assert len(acc.getHistory()) == 2
#     print("Q8 passed successfully!")
