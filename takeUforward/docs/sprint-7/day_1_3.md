# 🟢 Day 1.3 — Binary Search on 2D Matrix: Search in a 2D Matrix

## 1. Search in a 2D Matrix

Given a 2D integer matrix `mat` of size $n \times m$ where:
1. Each row is sorted in non-decreasing order.
2. The first element of each row is strictly greater than the last element of the previous row (if it exists).

Given an integer `target`, return `True` if `target` is in `mat`, or `False` otherwise.

You must write an algorithm that runs in $\mathcal{O}(\log(n \times m))$ time complexity.

### Example

```text
Input:  mat = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12]
], target = 8
Output: True
Explanation:
The target 8 exists in the matrix at coordinates (1, 3).

Input:  mat = [
  [1, 2, 4],
  [6, 7, 8],
  [9, 10, 34]
], target = 78
Output: False
Explanation:
78 does not exist in the matrix. Return False.

Input:  mat = [
  [1, 2, 4],
  [6, 7, 8],
  [9, 10, 34]
], target = 7
Output: True

Input:  mat = [[5]], target = 5  # Edge Case: 1x1 matrix
Output: True
```

### Think About

* **Why Physical Flattening is Suboptimal:**
  * Because the first element of every row exceeds the last element of the previous row, concatenating all rows yields one globally sorted 1D array of length $N \times M$.
  * However, actually copying the matrix into a 1D array would take $\mathcal{O}(N \times M)$ time and $\mathcal{O}(N \times M)$ extra memory, violating our logarithmic complexity requirement.

* **Virtual 1D Index to 2D Coordinate Mapping ($\mathcal{O}(1)$ Translation):**
  * We can treat the matrix as a **virtual 1D array** spanning indices $[0, N \times M - 1]$ without allocating any extra memory!
  * Given a 1D index `mid` and column count $M$:
    $$\text{row} = \text{mid} // M \qquad \text{col} = \text{mid} \bmod M$$
  * **Why this works:** Since every row contains $M$ elements, integer division `mid // M` counts how many full rows lie before `mid` (giving the row index), and the remainder `mid % M` gives the horizontal offset within that row (giving the column index).

* **Step-by-Step Binary Search Algorithm:**
  1. Set `low = 0`, `high = n * m - 1`.
  2. While `low <= high`:
     * `mid = low + (high - low) // 2`.
     * Translate to 2D cell: `row = mid // m`, `col = mid % m`.
     * **If `mat[row][col] == target`:**
       * Target found! Return `True`.
     * **If `mat[row][col] < target`:**
       * Target must be larger $\rightarrow$ search right half: `low = mid + 1`.
     * **Else (`mat[row][col] > target`):**
       * Target must be smaller $\rightarrow$ search left half: `high = mid - 1`.
  3. If loop exits without finding the target, return `False`.

* **Time Complexity:** $\mathcal{O}(\log(N \times M))$
  * Standard binary search over an imaginary sorted array of size $N \times M$.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-7/day_1_3/01.py)
