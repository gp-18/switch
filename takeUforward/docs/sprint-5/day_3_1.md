# 🟢 Day 3 — Arrays: Count Inversions (Divide & Conquer / Merge Sort Approach)

## 1. Count Inversions

Given an integer array `nums`, return the total number of **inversions** in the array.

Two elements `nums[i]` and `nums[j]` form an inversion if:
$$nums[i] > nums[j] \quad \text{and} \quad i < j$$

Inversion count measures how far an array is from being sorted:
* An already sorted array has an inversion count of **0**.
* An array sorted in reverse (descending) order has the **maximum** possible number of inversions.

### Example

```text
Input:  nums = [2, 3, 7, 1, 3, 5]
Output: 5
Explanation:
The 5 inversion pairs (where i < j and nums[i] > nums[j]) are:
1. nums[0] = 2 > nums[3] = 1 (indices 0 < 3)
2. nums[1] = 3 > nums[3] = 1 (indices 1 < 3)
3. nums[2] = 7 > nums[3] = 1 (indices 2 < 3)
4. nums[2] = 7 > nums[4] = 3 (indices 2 < 4)
5. nums[2] = 7 > nums[5] = 5 (indices 2 < 5)

Input:  nums = [-10, -5, 6, 11, 15, 17]
Output: 0
Explanation: The array is already sorted in non-decreasing order, so no inversions exist.

Input:  nums = [9, 5, 4, 2]
Output: 6
Explanation:
Array is strictly descending. All pairs form inversions:
(9, 5), (9, 4), (9, 2), (5, 4), (5, 2), (4, 2)
Total pairs = 4 * (4 - 1) / 2 = 6.

Input:  nums = [1]  # Edge Case: Single element
Output: 0
Explanation: A single element cannot form any pair.
```

### Think About

* **Brute Force vs Optimal:**
  * **Brute Force:** Compare every pair `(i, j)` where `i < j` using two nested loops.
    * Time Complexity: $\mathcal{O}(N^2)$ (TLE for $N = 10^5$).
    * Space Complexity: $\mathcal{O}(1)$.
  * **Optimal Approach (Divide & Conquer / Merge Sort):**
    * Can we count inversions while sorting the array in $\mathcal{O}(N \log N)$?
    * Suppose we divide `nums` into two halves: `left` (`nums[low..mid]`) and `right` (`nums[mid+1..high]`).
    * Inversions can be split into three independent categories:
      1. Inversions entirely inside the left half.
      2. Inversions entirely inside the right half.
      3. **Split Inversions:** Pairs `(i, j)` where `nums[i]` is in the left half and `nums[j]` is in the right half.

* **How Does Merge Step Count Split Inversions in $\mathcal{O}(1)$?**
  * When both the left half and right half are recursively sorted:
    * Let `left` point into `nums[low..mid]` and `right` point into `nums[mid+1..high]`.
    * If `nums[left] <= nums[right]`:
      * `nums[left]` does not form an inversion with `nums[right]`. Place `nums[left]` into `temp` and advance `left += 1`.
    * If `nums[left] > nums[right]`:
      * Because the left half is already sorted, if `nums[left]` is strictly greater than `nums[right]`, then **all remaining elements from index `left` to `mid`** are also strictly greater than `nums[right]`!
      * Therefore, `nums[right]` forms an inversion with every single element in `nums[left..mid]`.
      * Add `(mid - left + 1)` directly to the inversion counter!
      * Place `nums[right]` into `temp` and advance `right += 1`.
  * Total Inversions = `mergeSort(left) + mergeSort(right) + merge(left, right)`.

* **Maximum Inversion Count Formula:**
  * In the worst-case scenario (array sorted in strictly descending order), every possible pair forms an inversion:
    $$\text{Max Inversions} = \frac{N(N - 1)}{2} \in \mathcal{O}(N^2)$$
  * For $N = 10^5$, maximum inversions can reach $\approx \frac{10^{10}}{2} = 5 \times 10^9$, which exceeds the 32-bit signed integer limit ($2 \times 10^9$). Python handles arbitrarily large integers automatically, but in C++/Java a 64-bit integer (`long long` / `long`) must be used.

* **Relationship to Bubble Sort:**
  * The number of inversions in an array is mathematically identical to the minimum number of adjacent swaps required by Bubble Sort to completely sort the array.

* **Interview Follow-Up (Reverse Pairs & Variations):**
  * In problems like **Reverse Pairs** (where the condition is $nums[i] > 2 \times nums[j]$), we cannot count during the standard merge step because multiplying by 2 breaks the sorted pointer progression. Instead, we perform a dedicated two-pointer counting pass *immediately before* the merge step.

* **Time Complexity:** $\mathcal{O}(N \log N)$ — Identical to standard Merge Sort. The tree depth is $\log N$ and each level takes linear $\mathcal{O}(N)$ merge and count time.
* **Space Complexity:** $\mathcal{O}(N)$ — Auxiliary space for the temporary merge array and $\mathcal{O}(\log N)$ recursive call stack.

**File:** [01.py](../../code/sprint-5/day_3_1/01.py)
