# Find and fix an infinite while loop caused by a missing counter update.

# Example 1:
# Input (buggy): i = 1; while i <= 5: print(i)  (infinite loop, i remains 1)
# Output (fixed): i = 1; while i <= 5: print(i); i += 1  (prints 1 to 5 and terminates)

# Example 2:
# Input: count = 0; while count < 3: count += 1
# Output: Terminates after 3 iterations

# Buggy code:
# i = 1
# while i <= 5:
#     print(i)
#     # Missing i += 1 causes an infinite loop because i is never incremented

# Fixed code:
i = 1
while i <= 5:
    print(i, end=" ")
    i += 1
print()

# Example 2 demonstration:
count = 0
while count < 3:
    count += 1
print(f"Final count: {count} (terminated after 3 iterations)")
