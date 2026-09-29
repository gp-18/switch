# Compare a loop that stops at n with one that repeatedly halves n; describe the expected growth.

# Example 1:
# Scenario: Linear loop (i += 1 until n) vs Halving loop (n //= 2 until 0)
# Output: Linear loop: O(n) | Halving loop: O(log n)

# Example 2:
# Explanation: For n = 1024, linear takes 1024 steps while halving takes only 10 steps (2^10 = 1024).

n = 16
linear_count = 0
for i in range(n):
    linear_count += 1

halving_count = 0
val = n
while val > 0:
    halving_count += 1
    val //= 2

print(f"For n = {n}:")
print(f"Linear loop steps: {linear_count} -> O(n)")
print(f"Halving loop steps: {halving_count} -> O(log n)")
print("\nExpected growth:")
print("Linear loop: O(n) - directly proportional to n.")
print("Halving loop: O(log n) - logarithmic growth, much slower growth than linear.")
