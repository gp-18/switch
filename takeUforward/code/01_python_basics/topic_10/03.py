# Calculate the sum of numbers from 1 through n.

# Example 1:
# Input: n = 5
# Output: 15 (1 + 2 + 3 + 4 + 5 = 15)

# Example 2:
# Input: n = 10
# Output: 55

n = int(input("Enter n: "))
total_sum = 0
for i in range(1, n + 1):
    total_sum += i
print(f"Sum: {total_sum}")
