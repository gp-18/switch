# 🟢 Day 1.2 — Binary Search on 2D Matrix: Find Row with Maximum 1's

## 1. Find Row with Maximum 1's

Given a non-empty binary matrix `mat` of dimensions $n \times m$ consisting only of `0`s and `1`s, where **each row is sorted in non-decreasing (ascending) order**.

Find the **0-based index of the row** that contains the **maximum number of `1`s**.

* If multiple rows tie for the maximum number of `1`s, return the **smaller row index**.
* If no `1` exists anywhere in the matrix, return `-1`.

You must write an algorithm that runs in $\mathcal{O}(n + m)$ time complexity (or $\mathcal{O}(n \log m)$ using Binary Search per row).

### Example

```text
Input:  mat = [
  [1, 1, 1],
  [0, 0, 1],
  [0, 0, 0]
]
Output: 0
Explanation:
Row 0 has 3 ones, Row 1 has 1 one, Row 2 has 0 ones.
Row 0 has the maximum number of ones. Index = 0.

Input:  mat = [
  [0, 0],
  [0, 0]
]
Output: -1
Explanation:
The matrix does not contain any 1. Return -1.

Input:  mat = [
  [0, 0, 1],
  [0, 1, 1],
  [0, 1, 1]
]
Output: 1
Explanation:
Row 0 has 1 one, Row 1 has 2 ones, Row 2 has 2 ones.
Rows 1 and 2 tie with 2 ones; return the smaller index 1.

Input:  mat = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 1]
]  # Edge Case: Only last cell is 1
Output: 2
```

### Think About

* **Approach 1: Binary Search per Row ($\mathcal{O}(n \log m)$):**
  * Since every row is sorted (`0`s followed by `1`s), the number of `1`s in row $i$ is completely determined by the **first index where `1` appears** (`lower_bound(mat[i], 1)`):
    $$\text{count\_1s}(row) = m - \text{lower\_bound}(mat[row], 1)$$
  * Running binary search on each of the $n$ rows takes $\mathcal{O}(n \log m)$ time and $\mathcal{O}(1)$ space.

* **Approach 2: Optimal Staircase / Top-Right Traversal ($\mathcal{O}(n + m)$):**
  * We can achieve linear $\mathcal{O}(n + m)$ time by starting at the **top-right corner** (`row = 0, col = m - 1`) and moving only **left** or **down**:
    1. Initialize `row = 0`, `col = m - 1`, `ans = -1`.
    2. While `row < n` and `col >= 0`:
       * **If `mat[row][col] == 1`:**
         * The current row has strictly more `1`s than any previously discovered best row (because we only move left when we surpass the best column boundary so far!).
         * Update `ans = row`.
         * Move left to look for even more `1`s in this same row: `col -= 1`.
       * **Else (`mat[row][col] == 0`):**
         * Because the row is sorted, every element to the left of `col` in this row is also `0`.
         * Therefore, this row cannot contain more `1`s than the current best row.
         * Discard this row and move down: `row += 1`.
    3. Return `ans`.

* **Why Ties Always Pick the Smaller Row Index Automatically:**
  * Suppose Row 1 advances `col` left from `2` to `0` (`ans` becomes `1` when hitting `mat[1][1] == 1`). Now `col = 0`, and `mat[1][0] == 0`, so we move down to Row 2.
  * In Row 2, suppose it also has two `1`s (`[0, 1, 1]`). Its value at `col = 0` is `0`, so `mat[2][0] == 0` simply triggers `row += 1` without updating `ans`.
  * `ans` is ONLY updated when a row has a `1` strictly further to the left (`col` where the previous best had `0`), guaranteeing ties retain the smaller index!

* **Time Complexity:** $\mathcal{O}(n + m)$
  * In every step of the `while` loop, either `row` increments by `1` (at most $n$ times) or `col` decrements by `1` (at most $m$ times).
  * Thus, the loop executes at most $n + m$ times.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-7/day_1_2/01.py)
