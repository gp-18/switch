# Python Libraries --- Interview Notes + Practice Bank

Use this as a write-by-hand revision sheet and practice checklist for Python libraries used in DSA and coding interviews.

The goal is not to memorize every function. For interviews, focus on:
- What the library provides.
- The important methods/functions.
- When to use it.
- Typical time complexity.
- Common DSA patterns where it appears.
- The difference between similar tools.

---

# Part 1 --- Interview Notes to Write by Hand

## 1. Built-in Functions

### `sorted()` and `.sort()`

- `sorted(iterable)` returns a **new sorted list**.
- `list.sort()` sorts the list **in-place** and returns `None`.
- Both support `key=` for custom sorting.
- `reverse=True` sorts in descending order.
- Example:
  `sorted(words, key=len)`
- Interview trap: know the difference between modifying the original list and creating a new list.

### `min()` and `max()`

- `min(iterable)` returns the smallest value.
- `max(iterable)` returns the largest value.
- Both support `key=`.
- Example:
  `max(words, key=len)`

### `sum()`

- `sum(iterable)` returns the total.
- `sum(iterable, start)` starts accumulation from `start`.
- Product can be handled with `math.prod()` or `functools.reduce()`.

### `len()` and `.count()`

- `len(iterable)` returns the number of elements.
- `sequence.count(value)` counts occurrences.
- Know the difference between length and frequency.

### `any()` and `all()`

- `any(iterable)` is `True` when at least one element is truthy.
- `all(iterable)` is `True` when every element is truthy.
- `any([])` is `False`.
- `all([])` is `True`.
- Useful for validation and condition checks.

### `enumerate()`

- `enumerate(iterable, start=0)` gives `(index, value)` pairs.
- Avoid manually maintaining an index when iterating with both index and value.

### `zip()`

- `zip(a, b)` combines corresponding elements.
- Iteration stops when the shortest iterable is exhausted.
- Useful for processing two arrays together.

### `reversed()`

- Returns a reverse iterator.
- `list(reversed(arr))` creates a reversed list.
- String slicing `s[::-1]` is another common way to reverse a string.

### `range()`

- `range(stop)` gives `0` through `stop - 1`.
- `range(start, stop)` excludes `stop`.
- `range(start, stop, step)` controls the increment.
- `range()` is commonly used in loops and index-based problems.

---

## 2. `collections.deque`

### What to remember

- `deque` means double-ended queue.
- Fast insertion/removal from both ends.
- `append()` adds to the right.
- `appendleft()` adds to the left.
- `pop()` removes from the right.
- `popleft()` removes from the left.
- `extend()` adds multiple values to the right.
- `extendleft()` adds values to the left.
- `rotate()` rotates elements.
- Indexed access is supported, but deque is primarily designed for end operations.

### Interview use cases

- Queue implementation.
- Stack implementation.
- BFS traversal.
- Sliding window problems.
- Monotonic queue patterns.

### Complexity to remember

- `append()` / `appendleft()` -> typically `O(1)`.
- `pop()` / `popleft()` -> typically `O(1)`.
- Do not treat deque as a replacement for a list when frequent random indexing is required.

### Interview sentence

> Use `deque` when I need efficient insertion or removal from both ends.

---

## 3. `collections.Counter`

### What to remember

- `Counter` is designed for frequency counting.
- `Counter(iterable)` counts occurrences automatically.
- Missing keys return `0`.
- `most_common(k)` returns the top `k` frequent elements.
- `update()` adds counts.
- `subtract()` subtracts counts.
- Counter objects support useful arithmetic operations.

### Common operations

```python
from collections import Counter

counter = Counter(nums)
counter[x]
counter.most_common(k)
```

### Interview use cases

- Frequency counting.
- Anagrams.
- Top K frequent elements.
- Character counting.
- Comparing frequency distributions.

### Interview sentence

> I use `Counter` when the main requirement is frequency tracking.

---

## 4. `collections.defaultdict`

### What to remember

