# 🟢 Day 7.8 — Binary Search: Find Rotation Count of Rotated Sorted Array

## 1. Find Out How Many Times the Array is Rotated

Given an integer array `nums` of size $n$, sorted in ascending order with distinct values. The array has been right-rotated an unknown number of times, between $0$ and $n - 1$ (inclusive).

Determine the number of rotations performed on the array.

### Example

```text
Input:  nums = [4, 5, 6, 7, 0, 1, 2, 3]
Output: 4
Explanation:
Original array: [0, 1, 2, 3, 4, 5, 6, 7].
Right rotated 4 times brings [4, 5, 6, 7] to the front.
The minimum element 0 is at index 4, so rotation count = 4.

Input:  nums = [3, 4, 5, 1, 2]
Output: 3
Explanation:
Original array: [1, 2, 3, 4, 5].
The minimum element 1 is at index 3, so rotation count = 3.

Input:  nums = [4, 5, 1, 2]
Output: 2
Explanation:
The minimum element 1 is at index 2, so rotation count = 2.

Input:  nums = [1, 2, 3, 4, 5]  # Edge Case: 0 rotations (already sorted)
Output: 0
Explanation:
The minimum element 1 is at index 0, so rotation count = 0.
```

### Think About

* **The Core Mathematical Equivalence:**
  * In a right-rotated sorted array, the elements starting from the original 0-th element (the global minimum) have been shifted to some index $K$.
  * All $K$ elements that originally resided at the end of the array have been wrapped around to indices `0` through `K - 1`.
  * Therefore:
    $$\text{Number of Right Rotations} = \text{Index of the Minimum Element}$$

* **Binary Search for Minimum Element Index:**
  1. Initialize `low = 0`, `high = n - 1`, `ans = infinity`, `min_index = -1`.
  2. While `low <= high`:
     * If `nums[low] <= nums[high]`:
       * The range `[low..high]` is already sorted.
       * If `nums[low] < ans`: `ans = nums[low]`, `min_index = low`.
       * `break`.
     * Calculate `mid = low + (high - low) // 2`.
     * **Case 1: Left half is sorted (`nums[low] <= nums[mid]`):**
       * If `nums[low] < ans`: `ans = nums[low]`, `min_index = low`.
       * Search the unsorted right half: `low = mid + 1`.
     * **Case 2: Right half is sorted (`nums[mid] < nums[low]`):**
       * If `nums[mid] < ans`: `ans = nums[mid]`, `min_index = mid`.
       * Search the unsorted left half: `high = mid - 1`.
  3. Return `min_index`.

* **Time Complexity:** $\mathcal{O}(\log N)$ — Logarithmic binary search.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-5/day_7_8/01.py)
