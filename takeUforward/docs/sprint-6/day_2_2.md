# 🟢 Day 2.2 — Binary Search: Find Nth Root of a Number

## 1. Find Nth Root of a Number

Given two positive integers $N$ and $M$, find the $N$-th root of $M$.

The $N$-th root of a number $M$ is defined as an integer $X$ such that:
$$X^N = M$$

* If the $N$-th root is an exact integer, return $X$.
* If the $N$-th root is not an integer, return `-1`.

You must write an algorithm that runs in $\mathcal{O}(\log M \times \log N)$ time.

### Example

```text
Input:  N = 3, M = 27
Output: 3
Explanation: 3^3 = 27, so the 3rd root of 27 is 3.

Input:  N = 4, M = 69
Output: -1
Explanation: 2^4 = 16 and 3^4 = 81. No integer X satisfies X^4 = 69. Return -1.

Input:  N = 4, M = 81
Output: 3
Explanation: 3^4 = 81. Return 3.

Input:  N = 1, M = 14  # Edge Case: N = 1
Output: 14
Explanation: 14^1 = 14. Return 14.

Input:  N = 5, M = 1   # Edge Case: M = 1
Output: 1
Explanation: 1^5 = 1. Return 1.
```

### Think About

* **Binary Search on Monotonic Search Space:**
  * For $N \ge 1$, the function $f(X) = X^N$ is strictly increasing.
  * The potential integer root must lie in the range:
    $$1 \le X \le M$$
  * Thus, we can apply binary search over the range `[1, M]`.

* **The Overflow Danger & Early Stopping Helper Function:**
  * If $N = 30$ and $mid = 100$, computing $100^{30}$ exceeds $10^{60}$, causing integer overflow in most programming languages or redundant computations.
  * We use a helper function `powerCheck(mid, n, m)` that computes $mid^N$ via **Exponentiation by Squaring** with early stopping:
    * If at any point the running product exceeds $M$, immediately stop and return `2` (indicating $mid^N > M$).
    * If the final product equals $M$, return `1` ($mid^N == M$).
    * If the final product is less than $M$, return `0` ($mid^N < M$).

* **Binary Search Algorithm:**
  1. `low = 1, high = M`.
  2. While `low <= high`:
     * `mid = low + (high - low) // 2`.
     * `status = powerCheck(mid, N, M)`
     * If `status == 1`: exact root found! Return `mid`.
     * If `status == 0`: $mid^N < M$, root must be larger $\rightarrow$ search right: `low = mid + 1`.
     * If `status == 2`: $mid^N > M$, root must be smaller $\rightarrow$ search left: `high = mid - 1`.
  3. If loop ends without returning, no integer root exists $\rightarrow$ return `-1`.

* **Time Complexity:** $\mathcal{O}(\log M \times \log N)$
  * The outer binary search takes $\mathcal{O}(\log M)$ iterations.
  * The binary exponentiation helper function takes $\mathcal{O}(\log N)$ operations with early cutoff.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-6/day_2_2/01.py)
