# Implement a small LRU-style cache using OrderedDict.

# Example 1:
# Input: capacity = 2; put(1, 1), put(2, 2), get(1), put(3, 3) (evicts 2)
# Output: Cache keys: [1, 3]

# Example 2:
# Input: capacity = 1; put('a', 10), put('b', 20) (evicts 'a')
# Output: Cache keys: ['b']

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
lru.get(1)
lru.put(3, 3)
print(f"Cache keys: {list(lru.cache.keys())}")
