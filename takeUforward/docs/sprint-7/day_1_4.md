# 🟢 Day 1.4 — Binary Search on 2D Matrix: Search in 2D Matrix - II

## 1. Search in 2D Matrix - II

Given a 2D integer matrix `matrix` of dimensions $n \times m$ where:
1. All integers in each **row** are sorted in ascending order from **left to right**.
2. All integers in each **column** are sorted in ascending order from **top to bottom**.

Write an efficient algorithm to search for a specific integer `target` in the matrix. Return `True` if `target` exists, or `False` otherwise.

You must write an algorithm that runs in $\mathcal{O}(n + m)$ time complexity.

### Example

```text
Input:  matrix = [
  [1,  4,  7,  11, 15],
  [2,  5,  8,  12, 19],
  [3,  6,  9,  16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], target = 5
Output: True
Explanation:
Target 5 exists in the matrix at coordinates (1, 1).

Input:  matrix = [
  [1,  4,  7,  11, 15],
  [2,  5,  8,  12, 19],
  [3,  6,  9,  16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], target = 20
Output: False
Explanation:
20 does not exist in the matrix. Return False.

Input:  matrix = [
  [1,  4,  7,  11, 15],
  [2,  5,  8,  12, 19],
  [3,  6,  9,  16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], target = 1
Output: True

Input:  matrix = [[-5]], target = -5  # Edge Case: 1x1 matrix
Output: True
```

### Think About

* **Why Virtual 1D Binary Search Fails Here:**
  * Unlike *Search in a 2D Matrix I*, the first element of a row is **not** guaranteed to be larger than the last element of the previous row (e.g. `matrix[0][-1] = 15 > matrix[1][0] = 2`).
  * Thus, flattening the matrix row-by-row does **not** produce a globally sorted 1D array.

* **Choosing the Optimal Starting Corner (Saddleback Search):**
  * Consider all four corners of the matrix:
    * **`(0, 0)` (Top-Left):** Moving right **increases**, moving down **increases**. Ambiguous if `target` is larger!
    * **`(n - 1, m - 1)` (Bottom-Right):** Moving left **decreases**, moving up **decreases**. Ambiguous if `target` is smaller!
    * **`(0, m - 1)` (Top-Right):** Moving left **decreases**, moving down **increases**. **Unambiguous!**
    * **`(n - 1, 0)` (Bottom-Left):** Moving right **increases**, moving up **decreases**. **Also unambiguous!**
  * Starting at either `(0, m - 1)` or `(n - 1, 0)` allows us to eliminate an entire row or an entire column in every single comparison!

* **Step-by-Step Top-Right Traversal Algorithm:**
  1. Start at the top-right corner: `row = 0`, `col = m - 1`.
  2. While `row < n` and `col >= 0`:
     * **If `matrix[row][col] == target`:**
       * Target found! Return `True`.
     * **If `matrix[row][col] < target`:**
       * Because rows increase left-to-right, all elements to the left of `col` in `row` are also $< \text{target}$.
       * Therefore, `target` cannot be in the current row $\rightarrow$ eliminate this row: `row += 1`.
     * **Else (`matrix[row][col] > target`):**
       * Because columns increase top-to-bottom, all elements below `row` in `col` are also $> \text{target}$.
       * Therefore, `target` cannot be in the current column $\rightarrow$ eliminate this column: `col -= 1`.
  3. If the loop terminates without finding `target`, return `False`.

* **Time Complexity:** $\mathcal{O}(N + M)$
  * From `(0, M - 1)`, the pointer can take at most $N$ steps downward and $M$ steps leftward before exiting the matrix bounds.
  * Total comparisons $\le N + M$.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-7/day_1_4/01.py)
