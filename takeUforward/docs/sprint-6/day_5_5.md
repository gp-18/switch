# 🟢 Day 5.5 — Binary Search: Minimize Max Distance to Gas Station

## 1. Minimize Max Distance to Gas Station

Given a sorted array `arr` of size $n$, containing the integer coordinates of $n$ gas stations on the X-axis, and an integer $k$.

Place $k$ new gas stations anywhere on the non-negative X-axis (including non-integer coordinates).

Let `dist` be the maximum distance between adjacent gas stations after adding the $k$ new gas stations.

Find the **minimum possible value of `dist`**.

Answers within $10^{-6}$ of the true value will be accepted.

You must write an algorithm that runs in $\mathcal{O}(N \times \log(\frac{\max(dist)}{10^{-6}}))$ time complexity.

### Example

```text
Input:  n = 10, arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 10
Output: 0.50000
Explanation:
Initial stations are at coordinates 1 to 10 (each adjacent distance is 1.0).
Placing 10 new gas stations at [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]
halves every segment, making the maximum distance between adjacent stations 0.5.

Input:  n = 10, arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 1
Output: 1.00000
Explanation:
With only 1 station to place, we can reduce at most one gap of 1.0 to 0.5,
but all other 8 gaps remain 1.0. The maximum distance remains 1.0.

Input:  n = 10, arr = [3, 6, 12, 19, 33, 44, 67, 72, 89, 95], k = 2
Output: 14.00000
Explanation:
The largest gaps are 23 (between 44 and 67) and 17 (between 72 and 89).
Placing 2 stations strategically yields a minimum maximum distance of 14.00000.

Input:  n = 5, arr = [1, 2, 3, 4, 5], k = 4  # Edge Case
Output: 0.50000
```

### Think About

* **Binary Search on Continuous (Decimal) Answer Space:**
  * Unlike standard binary search on integers, the answer here is a real number (float).
  * **Search Range:**
    * $\text{low} = 0.0$ (minimum theoretical distance if infinitely many stations were placed).
    * $\text{high} = \max_{i=0}^{n-2}(arr[i+1] - arr[i])$ (the largest gap between any two adjacent initial stations).
  * **Precision Termination Condition:**
    * Since answers within $10^{-6}$ are accepted, loop condition is:
      $$\text{while } (high - low) > 10^{-6}:$$
  * **Continuous Bound Adjustments:**
    * Instead of `low = mid + 1` or `high = mid - 1` (which would skip continuous decimal values), update:
      * `low = mid` (when `mid` requires too many stations)
      * `high = mid` (when `mid` is achievable)

* **Greedy Feasibility Check (`numberOfGasStationsRequired`):**
  * For each adjacent gap $\text{gap} = arr[i] - arr[i - 1]$:
    * To ensure every sub-segment in this gap has length $\le dist$, how many stations must be inserted?
    * $\text{stations\_needed} = \lfloor \frac{\text{gap}}{dist} \rfloor$.
    * **Boundary adjustment:** If $\text{gap}$ is an exact multiple of $dist$ (e.g. $\text{gap} = 4.0, dist = 2.0$), dividing by $dist$ gives $2$, but placing only $1$ station in the middle splits it into $[0..2]$ and $[2..4]$ (both length $\le 2.0$). Thus:
      $$\text{if } gap == dist \times \text{stations\_needed}: \quad \text{stations\_needed} -= 1$$
    * Accumulate $\text{stations\_needed}$ across all $n - 1$ gaps.
  * If $\text{total\_stations} \le k$:
    * Distance `mid` is feasible! We can try to achieve an even smaller distance $\rightarrow high = mid$.
  * Else ($\text{total\_stations} > k$):
    * Distance `mid` is too small (requires more than $k$ stations) $\rightarrow low = mid$.

* **Time Complexity:** $\mathcal{O}(N \times \log(\frac{\max(dist)}{10^{-6}}))$
  * For $\max(dist) \le 10^9$, $\log_2(10^{15}) \approx 50$ iterations.
  * Each iteration scans the $N$ stations in $\mathcal{O}(N)$ time.
  * Total operations: $\approx 50 \times N \le 2.5 \times 10^5$, executing in milliseconds.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-6/day_5_5/01.py)

