# 🟢 Day 4.2 — Arrays: Merge Two Sorted Arrays Without Extra Space (Three-Pointer Reverse Merge & Gap Method)

## 1. Merge Two Sorted Arrays Without Extra Space

Given two integer arrays `nums1` and `nums2`, both sorted in non-decreasing order, and two integers `m` and `n` representing the number of valid elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array must not be returned by the function; instead, it should be stored **in-place** inside `nums1`. To accommodate this, `nums1` has a total length of `m + n`, where the first `m` elements denote the initial valid elements, and the last `n` elements are set to `0` and should be ignored/overwritten.

### Example

```text
Input:  nums1 = [-5, -2, 4, 5, 0, 0, 0], m = 4, nums2 = [-3, 1, 8], n = 3
Output: [-5, -3, -2, 1, 4, 5, 8]
Explanation:
The merged array is [-5, -3, -2, 1, 4, 5, 8], where [-5, -2, 4, 5] originate from nums1 and [-3, 1, 8] from nums2.

Input:  nums1 = [0, 2, 7, 8, 0, 0, 0], m = 4, nums2 = [-7, -3, -1], n = 3
Output: [-7, -3, -1, 0, 2, 7, 8]
Explanation:
The merged array is [-7, -3, -1, 0, 2, 7, 8], where [0, 2, 7, 8] originate from nums1 and [-7, -3, -1] from nums2.

Input:  nums1 = [1, 3, 5, 0, 0, 0, 0], m = 3, nums2 = [2, 4, 6, 7], n = 4
Output: [1, 2, 3, 4, 5, 6, 7]
Explanation:
Merging from the back places 7, 6, 5, 4, 3, 2, 1 sequentially into nums1 from index 6 down to 0.

Input:  nums1 = [1], m = 1, nums2 = [], n = 0  # Edge Case: nums2 is empty
Output: [1]
Explanation: No elements to merge; nums1 remains [1].

Input:  nums1 = [0], m = 0, nums2 = [1], n = 1  # Edge Case: nums1 is initially empty
Output: [1]
Explanation: nums2 replaces the placeholder 0 in nums1.
```

### Think About

* **Why Starting from the Beginning Fails In-Place ($\mathcal{O}(m \cdot n)$ or Extra Space):**
  * If we compare from index `0` and attempt to place the smaller element into the front of `nums1`, we would overwrite an uninspected valid element in `nums1`.
  * Shifting elements to the right to make room takes $\mathcal{O}(m)$ per insertion, degrading the overall runtime to $\mathcal{O}(m \cdot n)$.
  * Allocating an auxiliary array of size $m + n$ requires $\mathcal{O}(m + n)$ extra memory, which violates the strict $\mathcal{O}(1)$ auxiliary space constraint.

* **The Key Insight: Fill from the Back (Three-Pointer Technique):**
  * `nums1` conveniently has $n$ empty/zero slots at the end (indices `m` to `m + n - 1`).
  * The largest elements in the combined array must ultimately end up at the very end of `nums1`.
  * By placing the largest elements first, we write into the unused trailing buffer of `nums1`, guaranteeing we **never overwrite** any uninspected element of `nums1`.

* **Three-Pointer Setup & Step-by-Step Algorithm:**
  1. Initialize three pointers:
     * `i = m - 1`: points to the last valid element of `nums1`.
     * `j = n - 1`: points to the last element of `nums2`.
     * `k = m + n - 1`: points to the current write position at the back of `nums1`.
  2. While both `i >= 0` and `j >= 0`:
     * If `nums1[i] > nums2[j]`:
       * Place `nums1[k] = nums1[i]`
       * Decrement `i -= 1`
     * Else:
       * Place `nums1[k] = nums2[j]`
       * Decrement `j -= 1`
     * Decrement `k -= 1`
  3. **Handling Remaining Elements:**
     * If `j >= 0` (elements still remain in `nums2` after `nums1` is exhausted):
       * Copy the remaining elements: `nums1[k] = nums2[j]`, decrementing both `j` and `k`.
     * If `i >= 0` (elements still remain in `nums1` after `nums2` is exhausted):
       * They are **already in their correct sorted positions** at the front of `nums1`! No further copying is required.

* **Interview Follow-Up 1: What if `nums1` does NOT have extra buffer space? (Hard Variant):**
  * When `nums1` of size $m$ and `nums2` of size $n$ must both remain sorted without buffer space:
    1. **Two Pointers + Sort Method:**
       * Compare the largest remaining element in `nums1` (`nums1[left]`) with the smallest in `nums2` (`nums2[right]`).
       * If `nums1[left] > nums2[right]`: swap them, decrement `left`, and increment `right`.
       * Once the condition fails, sort both `nums1` and `nums2` individually.
       * Time: $\mathcal{O}(m \log m + n \log n)$, Space: $\mathcal{O}(1)$.
    2. **Gap Method (Shell Sort Technique):**
       * Initial gap: $\text{gap} = \lceil (m + n) / 2 \rceil$.
       * Compare elements separated by `gap` across the virtual concatenated array and swap if out of order.
       * Halve the gap: $\text{gap} = \lceil \text{gap} / 2 \rceil$ until $\text{gap} == 0$.
       * Time: $\mathcal{O}((m + n) \log(m + n))$, Space: $\mathcal{O}(1)$.

* **Interview Follow-Up 2: Connection to Merge Sort:**
  * This is precisely the merge subroutine of standard Merge Sort, adapted to work backwards in $\mathcal{O}(1)$ auxiliary space by leveraging the trailing buffer.

* **Time Complexity:** $\mathcal{O}(m + n)$ — Each element from `nums1` and `nums2` is inspected and placed into its final position at most once.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space — Merging is performed directly in-place within `nums1`.

**File:** [01.py](../../code/sprint-5/day_4_2/01.py)
