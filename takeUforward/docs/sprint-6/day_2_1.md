# 🟢 Day 2.1 — Binary Search: Find Square Root of a Number (Floor Sqrt)

## 1. Find Square Root of a Number

Given a non-negative integer `n`, find and return its square root. If `n` is not a perfect square, return the **floor value** of $\sqrt{n}$ (i.e. the largest integer $x$ such that $x^2 \le n$).

You must write an algorithm with $\mathcal{O}(\log n)$ runtime complexity.

### Example

```text
Input:  n = 36
Output: 6
Explanation: 6 * 6 = 36, which is exactly equal to 36.

Input:  n = 28
Output: 5
Explanation: The square root of 28 is approximately 5.2915... The floor integer value is 5 (5^2 = 25 <= 28 < 6^2 = 36).

Input:  n = 50
Output: 7
Explanation: 7^2 = 49 <= 50 < 8^2 = 64. The floor value is 7.

Input:  n = 0  # Edge Case: Zero
Output: 0

Input:  n = 1  # Edge Case: Unity
Output: 1
```

### Think About

* **Binary Search on the Answer Space:**
  * The answer is an integer $x$ lying in the monotonic search space:
    $$0 \le x \le n$$
  * Because $f(x) = x^2$ is monotonically strictly increasing for $x \ge 0$, we can binary search directly over this numerical range without needing an array!

* **Binary Search Algorithm:**
  1. Initialize `low = 0` (or `1` for $n \ge 1$), `high = n`.
  2. While `low <= high`:
     * Calculate `mid = low + (high - low) // 2`.
     * Calculate `val = mid * mid`.
     * **Condition 1: `val <= n`**
       * `mid` is a valid candidate because $mid^2 \le n$.
       * We want the *largest* such integer, so try searching to the right: `low = mid + 1`.
     * **Condition 2: `val > n`**
       * `mid` is too large ($mid^2 > n$).
       * Eliminate the right half: `high = mid - 1`.
  3. When the loop terminates (`low > high`), `high` will point to the largest integer whose square is $\le n$.
  4. Return `high` (or the tracked `ans`).

* **Avoiding Integer Overflow (PBC Favorite):**
  * In statically typed languages like C++ or Java where $n \le 2^{31} - 1$, computing `mid * mid` can easily overflow a 32-bit signed integer when $mid \approx 10^5$.
  * Use a 64-bit integer (`long long mid * mid`) or rewrite the condition as `mid <= n // mid` (for $mid > 0$). In Python, arbitrary-precision integers handle this natively.

* **Time Complexity:** $\mathcal{O}(\log n)$ — The search space of size $n$ is halved at every step.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-6/day_2_1/01.py)
