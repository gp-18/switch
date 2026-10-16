# 🟢 Day 1 — Arrays: Core Fundamentals & Traversal

## 1. Linear Search

Given an array of integers `nums` and an integer target `k`, find the index of `k` in `nums`. If `k` is present, return its 0-based index; otherwise, return `-1`.

### Example

```text
Input:  nums = [1, 2, 3, 4, 5], k = 3
Output: 2

Input:  nums = [5, 4, 3, 2, 1], k = 6
Output: -1
```

### Think About

* Scan sequentially from index `0` to `n - 1`.
* Early return as soon as `nums[i] == k` is matched.
* **Time Complexity:** $\mathcal{O}(N)$ worst/average case, $\mathcal{O}(1)$ best case.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01_linear_search.py](../../code/sprint-4/day_1/01_linear_search.py)

---

## 2. Largest Element

Given an array `nums` of $N$ integers, find and return the largest element in the array.

### Example

```text
Input:  nums = [2, 5, 1, 3, 0]
Output: 5

Input:  nums = [8, 10, 5, 7, 9]
Output: 10
```

### Think About

* Initialize `max_val = nums[0]`.
* Iterate through `nums` from index `1` to `N - 1`: if `nums[i] > max_val`, update `max_val = nums[i]`.
* Avoid sorting the array ($\mathcal{O}(N \log N)$); a single pass runs in $\mathcal{O}(N)$ time.
* **Time Complexity:** $\mathcal{O}(N)$
* **Space Complexity:** $\mathcal{O}(1)$

**File:** [02_largest_element.py](../../code/sprint-4/day_1/02_largest_element.py)

---

## 3. Second Largest Element

Given an array `nums` of $N$ integers, find and return the second largest distinct element without sorting. If no second largest distinct element exists, return `-1`.

### Example

```text
Input:  nums = [1, 2, 4, 7, 7, 5]
Output: 5

Input:  nums = [10, 10, 10]
Output: -1
```

### Think About

* Single pass approach with two variables: `largest = -float('inf')` and `second_largest = -float('inf')`.
* For each `num` in `nums`:
  * If `num > largest`: update `second_largest = largest`, then `largest = num`.
  * Else if `num < largest` and `num > second_largest`: update `second_largest = num`.
* Check if `second_largest` was updated; if not, return `-1`.
* **Time Complexity:** $\mathcal{O}(N)$
* **Space Complexity:** $\mathcal{O}(1)$

**File:** [03_second_largest.py](../../code/sprint-4/day_1/03_second_largest.py)

---

## 4. Maximum Consecutive Ones

Given a binary array `nums` containing only `0`s and `1`s, return the maximum number of consecutive `1`s present in the array.

### Example

```text
Input:  nums = [1, 1, 0, 1, 1, 1]
Output: 3

Input:  nums = [1, 0, 1, 1, 0, 1]
Output: 2
```

### Think About

* Maintain a current streak count `cnt = 0` and a maximum count `max_cnt = 0`.
* Iterate through the array:
  * If `num == 1`: increment `cnt += 1` and update `max_cnt = max(max_cnt, cnt)`.
  * If `num == 0`: reset `cnt = 0`.
* **Time Complexity:** $\mathcal{O}(N)$
* **Space Complexity:** $\mathcal{O}(1)$

**File:** [04_max_consecutive_ones.py](../../code/sprint-4/day_1/04_max_consecutive_ones.py)

---

## 5. Left Rotate Array by One

Given an array `nums` of $N$ integers, rotate the array to the left by one position in-place.

### Example

```text
Input:  nums = [1, 2, 3, 4, 5]
Output: [2, 3, 4, 5, 1]

Input:  nums = [3]
Output: [3]
```

### Think About

* Store the first element `temp = nums[0]`.
* Shift elements from index `1` to `N - 1` one place to the left: `nums[i - 1] = nums[i]`.
* Place `temp` at the last index: `nums[N - 1] = temp`.
* **Time Complexity:** $\mathcal{O}(N)$
* **Space Complexity:** $\mathcal{O}(1)$ extra space.

**File:** [05_left_rotate_by_one.py](../../code/sprint-4/day_1/05_left_rotate_by_one.py)

---

## 6. Left Rotate Array by K Places

Given an array `nums` of $N$ integers and an integer `k`, rotate the array to the left by `k` places.

### Example

```text
Input:  nums = [1, 2, 3, 4, 5, 6, 7], k = 2
Output: [3, 4, 5, 6, 7, 1, 2]

Input:  nums = [3, 7, 8, 9], k = 3
Output: [9, 3, 7, 8]
```

### Think About

* Normalize `k = k % N` since rotating by $N$ returns to the original array.
* **Optimal Reversal Algorithm ($\mathcal{O}(1)$ extra space):**
  1. Reverse the first `k` elements: `reverse(0, k - 1)`
  2. Reverse the remaining `N - k` elements: `reverse(k, N - 1)`
  3. Reverse the all array: `reverse(0, N - 1)`
* **Time Complexity:** $\mathcal{O}(N)$
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [06_left_rotate_by_k.py](../../code/sprint-4/day_1/06_left_rotate_by_k.py)