- `defaultdict` creates a default value when a missing key is accessed.
- `defaultdict(int)` is useful for counting.
- `defaultdict(list)` is useful for grouping.
- `defaultdict(set)` is useful when each key should map to unique values.
- It avoids repeated `if key not in dictionary` checks.

### Common patterns

```python
from collections import defaultdict

freq = defaultdict(int)
groups = defaultdict(list)
graph = defaultdict(list)
```

### Interview use cases

- Grouping.
- Graph adjacency lists.
- Frequency counting.
- Building maps without explicit initialization.

### Interview sentence

> I use `defaultdict` when every key needs an automatically initialized container or value.

---

## 5. `collections.OrderedDict`

### What to remember

- `OrderedDict` maintains insertion order.
- Normal Python dictionaries also preserve insertion order in modern Python.
- `OrderedDict` is still useful for specialized ordering operations.
- `move_to_end(key)` moves a key.
- `popitem()` removes the last item by default.
- `popitem(last=False)` removes the first item.

### Interview use cases

- LRU-cache-style implementations.
- Explicit movement of entries.
- Problems requiring ordered dictionary operations.

### Interview sentence

> I would use `OrderedDict` when I need dictionary behavior plus explicit ordering operations such as moving entries to the front or back.

---

## 6. `collections.namedtuple`

### What to remember

- A named tuple is an immutable tuple with named fields.
- Values can be accessed by both name and index.
- It is lightweight compared with creating a full class.
- It can represent simple immutable records.

### Example

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
point = Point(1, 2)

point.x
point[0]
```

### Interview use cases

- Lightweight records.
- Returning multiple related values.
- Immutable data structures.

---

## 7. `heapq`

### What to remember

- `heapq` provides heap operations.
- Python's `heapq` is a **min-heap**.
- The smallest value is available at index `0`.
- `heappush()` adds an item.
- `heappop()` removes the smallest item.
- `heapify()` converts a list into a heap.
- `nlargest()` finds the largest values.
- `nsmallest()` finds the smallest values.

### Core pattern

```python
import heapq

heap = []

heapq.heappush(heap, value)
smallest = heapq.heappop(heap)
```

### Max-heap trick

Python's `heapq` is a min-heap, so a common integer max-heap technique is to store negative values.

```python
heapq.heappush(heap, -value)
maximum = -heapq.heappop(heap)
```

### Interview use cases

- Priority queues.
- Top K problems.
- K largest/smallest elements.
- Merge K sorted lists.
- Dijkstra-style priority queues.

### Complexity to remember

- `heappush()` -> `O(log n)`.
- `heappop()` -> `O(log n)`.
- `heapify()` -> `O(n)`.
- Accessing the minimum at `heap[0]` -> `O(1)`.

### Interview sentence

> Use a heap when I repeatedly need the smallest or largest priority item rather than fully sorting all elements.

---

## 8. `bisect`

### What to remember

- `bisect` provides binary-search-based insertion-position operations.
- The input sequence must already be sorted for normal binary-search usage.
- `bisect_left(arr, x)` finds the leftmost valid insertion position.
- `bisect_right(arr, x)` finds the rightmost valid insertion position.
- `bisect()` is an alias for `bisect_right()`.
- `insort_left()` / `insort_right()` insert while maintaining sorted order.

### Example

```python
import bisect

arr = [1, 3, 3, 5]

