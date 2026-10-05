# Implement a simple BFS traversal of a graph using deque.

# Example 1:
# Input: graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}, start = 2
# Output: BFS Traversal: [2, 0, 3, 1]

# Example 2:
# Input: graph = {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}, start = 'A'
# Output: BFS Traversal: ['A', 'B', 'C', 'D']

from collections import deque

graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
start = 2

visited = set()
queue = deque([start])
visited.add(start)
traversal = []

while queue:
    node = queue.popleft()
    traversal.append(node)
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

print(f"BFS Traversal: {traversal}")