---

## 7. Move Zeros to End

Given an integer array `nums`, move all `0`s to the end of the array while maintaining the relative order of non-zero elements in-place.

### Example

```text
Input:  nums = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]

Input:  nums = [0, 0, 1]
Output: [1, 0, 0]
```

### Think About

* Find the index `j` of the first zero in the array. If no zero exists, return.
* Loop pointer `i` from `j + 1` to `N - 1`:
  * Whenever `nums[i] != 0`: swap `nums[i]` with `nums[j]`, then increment `j += 1`.
* All non-zeros stay in relative order, and zeros naturally slide to the back.
* **Time Complexity:** $\mathcal{O}(N)$
* **Space Complexity:** $\mathcal{O}(1)$ in-place.

**File:** [07_move_zeros_to_end.py](../../code/sprint-4/day_1/07_move_zeros_to_end.py)

---

## 8. Remove Duplicates from Sorted Array

Given an integer array `nums` sorted in non-decreasing order, remove duplicates in-place such that each unique element appears only once. Return the number of unique elements `k`.

### Example

```text
Input:  nums = [1, 1, 2]
Output: k = 2, nums = [1, 2, _]

Input:  nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Output: k = 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
```

### Think About

* Use two pointers: `i = 0` tracks the index of the last placed unique element.
* Pointer `j` iterates from `1` to `N - 1`:
  * If `nums[j] != nums[i]`: increment `i += 1` and set `nums[i] = nums[j]`.
* The number of unique elements is `i + 1`.
* **Time Complexity:** $\mathcal{O}(N)$
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [08_remove_duplicates.py](../../code/sprint-4/day_1/08_remove_duplicates.py)

---

## 9. Find Missing Number

Given an array `nums` containing $N$ distinct numbers taken from the range $[0, N]$ (or $[1, N]$), find the single number missing from the range.

### Example

```text
Input:  nums = [3, 0, 1]
Output: 2  # Range [0, 3], missing number is 2

Input:  nums = [1, 2, 4, 5], N = 5
Output: 3  # Range [1, 5], missing number is 3
```

### Think About

* **Approach 1 (Sum formula):**
  * Expected sum = $\frac{N(N + 1)}{2}$.
  * $\text{Missing} = \text{Expected Sum} - \sum \text{nums}$.
* **Approach 2 (XOR property):**
  * $\text{XOR}$ all numbers in the full range and $\text{XOR}$ all numbers present in `nums`.
  * Duplicates cancel out ($a \oplus a = 0$), leaving only the missing number.
* **Time Complexity:** $\mathcal{O}(N)$
* **Space Complexity:** $\mathcal{O}(1)$

**File:** [09_missing_number.py](../../code/sprint-4/day_1/09_missing_number.py)

---

## 10. Union of Two Sorted Arrays

Given two sorted arrays `a` and `b`, return a sorted list containing the union of elements from both arrays (all unique elements present in either array).

### Example

```text
Input:  a = [1, 2, 3, 4, 5], b = [2, 3, 4, 4, 5, 6]
Output: [1, 2, 3, 4, 5, 6]

Input:  a = [2, 2, 3, 4, 5], b = [1, 1, 2, 3, 4]
Output: [1, 2, 3, 4, 5]
```

### Think About

* Two-pointer traversal: `i = 0` for `a` and `j = 0` for `b`.
* Compare `a[i]` and `b[j]`:
  * If `a[i] <= b[j]`: consider `a[i]` for insertion; increment `i += 1`.
  * Else: consider `b[j]` for insertion; increment `j += 1`.
* Only append an element if the union list is empty or `union[-1] != element` (prevents duplicates).
* Exhaust remaining elements in `a` or `b` with the same duplicate check.
* **Time Complexity:** $\mathcal{O}(N + M)$
* **Space Complexity:** $\mathcal{O}(N + M)$ for the output array.

**File:** [10_union_sorted_arrays.py](../../code/sprint-4/day_1/10_union_sorted_arrays.py)

---

## 11. Intersection of Two Sorted Arrays

Given two sorted arrays `a` and `b`, find and return the intersection of the two arrays (elements common to both arrays).

### Example

```text
Input:  a = [1, 2, 2, 3, 3, 4, 5, 6], b = [2, 3, 3, 5, 6, 6, 7]
Output: [2, 3, 3, 5, 6]

Input:  a = [1, 2, 3], b = [4, 5, 6]
Output: []
```

### Think About

* Two pointers `i = 0` and `j = 0`:
  * If `a[i] < b[j]`: increment `i += 1`.
  * If `b[j] < a[i]`: increment `j += 1`.
  * If `a[i] == b[j]`: common element found! Append `a[i]` to `intersection`, then increment both `i += 1` and `j += 1`.
* Stop when either pointer reaches the end of its array.
* **Time Complexity:** $\mathcal{O}(N + M)$
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space (excluding output array).

**File:** [11_intersection_sorted_arrays.py](../../code/sprint-4/day_1/11_intersection_sorted_arrays.py)
