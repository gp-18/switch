# 🟢 Day 4 — Arrays: 4 Sum & Quadruplet Problems

## 1. 4 Sum

Given an integer array `nums` and an integer `target`. Return all unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:
- $a, b, c, d$ are distinct valid indices of `nums` ($0 \le a < b < c < d < n$)
- `nums[a] + nums[b] + nums[c] + nums[d] == target`

Notice that the solution set must not contain duplicate quadruplets. The output and the quadruplets can be returned in any order.

### Example

```text
Input:  nums = [1, -2, 3, 5, 7, 9], target = 7
Output: [[-2, 1, 3, 5]]

Input:  nums = [1, 1, 3, 4, -3], target = 5
Output: [[-3, 1, 3, 4]]

Input:  nums = [7, -7, 1, 2, 14, 3], target = 9  # Edge Case: No quadruplets sum to target
Output: []
```

### Think About

* **Optimal Approach (Sort + Two Fixed Pointers + Two Moving Pointers):**
  * Extending the 2-Sum and 3-Sum two-pointer pattern: sort `nums` in ascending order ($\mathcal{O}(N \log N)$).
  * First outer loop fixes `i` from `0` to `n - 4`:
    * If `i > 0` and `nums[i] == nums[i - 1]`: skip to avoid duplicate first elements.
  * Second inner loop fixes `j` from `i + 1` to `n - 3`:
    * If `j > i + 1` and `nums[j] == nums[j - 1]`: skip to avoid duplicate second elements.
  * Use two moving pointers for the remaining pair: `k = j + 1` and `l = n - 1`:
    * While `k < l`:
      * `sum_val = nums[i] + nums[j] + nums[k] + nums[l]`
      * If `sum_val == target`:
        * Append `[nums[i], nums[j], nums[k], nums[l]]` to answer.
        * Move pointers: `k += 1`, `l -= 1`.
        * Skip duplicate values: `while k < l and nums[k] == nums[k - 1]: k += 1`.
        * Skip duplicate values: `while k < l and nums[l] == nums[l + 1]: l -= 1`.
      * Else if `sum_val < target`: advance `k += 1` to increase sum.
      * Else: decrement `l -= 1` to decrease sum.
* **Avoiding Duplicates:** Handled directly during traversal by skipping adjacent duplicates for `nums[i]`, `nums[j]`, `nums[k]`, and `nums[l]`, requiring $\mathcal{O}(1)$ auxiliary memory without an external hash set.
* **Time Complexity:** $\mathcal{O}(N^3)$ — Sorting takes $\mathcal{O}(N \log N)$, and the two outer loops plus inner two-pointer traversal take $\mathcal{O}(N^3)$ total.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space (excluding the output list).

**File:** [01.py](../../code/sprint-4/day_4/01.py)
