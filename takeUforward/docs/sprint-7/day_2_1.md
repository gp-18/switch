# 🟢 Day 2.1 — Binary Search on 2D Matrix: Find Peak Element - II

## 1. Find Peak Element - II

Given a 0-indexed $n \times m$ matrix `mat` where **no two adjacent cells are equal**, find any **peak element** `mat[i][j]` and return its coordinates `[i, j]`.

A peak element in a 2D grid is an element that is **strictly greater** than all four of its adjacent neighbors (left, right, top, and bottom).

Assume the entire matrix is surrounded by an outer perimeter with the value `-1` in every boundary cell.

You must write an algorithm that runs in $\mathcal{O}(N \times \log M)$ time complexity.

### Example

```text
Input:  mat = [
  [10, 20, 15],
  [21, 30, 14],
  [7,  16, 32]
]
Output: [1, 1]
Explanation:
The value at [1, 1] is 30, which is strictly greater than all its neighbors:
20 (top), 16 (bottom), 21 (left), and 14 (right).
(Note: [2, 2] with value 32 is also a valid peak element).

Input:  mat = [
  [10, 7],
  [11, 17]
]
Output: [1, 1]
Explanation:
17 is strictly greater than 7 (top), 11 (left), and the -1 outer perimeter.

Input:  mat = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
Output: [2, 2]
Explanation:
9 is strictly greater than 6, 8, and the -1 outer boundaries.

Input:  mat = [
  [4, 2, 5, 1, 4, 5],
  [2, 9, 3, 2, 3, 2],
  [1, 7, 6, 0, 1, 3],
  [3, 6, 2, 3, 7, 2]
]
Output: [1, 1]
```

### Think About

* **Why Brute Force is Suboptimal:**
  * Finding the global maximum by scanning every cell guarantees a peak (since no two adjacent cells are equal), but takes $\mathcal{O}(N \times M)$ time.

* **Reducing 2D Peak Finding to 1D via Column Binary Search:**
  * Apply binary search over the column indices `[0, M - 1]`.
  * For a middle column `mid`, scan all $N$ rows in that column to find the **row index** `row` containing the **column's maximum element** (`mat[row][mid]`).
  * **Crucial Guarantee:** Because `mat[row][mid]` is the maximum element of column `mid`, it is automatically strictly greater than both its vertical neighbors (**top** and **bottom**)!
  * Therefore, we only need to compare `mat[row][mid]` against its **left** (`mat[row][mid - 1]`) and **right** (`mat[row][mid + 1]`) horizontal neighbors!

* **Eliminating Half of the Columns (Slope Argument):**
  * Let `left = mat[row][mid - 1]` if `mid - 1 >= 0` else `-1`.
  * Let `right = mat[row][mid + 1]` if `mid + 1 < m` else `-1`.
  * **Condition 1 (`mat[row][mid] > left and mat[row][mid] > right`):**
    * It is greater than its top, bottom, left, and right neighbors $\rightarrow$ Valid 2D peak! Return `[row, mid]`.
  * **Condition 2 (`left > mat[row][mid]`):**
    * A strictly larger value exists to the left in column `mid - 1`.
    * Moving towards larger neighbors cannot go on indefinitely (the perimeter is `-1` and adjacent values differ), so a peak is **guaranteed** to exist in the left half `[0, mid - 1]`.
    * Eliminate right half: `high = mid - 1`.
  * **Condition 3 (`right > mat[row][mid]`):**
    * A strictly larger value exists to the right. Eliminate left half: `low = mid + 1`.

* **Step-by-Step Algorithm:**
  1. Set `low = 0`, `high = m - 1`.
  2. While `low <= high`:
     * `mid = low + (high - low) // 2`.
     * Find `row = index of maximum value in column mid`.
     * Determine `left` and `right` neighbors (using `-1` or `-infinity` out of bounds).
     * Check if `mat[row][mid]` beats both `left` and `right` $\rightarrow$ return `[row, mid]`.
     * Else shift `high = mid - 1` if `left > mat[row][mid]`, otherwise `low = mid + 1`.
  3. Return `[-1, -1]` (fallback).

* **Time Complexity:** $\mathcal{O}(N \times \log M)$
  * Binary search runs across the $M$ columns in $\mathcal{O}(\log M)$ iterations.
  * Each iteration finds the maximum in a column of height $N$ in $\mathcal{O}(N)$ time.
  * *(Tip: If $M < N$, searching on rows instead gives $\mathcal{O}(M \times \log N)$).*
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-7/day_2_1/01.py)
