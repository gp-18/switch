# 🟢 Day 7.2 — Binary Search: Search Insert Position

## 1. Search Insert Position

Given a sorted array of distinct integers `nums` and a target value `target`:

* Return the index if the `target` is found.
* If not, return the index where it would be if it were inserted in order.

You must write an algorithm with $\mathcal{O}(\log N)$ runtime complexity.

### Example

```text
Input:  nums = [1, 3, 5, 6], target = 5
Output: 2
Explanation: The target value 5 is found at index 2.

Input:  nums = [1, 3, 5, 6], target = 2
Output: 1
Explanation: 2 is not found, but inserting it at index 1 maintains sorted order: [1, 2, 3, 5, 6].

Input:  nums = [1, 3, 5, 6], target = 7
Output: 4
Explanation: 7 is greater than all elements; insert at index 4 (the end of the array).

Input:  nums = [1, 3, 5, 6], target = 0  # Edge Case: smaller than all elements
Output: 0
Explanation: 0 is smaller than all elements; insert at index 0.
```

### Think About

* **The Core Insight: Search Insert Position IS Lower Bound!**
  * When searching for where `target` belongs:
    1. If `target` is already in `nums`, we want its exact index.
    2. If `target` is NOT in `nums`, we want the index of the first element that is **greater than** `target`. Inserting `target` at that index pushes that larger element (and all subsequent elements) to the right.
  * In both cases, we are looking for the smallest index `i` such that:
    $$nums[i] \ge target$$
  * This is the exact definition of **Lower Bound**!

* **Binary Search Algorithm:**
  1. Initialize `low = 0`, `high = n - 1`.
  2. Initialize `ans = n`.
  3. While `low <= high`:
     * Calculate `mid = low + (high - low) // 2`.
     * If `nums[mid] >= target`:
       * `ans = mid` (potential insertion index).
       * Try searching left for a smaller index: `high = mid - 1`.
     * Else (`nums[mid] < target`):
       * Search right: `low = mid + 1`.
  4. Return `ans` (or simply `low`, because upon loop termination `low` is always equal to the insertion index!).

* **Time Complexity:** $\mathcal{O}(\log N)$ — Classical binary search halving the search space each step.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-5/day_7_2/01.py)
