# 🟢 Day 4.3 — Binary Search: Painter's Partition Problem

## 1. Painter's Partition Problem

You are given $A$ painters and an array $C$ of $N$ integers where $C[i]$ denotes the length of the $i$-th wooden board. Each painter takes $B$ units of time to paint $1$ unit of board length.

You must assign boards to painters subject to the following rules:
1. Each painter paints only a **contiguous segment** of boards.
2. No board can be split between multiple painters.
3. Every board must be painted by exactly one painter.

The goal is to **minimize the maximum time** required to paint all boards.

Return the minimum time required modulo $10000003$.

You must write an algorithm that runs in $\mathcal{O}(N \times \log(\sum(C)))$ time complexity.

### Example

```text
Input:  A = 2, B = 5, C = [1, 10]
Output: 50
Explanation:
- Painter 1 paints board 0 (length = 1), time = 1 * 5 = 5.
- Painter 2 paints board 1 (length = 10), time = 10 * 5 = 50.
Max time = max(5, 50) = 50.
50 % 10000003 = 50.

Input:  A = 10, B = 1, C = [1, 8, 11, 3]
Output: 11
Explanation:
Assign each of the 4 boards to a different painter.
Max time = max(1, 8, 11, 3) * 1 = 11.
11 % 10000003 = 11.

Input:  A = 3, B = 2, C = [5, 10, 30, 20]
Output: 60
Explanation:
One optimal assignment:
- Painter 1: [5, 10] -> length = 15
- Painter 2: [30]     -> length = 30
- Painter 3: [20]     -> length = 20
Max board length assigned = 30.
Total time = 30 * B = 30 * 2 = 60.
60 % 10000003 = 60.

Input:  A = 1, B = 3, C = [10, 20, 30]  # Edge Case: Single painter
Output: 180
Explanation:
1 painter must paint all boards (total length = 60). Time = 60 * 3 = 180.
```

### Think About

* **Structural Equivalence to Book Allocation & Split Array:**
  * Since each unit of board takes $B$ units of time for any painter, the total time for a painter painting $L$ units of board length is $L \times B$.
  * Therefore, minimizing the maximum time is equivalent to **minimizing the maximum total board length assigned to any single painter**.
  * Once the minimal maximum board length $X$ is determined, the answer is simply:
    $$\text{ans} = (X \times B) \pmod{10000003}$$

* **The Monotonicity Principle (Binary Search on Answers):**
  * Let $X$ be a candidate upper limit on the board length assigned to any painter.
  * As $X$ **increases**, each painter can take on more board length, requiring **fewer or equal painters**.
  * If all boards can be painted using $\le A$ painters with ceiling $X$, then any ceiling $> X$ is also feasible.
  * If ceiling $X$ requires $> A$ painters, any smaller ceiling will also fail.
  * This monotonicity allows binary search on $X$!

* **Search Space Boundaries for $X$:**
  * **Lower bound (`low = max(C)`):** At least one painter must paint the longest single board. No painter can be assigned less than $\max(C)$ if that board is to be painted without splitting.
  * **Upper bound (`high = sum(C)`):** If only $1$ painter were assigned to paint all $N$ boards.
  * Search space range: $[\max(C), \sum(C)]$.

* **Greedy Feasibility Simulation (`canPaint`):**
  * Given a limit `mid`:
    * Start with `painters = 1` and `current_length = 0`.
    * Walk through boards $C[i]$:
      * If `current_length + C[i] > mid`:
        * Allocate to a new painter: `painters += 1`, `current_length = C[i]`.
        * If `painters > A`, return `False` immediately.
      * Else:
        * `current_length += C[i]`.
    * Return `True` if `painters <= A`.

* **Step-by-Step Binary Search Algorithm:**
  1. Set `low = max(C)`, `high = sum(C)`, `ans = high`.
  2. While `low <= high`:
     * `mid = low + (high - low) // 2`.
     * If `canPaint(C, A, mid)`:
       * Feasible with $\le A$ painters! Record candidate: `ans = mid`.
       * Try finding a smaller maximum length: `high = mid - 1`.
     * Else:
       * Requires more than $A$ painters; limit is too tight: `low = mid + 1`.
  3. Calculate `(ans * B) % 10000003` and return.

* **Time Complexity:** $\mathcal{O}(N \times \log(\sum(C)))$
  * Binary search takes $\mathcal{O}(\log(\sum(C)))$ steps.
  * In each step, we iterate through the $N$ boards in $\mathcal{O}(N)$ time.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-6/day_4_3/01.py)

