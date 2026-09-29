# Explain and demonstrate the difference between == and is using two equal lists and a None check.

# Example 1:
# Input: a = [1, 2, 3], b = [1, 2, 3]
# Output: a == b -> True (value equality), a is b -> False (different memory addresses)

# Example 2:
# Input: x = None
# Output: x is None -> True ('is' checks object identity with singleton None)

# 1. Demonstration with lists:
# '==' compares values (structural equality)
# 'is' compares memory addresses / object identities
a = [1, 2, 3]
b = [1, 2, 3]

print(f"a == b -> {a == b} (value equality: both lists have identical elements)")
print(f"a is b -> {a is b} (identity equality: distinct objects in memory)")

# When two references point to the same object:
c = a
print(f"c = a -> c is a -> {c is a} (both variables reference the same list object)")

# 2. Demonstration with None check:
# None is a built-in singleton object in Python, so identity comparison using 'is' is best practice.
x = None
print(f"\nx is None -> {x is None} ('is' checks object identity with singleton None)")
