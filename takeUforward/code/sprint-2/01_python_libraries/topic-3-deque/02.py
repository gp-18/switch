# Implement a stack using deque.

# Example 1:
# Input: push(1), push(2), pop()
# Output: Popped: 2, Remaining: deque([1])

# Example 2:
# Input: push('x'), push('y'), pop()
# Output: Popped: 'y', Remaining: deque(['x'])

from collections import deque

stack = deque()

def push(val):
    stack.append(val)

def pop():
    return stack.pop() if stack else None

push(1)
push(2)
val = pop()
print(f"Popped: {val}, Remaining: {stack}")
