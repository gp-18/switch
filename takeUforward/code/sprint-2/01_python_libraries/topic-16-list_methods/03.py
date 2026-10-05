# Demonstrate why pop(0) can be inefficient for a queue.

# Example 1:
# Input: a.pop(0) on a list of size n
# Output: Takes O(n) time because all following elements must shift left

# Example 2:
# Input: Compare with deque.popleft()
# Output: deque.popleft() takes O(1) time

a = list(range(5))
val = a.pop(0)
print(f"Popped from front: {val}, remaining: {a}")
print("pop(0) takes O(n) time because all following elements must shift left.")
