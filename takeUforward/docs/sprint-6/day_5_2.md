# 🟢 Day 5.2 — Binary Search: Find Peak Element

## 1. Find Peak Element

Given an array `arr` of integers, find the index (0-based) of a **peak element**.

A peak element is an element that is strictly greater than its neighbors:
$$arr[i - 1] < arr[i] \quad \text{and} \quad arr[i + 1] < arr[i]$$

For boundary elements:
* For $arr[0]$, assume its left neighbor is $-\infty$ ($arr[-1] = -\infty$).
* For $arr[n - 1]$, assume its right neighbor is $-\infty$ ($arr[n] = -\infty$).

If the array contains multiple peak elements, return the index of **any** peak element.

You must write an algorithm that runs in $\mathcal{O}(\log N)$ time complexity.

### Example

```text
Input:  arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
Output: 7
Explanation:
At index 7, element is 8.
Its neighbors are arr[6] = 7 and arr[8] = 5.
Since 7 < 8 and 8 > 5, 8 is a peak element. Index = 7.

Input:  arr = [1, 2, 1, 3, 5, 6, 4]
Output: 1
Explanation:
There are two peak elements: index 1 (value 2) and index 5 (value 6).
Returning either 1 or 5 is valid.

Input:  arr = [-2, -1, 3, 4, 5]
Output: 4
Explanation:
Strictly increasing array. The last element 5 is greater than arr[3] = 4,
and its right neighbor is -infinity. Index = 4.

Input:  arr = [5, 4, 3, 2, 1]  # Edge Case: Strictly decreasing array
Output: 0
Explanation:
The first element 5 is greater than arr[1] = 4, and its left neighbor is -infinity. Index = 0.

Input:  arr = [10]  # Edge Case: Single element
Output: 0
Explanation:
The only element is greater than both its -infinity boundary neighbors.
```

### Think About

* **Handling Boundaries First ($0$-th and $(n-1)$-th indices):**
  * If $n = 1$, the only element is trivially a peak $\rightarrow$ return `0`.
  * If $arr[0] > arr[1]$, $arr[0]$ is a peak $\rightarrow$ return `0`.
  * If $arr[n - 1] > arr[n - 2]$, $arr[n - 1]$ is a peak $\rightarrow$ return `n - 1`.
  * By validating the boundaries upfront, the binary search space is cleanly reduced to the interior indices:
    $$1 \le mid \le n - 2$$
  * This guarantees that for every `mid`, both `arr[mid - 1]` and `arr[mid + 1]` exist without any bounds-checking overhead!

* **Why Binary Search Works on Unsorted Arrays (The Slope Property):**
  * Binary search does **not** always require a globally sorted array; it requires a decision rule that allows eliminating half the search space based on local information.
  * For any interior element `arr[mid]`:
    1. **Peak Condition:** If $arr[mid - 1] < arr[mid]$ and $arr[mid] > arr[mid + 1]$, `mid` is a local maximum. Return `mid` immediately!
    2. **Upward Slope ($arr[mid] > arr[mid - 1]$):**
       * The array values are rising from left to right at `mid`.
       * Since the values cannot continue rising infinitely (the boundary at $n-1$ drops to $-\infty$), there **must** exist at least one peak in the right half.
       * Eliminate the left half: `low = mid + 1`.
    3. **Downward Slope or Valley ($arr[mid] \le arr[mid - 1]$):**
       * The values are decreasing from left to right at `mid`.
       * There **must** exist at least one peak in the left half.
       * Eliminate the right half: `high = mid - 1`.

* **Step-by-Step Binary Search Algorithm:**
  1. Check boundary edge cases:
     * If $n == 1 \implies$ return `0`.
     * If $arr[0] > arr[1] \implies$ return `0`.
     * If $arr[n - 1] > arr[n - 2] \implies$ return `n - 1`.
  2. Set `low = 1`, `high = n - 2`.
  3. While `low <= high`:
     * `mid = low + (high - low) // 2`.
     * If $arr[mid] > arr[mid - 1]$ and $arr[mid] > arr[mid + 1]$:
       * Return `mid`.
     * If $arr[mid] > arr[mid - 1]$:
       * Moving up towards a right peak: `low = mid + 1`.
     * Else:
       * Moving down, peak lies on the left: `high = mid - 1`.
  4. Return `-1` (fallback, though mathematically a peak is guaranteed to exist).

* **Time Complexity:** $\mathcal{O}(\log N)$
  * The search space $[1, n - 2]$ is halved in each step.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-6/day_5_2/01.py)

