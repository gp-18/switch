# 🟢 Day 6.2 — Arrays: Largest Subarray with Sum 0 (Prefix Sum & Hash Map)

## 1. Largest Subarray with Sum 0

Given an integer array `arr` of size $n$ containing both positive and negative integers, find the length of the longest contiguous subarray with sum equal to $0$. If no such subarray exists, return $0$.

### Example

```text
Input:  arr = [15, -2, 2, -8, 1, 7, 10, 23]
Output: 5
Explanation:
The contiguous subarray [-2, 2, -8, 1, 7] has sum = -2 + 2 - 8 + 1 + 7 = 0. Its length is 5, which is the maximum among all zero-sum subarrays.

Input:  arr = [2, 10, 4]
Output: 0
Explanation:
All elements are positive; no subarray can sum to 0. Return 0.

Input:  arr = [1, 0, -4, 3, 1, 0]
Output: 5
Explanation:
The subarray [0, -4, 3, 1, 0] from index 1 to 5 sums to 0 - 4 + 3 + 1 + 0 = 0. Its length is 5.

Input:  arr = [1, -1, 3, 2, -2, 4, -4]
Output: 7
Explanation:
The entire array sums to 1 - 1 + 3 + 2 - 2 + 4 - 4 = 0. Length = 7.
```

### Think About

* **The Core Mathematical Intuition:**
  * If the cumulative sum from index $0$ to $i$ is $S$, and later at index $j$ ($j > i$) the cumulative sum is **again $S$**, what does that mean?
  * It means the elements added between index $i + 1$ and $j$ contributed a net change of $0$:
    $$\sum_{k=i+1}^{j} arr[k] = S - S = 0$$
  * Thus, whenever a prefix sum repeats, the subarray between the two occurrences sums to $0$, with length $j - i$.

* **Step-by-Step Algorithm:**
  1. Maintain a hash map `sum_map = {}` to store `{cumulative_sum: earliest_index}`.
  2. Maintain `running_sum = 0` and `max_len = 0`.
  3. Iterate through index `i` from $0$ to $n - 1$:
     * Add `arr[i]` to `running_sum`.
     * **Case 1: `running_sum == 0`**
       * The subarray from index $0$ to $i$ has sum 0.
       * `max_len = i + 1`.
     * **Case 2: `running_sum in sum_map`**
       * We saw this exact sum earlier at index `sum_map[running_sum]`.
       * The subarray between that index and `i` has sum 0:
         `max_len = max(max_len, i - sum_map[running_sum])`.
     * **Case 3: `running_sum not in sum_map`**
       * Record its earliest occurrence: `sum_map[running_sum] = i`.
       * Do **not** update if already present, to maximize future $i - \text{earliest\_index}$.

* **Connection to "Longest Subarray with Sum K":**
  * This is a special, elegant instance of the Subarray Sum $K$ problem where $k = 0$.
  * Since $k = 0$, the remaining sum condition $S - k$ simply reduces to checking if $S$ itself was seen before!

* **Time Complexity:** $\mathcal{O}(N)$ — Single pass through the array with $\mathcal{O}(1)$ average hash map operations.
* **Space Complexity:** $\mathcal{O}(N)$ auxiliary space — For storing prefix sums in the hash map.

**File:** [01.py](../../code/sprint-5/day_6_2/01.py)
