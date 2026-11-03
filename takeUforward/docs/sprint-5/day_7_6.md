# 🟢 Day 7.6 — Binary Search: Search in Rotated Sorted Array-II (With Duplicates)

## 1. Search in Rotated Sorted Array-II

Given an integer array `nums` sorted in ascending order that **may contain duplicate values**, and a target value `k`. The array has been rotated at an unknown pivot point.

Return `True` if `k` is present in `nums`, and `False` otherwise.

### Example

```text
Input:  nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 3
Output: True
Explanation: 3 is present in the array.

Input:  nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 10
Output: False
Explanation: 10 is not present in the array.

Input:  nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 7
Output: True
Explanation: 7 is present at index 0.

Input:  nums = [3, 1, 2, 3, 3, 3, 3], k = 2  # Edge Case: duplicates at boundaries and mid
Output: True

Input:  nums = [1, 0, 1, 1, 1], k = 0
Output: True
```

### Think About

* **Why Duplicates Break Standard Binary Search:**
  * In Rotated Array-I (distinct elements), `nums[low] <= nums[mid]` decisively indicated that the left half was sorted.
  * With duplicates, consider:
    * `nums = [3, 1, 2, 3, 3, 3, 3]` $\rightarrow low=0, mid=3, high=6 \implies nums[low] = nums[mid] = nums[high] = 3$.
    * Here, `nums[low] <= nums[mid]` is True, but the left half `[3, 1, 2, 3]` is **NOT** sorted!
    * Similarly, in `[3, 3, 3, 3, 1, 2, 3]`, $nums[low] = nums[mid] = nums[high] = 3$, but now the right half contains the rotation pivot!
  * **Conclusion:** When $nums[low] == nums[mid] == nums[high]$, we cannot identify which half is sorted.

* **The Fix: Shrink the Search Space (Trimming Duplicates):**
  * When `nums[low] == nums[mid] == nums[high]`:
    * If `nums[mid] == k`, we already found the answer (`True`).
    * Otherwise, neither `nums[low]` nor `nums[high]` can be the target without `nums[mid]` being the target.
    * Safely shrink the search space:
      `low += 1`
      `high -= 1`
      `continue`
  * Once the boundary values differ, at least one half is unambiguously sorted, and we proceed with standard rotated search.

* **Time Complexity Analysis:**
  * **Best and Average Case:** $\mathcal{O}(\log N)$ — When duplicates are few or values at boundaries differ.
  * **Worst Case:** $\mathcal{O}(N / 2) \approx \mathcal{O}(N)$ — When nearly all elements are identical (e.g. `[3, 3, 3, 3, 3, 3, 1]`), we must linearly increment `low` and decrement `high`.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-5/day_7_6/01.py)
