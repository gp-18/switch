# 🟢 Day 3.1 — Arrays: 3 Sum Practice & Confidence Boosters

## 1. Check if Triplet with Zero Sum Exists

Given an integer array `nums`, determine whether there exists any triplet `(nums[i], nums[j], nums[k])` with $i \ne j \ne k$ such that their sum equals `0`. Return `True` if such a triplet exists, otherwise return `False`.

### Example

```text
Input:  nums = [0, -1, 2, -3, 1]
Output: True

Input:  nums = [1, 2, 3]
Output: False

Input:  nums = [1, -1]  # Edge Case: Array length less than 3
Output: False
```

### Think About

* Sort `nums` in ascending order to enable the two-pointer approach.
* Iterate `i` from `0` to `n - 3`:
  * Set `low = i + 1` and `high = n - 1`.
  * While `low < high`:
    * `current_sum = nums[i] + nums[low] + nums[high]`
    * If `current_sum == 0`: return `True` immediately.
    * Else if `current_sum < 0`: advance `low += 1` to get a larger sum.
    * Else: decrement `high -= 1` to get a smaller sum.
* If the loops finish without finding any valid triplet, return `False`.
* **Time Complexity:** $\mathcal{O}(N^2)$ — $\mathcal{O}(N \log N)$ sorting + $\mathcal{O}(N^2)$ two-pointer traversal.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-4/day_3_1/01.py)

---

## 2. Triplet Sum Equal to Target

Given an integer array `nums` and an integer `target`, find any one triplet `[nums[i], nums[j], nums[k]]` such that $i \ne j \ne k$ and their sum equals `target`. Return the triplet in a list. If no such triplet exists, return an empty list `[]`.

### Example

```text
Input:  nums = [12, 3, 4, 1, 6, 9], target = 24
Output: [3, 9, 12]

Input:  nums = [1, 2, 3, 4, 5], target = 50
Output: []

Input:  nums = [-5, 2, 3], target = 0  # Edge Case: Exact size 3 array
Output: [-5, 2, 3]
```

### Think About

* Sort `nums` in ascending order.
* Iterate `i` from `0` to `n - 3`:
  * Set `low = i + 1` and `high = n - 1`.
  * While `low < high`:
    * `total = nums[i] + nums[low] + nums[high]`
    * If `total == target`: return `[nums[i], nums[low], nums[high]]` immediately.
    * Else if `total < target`: advance `low += 1`.
    * Else: decrement `high -= 1`.
* Return `[]` if no valid triplet matches `target`.
* **Time Complexity:** $\mathcal{O}(N^2)$
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [02.py](../../code/sprint-4/day_3_1/02.py)

---

## 3. Count Triplets with Given Sum

Given an array of distinct integers `nums` and an integer `target`, count the total number of unique triplets `(i, j, k)` with $i < j < k$ such that `nums[i] + nums[j] + nums[k] == target`.

### Example

```text
Input:  nums = [1, 2, 3, 4, 5], target = 9
Output: 2

Input:  nums = [0, -1, 2, -3, 1], target = -2
Output: 2

Input:  nums = [1, 2, 3], target = 10  # Edge Case: No triplet reaches target
Output: 0
```

### Think About

* Sort `nums` in ascending order and initialize `count = 0`.
* Iterate `i` from `0` to `n - 3`:
  * Set `low = i + 1` and `high = n - 1`.
  * While `low < high`:
    * `current_sum = nums[i] + nums[low] + nums[high]`
    * If `current_sum == target`: increment `count += 1`, move both `low += 1` and `high -= 1`.
    * Else if `current_sum < target`: advance `low += 1`.
    * Else: decrement `high -= 1`.
* Return `count`.
* **Time Complexity:** $\mathcal{O}(N^2)$
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [03.py](../../code/sprint-4/day_3_1/03.py)

---

## 4. Count Triplets with Sum Less Than Target (3 Sum Smaller)

Given an integer array `nums` of length $n$ and an integer `target`, return the number of triplets `(i, j, k)` with $0 \le i < j < k < n$ such that `nums[i] + nums[j] + nums[k] < target`.

### Example

```text
Input:  nums = [-2, 0, 1, 3], target = 2
Output: 2

Input:  nums = [5, 1, 3, 4, 7], target = 12
Output: 4

Input:  nums = [1, 2, 3], target = 5  # Edge Case: Smallest sum is 6 (>= 5)
Output: 0
```

### Think About

* Sort `nums` in ascending order and initialize `count = 0`.
* Iterate `i` from `0` to `n - 3`:
  * Set `low = i + 1` and `high = n - 1`.
  * While `low < high`:
    * If `nums[i] + nums[low] + nums[high] < target`:
      * Since the array is sorted, pairing `nums[i]` and `nums[low]` with any element between `low + 1` and `high` also produces a sum strictly less than `target`.
      * Add all `(high - low)` pairs directly: `count += (high - low)`.
      * Advance `low += 1`.
    * Else:
      * Sum is too large or equal, decrement `high -= 1`.
* **Time Complexity:** $\mathcal{O}(N^2)$
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [04.py](../../code/sprint-4/day_3_1/04.py)

---

## 5. 3 Sum Closest

Given an integer array `nums` of length $n$ and an integer `target`, find three integers in `nums` such that their sum is closest to `target`. Return the sum of the three integers. Assume exactly one solution exists.

### Example

```text
Input:  nums = [-1, 2, 1, -4], target = 1
Output: 2

Input:  nums = [0, 0, 0], target = 1
Output: 0

Input:  nums = [1, 1, 1], target = -100  # Edge Case: Sum far from negative target
Output: 3
```

### Think About

* Sort `nums` in ascending order.
* Initialize `closest_sum = nums[0] + nums[1] + nums[2]`.
* Iterate `i` from `0` to `n - 3`:
  * Set `low = i + 1` and `high = n - 1`.
  * While `low < high`:
    * `current_sum = nums[i] + nums[low] + nums[high]`
    * If `abs(current_sum - target) < abs(closest_sum - target)`:
      * Update `closest_sum = current_sum`.
    * If `current_sum == target`: return `target` immediately.
    * Else if `current_sum < target`: advance `low += 1`.
    * Else: decrement `high -= 1`.
* Return `closest_sum`.
* **Time Complexity:** $\mathcal{O}(N^2)$
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [05.py](../../code/sprint-4/day_3_1/05.py)
