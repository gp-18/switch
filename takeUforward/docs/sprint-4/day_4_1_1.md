# 🟢 Day 4.1 — Arrays: 4 Sum Practice & PBC Interview Questions

## 1. Check if Quadruplet with Target Sum Exists

Given an integer array `nums` and an integer `target`, determine whether there exists any quadruplet `(nums[a], nums[b], nums[c], nums[d])` with distinct indices $a < b < c < d$ such that their sum equals `target`. Return `True` if such a quadruplet exists, otherwise return `False`.

### Example

```text
Input:  nums = [1, 0, -1, 0, -2, 2], target = 0
Output: True  # Quadruplet (-2, -1, 1, 2) sums to 0

Input:  nums = [1, 2, 3, 4], target = 50
Output: False # Max sum is 1 + 2 + 3 + 4 = 10 != 50

Input:  nums = [1, 2, 3], target = 6  # Edge Case: Array length < 4
Output: False
```

### Think About

* Sort `nums` in ascending order to enable directional pointer movements.
* First loop `i` from `0` to `n - 4` (pin first number).
* Second loop `j` from `i + 1` to `n - 3` (pin second number).
* Use two moving pointers: `k = j + 1` and `l = n - 1`.
* While `k < l`:
  * `current_sum = nums[i] + nums[j] + nums[k] + nums[l]`
  * If `current_sum == target`: return `True` immediately.
  * Else if `current_sum < target`: advance `k += 1` to get a larger sum.
  * Else: decrement `l -= 1` to get a smaller sum.
* If all loops complete without finding any match, return `False`.
* **Time Complexity:** $\mathcal{O}(N^3)$ — $\mathcal{O}(N \log N)$ sorting + two outer loops with a linear two-pointer search.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-4/day_4_1/01.py)

---

## 2. Find Any One Quadruplet Equal to Target

Given an integer array `nums` and an integer `target`, find and return any one quadruplet `[nums[a], nums[b], nums[c], nums[d]]` with distinct indices such that their sum equals `target`. If no such quadruplet exists, return an empty list `[]`.

### Example

```text
Input:  nums = [2, 7, 4, 0, 9, 5, 1, 3], target = 20
Output: [2, 4, 5, 9]  # 2 + 4 + 5 + 9 = 20

Input:  nums = [1, 2, 3, 4, 5], target = 100
Output: []

Input:  nums = [5, 5, 5, 5], target = 20  # Edge Case: Exact size 4 array
Output: [5, 5, 5, 5]
```

### Think About

* Sort `nums` in ascending order.
* Loop `i` from `0` to `n - 4`:
  * Loop `j` from `i + 1` to `n - 3`:
    * Set `k = j + 1` and `l = n - 1`.
    * While `k < l`:
      * `total = nums[i] + nums[j] + nums[k] + nums[l]`
      * If `total == target`: return `[nums[i], nums[j], nums[k], nums[l]]` immediately.
      * Else if `total < target`: advance `k += 1`.
      * Else: decrement `l -= 1`.
* Return `[]` if no quadruplet reaches `target`.
* **Time Complexity:** $\mathcal{O}(N^3)$
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [02.py](../../code/sprint-4/day_4_1/02.py)

---

## 3. Count Quadruplets with Sum Less Than Target (4 Sum Smaller)

Given an integer array `nums` of length $n$ and an integer `target`, return the total number of unique index quadruplets `(a, b, c, d)` with $0 \le a < b < c < d < n$ such that `nums[a] + nums[b] + nums[c] + nums[d] < target`.

### Example

```text
Input:  nums = [1, 2, 3, 4, 5], target = 12
Output: 2  # Quadruplets: (1, 2, 3, 4) sum=10, (1, 2, 3, 5) sum=11

Input:  nums = [-2, 0, 1, 3, 5], target = 5
Output: 4

Input:  nums = [2, 3, 4, 5], target = 14  # Edge Case: Min sum is 14 (not < 14)
Output: 0
```

### Think About

* Sort `nums` in ascending order and initialize `count = 0`.
* Outer loop `i` from `0` to `n - 4`.
* Inner loop `j` from `i + 1` to `n - 3`.
* Set moving pointers `k = j + 1` and `l = n - 1`.
* While `k < l`:
  * If `nums[i] + nums[j] + nums[k] + nums[l] < target`:
    * **Key Interval Shortcut:** Because the array is sorted, pairing `nums[i]`, `nums[j]`, and `nums[k]` with **any** number between index `k + 1` and `l` will also produce a sum strictly less than `target`!
    * Add all `(l - k)` valid quadruplets at once: `count += (l - k)`.
    * Advance `k += 1` to test a larger third element.
  * Else:
    * Sum is too large or equal, decrement `l -= 1`.
