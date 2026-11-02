# 🟢 Day 7.4 — Binary Search: First and Last Occurrence in a Sorted Array

## 1. First and Last Occurrence

Given an array of integers `nums` sorted in non-decreasing order and an integer `target`, find the starting and ending position of `target`.

* If `target` is found in the array, return `[first_occurrence, last_occurrence]`.
* If `target` is not found, return `[-1, -1]`.

You must write an algorithm with $\mathcal{O}(\log N)$ runtime complexity.

### Example

```text
Input:  nums = [5, 7, 7, 8, 8, 10], target = 8
Output: [3, 4]
Explanation: The target 8 appears at indices 3 and 4.

Input:  nums = [5, 7, 7, 8, 8, 10], target = 6
Output: [-1, -1]
Explanation: The target 6 is not present in nums.

Input:  nums = [5, 7, 7, 8, 8, 10], target = 5
Output: [0, 0]
Explanation: 5 occurs only once at index 0.

Input:  nums = [], target = 0  # Edge Case: Empty array
Output: [-1, -1]

Input:  nums = [2, 2, 2, 2], target = 2  # Edge Case: All elements match
Output: [0, 3]
```

### Think About

* **Why Standard Binary Search Isn't Enough:**
  * When `nums[mid] == target`, standard binary search halts and returns `mid`.
  * But with duplicate numbers, `mid` could be in the middle of a run of identical elements!
  * To find the **first** occurrence, we must continue searching the left half (`high = mid - 1`).
  * To find the **last** occurrence, we must continue searching the right half (`low = mid + 1`).

* **Two Binary Searches Implementation:**
  1. **`firstOccurrence(nums, target)`:**
     * `low = 0, high = n - 1, first = -1`
     * While `low <= high`:
       * `mid = low + (high - low) // 2`
       * If `nums[mid] == target`:
         * `first = mid`
         * Search further left: `high = mid - 1`
       * Else if `nums[mid] < target`:
         * `low = mid + 1`
       * Else:
         * `high = mid - 1`
     * Return `first`.
  2. **Early Exit Optimization:**
     * If `first == -1`, `target` is completely absent! Immediately return `[-1, -1]` without running the second binary search.
  3. **`lastOccurrence(nums, target)`:**
     * `low = 0, high = n - 1, last = -1`
     * While `low <= high`:
       * `mid = low + (high - low) // 2`
       * If `nums[mid] == target`:
         * `last = mid`
         * Search further right: `low = mid + 1`
       * Else if `nums[mid] < target`:
         * `low = mid + 1`
       * Else:
         * `high = mid - 1`
     * Return `last`.

* **Alternative Technique: Using Lower Bound & Upper Bound:**
  * `first = lower_bound(nums, target)`
  * `last = upper_bound(nums, target) - 1`
  * If `first == n` or `nums[first] != target`: return `[-1, -1]`.
  * Otherwise, return `[first, last]`.

* **Interview Follow-Up (Count Occurrences):**
  * Number of times `target` appears in sorted array = `last - first + 1` (if found), else `0`.

* **Time Complexity:** $2 \times \mathcal{O}(\log N) \approx \mathcal{O}(\log N)$
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-5/day_7_4/01.py)