left = bisect.bisect_left(arr, 3)
right = bisect.bisect_right(arr, 3)
```

### Interview use cases

- Binary search.
- Finding insertion positions.
- First/last occurrence.
- Maintaining a sorted sequence.
- Range-style queries.

### Complexity to remember

- Search for an insertion position -> `O(log n)`.
- Inserting into a Python list still requires shifting elements, so insertion itself can be `O(n)`.

### Interview sentence

> `bisect` helps me find where a value belongs in a sorted list using binary search.

---

## 9. `itertools`

`itertools` provides iterator-building tools for common iteration patterns.

### `combinations()`

- Selects items without considering order.
- Example:
  `combinations([1, 2, 3], 2)`
- `(1, 2)` and `(2, 1)` are not both produced.

### `combinations_with_replacement()`

- Like combinations, but an item may be selected more than once.

### `permutations()`

- Order matters.
- Example:
  `(1, 2)` and `(2, 1)` are different.

### `product()`

- Generates Cartesian products.

### `cycle()`

- Repeats an iterable indefinitely.
- Be careful: converting an infinite iterator directly to `list()` does not terminate.

### `repeat()`

- Repeats a value a specified number of times or indefinitely.

### `chain()`

- Combines multiple iterables into one sequence.

### `accumulate()`

- Produces cumulative results.
- Default behavior is cumulative sum.
- A custom function can create cumulative products or other operations.

### `groupby()`

- Groups consecutive items based on a key.
- Important interview point: it groups consecutive matching values; it does not automatically group all equal values regardless of position.

### Interview use cases

- Combinations/permutations.
- Cartesian products.
- Cumulative calculations.
- Flattening iterables.
- Complex iteration patterns.

---

## 10. `functools`

### `lru_cache`

- Caches function results.
- Useful for memoization.
- Especially useful in recursive problems such as Fibonacci and dynamic programming.
- `maxsize` controls the cache size.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def solve(n):
    ...
```

### `reduce()`

- Repeatedly combines values into one result.
- Example:
  `reduce(lambda x, y: x + y, [1, 2, 3, 4])`
- Often a loop or built-in such as `sum()` is clearer for simple cases.

### `partial()`

- Creates a new function with some arguments already fixed.

### `wraps()`

- Used inside decorators.
- Preserves important metadata of the original function.

### Interview use cases

- Memoization.
- Recursive optimization.
- Function manipulation.
- Decorators.

---

## 11. `math`

### Important functions

- `math.sqrt(x)` -> square root.
- `math.pow(x, y)` -> power as a floating-point result.
- `math.prod(iterable)` -> product.
- `math.factorial(n)` -> factorial.
- `math.gcd(a, b)` -> greatest common divisor.
- `math.lcm(a, b)` -> least common multiple.
- `math.ceil(x)` -> ceiling.
- `math.floor(x)` -> floor.
- `math.log(x)` -> natural logarithm.
- `math.log2(x)` -> base-2 logarithm.
- `math.log10(x)` -> base-10 logarithm.
- `math.isfinite(x)` -> checks finite value.
- `math.isinf(x)` -> checks infinity.
- `math.pi` and `math.e` provide common constants.

### Interview use cases

- GCD/LCM.
- Mathematical formulas.
- Factorials.
- Geometry.
- Logarithmic calculations.
- Rounding calculations.

---

## 12. `random`

### Important functions

- `random.random()` -> floating-point value in `[0.0, 1.0)`.
- `random.randint(a, b)` -> integer including both endpoints.
- `random.randrange()` -> value selected from a `range()`-like sequence.
- `random.choice(seq)` -> one random element.
- `random.sample(population, k)` -> `k` unique sampled positions/items without replacement.
- `random.shuffle(list)` -> shuffles a list in-place.
- `random.uniform(a, b)` -> random floating-point value in the specified interval.

### Interview use cases

- Test-case generation.
- Randomized testing.
- Shuffling.
- Sampling.

### Interview trap

> `shuffle()` modifies the list in-place and does not return the shuffled list.

---

## 13. `string`

### Useful constants

- `string.ascii_lowercase`
- `string.ascii_uppercase`
- `string.ascii_letters`
- `string.digits`
- `string.hexdigits`
- `string.punctuation`
- `string.whitespace`

### Interview use cases

- Character validation.
- Building character sets.
- Filtering characters.
- String-related DSA problems.

### Interview sentence

> The `string` module is useful when I need predefined character sets instead of manually writing them.

---

## 14. List Methods

### Important methods

