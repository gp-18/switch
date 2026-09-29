# State the time complexity of two nested loops that each run n times.

# Example 1:
# Scenario: for i in range(n): for j in range(n): ...
# Output: Time Complexity: O(n^2) (Quadratic Time)

# Example 2:
# Explanation: For n = 10, total iterations = 100; for n = 20, iterations = 400.

n = 3
count = 0
for i in range(n):
    for j in range(n):
        count += 1
print(f"For n = {n}, nested loops ran {count} times.")

print("\nTime Complexity: O(n^2) (Quadratic Time)")
print("Explanation: For n = 10, total iterations = 100; for n = 20, iterations = 400.")
