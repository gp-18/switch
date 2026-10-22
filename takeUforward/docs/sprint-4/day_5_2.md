# 🟢 Day 5.2 — Arrays: Next Permutation (Lexicographical Ordering)

## 1. Next Permutation

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

The **next permutation** of an array of integers is the next lexicographically greater permutation of its integers. More formally, if all the permutations of the array are sorted in lexicographical order, then the next permutation of that array is the permutation that immediately follows it in that sorted order.

If such an arrangement is not possible (i.e., the array is already at the last permutation in descending order), rearrange it into the lowest possible order (i.e., sorted in ascending order).

You must rearrange the numbers **in-place** and use only constant extra memory $\mathcal{O}(1)$.

### Example

```text
Input:  nums = [1, 2, 3]
Output: [1, 3, 2]
Explanation: The next permutation of [1, 2, 3] is [1, 3, 2].

Input:  nums = [3, 2, 1]  # Edge Case: Last permutation (descending order)
Output: [1, 2, 3]
Explanation: [3, 2, 1] is the highest permutation, so wrap around to the lowest: [1, 2, 3].

Input:  nums = [1, 1, 5]
Output: [1, 5, 1]
Explanation: Duplicates present; the next permutation is [1, 5, 1].
```

### Think About

* **Core Intuition (Smallest Possible Increase):**
  * To get the *immediate* next permutation, we want to modify the array as far to the right as possible (lowest significant positions).
* **The 3-Step In-Place Algorithm:**
  1. **Step 1: Find the Breakpoint (Pivot Index):**
     * Traverse backwards from right to left (`i = n - 2` down to `0`).
     * Find the first index `ind` where `nums[i] < nums[i + 1]`.
     * If the suffix is entirely in descending order, no rearrangement of that suffix can produce a larger value. The element at `ind` is the first element that can be swapped with a larger value.
  2. **Step 2: Handle Edge Case (Already Last Permutation):**
     * If no such breakpoint is found (`ind == -1`), the entire array is in descending order (e.g., `[5, 4, 3, 2, 1]`).
     * Reverse the whole array in-place to get the first (smallest) permutation and return.
  3. **Step 3: Find the Successor & Swap:**
     * Traverse backwards from the end (`n - 1` down to `ind + 1`).
     * Find the first element `nums[j]` strictly greater than `nums[ind]`.
     * Swap `nums[ind]` and `nums[j]`.
     * This places the smallest possible greater element into position `ind`.
  4. **Step 4: Reverse the Suffix:**
     * The subarray from index `ind + 1` to `n - 1` is still in strictly descending order.
     * Reverse this suffix in-place so that it becomes sorted in ascending order (the smallest possible configuration for that suffix).
* **Time Complexity:** $\mathcal{O}(N)$ — Three linear passes in the worst case: finding pivot ($\mathcal{O}(N)$), finding next greater element ($\mathcal{O}(N)$), and reversing suffix ($\mathcal{O}(N)$).
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space — In-place pointer swaps without extra memory.

**File:** [01.py](../../code/sprint-4/day_5_2/01.py)
