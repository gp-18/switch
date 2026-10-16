# 🟢 Day 2 — Arrays: Core & Basic Problems

## 1. Majority Element-I

Given an integer array `nums` of size $n$, return the majority element of the array. The majority element of an array is an element that appears strictly more than $\lfloor n / 2 \rfloor$ times in the array. The array is guaranteed to always have a majority element.

### Example

```text
Input:  nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
Output: 7

Input:  nums = [1, 1, 1, 2, 1, 2]
Output: 1

Input:  nums = [-1, -1, -1, -1]  # Edge Case: All elements are identical negatives
Output: -1
```

### Think About

* **Boyer-Moore Voting Algorithm ($\mathcal{O}(1)$ Space):**
  * Maintain `candidate = None` and `count = 0`.
  * Iterate through `nums`:
    * If `count == 0`: set `candidate = num` and `count = 1`.
    * Else if `num == candidate`: increment `count += 1`.
    * Else: decrement `count -= 1`.
  * Since the majority element appears more than $n / 2$ times, non-majority elements cannot cancel all of its votes, and `candidate` will hold the majority element.
* **Alternative (Sorting):** Sort `nums` and return `nums[n // 2]` because any element occupying $> n / 2$ positions must cross the middle index.
* **Time Complexity:** $\mathcal{O}(N)$ using Boyer-Moore, $\mathcal{O}(N \log N)$ using sorting.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** `01_majority_element.py`

---

## 2. Leaders in an Array

Given an integer array `nums`, return a list of all the leaders in the array. An element is a leader if its value is strictly greater than all elements to its right in the array. The rightmost element is always a leader. The elements in the leader array must appear in the order they appear in the `nums` array.

### Example

```text
Input:  nums = [1, 2, 5, 3, 1, 2]
Output: [5, 3, 2]

Input:  nums = [-3, 4, 5, 1, -4, -5]
Output: [5, 1, -4, -5]

Input:  nums = [10]  # Edge Case: Single element is always a leader
Output: [10]
```

### Think About

* Scanning left to right requires checking all elements to the right for each element, leading to $\mathcal{O}(N^2)$ time.
* Optimal approach: Traverse from right to left (index $n - 1$ down to 0).
* Maintain a running suffix maximum `max_from_right = -float('inf')`.
* For each `nums[i]`:
  * If `nums[i] > max_from_right`: append `nums[i]` to `leaders` and update `max_from_right = nums[i]`.
* Since leaders are collected from right to left, reverse the `leaders` list at the end before returning to preserve original order.
* **Time Complexity:** $\mathcal{O}(N)$
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space (excluding the output list).

**File:** `02_leaders_in_array.py`

---

## 3. Rearrange Array Elements by Sign

Given an integer array `nums` of even length consisting of an equal number of positive and negative integers, return the rearranged array such that:
1. Every consecutive pair of integers have opposite signs.
2. For all integers with the same sign, the order in which they were present in `nums` is preserved.
3. The rearranged array begins with a positive integer.

### Example

```text
Input:  nums = [2, 4, 5, -1, -3, -4]
Output: [2, -1, 4, -3, 5, -4]

Input:  nums = [1, -1, -3, -4, 2, 3]
Output: [1, -1, 2, -3, 3, -4]

Input:  nums = [3, -2]  # Edge Case: Smallest even array of size 2
Output: [3, -2]
```

### Think About

* Positive numbers must be placed at even indices (`0, 2, 4, ...`).
* Negative numbers must be placed at odd indices (`1, 3, 5, ...`).
* Initialize an answer array `ans = [0] * n`, and two pointer indices `pos_idx = 0` and `neg_idx = 1`.
* Traverse `nums` in a single pass:
  * If `num > 0`: `ans[pos_idx] = num`, then `pos_idx += 2`.
  * If `num < 0`: `ans[neg_idx] = num`, then `neg_idx += 2`.
* Because `pos_idx` and `neg_idx` increment sequentially, the relative order of both positive and negative numbers is strictly preserved.
* **Time Complexity:** $\mathcal{O}(N)$
* **Space Complexity:** $\mathcal{O}(N)$ for output array, $\mathcal{O}(1)$ auxiliary space.

**File:** `03_rearrange_array_by_sign.py`

---

## 4. Two Sum

Given an array of integers `nums` and an integer `target`, return the 0-based indices of two elements in `nums` such that they add up to `target`. Each input will have exactly one solution, and the same element cannot be used twice. Return the answer in any order.

### Example

```text
Input:  nums = [1, 6, 2, 10, 3], target = 7
Output: [0, 1]  # nums[0] + nums[1] = 1 + 6 = 7

Input:  nums = [1, 3, 5, -7, 6, -3], target = 0
Output: [1, 5]  # nums[1] + nums[5] = 3 + (-3) = 0

Input:  nums = [3, 3], target = 6  # Edge Case: Identical duplicate elements forming target sum
Output: [0, 1]
```

### Think About

* **Part A: If the Array is Sorted (Low-High Two-Pointer Approach):**
  * Initialize two pointers: `low = 0` and `high = n - 1`.
  * While `low < high`:
    * If `nums[low] + nums[high] == target`: return `[low, high]`.
    * If `nums[low] + nums[high] < target`: sum is too small, advance `low += 1`.
    * If `nums[low] + nums[high] > target`: sum is too large, advance `high -= 1`.
  * **Time Complexity:** $\mathcal{O}(N)$
  * **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

* **Part B: If the Array is Unsorted (Frequency / Hash Map Concept):**
  * Maintain a dictionary / hash map `seen = {}` mapping `{value: index}`.
  * For each element `nums[i]` at index `i`:
    * Calculate `complement = target - nums[i]`.
    * If `complement` exists in `seen`: return `[seen[complement], i]`.
    * Otherwise, record current element: `seen[nums[i]] = i`.
  * **Time Complexity:** $\mathcal{O}(N)$
  * **Space Complexity:** $\mathcal{O}(N)$ auxiliary space for the hash map.

**File:** `04_two_sum.py`
