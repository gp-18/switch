# For a list of numbers, print every pair of distinct positions and explain why the work grows quadratically.

# Example 1:
# Input: [10, 20, 30]
# Output:
# Pair (0, 1): 10, 20
# Pair (0, 2): 10, 30
# Pair (1, 2): 20, 30

# Example 2:
# Explanation: For n items, there are n*(n-1)/2 pairs, giving O(n^2) quadratic growth.

raw_input = input("Enter list of numbers separated by spaces (e.g. 10 20 30): ")
lst = [int(x) for x in raw_input.split()] if raw_input.strip() else [10, 20, 30]

n = len(lst)
pair_count = 0
for i in range(n):
    for j in range(i + 1, n):
        print(f"Pair ({i}, {j}): {lst[i]}, {lst[j]}")
        pair_count += 1

print(f"\nTotal pairs: {pair_count}")
print("Explanation: For n items, there are n * (n - 1) / 2 pairs.")
print("The outer loop runs n times and the inner loop runs on average n/2 times, which is O(n^2) quadratic growth.")
