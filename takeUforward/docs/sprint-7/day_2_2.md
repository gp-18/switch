# 🟢 Day 2.2 — Binary Search on 2D Matrix: Matrix Median

## 1. Matrix Median

Given a 2D array `matrix` of dimensions $N \times M$ where **each row is sorted in non-decreasing (ascending) order**, and $N \times M$ is guaranteed to be **odd**.

Find and return the **median** of the given matrix (the middle element if all $N \times M$ numbers were arranged into a single sorted list).

You must write an algorithm that runs in $\mathcal{O}(N \times \log M \times \log(\max - \min + 1))$ time complexity.

### Example

```text
Input:  matrix = [
  [1, 4, 9],
  [2, 5, 6],
  [3, 7, 8]
]
Output: 5
Explanation:
Sorted 1D elements: [1, 2, 3, 4, 5, 6, 7, 8, 9].
The middle (5th) element is 5.

Input:  matrix = [
  [1, 3, 8],
  [2, 3, 4],
  [1, 2, 5]
]
Output: 3
Explanation:
Sorted 1D elements: [1, 1, 2, 2, 3, 3, 4, 5, 8].
The middle (5th) element is 3.

Input:  matrix = [
  [1, 4, 15],
  [2, 5, 6],
  [3, 8, 11]
]
Output: 5
Explanation:
Sorted 1D elements: [1, 2, 3, 4, 5, 6, 8, 11, 15]. Median = 5.

Input:  matrix = [
  [1,  2,  3,  4,  5],
  [8,  9,  11, 12, 13],
  [21, 23, 25, 27, 29]
]
Output: 11
```

### Think About

* **Why Brute Force is Suboptimal:**
  * Extracting all $N \times M$ elements into a 1D array and sorting takes $\mathcal{O}(N \cdot M \cdot \log(N \cdot M))$ time and $\mathcal{O}(N \cdot M)$ extra memory.

* **Binary Search on the Value Range (Answer Space):**
  * For an odd total count $N \times M$, define the required half-count:
    $$req = \frac{N \times M}{2}$$
  * A value $X$ is the **median** if it is the **smallest integer** such that the number of elements in the matrix $\le X$ is **strictly greater** than `req`:
    $$\text{count}(\le X) > \frac{N \times M}{2}$$
  * Since $\text{count}(\le X)$ is monotonically non-decreasing as $X$ increases, we can binary search on the **value space** $[\min, \max]$ rather than indices!

* **Search Space Boundaries:**
  * Because every row is sorted left-to-right:
    * **Lower bound (`low`):** The global minimum across the first column $\min_{i=0}^{N-1}(matrix[i][0])$.
    * **Upper bound (`high`):** The global maximum across the last column $\max_{i=0}^{N-1}(matrix[i][M-1])$.

* **Counting Elements $\le mid$ Using Upper Bound ($\mathcal{O}(N \log M)$):**
  * For any candidate value `mid`, how many elements in a sorted row are $\le mid$?
  * The **upper bound** (first index where `row[idx] > mid`) gives the exact count of elements $\le mid$ in that row!
  * Sum `upper_bound(matrix[i], mid)` across all $N$ rows to compute `small_equal`.

* **Step-by-Step Binary Search Algorithm:**
  1. Compute global `low` (min of first column) and `high` (max of last column).
  2. Set `req = (n * m) // 2`.
  3. While `low <= high`:
     * `mid = low + (high - low) // 2`.
     * Compute `small_equal = countSmallEqual(matrix, n, m, mid)`.
     * **If `small_equal <= req`:**
       * Not enough elements are $\le mid$; `mid` is too small to be the median.
       * Search right: `low = mid + 1`.
     * **Else (`small_equal > req`):**
       * `mid` could be the median (or greater than it).
       * Search left for the **smallest** such integer: `high = mid - 1`.
  4. Return `low`.
  *(Note: Because $\text{count}(\le X)$ only jumps at numbers present in the matrix, the smallest $X$ where $\text{count}(\le X) > req$ is mathematically guaranteed to exist inside the matrix!)*

* **Time Complexity:** $\mathcal{O}(N \times \log M \times \log(\max - \min + 1))$
  * Outer binary search takes $\mathcal{O}(\log(\max - \min + 1)) \approx 30$ steps (for values up to $10^9$).
  * Each step runs `upper_bound` ($\mathcal{O}(\log M)$) across $N$ rows ($\mathcal{O}(N \log M)$).
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-7/day_2_2/01.py)