- `append(x)` -> add one item to the end.
- `extend(iterable)` -> add multiple items.
- `insert(index, x)` -> insert at a position.
- `remove(x)` -> remove the first matching value.
- `pop()` -> remove and return the last item.
- `pop(index)` -> remove and return an item at an index.
- `index(x)` -> find the first matching index.
- `count(x)` -> count occurrences.
- `sort()` -> sort in-place.
- `reverse()` -> reverse in-place.
- `clear()` -> remove all items.
- `copy()` -> shallow copy.

### Interview complexity points

- `append()` -> typically `O(1)` amortized.
- `pop()` from the end -> typically `O(1)`.
- `pop(0)` / inserting at the front -> `O(n)` because elements shift.
- Searching with `index()` or `in` -> `O(n)`.
- Sorting -> `O(n log n)`.

### Interview trap

> Use `deque` rather than a list when frequent queue operations from the front are required.

---

## 15. Dictionary Methods

### Important methods

- `d[key]` -> access value; missing key raises `KeyError`.
- `d.get(key)` -> safely get a value.
- `d.get(key, default)` -> return a fallback.
- `d[key] = value` -> add/update.
- `update()` -> add/update multiple entries.
- `pop(key)` -> remove and return a value.
- `popitem()` -> remove and return the last key-value pair.
- `keys()` -> keys view.
- `values()` -> values view.
- `items()` -> key-value pairs view.
- `clear()` -> remove all entries.
- `copy()` -> shallow copy.

### Interview complexity points

- Average-case dictionary lookup, insertion, and deletion are typically `O(1)`.
- Dictionary keys must be hashable.
- Dictionaries preserve insertion order in modern Python.

### Interview pattern

```python
freq = {}

for value in arr:
    freq[value] = freq.get(value, 0) + 1
```

---

## 16. Set Methods

### Important methods

- `add(x)` -> add an item.
- `remove(x)` -> remove an item; raises an error if missing.
- `discard(x)` -> remove an item if present; no error if missing.
- `pop()` -> removes an arbitrary set element.
- `clear()` -> remove all items.
- `copy()` -> shallow copy.

### Set operations

- Union: `s1 | s2`
- Intersection: `s1 & s2`
- Difference: `s1 - s2`
- Symmetric difference: `s1 ^ s2`
- Subset: `s1 <= s2`
- Superset: `s1 >= s2`

### Interview complexity points

- Average-case membership lookup is typically `O(1)`.
- Sets are useful when uniqueness or fast membership testing matters.
- Sets are unordered collections.

### Interview sentence

> I use a set when I need unique values or fast average-case membership checks.

---

## 17. String Methods

### Important methods

- `upper()` / `lower()` -> change case in a returned string.
- `capitalize()` -> first character uppercase and remaining characters lowercase.
- `title()` -> title-case words.
- `strip()` / `lstrip()` / `rstrip()` -> remove whitespace from ends.
- `split()` -> convert a string into a list.
- `join()` -> combine strings using a separator.
- `replace()` -> replace occurrences.
- `find()` -> return index or `-1`.
- `index()` -> return index or raise `ValueError`.
- `startswith()` / `endswith()` -> prefix/suffix checks.
- `count()` -> count non-overlapping occurrences.
- `isalpha()` -> alphabetic characters.
- `isdigit()` -> digit characters.
- `isalnum()` -> alphabetic or numeric characters.

### Important interview traps

- Strings are immutable.
- `s.upper()` returns a new string; it does not modify `s`.
- `strip()` removes from the ends, not the middle.
- `find()` returns `-1` when absent.
- `index()` raises `ValueError` when absent.
- `split()` returns a list.
- `join()` is called on the separator.

---

# Part 2 --- Common Interview Patterns

## Pattern 1: Frequency Counting

Use `Counter` when only frequencies are required.

```python
from collections import Counter

freq = Counter(nums)
```

Use a normal dictionary when you want explicit control.

```python
freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1
```

---

## Pattern 2: Grouping

Use `defaultdict(list)` when multiple values belong to one key.

```python
from collections import defaultdict

groups = defaultdict(list)

for item in items:
    groups[key(item)].append(item)
```

