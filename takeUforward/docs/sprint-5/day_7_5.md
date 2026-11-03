# 🟢 Day 7.5 — Binary Search: Search in Rotated Sorted Array-I (Distinct Elements)

## 1. Search in Rotated Sorted Array-I

Given an integer array `nums` sorted in ascending order with **distinct** values, and an integer `k` (target). The array has been rotated at an unknown pivot point.

Find the index at which `k` is present. If `k` is not present, return `-1`.

You must write an algorithm with $\mathcal{O}(\log N)$ runtime complexity.

### Example

```text
Input:  nums = [4, 5, 6, 7, 0, 1, 2], k = 0
Output: 4
Explanation: 0 is present at index 4.

Input:  nums = [4, 5, 6, 7, 0, 1, 2], k = 3
Output: -1
Explanation: 3 is not present in nums.

Input:  nums = [4, 5, 6, 7, 0, 1, 2], k = 5
Output: 1
Explanation: 5 is present at index 1.

Input:  nums = [1], k = 0  # Edge Case: Single element missing
Output: -1

Input:  nums = [1], k = 1  # Edge Case: Single element found
Output: 0
```

### Think About

* **The Core Invariant of Rotated Sorted Arrays:**
  * Even though the array is rotated, **at least one half (left or right) is ALWAYS strictly sorted** at every step!
  * If the pivot is in the right half, the left half is sorted (`nums[low] <= nums[mid]`).
  * If the pivot is in the left half, the right half is sorted (`nums[mid] <= nums[high]`).

* **Step-by-Step Decision Logic:**
  1. `low = 0`, `high = len(nums) - 1`.
  2. While `low <= high`:
     * Calculate `mid = low + (high - low) // 2`.
     * If `nums[mid] == k`: return `mid`.
     * **Case 1: Left half is sorted (`nums[low] <= nums[mid]`):**
       * Check if target `k` falls within the sorted left boundaries:
         $$nums[low] \le k \le nums[mid]$$
       * If yes: eliminate the right half $\rightarrow$ `high = mid - 1`.
       * If no: eliminate the left half $\rightarrow$ `low = mid + 1`.
     * **Case 2: Right half is sorted (`nums[mid] <= nums[high]`):**
       * Check if target `k` falls within the sorted right boundaries:
         $$nums[mid] \le k \le nums[high]$$
       * If yes: eliminate the left half $\rightarrow$ `low = mid + 1`.
       * If no: eliminate the right half $\rightarrow$ `high = mid - 1`.
  3. If loop ends without finding `k`, return `-1`.

* **Time Complexity:** $\mathcal{O}(\log N)$ — Search space is halved in each step.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-5/day_7_5/01.py)
