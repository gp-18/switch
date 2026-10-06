# 10 Practice Questions: Attributes and Methods (BankAccount in Python)

## Q1. Create the class and getters
**Task:** Create `BankAccount` with private attributes `__name` and `__balance`, set in `__init__`. Add `getName()` and `getBalance()`.

```python
acc = BankAccount("Parth", 1000)
assert acc.getName() == "Parth"
assert acc.getBalance() == 1000
```

## Q2. Setter with validation
**Task:** Add `setName(name)`. Reject empty or whitespace-only names with `ValueError`, and non-strings with `TypeError`. Strip extra spaces before saving.

```python
acc.setName("  Rahul  ")
assert acc.getName() == "Rahul"
# acc.setName("")   -> ValueError
# acc.setName(123)  -> TypeError
```

## Q3. Deposit
**Task:** Add `deposit(amount)`. Amount must be a positive number. Otherwise raise `ValueError`. Return the new balance.

```python
acc = BankAccount("Parth", 1000)
assert acc.deposit(500) == 1500
# acc.deposit(0)    -> ValueError
# acc.deposit(-10)  -> ValueError
```

## Q4. Withdraw
**Task:** Add `withdraw(amount)`. If the amount is more than the balance, print `"Insufficient amount"` and return `False`. Otherwise subtract and return `True`. Reject zero or negative amounts with `ValueError`.

```python
acc = BankAccount("Parth", 1000)
assert acc.withdraw(300) is True
assert acc.getBalance() == 700
assert acc.withdraw(5000) is False
assert acc.getBalance() == 700   # unchanged
```

## Q5. Is private really private?
**Task:** Try `print(acc.__balance)` and observe the error. Then find the real attribute name Python created (hint: run `print(acc.__dict__)`) and read the balance through it. Write 3 lines in a comment explaining what you learned.

```python
acc = BankAccount("Parth", 1000)
# print(acc.__balance)            -> AttributeError
print(acc.__dict__)               # see the mangled name
print(acc._BankAccount__balance)  # works
```

**Goal:** Understand name mangling. `__balance` becomes `_BankAccount__balance`. It stops accidents, not determined access, so Python privacy is by convention.

## Q6. Default values and safe initialisation
**Task:** Make `balance` default to `0` in `__init__`. Reject a negative starting balance with `ValueError`. Reuse your `setName` validation inside `__init__` so the rules live in one place.

```python
acc = BankAccount("Parth")
assert acc.getBalance() == 0
# BankAccount("Parth", -5)  -> ValueError
# BankAccount("", 100)      -> ValueError
```

## Q7. String representation
**Task:** Add `__str__` (friendly text for users) and `__repr__` (unambiguous text for developers). Never expose more than name and balance.

```python
acc = BankAccount("Parth", 1000)
assert str(acc) == "Account holder: Parth | Balance: 1000"
assert repr(acc) == "BankAccount(name='Parth', balance=1000)"
```

## Q8. Transaction history
**Task:** Add a private list `__history`. Every successful deposit or withdrawal appends a tuple like `("deposit", 500)`. Add `getHistory()` that returns a **copy** of the list so outside code cannot change it.

```python
acc = BankAccount("Parth", 1000)
acc.deposit(500)
acc.withdraw(200)
h = acc.getHistory()
assert h == [("deposit", 500), ("withdraw", 200)]
h.append(("hack", 999999))
assert len(acc.getHistory()) == 2   # original not affected
```

## Q9. Replace getters and setters with `@property`
**Task:** Rewrite the class the Pythonic way. `name` gets a getter and a validating setter. `balance` gets a getter only (read-only).

```python
acc = BankAccount("Parth", 1000)
acc.name = "Rahul"            # uses the setter
assert acc.name == "Rahul"
assert acc.balance == 1000
# acc.balance = 5000          -> AttributeError (no setter)
```

**Goal:** Know why Python prefers `@property` over `getX()` / `setX()`.

## Q10. Class attribute, instance attribute and transfer
**Task:**
- Add a class attribute `bank_name = "PyBank"` and a class attribute `total_accounts = 0` that increases every time an account is created.
- Add `transfer(self, other, amount)` that withdraws from `self` and deposits into `other`. If the withdrawal fails, nothing changes anywhere and it returns `False`.

```python
a = BankAccount("A", 1000)
b = BankAccount("B", 500)
assert BankAccount.total_accounts >= 2
assert a.transfer(b, 300) is True
assert (a.balance, b.balance) == (700, 800)
assert a.transfer(b, 99999) is False
assert (a.balance, b.balance) == (700, 800)
```

**Goal:** Tell class attributes (shared) from instance attributes (per object), and keep an operation atomic.