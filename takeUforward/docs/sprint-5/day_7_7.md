# 🟢 Day 7.7 — Binary Search: Find Minimum in Rotated Sorted Array

## 1. Find Minimum in Rotated Sorted Array

Given an integer array `nums` of size $n$, sorted in ascending order with **distinct** values, and rotated an unknown number of times (between 1 and $n$), find the minimum element in the array.

You must write an algorithm with $\mathcal{O}(\log N)$ runtime complexity.

### Example

```text
Input:  nums = [4, 5, 6, 7, 0, 1, 2, 3]
Output: 0
Explanation: 0 is the minimum element in the array.

Input:  nums = [3, 4, 5, 1, 2]
Output: 1
Explanation: 1 is the minimum element in the array.

Input:  nums = [4, 5, 6, 7, -7, 1, 2, 3]
Output: -7
Explanation: -7 is the minimum element in the array.

Input:  nums = [11, 13, 15, 17]  # Edge Case: Rotated n times (already fully sorted)
Output: 11
Explanation: The first element 11 is the minimum.
```

### Think About

* **The Core Observation (Minimum in a Sorted Half):**
  * In any sorted subarray, the minimum element is located at the **very first index** of that sorted subarray.
  * In a rotated sorted array, the rotation pivot separates the array into two sorted pieces. The overall minimum is located right at the inflection point (the start of the second piece).

* **Algorithm & Search Space Reduction:**
  1. Initialize `low = 0`, `high = n - 1`, and `ans = infinity`.
  2. While `low <= high`:
     * **Optimization (Already Sorted Subarray):**
       * If `nums[low] <= nums[high]`:
         * The current search space `nums[low..high]` is already completely sorted!
         * `ans = min(ans, nums[low])`
         * `break` (no need to search further!).
     * Calculate `mid = low + (high - low) // 2`.
     * **Case 1: Left half is sorted (`nums[low] <= nums[mid]`):**
       * Smallest element in the left half is `nums[low]`.
       * Update `ans = min(ans, nums[low])`.
       * Eliminate left half and search the unsorted right half: `low = mid + 1`.
     * **Case 2: Right half is sorted (`nums[mid] < nums[low]`):**
       * Smallest element in the right half is `nums[mid]`.
       * Update `ans = min(ans, nums[mid])`.
       * Eliminate right half and search the unsorted left half: `high = mid - 1`.
  3. Return `ans`.

* **Time Complexity:** $\mathcal{O}(\log N)$ — Search space is halved each step.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-5/day_7_7/01.py)
