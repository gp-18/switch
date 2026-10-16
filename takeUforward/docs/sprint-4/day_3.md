# 🟢 Day 3 — Arrays: 3 Sum & Triplet Problems

## 1. 3 Sum

Given an integer array `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` such that $i \ne j$, $i \ne k$, and $j \ne k$, and `nums[i] + nums[j] + nums[k] == 0`. The solution set must not contain duplicate triplets.

### Example

```text
Input:  nums = [2, -2, 0, 3, -3, 5]
Output: [[-3, -2, 5], [-3, 0, 3], [-2, 0, 2]]

Input:  nums = [2, -1, -1, 3, -1]
Output: [[-1, -1, 2]]

Input:  nums = [8, -6, 5, 4]  # Edge Case: No triplets sum to 0
Output: []
```

### Think About

* **Optimal Approach (Sort + Two Pointers):**
  * Sort `nums` in ascending order so that identical values are grouped together and two pointers can be used.
  * Iterate `i` from `0` to `n - 3`:
    * If `nums[i] > 0`: break early, because the sum of three positive numbers can never equal 0.
    * If `i > 0` and `nums[i] == nums[i - 1]`: skip to prevent duplicate triplets with the same first element.
    * Initialize two pointers: `low = i + 1` and `high = n - 1`.
    * While `low < high`:
      * `current_sum = nums[i] + nums[low] + nums[high]`
      * If `current_sum == 0`:
        * Append `[nums[i], nums[low], nums[high]]` to results.
        * Skip duplicates: advance `low` while `low < high and nums[low] == nums[low + 1]`.
        * Skip duplicates: decrease `high` while `low < high and nums[high] == nums[high - 1]`.
        * Move both pointers inward: `low += 1`, `high -= 1`.
      * Else if `current_sum < 0`: advance `low += 1` to get a larger sum.
      * Else: decrement `high -= 1` to get a smaller sum.
* **Avoiding Duplicates:** Handled directly during traversal by skipping adjacent duplicates for `nums[i]`, `nums[low]`, and `nums[high]`, requiring no extra hash set.
* **Time Complexity:** $\mathcal{O}(N^2)$ — $\mathcal{O}(N \log N)$ for sorting + $\mathcal{O}(N^2)$ for the two-pointer search.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space (excluding the output list).

**File:** [01.py](../../code/sprint-4/day_3/01.py)
