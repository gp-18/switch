# 🟢 Day 3.2 — Binary Search: Minimum Days to Make M Bouquets

## 1. Minimum Days to Make M Bouquets

Given $n$ roses and an array `nums` where `nums[i]` denotes that the $i$-th rose will bloom on the `nums[i]`-th day.

Only **adjacent bloomed roses** can be picked to make a bouquet. Exactly $k$ adjacent bloomed roses are required to make a single bouquet.

Find the **minimum number of days** required to make at least $m$ bouquets, each containing $k$ roses. Return `-1` if it is impossible to make $m$ bouquets.

You must write an algorithm that runs in $\mathcal{O}(N \times \log(\max(nums) - \min(nums) + 1))$ time complexity.

### Example

```text
Input:  n = 8, nums = [7, 7, 7, 7, 13, 11, 12, 7], m = 2, k = 3
Output: 12
Explanation:
On day 12, roses with bloom day <= 12 have bloomed:
Bloom status: [7(Y), 7(Y), 7(Y), 7(Y), 13(N), 11(Y), 12(Y), 7(Y)]
- First 3 roses [7, 7, 7] make bouquet 1.
- Rose at index 3 is bloomed, but broken by index 4 (blooms on day 13).
- Last 3 roses [11, 12, 7] make bouquet 2.
Total = 2 bouquets formed <= 12 days. Minimum day = 12.

Input:  n = 5, nums = [1, 10, 3, 10, 2], m = 3, k = 2
Output: -1
Explanation:
To make 3 bouquets of 2 flowers each, we need at least 3 * 2 = 6 flowers.
Since we only have 5 flowers in total (n = 5), it is impossible. Return -1.

Input:  n = 5, nums = [1, 10, 3, 10, 2], m = 3, k = 1
Output: 3
Explanation:
Each bouquet requires k = 1 rose.
On day 3, flowers at indices 0, 2, 4 have bloomed (nums = 1, 3, 2 <= 3).
We have 3 bloomed flowers, giving 3 bouquets. Output = 3.

Input:  n = 5, nums = [1, 2, 3, 4, 5], m = 1, k = 5  # Edge Case: All flowers needed
Output: 5
Explanation:
To get 5 adjacent bloomed roses, all flowers must bloom, which happens on day 5.
```

### Think About

* **Impossible Edge Case ($m \times k > n$):**
  * To make $m$ bouquets of $k$ roses each, you need at least $m \times k$ flowers.
  * If $m \times k > n$, even if all flowers bloom, you will never have enough roses. Immediately return `-1`.
  * *Note for typed languages (C++/Java):* $m \times k$ can equal $10^6 \times 10^5 = 10^{11} > 2^{31} - 1$. Use a 64-bit integer (`long long`) to prevent overflow during multiplication.

* **The Monotonicity Principle (Binary Search on Answers):**
  * As the days increase, more flowers bloom and previously bloomed flowers never un-bloom.
  * Consequently, the number of bouquets that can be formed on day $D$ is a **monotonically non-decreasing** function of $D$:
    $$D_1 < D_2 \implies \text{Bouquets}(D_1) \le \text{Bouquets}(D_2)$$
  * If it is possible to make $m$ bouquets on day $D$, it is guaranteed to be possible on any day $> D$.
  * Our objective is to find the **smallest (earliest) day** $D$ such that $\text{Bouquets}(D) \ge m \implies$ **Binary Search!**

* **Search Space Boundaries:**
  * **Lower bound (`low = min(nums)`):** No flower can bloom before day $\min(nums)$.
  * **Upper bound (`high = max(nums)`):** On day $\max(nums)$, every flower in the garden has bloomed, providing the maximum possible number of bouquets.
  * Search space range: $[\min(nums), \max(nums)]$.

* **Greedy Counting of Adjacent Bloomed Roses:**
  * To check if $m$ bouquets can be formed on day `mid`:
    * Maintain a running count `consecutive = 0` and `bouquets = 0`.
    * Traverse `nums`:
      * If `bloom_day <= mid`:
        * `consecutive += 1`
        * If `consecutive == k`:
          * `bouquets += 1`
          * `consecutive = 0` (greedily form the bouquet and start fresh).
      * Else (`bloom_day > mid`):
        * The flower has not bloomed yet, breaking the contiguous chain: reset `consecutive = 0`.
    * Return `True` if `bouquets >= m`, else `False`.

* **Step-by-Step Binary Search Algorithm:**
  1. Check if $m \times k > n$: return `-1`.
  2. Set `low = min(nums)`, `high = max(nums)`, `ans = -1`.
  3. While `low <= high`:
     * `mid = low + (high - low) // 2`.
     * Check if day `mid` can form $\ge m$ bouquets.
     * **If feasible (`bouquets >= m`):**
       * Record candidate: `ans = mid`.
       * Search for an earlier day on the left: `high = mid - 1`.
     * **Else (`bouquets < m`):**
       * Not enough flowers bloomed yet: `low = mid + 1`.
  4. Return `ans`.

* **Time Complexity:** $\mathcal{O}(N \times \log(\max(nums) - \min(nums) + 1))$
  * Binary search takes $\mathcal{O}(\log(\text{range}))$ iterations where $\text{range} \le 10^9$ ($\approx 30$ steps).
  * In each iteration, we make one linear pass over the array of size $N$ ($\mathcal{O}(N)$).
  * Total time: $\mathcal{O}(N \times \log(\text{range}))$. For $N = 10^5$, operations $\approx 3 \times 10^6$, running in under $0.05$ seconds.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-6/day_3_2/01.py)

