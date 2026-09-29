# Print numbers from 1 to 20 but skip multiples of 3 using continue.

# Example 1:
# Output: 1 2 4 5 7 8 10 11 13 14 16 17 19 20 (skips 3, 6, 9, 12, 15, 18)

# Example 2:
# Output (first four): 1, 2, 4, 5 (3 skipped)

for num in range(1, 21):
    if num % 3 == 0:
        continue
    print(num, end=" ")
print()
