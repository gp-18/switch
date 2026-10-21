# 🟢 Day 4.2 — Arrays: Sort an Array of 0's, 1's, and 2's (Dutch National Flag Algorithm)

## 1. Sort an Array of 0's, 1's, and 2's

Given an array `nums` consisting of only `0`, `1`, or `2`. Sort the array in non-decreasing order.
The sorting must be done **in-place**, without making a copy of the original array.

### Example

```text
Input:  nums = [1, 0, 2, 1, 0]
Output: [0, 0, 1, 1, 2]
Explanation: The nums array in sorted order has 2 zeroes, 2 ones and 1 two.

Input:  nums = [0, 0, 1, 1, 1]
Output: [0, 0, 1, 1, 1]
Explanation: The nums array in sorted order has 2 zeroes, 3 ones and zero twos.

Input:  nums = [2, 0, 1]  # Edge Case: Single occurrence of each value
Output: [0, 1, 2]
```

### Think About

* **Optimal Approach (Dutch National Flag Algorithm):**
  * Use 3 pointers: `low`, `mid`, and `high` to divide the array into 4 logical partitions:
    * `nums[0 ... low - 1]` contains only `0`s (extreme left)
    * `nums[low ... mid - 1]` contains only `1`s
    * `nums[mid ... high]` is the **unsorted segment** containing an arbitrary mix of `0`, `1`, and `2`
    * `nums[high + 1 ... n - 1]` contains only `2`s (extreme right)
  * **Pointer Invariant & Iteration Rules:**
    * Initialize `low = 0`, `mid = 0`, and `high = n - 1`.
    * Loop while `mid <= high`:
      * **Case 1 (`nums[mid] == 0`):**
        * Swap `nums[low]` and `nums[mid]`.
        * Increment both `low += 1` and `mid += 1` (the element swapped into `mid` is known to be `1`, so `mid` can safely advance).
      * **Case 2 (`nums[mid] == 1`):**
        * It is already in the correct partition. Simply advance `mid += 1`.
      * **Case 3 (`nums[mid] == 2`):**
        * Swap `nums[mid]` and `nums[high]`.
        * Decrement `high -= 1`.
        * **Crucial:** Do **not** increment `mid` here, because the element swapped from `high` to `mid` is unexamined and might be `0`, `1`, or `2`. It must be evaluated in the next iteration.
* **Why In-Place with One Pass:**
  * By swapping elements directly to their respective boundaries in a single traversal, no extra memory or secondary counting pass is required.
* **Time Complexity:** $\mathcal{O}(N)$ — Single pass traversal where each iteration advances `mid` or decrements `high`.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space — Strictly in-place modification.

**File:** [01.py](../../code/sprint-4/day_4_2/01.py)
