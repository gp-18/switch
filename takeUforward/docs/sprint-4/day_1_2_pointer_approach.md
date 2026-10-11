# Two Pointer Approach

Notes for DSA practice and Product-Based Company (PBC) interviews. All code is in Python.

Contents
- [Part 1: What Is the Two Pointer Approach?](#part-1-what-is-the-two-pointer-approach)
- [Part 2: Revision Notes](#part-2-revision-notes)
- [Part 3: How to Identify a Two Pointer Problem](#part-3-how-to-identify-a-two-pointer-problem)
- [Part 4: 20 Practice Questions](#part-4-20-practice-questions)

---

## Part 1: What Is the Two Pointer Approach?

### 1.1 The short answer (for interviews)

> The Two Pointer Approach uses two variables that hold positions (indices) in an array. We move them step by step based on a condition, so we solve the problem in one pass instead of checking every pair. This usually brings time from O(N^2) down to O(N).

### 1.2 What is a pointer?

In an array, a **pointer** is just a variable that stores an **index**. It tells us "I am looking at this position right now".

```python
nums = [4, 7, 1, 9, 3]
left = 0              # left points to nums[0] = 4
right = len(nums) - 1 # right points to nums[4] = 3
```

There is no special memory address here. It is only an index number.

### 1.3 Why do we use two pointers?

Many problems need us to look at **pairs** of elements. The simple way is two loops, one inside the other. That checks every pair and is slow.

With two pointers, each move **removes some choices for good**. We never look at the same thing again. So we finish in one walk.

### 1.4 How do the two pointers work together?

- Each pointer has a job.
- We look at the values at both pointers.
- A **condition** tells us which pointer to move.
- The pointers never go back. They only move in one direction.

### 1.5 Two ways to use two pointers

| Style | Start | Movement | Typical use |
|---|---|---|---|
| Opposite ends | `left = 0`, `right = N - 1` | Move toward each other | Reverse, palindrome, pair sum in a sorted array |
| Same direction | Both near the start | Move forward, one faster or only when a condition is true | Remove duplicates, move zeros, partition |

There is also a third small variant: **one pointer per array** when we have two sorted arrays (merge, intersection).

### 1.6 When do the pointers move and when do they stop?

- **Opposite ends:** they move inward. Stop when `left >= right`.
- **Same direction:** the fast pointer visits every index. Stop when it reaches the end.
- **Two arrays:** stop when one pointer reaches the end of its array (or both, for merge).

### 1.7 Simple approach vs two pointers

Problem: in a **sorted** array, is there a pair with sum equal to `target`?

Simple way (check every pair):

```python
def has_pair_simple(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return True
    return False
```

Time O(N^2). Space O(1).

Two pointers:

```python
def has_pair_two_pointers(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return True
        elif total < target:
            left += 1      # need a bigger sum
        else:
            right -= 1     # need a smaller sum
    return False
```

Time O(N). Space O(1).

### 1.8 Step-by-step example

`nums = [1, 3, 4, 6, 9]`, `target = 10`

| Step | left | right | nums[left] + nums[right] | Decision |
|---|---|---|---|---|
| 1 | 0 | 4 | 1 + 9 = 10 | Equal, found it |

Another run with `target = 11`:

| Step | left | right | Sum | Decision |
|---|---|---|---|---|
| 1 | 0 (1) | 4 (9) | 10 | Too small, move `left` |
| 2 | 1 (3) | 4 (9) | 12 | Too big, move `right` |
| 3 | 1 (3) | 3 (6) | 9 | Too small, move `left` |
| 4 | 2 (4) | 3 (6) | 10 | Too small, move `left` |
| 5 | 3 | 3 | - | `left == right`, stop. Answer is False |

Why is moving `left` safe when the sum is too small? Because `nums[right]` is already the biggest number we can still use. If `nums[left]` is too small even with the biggest partner, it can never work. So we drop it.

### 1.9 Another easy example: reverse an array

```python
def reverse(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums
```

### 1.10 Time and space complexity

- **Time:** O(N). Each pointer moves at most N steps in total, and never goes back.
- **Space:** O(1). We only use a few variables. (If we build a new output array, that extra space is for the output, not for the technique.)
- If the problem needs a **sorted** array and the input is not sorted, sorting first costs O(N log N), and that becomes the total time.

---

## Part 2: Revision Notes

### 2.1 Basic idea
Two index variables walk through the array. A condition decides which one moves. We avoid checking every pair.

### 2.2 Things to remember
- Pointers only move forward or inward. They do not reset.
- Every pointer move must be **justified**: "why can I forget this element?"
- Two pointers on opposite ends usually need a **sorted** array (or a problem where order does not matter, like reverse).
- Check `left < right` (not `<=`) when a pair needs two different elements.
- Edge cases: empty array, one element, all same values, all already good.

### 2.3 Types of two pointer technique

| Type | Meaning in simple words |
|---|---|
| Opposite ends | One finger at each end, walk toward the middle |
| Reader and writer (slow and fast) | Fast reads every element. Slow marks where the next good element goes |
| Two arrays | One finger per sorted array, move the one with the smaller value |
| Fast and slow with different speeds | One moves 1 step, the other 2 steps (used for cycle ideas) |
| Three pointers | Extra pointer for a third group (example: sort values 0, 1, 2) |

### 2.4 Which way do pointers move?

| Situation | Movement |
|---|---|
| Pair in sorted array | Toward each other |
| Remove or filter in place | Both forward, slow only moves when we keep an element |
| Merge sorted arrays | Both forward, move the smaller one |
| Fill result from the back | Pointers move backward |

### 2.5 How conditions decide movement
- Sum too small in a sorted array: move `left` (we need a bigger number).
- Sum too big: move `right` (we need a smaller number).
- Element is good (keep it): write it at `slow`, then `slow += 1`.
- Element is bad: skip it, only `fast` moves.
- `a[i] < b[j]` in two sorted arrays: move `i`.

### 2.6 Common patterns in array problems
1. Pair or triplet with a target sum (sorted).
2. In-place removal, compaction, or partition.
3. Merging or comparing two sorted arrays.
4. Reverse or mirror checks.
5. Best area or best value from both ends (greedy move of the weaker side).

### 2.7 Common mistakes
- Using two pointers on an **unsorted** array for a pair-sum problem (use a hash map instead).
- Moving the wrong pointer.
- Off-by-one: `<` vs `<=`.
- Forgetting to copy the leftover elements when merging.
- Not skipping duplicates in 3Sum style problems.
- Forgetting `k = k % n` when rotating.

### 2.8 Complexity

| Pattern | Time | Space |
|---|---|---|
| Opposite ends | O(N) | O(1) |
| Reader and writer | O(N) | O(1) |
| Two arrays | O(N + M) | O(1) extra (O(N + M) if you build a new array) |
| Triplets (sort + loop + two pointers) | O(N^2) | O(1) extra, plus sort space |

### 2.9 Quick revision table

| Pattern | Pointers start | Move rule | Example |
|---|---|---|---|
| Opposite ends | 0 and N-1 | Based on sum or comparison | Container With Most Water |
| Reader and writer | 0 and 0 | Writer moves only on keep | Remove Duplicates II |
| Two arrays | 0 in each | Move smaller | Merge two arrays |
| Three pointers | low, mid, high | Based on value at mid | Sort Colors |
| Fast and slow | 0 and 0 | 1 step and 2 steps | Find the Duplicate Number |

### 2.10 Pseudocode templates

**Opposite ends**

```python
left, right = 0, len(nums) - 1
while left < right:
    if condition_met(nums[left], nums[right]):
        # record answer
        left += 1
        right -= 1
    elif need_bigger_value:
        left += 1
    else:
        right -= 1
```

**Reader and writer**

```python
slow = 0
for fast in range(len(nums)):
    if is_good(nums[fast]):
        nums[slow] = nums[fast]
        slow += 1
# first `slow` elements are the answer
```

**Two sorted arrays**

```python
i = j = 0
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        i += 1
    elif a[i] > b[j]:
        j += 1
    else:
        # equal: record, then move both
        i += 1
        j += 1
# handle leftovers if the problem needs them
```

**Three pointers (low, mid, high)**

```python
low, mid, high = 0, 0, len(nums) - 1
while mid <= high:
    if nums[mid] == 0:
        nums[low], nums[mid] = nums[mid], nums[low]
        low += 1
        mid += 1
    elif nums[mid] == 1:
        mid += 1
    else:
        nums[mid], nums[high] = nums[high], nums[mid]
        high -= 1
```

---

## Part 3: How to Identify a Two Pointer Problem

### 3.1 Clues in the problem statement
- "Sorted array" plus "find a pair / triplet / closest sum".
- "In-place", "without extra space", "O(1) space".
- "Remove", "move", "partition", "rearrange".
- "Two sorted arrays" or "merge".
- "Maximum area", "minimum difference" between two elements, where both ends matter.
- The brute force is two nested loops over the same array.

### 3.2 Common array problem types
- Pair or triplet sum (sorted, or sort first).
- Partition by a rule (even/odd, sign, three colors).
- In-place cleanup (duplicates, zeros, specific value).
- Merge or compare two sorted arrays.
- Area or distance between two positions.

### 3.3 How a sorted array helps
When the array is sorted, the sum of two pointers gives us a **direction**:
- Sum too small: only a bigger number can fix it, so move `left`.
- Sum too big: only a smaller number can fix it, so move `right`.

Without order, we do not know which way to go, so this logic breaks.

### 3.4 Reducing time complexity
Checking all pairs is O(N^2). Two pointers makes each element be dropped once, so the walk is O(N). For triplets, we fix one element and use two pointers on the rest: O(N^2) instead of O(N^3).

### 3.5 Which pointer should move?
Ask: "Which pointer is **blocking** me from improving the answer?"
- Pair sum: the side that makes the sum wrong.
- Container With Most Water: the shorter wall, because the area is limited by it. Moving the taller wall can never help.
- Merge: the pointer on the smaller value.

### 3.6 When should one pointer move faster?
- When one pointer **reads** everything and the other only **writes** the kept items (reader and writer).
- When the problem treats the array like a chain of jumps and we look for a cycle (fast moves 2, slow moves 1).

### 3.7 Two pointers vs sliding window

| | Two pointers | Sliding window |
|---|---|---|
| Idea | Two positions that help decide an answer | A range (window) between two pointers that grows and shrinks |
| Focus | The values at the pointers | The contents of the subarray between them |
| Typical question | Pair with sum, partition, merge | Longest or shortest subarray with a property |
| Pointers | Often opposite ends | Same direction, `left <= right` |

Sliding window is a special form of two pointers where both move forward and the part between them matters.

### 3.8 When to avoid two pointers
- Unsorted array and you need a pair: hash map is usually better.
- You need subarray sums with negative numbers: use prefix sums with a hash map.
- The answer depends on all combinations and no move can be justified.
- You cannot explain why a pointer move is safe. Then it is not the right tool.

Not every sorted array problem uses two pointers. Binary search or a simple loop may be better.

### 3.9 Checklist for a new array problem
1. What exactly is asked? Write input and output in your own words.
2. Is the array sorted, or can I sort it without breaking the answer?
3. Do I need two positions at the same time?
4. What value tells me to move a pointer, and which one?
5. Can I explain why the skipped elements are safe to skip?
6. Is the time better than the brute force? Is space O(1)?
7. Check edge cases (empty, one element, duplicates).

### 3.10 Small examples

| Problem | Two pointers? | Why |
|---|---|---|
| Sorted array, find two numbers with sum 9 | Yes | Sum tells which side to move |
| Unsorted array, find two numbers with sum 9 | Not directly | No direction. Use a hash map (or sort first if indices are not needed) |
| Remove all 5s from an array in place | Yes | Reader and writer |
| Longest subarray with sum at most K (all positive) | Sliding window | Window grows and shrinks |
| Maximum subarray sum (with negatives) | No | Use Kadane's algorithm |
| Merge two sorted arrays | Yes | One pointer per array |

---

## Part 4: 20 Practice Questions (Easy & Confidence-Boosting)

Here are 20 beginner-friendly array problems to practice the Two Pointer approach step-by-step. They are arranged to build your confidence and intuition. No full solutions are given so you can solve them yourself!

---

## 1. Reverse an Array

Given an array of integers `nums`, reverse the array in-place so that the first element becomes the last and the last becomes the first.

### Example

```text
Input:  nums = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]

Input:  nums = [10, 20]
Output: [20, 10]

Input:  nums = [7]
Output: [7]  # A single element remains unchanged
```

### Think About

* Put your left finger at the start (`left = 0`) and your right finger at the end (`right = len(nums) - 1`).
* Swap `nums[left]` and `nums[right]`.
* Move `left` one step forward (`left += 1`) and `right` one step backward (`right -= 1`).
* Keep swapping until the fingers meet or cross (`while left < right`).
* **Time Complexity:** $\mathcal{O}(N)$
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space

**File:** `01_reverse_array.py`

---

## 2. Check if Array is a Palindrome

Given an array of integers `nums`, determine if the array reads the same forward and backward. Return `True` if it is a palindrome, otherwise return `False`.

### Example

```text
Input:  nums = [1, 2, 3, 2, 1]
Output: True

Input:  nums = [1, 2, 3, 4]
Output: False

Input:  nums = [5]
Output: True  # Single element is always a palindrome
```

### Think About

* Place `left = 0` at the start and `right = len(nums) - 1` at the end.
* Compare `nums[left]` and `nums[right]`:
  * If they are not equal, return `False` immediately (not a palindrome).
  * If they are equal, move inward: `left += 1` and `right -= 1`.
* If the pointers cross and no mismatch was found, return `True`.
* **Time Complexity:** $\mathcal{O}(N)$
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space

**File:** `02_is_array_palindrome.py`

---

## 3. Reverse Subarray Between Indices L and R

Given an array `nums` and two valid indices `L` and `R` where $0 \le L \le R < \text{len}(nums)$, reverse only the elements from index `L` to index `R` in-place. Leave all other elements in their original positions.

### Example

```text
Input:  nums = [1, 2, 3, 4, 5, 6], L = 1, R = 4
Output: [1, 5, 4, 3, 2, 6]

Input:  nums = [9, 8, 7, 6], L = 0, R = 2
Output: [7, 8, 9, 6]

Input:  nums = [4, 5, 6], L = 1, R = 1
Output: [4, 5, 6]  # Subarray of length 1 stays unchanged
```

### Think About

* This is the exact same logic as reversing an array, but your fingers start at `left = L` and `right = R`.
* Swap `nums[left]` and `nums[right]`, then move inward (`left += 1`, `right -= 1`).
* Stop when `left >= right`.
* **Time Complexity:** $\mathcal{O}(R - L + 1) \subseteq \mathcal{O}(N)$
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space

**File:** `03_reverse_subarray.py`

---

## 4. Sum of Mirror Pairs (Ends to Middle)

Given an array of integers `nums`, calculate the sum of pairs starting from both ends: add the first and last element, then the second and second-last element, and so on. Return these sums in a list. If the array has an odd length, include the middle single element alone at the end.

### Example

```text
Input:  nums = [1, 2, 3, 4, 5]
Output: [6, 6, 3]  # (1 + 5 = 6), (2 + 4 = 6), middle 3

Input:  nums = [10, 20, 30, 40]
Output: [50, 50]  # (10 + 40 = 50), (20 + 30 = 50)

Input:  nums = [9]
Output: [9]  # Single element middle
```

### Think About

* Initialize `left = 0`, `right = len(nums) - 1`, and an empty list `result = []`.
* While `left < right`:
  * Append `nums[left] + nums[right]` to `result`.
  * Move `left += 1` and `right -= 1`.
* If `left == right` after the loop (odd number of elements), append `nums[left]` alone.
* **Time Complexity:** $\mathcal{O}(N)$
* **Space Complexity:** $\mathcal{O}(N)$ for the output list

**File:** `04_sum_mirror_pairs.py`

---

## 5. Two Sum in a Sorted Array (Two Sum II)

Given an array of integers `nums` already sorted in ascending order, find two numbers such that they add up to a given `target`. Return their 1-based indices `[index1, index2]`. Assume exactly one solution exists.

### Example

```text
Input:  nums = [2, 7, 11, 15], target = 9
Output: [1, 2]  # nums[0] + nums[1] = 2 + 7 = 9 (1-based: indices 1 and 2)

Input:  nums = [2, 3, 4], target = 6
Output: [1, 3]  # 2 + 4 = 6 (1-based: indices 1 and 3)

Input:  nums = [-5, -2, 1, 4], target = -7
Output: [1, 2]  # -5 + -2 = -7
```

### Think About

* Put `left = 0` (pointing to smallest number) and `right = len(nums) - 1` (pointing to largest number).
* Check `current_sum = nums[left] + nums[right]`:
  * If `current_sum == target`: you found it! Return `[left + 1, right + 1]`.
  * If `current_sum < target`: the sum is too small. We need a bigger number, so advance `left += 1`.
  * If `current_sum > target`: the sum is too big. We need a smaller number, so move `right -= 1`.
* **Time Complexity:** $\mathcal{O}(N)$
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space

**File:** `05_two_sum_sorted.py`

---

## 6. Count Pairs with Given Sum in a Sorted Array

Given an array of distinct integers `nums` sorted in ascending order, and an integer `target`, count how many unique pairs `(nums[i], nums[j])` with $i < j$ add up to `target`.

### Example

```text
Input:  nums = [1, 2, 3, 4, 5, 6], target = 7
Output: 3  # Pairs: (1, 6), (2, 5), (3, 4)

Input:  nums = [1, 3, 5, 7, 9], target = 12
Output: 2  # Pairs: (3, 9), (5, 7)

Input:  nums = [2, 4, 6], target = 15
Output: 0  # No pair sums to 15
```

### Think About

* Initialize `left = 0`, `right = len(nums) - 1`, and `count = 0`.
* While `left < right`:
  * If `nums[left] + nums[right] == target`: we found a pair! Increment `count += 1`, and move both: `left += 1`, `right -= 1`.
  * If `nums[left] + nums[right] < target`: need a larger sum, move `left += 1`.
  * If `nums[left] + nums[right] > target`: need a smaller sum, move `right -= 1`.
* **Time Complexity:** $\mathcal{O}(N)$
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space

**File:** `06_count_pairs_sorted.py`

---

## 7. Count Pairs Whose Sum is Less than Target (Sorted Array)

Given an array `nums` of integers sorted in ascending order and an integer `target`, count how many pairs `(i, j)` with $i < j$ have a sum strictly less than `target` ($nums[i] + nums[j] < target$).

### Example

```text
Input:  nums = [1, 2, 3, 4, 5], target = 6
Output: 4  # Pairs: (1, 2), (1, 3), (1, 4), (2, 3)

Input:  nums = [-1, 1, 2, 3], target = 2
Output: 2  # Pairs: (-1, 1), (-1, 2)

Input:  nums = [4, 5, 6], target = 5
Output: 0  # Smallest sum is 4 + 5 = 9, none < 5
```

### Think About

* Put `left = 0` and `right = len(nums) - 1`.
* If `nums[left] + nums[right] < target`:
  * Since the array is sorted, pairing `nums[left]` with **any** number between `left + 1` and `right` will ALSO have a sum less than `target`!
  * So add all `(right - left)` pairs to your count at once!
  * Then move `left += 1` to check the next number.
* If `nums[left] + nums[right] >= target`: sum is too large, move `right -= 1`.
* **Time Complexity:** $\mathcal{O}(N)$
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space

**File:** `07_count_pairs_less_than_target.py`

---

## 8. Squares of a Sorted Array

Given an array of integers `nums` sorted in non-decreasing order (which may include negative numbers), return an array of the squares of each number, also sorted in non-decreasing order.

### Example

```text
Input:  nums = [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]

Input:  nums = [-7, -3, 2, 3, 11]
Output: [4, 9, 9, 49, 121]

Input:  nums = [-5, -4, -3, -2, -1]
Output: [1, 4, 9, 16, 25]  # All negatives reversed when squared
```

### Think About

* Negative numbers like -4 produce big squares ($(-4)^2 = 16$). The largest squares will always be at the extreme left or extreme right.
* Create a new array `result` of the same length $N$, and fill it from the **very back** (`pos = N - 1` down to 0).
* Compare `nums[left] ** 2` and `nums[right] ** 2`:
  * Whichever square is bigger, place it at `result[pos]` and move that pointer inward.
  * Decrement `pos -= 1`.
* **Time Complexity:** $\mathcal{O}(N)$
* **Space Complexity:** $\mathcal{O}(N)$ for result array, $\mathcal{O}(1)$ auxiliary space

**File:** `08_squares_sorted_array.py`

---

## 9. Sort Array By Parity (Evens First, Odds Last)

Given an array of integers `nums`, rearrange the array in-place so that all even integers appear at the beginning and all odd integers appear at the end. Any order inside the even and odd groups is acceptable.

### Example

```text
Input:  nums = [3, 1, 2, 4]
Output: [4, 2, 1, 3]  # (or [2, 4, 3, 1] — any even-then-odd order is valid)

Input:  nums = [1, 3, 5, 2]
Output: [2, 3, 5, 1]

Input:  nums = [2, 4, 6]
Output: [2, 4, 6]  # Already all even
```

### Think About

* Put `left = 0` at the start and `right = len(nums) - 1` at the end.
* While `nums[left] % 2 == 0`: move `left += 1` (even numbers are already on the correct side).
* While `nums[right] % 2 != 0`: move `right -= 1` (odd numbers are already on the correct side).
* When `left < right`, swap `nums[left]` and `nums[right]`, then advance both.
* **Time Complexity:** $\mathcal{O}(N)$
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space

**File:** `09_sort_array_by_parity.py`

---

## 10. Segregate 0s and 1s in an Array

Given a binary array `nums` containing only `0`s and `1`s, sort the array in-place so that all `0`s are on the left and all `1`s are on the right.

### Example

```text
Input:  nums = [0, 1, 0, 1, 1, 0]
Output: [0, 0, 0, 1, 1, 1]

Input:  nums = [1, 1, 0, 0, 1]
Output: [0, 0, 1, 1, 1]

Input:  nums = [1, 1, 1]
Output: [1, 1, 1]  # No zeros present
```

### Think About

* Put `left = 0` and `right = len(nums) - 1`.
* Advance `left` while `nums[left] == 0` (`left += 1`).
* Decrement `right` while `nums[right] == 1` (`right -= 1`).
* When `left < right`, swap `nums[left]` and `nums[right]`.
* **Time Complexity:** $\mathcal{O}(N)$
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space

**File:** `10_segregate_0s_and_1s.py`

---

## 11. Move All Zeros to the End

Given an array of integers `nums`, move all `0`s to the end of the array in-place while maintaining the relative order of the non-zero elements.

### Example

```text
Input:  nums = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]

Input:  nums = [0, 0, 1]
Output: [1, 0, 0]

Input:  nums = [4, 5, 6]
Output: [4, 5, 6]  # No zeros to move
```

### Think About

* Use the Reader and Writer pattern: `slow = 0`.
* Loop `fast` from 0 to `len(nums) - 1`:
  * If `nums[fast] != 0`: swap `nums[slow]` and `nums[fast]`, then increment `slow += 1`.
* Every non-zero number gets placed into the next available front spot, naturally pushing zeros to the back.
* **Time Complexity:** $\mathcal{O}(N)$
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space

**File:** `11_move_zeros_to_end.py`

---

## 12. Remove Element In-Place

Given an array `nums` and a value `val`, remove all instances of `val` in-place. Return the number of elements left that are not equal to `val` ($k$). The first $k$ elements of `nums` should hold the answer.

### Example

```text
Input:  nums = [3, 2, 2, 3], val = 3
Output: k = 2, nums starts with [2, 2]

Input:  nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
Output: k = 5, nums starts with [0, 1, 3, 0, 4]

Input:  nums = [7, 7, 7], val = 7
Output: k = 0, nums is empty of valid elements
```

### Think About

* Writer pointer `slow = 0`.
* Reader pointer `fast` scans every element from index 0 to $N - 1$:
  * If `nums[fast] != val`: copy `nums[slow] = nums[fast]` and advance `slow += 1`.
* Return `slow`.
* **Time Complexity:** $\mathcal{O}(N)$
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space

**File:** `12_remove_element.py`

---

## 13. Remove Duplicates from a Sorted Array

Given an array `nums` sorted in ascending order, remove duplicates in-place so that each unique element appears only once. Return the number of unique elements $k$.

### Example

```text
Input:  nums = [1, 1, 2]
Output: k = 2, nums starts with [1, 2]

Input:  nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Output: k = 5, nums starts with [0, 1, 2, 3, 4]

Input:  nums = [5]
Output: k = 1, nums = [5]  # Single element has no duplicates
```

### Think About

* If the array is empty, return 0.
* The first element is always kept: set writer pointer `slow = 0`.
* Loop reader pointer `fast` from index 1 to $N - 1$:
  * If `nums[fast] != nums[slow]`: you found a new unique number!
  * Increment `slow += 1` and write `nums[slow] = nums[fast]`.
* Return `slow + 1` (the number of unique elements placed).
* **Time Complexity:** $\mathcal{O}(N)$
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space

**File:** `13_remove_duplicates_sorted.py`

---

## 14. Move Negative Numbers to Front, Positives to Back

Given an array `nums` of positive and negative integers, rearrange the array in-place so that all negative numbers appear on the left and all positive numbers appear on the right. Any order inside each group is fine.

### Example

```text
Input:  nums = [3, -1, 4, -5, 2]
Output: [-1, -5, 4, 3, 2]  # Any order where negatives are on the left

Input:  nums = [-2, -3, 4, -1, 5]
Output: [-2, -3, -1, 4, 5]

Input:  nums = [-4, -2, -1]
Output: [-4, -2, -1]  # Already all negative
```

### Think About

* Put `left = 0` and `right = len(nums) - 1`.
* Advance `left` while `nums[left] < 0` (negative numbers are happy on the left).
* Decrement `right` while `nums[right] >= 0` (positives are happy on the right).
* When `left < right`: swap `nums[left]` and `nums[right]`.
* **Time Complexity:** $\mathcal{O}(N)$
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space

**File:** `14_move_negatives_front.py`

---

## 15. Find Pair with Target Difference in Sorted Array

Given an array of integers `nums` sorted in ascending order and a positive integer `diff`, return `True` if there exists a pair of distinct indices $(i, j)$ such that $nums[j] - nums[i] == diff$, otherwise return `False`.

### Example

```text
Input:  nums = [1, 2, 4, 7, 10], diff = 3
Output: True  # (4 - 1 = 3, or 7 - 4 = 3, or 10 - 7 = 3)

Input:  nums = [2, 3, 5, 8], diff = 4
Output: False

Input:  nums = [1, 5, 5, 9], diff = 0
Output: True  # (5 - 5 = 0 using indices 1 and 2)
```

### Think About

* Both pointers start at the front: `i = 0` and `j = 1`.
* While `i < len(nums)` and `j < len(nums)`:
  * If `i != j` and `nums[j] - nums[i] == diff`: return `True`.
  * If `nums[j] - nums[i] < diff`: difference is too small, move `j += 1` to get a larger value.
  * If `nums[j] - nums[i] > diff`: difference is too big, move `i += 1` to increase `nums[i]`.
  * If `i == j`: make sure `j` stays ahead by doing `j += 1`.
* **Time Complexity:** $\mathcal{O}(N)$
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space

**File:** `15_pair_with_difference.py`

---

## 16. Merge Two Sorted Arrays

Given two sorted integer arrays `a` and `b`, merge them into a single new sorted array containing all elements from both.

### Example

```text
Input:  a = [1, 3, 5], b = [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]

Input:  a = [1, 2, 7], b = [3, 4]
Output: [1, 2, 3, 4, 7]

Input:  a = [], b = [1, 5, 9]
Output: [1, 5, 9]  # One array is empty
```

### Think About

* Put finger `i = 0` on array `a` and finger `j = 0` on array `b`.
* Compare `a[i]` and `b[j]`:
  * If `a[i] <= b[j]`: append `a[i]` to `result` and move `i += 1`.
  * Else: append `b[j]` to `result` and move `j += 1`.
* When one array runs out, append all leftover elements from the other array.
* **Time Complexity:** $\mathcal{O}(N + M)$
* **Space Complexity:** $\mathcal{O}(N + M)$ for the new output list

**File:** `16_merge_two_sorted_arrays.py`

---

## 17. Intersection of Two Sorted Arrays

Given two sorted integer arrays `a` and `b`, return a list of elements that appear in **both** arrays (including duplicates if an element appears multiple times in both).

### Example

```text
Input:  a = [1, 2, 2, 3, 4], b = [2, 2, 4, 6]
Output: [2, 2, 4]

Input:  a = [1, 3, 5], b = [2, 4, 6]
Output: []

Input:  a = [3, 3, 3], b = [3, 3]
Output: [3, 3]  # Min frequency of common element is preserved
```

### Think About

* Put `i = 0` on `a` and `j = 0` on `b`.
* While `i < len(a)` and `j < len(b)`:
  * If `a[i] < b[j]`: `a[i]` is too small to match, move `i += 1`.
  * If `b[j] < a[i]`: `b[j]` is too small to match, move `j += 1`.
  * If `a[i] == b[j]`: common element! Append to `result`, then advance both `i += 1` and `j += 1`.
* **Time Complexity:** $\mathcal{O}(N + M)$
* **Space Complexity:** $\mathcal{O}(\min(N, M))$ for output

**File:** `17_intersection_sorted_arrays.py`

---

## 18. Union of Two Sorted Arrays

Given two sorted integer arrays `a` and `b`, return a sorted list containing the union of elements from both arrays (all unique elements appearing in either array, with no duplicates in the output).

### Example

```text
Input:  a = [1, 2, 3, 4], b = [2, 3, 5]
Output: [1, 2, 3, 4, 5]

Input:  a = [2, 2, 3], b = [1, 1, 2]
Output: [1, 2, 3]

Input:  a = [1, 1, 1], b = [1, 1]
Output: [1]  # Duplicates collapsed into one
```

### Think About

* Put `i = 0` on `a` and `j = 0` on `b`, with an empty list `result = []`.
* Helper rule: only append a value `val` to `result` if `len(result) == 0` or `result[-1] != val` (to prevent duplicates).
* While `i < len(a)` and `j < len(b)`:
  * If `a[i] <= b[j]`: add `a[i]` using helper rule, move `i += 1`.
  * Else: add `b[j]` using helper rule, move `j += 1`.
* Drain any remaining elements from `a` or `b` with the same helper rule.
* **Time Complexity:** $\mathcal{O}(N + M)$
* **Space Complexity:** $\mathcal{O}(N + M)$ for output

**File:** `18_union_sorted_arrays.py`

---

## 19. Check if Array A is a Subsequence of Array B

Given two integer arrays `a` and `b`, return `True` if `a` is a subsequence of `b`, or `False` otherwise. (An array `a` is a subsequence of `b` if `a` can be formed by deleting zero or more elements from `b` without changing the order of the remaining elements).

### Example

```text
Input:  a = [1, 3, 5], b = [1, 2, 3, 4, 5, 6]
Output: True  # 1, 3, 5 appear in b in the exact same relative order

Input:  a = [5, 3], b = [1, 2, 3, 4, 5]
Output: False  # Elements are present, but their order is reversed

Input:  a = [], b = [1, 2, 3]
Output: True  # Empty array is always a valid subsequence
```

### Think About

* Put finger `i = 0` on `a` (the target pattern) and finger `j = 0` on `b` (the main list).
* While `i < len(a)` and `j < len(b)`:
  * If `a[i] == b[j]`: you matched the current number! Advance `i += 1`.
  * Always advance `j += 1` to keep searching forward in `b`.
* If `i == len(a)`, all numbers of `a` were matched in order: return `True`, otherwise `False`.
* **Time Complexity:** $\mathcal{O}(\text{len}(b))$
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space

**File:** `19_is_subsequence_array.py`

---

## 20. Valid Mountain Array

Given an array of integers `arr`, return `True` if and only if it is a valid mountain array. An array is a mountain array if `len(arr) >= 3` and the numbers strictly increase to a single peak, then strictly decrease to the end.

### Example

```text
Input:  arr = [0, 3, 2, 1]
Output: True  # Uphill 0 -> 3, downhill 3 -> 2 -> 1

Input:  arr = [3, 5, 5]
Output: False  # Plateau / duplicate numbers not allowed

Input:  arr = [2, 1]
Output: False  # Length must be at least 3
```

### Think About

* Think of two climbers starting from opposite ends:
  * Left climber starts at `left = 0` and climbs uphill while `left + 1 < len(arr)` and `arr[left] < arr[left + 1]`.
  * Right climber starts at `right = len(arr) - 1` and climbs uphill from the back while `right - 1 >= 0` and `arr[right] < arr[right - 1]`.
* If both climbers meet at the exact same peak (`left == right`) and that peak is not at index 0 and not at the last index, return `True`!
* **Time Complexity:** $\mathcal{O}(N)$
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space

**File:** `20_valid_mountain_array.py`