* **Time Complexity:** $\mathcal{O}(N^3)$
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [03.py](../../code/sprint-4/day_4_1/03.py)

---

## 4. 4 Sum Closest to Target (Amazon, Microsoft, Bloomberg)

Given an integer array `nums` of length $n$ and an integer `target`, find four integers in `nums` such that their sum is closest to `target`. Return the sum of the four integers. Assume exactly one closest sum exists.

### Example

```text
Input:  nums = [1, 0, -1, 0, -2, 2], target = 1
Output: 1  # Quadruplet (-2, 0, 1, 2) has sum = 1, exact match distance 0

Input:  nums = [-1, 2, 1, -4, 5, -3], target = 5
Output: 4  # Quadruplet (-3, 1, 2, 4) or (-1, -3, 5, 2) sum = 3/4, closest is 4

Input:  nums = [1, 1, 1, 1], target = -100  # Edge Case: Small array far from negative target
Output: 4
```

### Think About

* Frequently asked in PBC interviews (Amazon, Microsoft) as an extension of 3 Sum Closest.
* Sort `nums` in ascending order.
* Initialize `closest_sum = nums[0] + nums[1] + nums[2] + nums[3]`.
* Loop `i` from `0` to `n - 4`:
  * Loop `j` from `i + 1` to `n - 3`:
    * Set `k = j + 1` and `l = n - 1`.
    * While `k < l`:
      * `current_sum = nums[i] + nums[j] + nums[k] + nums[l]`
      * If `abs(current_sum - target) < abs(closest_sum - target)`:
        * Update `closest_sum = current_sum`.
      * If `current_sum == target`: return `target` immediately (distance is 0).
      * Else if `current_sum < target`: advance `k += 1` to increase sum.
      * Else: decrement `l -= 1` to decrease sum.
* Return `closest_sum`.
* **Time Complexity:** $\mathcal{O}(N^3)$
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [04.py](../../code/sprint-4/day_4_1/04.py)

---

## 5. Generalized K-Sum: Two-Pointer Reduction (Google, Meta, Apple)

Implement the universal **K-Sum** algorithm to find all unique combinations of $k$ integers in `nums` that sum to `target`. In PBC interviews (Google, Meta, Apple), after you write 3-Sum or 4-Sum, interviewers ask: *"How do you generalize this to any $k$ without hardcoding $k$ nested loops?"*

### Example

```text
Input:  nums = [1, 0, -1, 0, -2, 2], target = 0, k = 4
Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

Input:  nums = [2, 2, 2, 2, 2], target = 8, k = 4
Output: [[2, 2, 2, 2]]

Input:  nums = [1, 2, 3], target = 6, k = 4  # Edge Case: n < k
Output: []
```

### Think About

* **The Core PBC Interview Generalization:**
  * Every $K$-Sum problem can be broken down recursively into $(K - 1)$-Sum until it reaches the base case: **2-Sum**.
  * Base case ($k == 2$): Use the classic Low-High Two Pointers on the remaining sorted array ($\mathcal{O}(N)$ time, $\mathcal{O}(1)$ space).
  * Recursive step ($k > 2$):
    * Iterate through candidate elements: `for i in range(start, n - k + 1)`.
    * Skip duplicates: `if i > start and nums[i] == nums[i - 1]: continue`.
    * Early pruning: If $nums[i] \times k > \text{target}$ or $nums[-1] \times k < \text{target}$, break or continue.
    * Recursively call $(k - 1)$-Sum with updated target: $\text{target} - nums[i]$.
    * Append $nums[i]$ to each returned sub-combination.
* When $k = 4$, this cleanly executes the exact 4-Sum logic in $\mathcal{O}(N^3)$ time without deep nested code!
* **Time Complexity:** $\mathcal{O}(N^{k - 1})$ — For $k = 4$, time is $\mathcal{O}(N^3)$.
* **Space Complexity:** $\mathcal{O}(k)$ recursion stack space.

**File:** [05.py](../../code/sprint-4/day_4_1/05.py)
