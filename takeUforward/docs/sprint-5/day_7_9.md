# 🟢 Day 7.9 — Binary Search: Single Element in a Sorted Array

## 1. Single Element in a Sorted Array

Given an array `nums` sorted in non-decreasing order. Every number in the array appears twice, **except for exactly one element** which appears once.

Find and return the single number in the array.

You must design an algorithm that runs in $\mathcal{O}(\log N)$ time and $\mathcal{O}(1)$ space.

### Example

```text
Input:  nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
Output: 4
Explanation: Only 4 appears once; all other elements appear twice.

Input:  nums = [1, 1, 3, 5, 5]
Output: 3
Explanation: Only 3 appears once.

Input:  nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7]
Output: 7
Explanation: 7 is the single element at the very end.

Input:  nums = [1]  # Edge Case: Single element array
Output: 1

Input:  nums = [2, 3, 3]  # Edge Case: Single element at start
Output: 2
```

### Think About

* **The Index Parity Invariant:**
  * Notice how pairs are indexed before and after the single element:
    * **Before the single element:** Pairs start on **even** indices and end on **odd** indices:
      $$\text{Pair} = (\text{even}, \text{odd}) \implies nums[2k] == nums[2k + 1]$$
    * **After the single element:** The single element disrupts the sequence by shifting all subsequent indices by $1$!
      $$\text{Pair} = (\text{odd}, \text{even}) \implies nums[2k + 1] == nums[2k + 2]$$
  * **Conclusion:**
    * If `nums[mid]` belongs to an `(even, odd)` pair: we are still on the **left side** of the single element $\rightarrow$ single element is to the right!
    * If `nums[mid]` belongs to an `(odd, even)` pair: we are on the **right side** of the single element $\rightarrow$ single element is to the left!

* **Handling Boundary Edge Cases First:**
  * If $n == 1$: return `nums[0]`.
  * If `nums[0] != nums[1]`: `nums[0]` is the single element.
  * If `nums[n - 1] != nums[n - 2]`: `nums[n - 1]` is the single element.
  * This allows us to safely initialize binary search on the interior range `low = 1, high = n - 2`, avoiding any out-of-bounds checks for `mid - 1` and `mid + 1`!

* **Binary Search Algorithm:**
  1. `low = 1`, `high = n - 2`.
  2. While `low <= high`:
     * Calculate `mid = low + (high - low) // 2`.
     * If `nums[mid] != nums[mid - 1]` and `nums[mid] != nums[mid + 1]`:
       * Found the single element! Return `nums[mid]`.
     * **Check if we are in the left half:**
       * `(mid % 2 == 1 and nums[mid] == nums[mid - 1])` OR `(mid % 2 == 0 and nums[mid] == nums[mid + 1])`
       * If yes: single element is to the right $\rightarrow$ `low = mid + 1`.
       * If no: single element is to the left $\rightarrow$ `high = mid - 1`.

* **XOR Index Trick (Cleanest Code):**
  * Notice that for any index `mid`, its expected twin is at `mid ^ 1`:
    * If `mid` is even: `mid ^ 1 = mid + 1`.
    * If `mid` is odd: `mid ^ 1 = mid - 1`.
  * If `nums[mid] == nums[mid ^ 1]`: we are in the left half $\rightarrow$ `low = mid + 1`. Else: `high = mid - 1`.

* **Time Complexity:** $\mathcal{O}(\log N)$ — Logarithmic binary search.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-5/day_7_9/01.py)