---

## Pattern 3: Queue / BFS

Use `deque`.

```python
from collections import deque

queue = deque([start])

while queue:
    node = queue.popleft()
```

---

## Pattern 4: Top K

Use `Counter` for frequencies and `heapq` when a heap-based solution is appropriate.

```python
from collections import Counter
import heapq
```

Know both approaches because interview questions may ask for a particular complexity.

---

## Pattern 5: Binary Search

Use `bisect` when the problem is about finding an insertion position in a sorted list.

```python
import bisect

position = bisect.bisect_left(arr, target)
```

---

## Pattern 6: Memoization

Use `functools.lru_cache` for repeated recursive states.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def solve(state):
    ...
```

---

## Pattern 7: Sorting with a Key

```python
arr.sort(key=lambda x: x[1])
```

For multiple criteria:

```python
arr.sort(key=lambda x: (x[1], x[0]))
```

Remember that the tuple key is compared from left to right.

---

# Part 3 --- Practice Questions

## Topic 1: Built-in Functions

1. Given a list of integers, return a new sorted list without modifying the original list.
2. Sort a list of strings by length from shortest to longest.
3. Given a list of numbers, find the minimum, maximum, and total using built-in functions.
4. Given a list of Boolean values, determine whether at least one value is `True` and whether all values are `True`.
5. Given a list of names, print each name with its 1-based position using `enumerate()`.

---

## Topic 2: `enumerate()`, `zip()`, `range()` and `reversed()`

1. Given a list of numbers, print each index and value using `enumerate()`.
2. Given two lists of names and scores, combine them using `zip()` and print each pair.
3. Demonstrate what happens when the two lists passed to `zip()` have different lengths.
4. Generate all even numbers from 0 through 20 using `range()`.
5. Reverse a list using `reversed()` and compare it with slicing using `[::-1]`.

---

## Topic 3: `deque`

1. Implement a queue using `deque` with enqueue and dequeue operations.
2. Implement a stack using `deque`.
3. Given a list of integers, use a deque to simulate a sliding window of fixed size.
4. Implement a simple BFS traversal of a graph using `deque`.
5. Demonstrate `appendleft()`, `popleft()`, `append()`, and `pop()` and explain why deque is useful for queues.

---

## Topic 4: `Counter`

1. Count the frequency of every number in a list using `Counter`.
2. Count the frequency of every character in a string.
3. Given a list of numbers, return the `k` most frequent values.
4. Check whether two strings are anagrams using frequency counts.
5. Compare two `Counter` objects and explain the result of their addition, subtraction, intersection, and union.

---

## Topic 5: `defaultdict`

1. Count the frequency of numbers using `defaultdict(int)`.
2. Group words by their first character using `defaultdict(list)`.
3. Build a graph adjacency list using `defaultdict(list)`.
4. Map each student to a set of subjects using `defaultdict(set)`.
5. Rewrite a normal dictionary grouping solution using `defaultdict` and compare the two implementations.

---

## Topic 6: `OrderedDict`

1. Create an `OrderedDict` and move one key to the end.
2. Move a key to the beginning using `move_to_end(..., last=False)`.
3. Remove the oldest entry using `popitem(last=False)`.
4. Implement a small LRU-style cache using `OrderedDict`.
5. Explain why a normal modern Python dictionary and `OrderedDict` are not identical in terms of available ordering operations.

---

## Topic 7: `namedtuple`

1. Create a `Point` named tuple containing `x` and `y`.
2. Store three students using a named tuple with `name`, `age`, and `score`.
3. Access named-tuple fields using both field names and indexes.
4. Attempt to modify a named-tuple field and explain the result.
5. Return a named tuple from a function that calculates two related values.

---

## Topic 8: `heapq`

1. Create a min-heap and insert five integers using `heappush()`.
2. Repeatedly pop values from a heap and verify that they come out in priority order.
3. Convert an unsorted list into a heap using `heapify()`.
4. Find the `k` smallest values from a list using a heap.
5. Implement a max-heap for integers using the negative-value technique.

---

## Topic 9: `bisect`

1. Find the leftmost insertion position of a target in a sorted list.
2. Find the rightmost insertion position of a target with duplicates.
3. Determine how many occurrences of a target exist using `bisect_left()` and `bisect_right()`.
4. Insert values into a sorted list using `insort()`.
5. Given a sorted list and several queries, return the insertion position for every query.

---

## Topic 10: `itertools`

1. Generate all 2-element combinations of a list.
2. Generate all 2-element permutations of a list and explain why the result differs from combinations.
3. Generate the Cartesian product of two small lists.
4. Flatten several lists using `itertools.chain()`.
5. Generate cumulative sums and cumulative products using `itertools.accumulate()`.

---

## Topic 11: `itertools.groupby()`

1. Group consecutive equal values in `[1, 1, 2, 2, 3]`.
2. Explain what happens when equal values are separated, such as `[1, 2, 1, 1]`.
3. Sort a list before using `groupby()` and compare the result.
4. Group words by a key after sorting them by that key.
5. Count the size of each consecutive group using `groupby()`.

---

## Topic 12: `functools`

1. Use `reduce()` to calculate the sum of a list.
2. Use `reduce()` to calculate the product of a list.
3. Write recursive Fibonacci and add `lru_cache` memoization.
4. Use `partial()` to create a specialized multiplication function.
5. Write a simple decorator and use `functools.wraps()` to preserve the wrapped function's metadata.

---

## Topic 13: `math`

1. Calculate the GCD of two integers using `math.gcd()`.
2. Calculate the LCM of two integers using `math.lcm()`.
3. Calculate the square root and factorial of supplied values.
4. Given a decimal value, calculate both its floor and ceiling.
5. Write a program that demonstrates `log()`, `log2()`, and `log10()` on appropriate positive inputs.

---

## Topic 14: `random`

1. Generate a random integer between 1 and 100.
2. Select a random element from a list.
3. Select three unique random elements from a list using `sample()`.
4. Shuffle a list and verify that the original list has been modified.
5. Create random test data for an algorithm and explain why random inputs are useful during testing.

---

## Topic 15: `string`

1. Print all lowercase English letters using `string.ascii_lowercase`.
2. Build a set of all digits using `string.digits`.
3. Remove punctuation from a sentence using a character set from `string`.
4. Check whether every character in a string belongs to a chosen allowed character set.
5. Create a simple character-validation function using `ascii_letters` and `digits`.

---

## Topic 16: List Methods

1. Build a list using `append()` and `extend()` and explain the difference.
2. Remove values using both `remove()` and `pop()` and explain their differences.
3. Demonstrate why `pop(0)` can be inefficient for a queue.
4. Sort a list in-place and compare the result with `sorted()`.
5. Create a shallow copy of a list and demonstrate what copying means.

---

## Topic 17: Dictionary Methods

1. Count the frequency of every value in a list using `dict.get()`.
2. Retrieve a missing key safely using `get()` with a default value.
3. Build a dictionary from two lists using `zip()`.
4. Iterate through keys, values, and key-value pairs using `keys()`, `values()`, and `items()`.
5. Given a dictionary, remove an entry safely and handle a key that does not exist.

---

## Topic 18: Set Methods and Set Operations

1. Remove duplicates from a list using a set.
2. Find the intersection of two sets.
3. Find values that appear in the first set but not the second.
4. Determine whether one set is a subset of another.
5. Given two lists, find their common unique values using set operations.

---

## Topic 19: String Methods

1. Normalize a user-entered name using `strip()`, `lower()`, and `title()`.
2. Count a chosen character in a string.
3. Split a comma-separated string and clean each item.
4. Reverse a string and check whether it is a palindrome.
5. Demonstrate the difference between `find()` and `index()` when the target is missing.

---

## Topic 20: Choosing the Correct Library

1. You need to remove items from both ends of a queue. Which data structure would you choose and why?
2. You need to find the top 5 most frequent numbers. Which library or combination of libraries would you consider?
3. You need to repeatedly retrieve the smallest priority value. Which library would you choose?
4. You need to find where a value should be inserted into a sorted list. Which library would you choose?
5. You need to cache results of a recursive function. Which `functools` feature would you use?

---

# Part 4 --- Interview Comparison Notes

## `list` vs `deque`

| Requirement | Preferred |
|---|---|
| Random indexing | `list` |
| Append to end | `list` or `deque` |
| Remove from end | `list` or `deque` |
| Add/remove from left | `deque` |
| BFS queue | `deque` |

---

## `dict` vs `defaultdict` vs `Counter`

| Requirement | Preferred |
|---|---|
| General key-value mapping | `dict` |
| Automatic default values | `defaultdict` |
| Grouping values | `defaultdict(list)` |
| Frequency counting | `Counter` |
| Top frequent values | `Counter` |

---

## `list` vs `set`

| Requirement | Preferred |
|---|---|
| Preserve sequence/order for normal list processing | `list` |
| Allow duplicate values | `list` |
| Unique values | `set` |
| Fast average-case membership | `set` |
| Index-based access | `list` |

---

## `sorted()` vs `.sort()`

| `sorted()` | `.sort()` |
|---|---|
| Returns a new list | Modifies the list |
| Original iterable can remain unchanged | Original list is changed |
| Works with many iterables | List method |
| Useful when original order is needed | Useful for in-place sorting |

---

## `heapq` vs `sorted()`

- Use sorting when you need the complete ordering.
- Use a heap when you repeatedly need the highest/lowest priority item.
- A heap does not mean the entire list is sorted.
- For interview problems, identify whether the problem needs all elements ordered or only priority access.

---

## `find()` vs `index()`

- `find()` returns `-1` when the substring is missing.
- `index()` raises `ValueError` when the substring is missing.
- Choose based on how you want missing values handled.

---

# Part 5 --- Complexity Cheat Sheet

| Operation / Tool | Typical Complexity |
|---|---:|
| `len(list)` | `O(1)` |
| `list.append()` | `O(1)` amortized |
| `list.pop()` from end | `O(1)` |
| `list.pop(0)` | `O(n)` |
| List membership `x in list` | `O(n)` |
| List sorting | `O(n log n)` |
| Dictionary lookup | `O(1)` average |
| Dictionary insertion | `O(1)` average |
| Set membership | `O(1)` average |
| `deque.append()` | `O(1)` |
| `deque.appendleft()` | `O(1)` |
| `deque.pop()` | `O(1)` |
| `deque.popleft()` | `O(1)` |
| `heapq.heappush()` | `O(log n)` |
| `heapq.heappop()` | `O(log n)` |
| `heapq.heapify()` | `O(n)` |
| `bisect` search | `O(log n)` |
| List insertion after `bisect` | `O(n)` |

> Complexity can depend on the exact operation and implementation. Treat these as common interview-level complexities, not universal guarantees for every operation.

---

# Part 6 --- Roadmap: What to Learn Before DSA Interviews

Follow this order.

1. **Built-ins**
   - `sorted`
   - `min`
   - `max`
   - `sum`
   - `len`
   - `any`
   - `all`
   - `enumerate`
   - `zip`
   - `range`

2. **Core collections**
   - `list`
   - `dict`
   - `set`
   - `deque`

3. **Frequency and grouping**
   - `Counter`
   - `defaultdict`

4. **Priority-based problems**
   - `heapq`

5. **Searching**
   - `bisect`

6. **Iteration tools**
   - `itertools`

7. **Function utilities**
   - `functools`
   - especially `lru_cache`

8. **Supporting modules**
   - `math`
   - `string`
   - `random`

9. **Interview patterns**
   - Frequency counting.
   - Grouping.
   - Queue/BFS.
   - Top K.
   - Heap/Priority Queue.
   - Binary search.
   - Memoization.
   - Custom sorting.

10. **Then connect libraries to DSA**
    - Arrays/lists.
    - Strings.
    - Hashing with dictionaries/sets.
    - Two pointers.
    - Sliding window.
    - Stack/queue.
    - Binary search.
    - Recursion.
    - Linked lists.
    - Trees/graphs.
    - Heaps.
    - Dynamic programming.

---

# Part 7 --- Interview Questions You Should Be Able to Answer

1. Why would you use `deque` instead of a list for a queue?
2. What is the difference between `Counter` and `defaultdict(int)`?
3. What is the difference between `dict.get()` and `d[key]`?
4. Why is a set useful for membership testing?
5. What is the difference between `sorted()` and `.sort()`?
6. What is the difference between a min-heap and a max-heap in Python?
7. Why does `heapq` use negative values for a common integer max-heap technique?
8. What does `bisect_left()` return?
9. What is the difference between `bisect_left()` and `bisect_right()`?
10. Why must a list generally be sorted before using `bisect` as a binary-search tool?
11. What is the difference between combinations and permutations?
12. What does `itertools.groupby()` actually group?
13. Why is `lru_cache` useful in recursive problems?
14. What is memoization?
15. What is the difference between `find()` and `index()`?
16. Why does `list.pop(0)` have different performance characteristics from `deque.popleft()`?
17. What is the average-case complexity of dictionary lookup?
18. What is the average-case complexity of set membership?
19. What is the complexity of `heapq.heappush()`?
20. What is the complexity of `heapq.heapify()`?
21. When would you use `Counter` instead of manually building a frequency dictionary?
22. When would you use `defaultdict(list)`?
23. When would `OrderedDict` still be useful?
24. What does `random.shuffle()` return?
25. Why are strings and named tuples useful as immutable data structures?

---

# Part 8 --- Ready for DSA When You Can

- [ ] Use `sorted()` and `.sort()` correctly.
- [ ] Explain `key=` and `reverse=`.
- [ ] Use `enumerate()` without manually tracking indexes.
- [ ] Use `zip()` and understand that it stops at the shortest iterable.
- [ ] Use `deque` for queue/BFS problems.
- [ ] Use `Counter` for frequency problems.
- [ ] Use `defaultdict` for grouping and graph construction.
- [ ] Use `heapq` for priority queues and Top K patterns.
- [ ] Use `bisect` for insertion positions in sorted arrays.
- [ ] Explain combinations vs permutations.
- [ ] Use `lru_cache` for memoization.
- [ ] Use sets for uniqueness and average-case membership.
- [ ] Use dictionaries for hashing/frequency maps.
- [ ] Explain common time complexities.
- [ ] Identify the correct Python library from the problem requirement.
- [ ] Solve the practice questions without looking at solutions.
- [ ] Dry-run the code on empty, single-item, duplicate, boundary, and large inputs.

---

# Part 9 --- Final Interview Memory Sheet

Write these from memory before an interview:

```text
deque
    Queue / BFS / sliding window
    append / appendleft
    pop / popleft

Counter
    Frequency
    most_common(k)

defaultdict
    Grouping
    Graph
    defaultdict(list)
    defaultdict(int)

heapq
    Min-heap
    heappush / heappop
    heapify
    Top K / priority queue

bisect
    Sorted list
    Binary-search insertion position
    bisect_left / bisect_right

itertools
    combinations
    permutations
    product
    chain
    accumulate
    groupby

functools
    lru_cache
    reduce
    partial
    wraps

math
    gcd / lcm
    sqrt / factorial
    ceil / floor
    logs

string
    ascii_letters
    digits
    punctuation
    whitespace

built-ins
    sorted
    min / max
    sum
    any / all
    enumerate
    zip
    range
    reversed
```

## Practice Rule

Attempt every question yourself first.

For each problem:
1. Read the question.
2. Identify the required data structure/library.
3. Write the approach in plain English.
4. Write the code.
5. Test a normal case.
6. Test an edge case.
7. State the time and space complexity.
8. Explain why you selected that library.

Do not move on based only on reading notes. Write and run the code.

