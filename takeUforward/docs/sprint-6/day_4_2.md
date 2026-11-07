# 🟢 Day 4.2 — Binary Search: Kth Missing Positive Number

## 1. Kth Missing Positive Number

Given a sorted array of unique positive integers `arr`, your task is to return the **$k$-th missing positive number** that is not present in `arr`.

The array is guaranteed to be strictly increasing, and the missing numbers are those positive integers that do not appear in `arr` but would appear in a full sequence of natural numbers starting from $1$ ($[1, 2, 3, 4, 5, \dots]$).

You must write an algorithm that runs in $\mathcal{O}(\log N)$ time complexity.

### Example

```text
Input:  arr = [3, 5, 7, 10], k = 6
Output: 9
Explanation:
The natural numbers are: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...
Missing numbers are: [1, 2, 4, 6, 8, 9, 11, ...]
The 6th missing positive number is 9.

Input:  arr = [1, 4, 6, 8, 9], k = 3
Output: 5
Explanation:
Missing numbers are: [2, 3, 5, 7, 10, ...]
The 3rd missing positive number is 5.

Input:  arr = [2, 3, 7, 11, 15], k = 5
Output: 8
Explanation:
Missing numbers are: [1, 4, 5, 6, 8, 9, 10, ...]
The 5th missing positive number is 8.

Input:  arr = [5, 6, 7], k = 2  # Edge Case: k-th missing lies before arr[0]
Output: 2
Explanation:
Missing numbers start at 1: [1, 2, 3, 4, 8, ...]. The 2nd missing is 2.

Input:  arr = [1, 2, 3, 4], k = 2  # Edge Case: k-th missing lies beyond arr[-1]
Output: 6
Explanation:
No missing numbers <= 4. Missing numbers start after 4: [5, 6, ...]. The 2nd missing is 6.
```

### Think About

* **The Missing Count Invariant:**
  * In a perfect sequence without any missing numbers starting at $1$, the number at index $i$ should equal $i + 1$:
    * At index $0 \rightarrow 1$
    * At index $1 \rightarrow 2$
    * At index $i \rightarrow i + 1$
  * When numbers are missing, the actual value `arr[i]` is strictly greater than its expected value $i + 1$.
  * Therefore, the exact count of missing numbers strictly to the left of index $i$ is:
    $$\text{missing}(i) = arr[i] - (i + 1)$$
  * Because `arr` is strictly increasing, $\text{missing}(i)$ is **monotonically non-decreasing**:
    $$i_1 < i_2 \implies \text{missing}(i_1) \le \text{missing}(i_2)$$

* **Binary Search on the Array Indices:**
  * We can binary search the index range $[0, n - 1]$ to locate the partition boundary: the largest index `right` where the missing count is strictly less than $k$ ($\text{missing}(right) < k$).
  * Initialize `left = 0`, `right = n - 1`.
  * While `left <= right`:
    * Compute `mid = left + (right - left) // 2`.
    * Calculate `missing = arr[mid] - (mid + 1)`.
    * **If `missing < k`:**
      * Fewer than $k$ numbers are missing up to index `mid`. The $k$-th missing number must lie to the right: `left = mid + 1`.
    * **Else (`missing >= k`):**
      * At least $k$ numbers are already missing by index `mid`. Search to the left: `right = mid - 1`.

* **Derivation of the Final Answer (`left + k`):**
  * When binary search terminates, `right` and `left` cross such that `right = left - 1`.
  * The $k$-th missing number lies between `arr[right]` and `arr[left]`.
  * Up to index `right`, the number of missing elements is:
    $$\text{missing\_count} = arr[right] - (right + 1)$$
  * We still need $(k - \text{missing\_count})$ more numbers beyond `arr[right]`:
    $$\text{ans} = arr[right] + (k - \text{missing\_count})$$
    $$\text{ans} = arr[right] + k - (arr[right] - (right + 1))$$
    $$\text{ans} = arr[right] + k - arr[right] + right + 1 = right + 1 + k$$
  * Since `left = right + 1`, this simplifies directly to:
    $$\text{ans} = left + k$$
  * This formula cleanly handles all edge cases, including when the answer lies before `arr[0]` (`right = -1, left = 0 \implies 0 + k = k`) or beyond `arr[-1]`.

* **Time Complexity:** $\mathcal{O}(\log N)$
  * Binary search cuts the search space of $N$ indices in half each iteration.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-6/day_4_2/01.py)

