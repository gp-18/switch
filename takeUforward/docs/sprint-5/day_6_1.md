# 🟢 Day 6.1 — Arrays: Longest Subarray with Sum K (Prefix Sum & Hash Map)

## 1. Longest Subarray with Sum K

Given an array `nums` of size $n$ and an integer $k$, find the length of the longest contiguous sub-array that sums to $k$. If no such sub-array exists, return $0$.

A **sub-array** is a contiguous sequence of elements within an array.

### Example

```text
Input:  nums = [10, 5, 2, 7, 1, 9], k = 15
Output: 4
Explanation:
The longest sub-array with sum equal to 15 is [5, 2, 7, 1], which starts at index 1 and ends at index 4 (5 + 2 + 7 + 1 = 15). Length = 4.

Input:  nums = [-3, 2, 1], k = 6
Output: 0
Explanation:
There is no contiguous sub-array whose elements sum to 6. Hence, return 0.

Input:  nums = [-1, 1, 1], k = 1
Output: 3
Explanation:
The entire array [-1, 1, 1] sums to -1 + 1 + 1 = 1, giving maximum length = 3.

Input:  nums = [2, 0, 0, 3], k = 3
Output: 3
Explanation:
The longest sub-array is [0, 0, 3] from index 1 to 3 with length = 3.
```

### Think About

* **The Prefix Sum Principle:**
  * Let the cumulative running sum from index `0` up to index `i` be `current_sum`.
  * If there exists an earlier index `j` ($j < i$) where the cumulative sum was `current_sum - k`, then the sum of elements from index `j + 1` to `i` is precisely:
    $$\text{sum}(nums[j+1 \dots i]) = \text{current\_sum} - (\text{current\_sum} - k) = k$$
  * The length of this valid subarray is $i - j$.

* **Why a Hash Map is Essential:**
  * Storing each prefix sum in a hash map (`preSumMap[sum] = index`) enables instant $\mathcal{O}(1)$ average lookup to check whether `current_sum - k` has been seen before.

* **Critical Edge Case: Preserving the Earliest Index (Zero Handling):**
  * Consider `nums = [2, 0, 0, 3], k = 3`:
    * At index 0: `sum = 2` $\rightarrow$ store `{2: 0}`
    * At index 1: `sum = 2` $\rightarrow$ `sum` was already seen at index 0!
    * If we overwrite `preSumMap[2] = 1`, when we reach index 3 (`sum = 5`, `rem = 5 - 3 = 2`), we would calculate length as $3 - 1 = 2$ instead of the maximal $3 - 0 = 3$.
  * **Rule:** ONLY insert `sum` into the map if it is **not already present** (`if sum not in preSumMap: preSumMap[sum] = i`). This guarantees we always record the earliest possible index, maximizing $i - \text{first\_seen}$.

* **Two Pointers vs. Hash Map (Key Interview Distinction):**
  * **If array has ONLY positive integers ($nums[i] > 0$):**
    * Running sum is strictly monotonic.
    * A Two-Pointer / Sliding Window approach achieves $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space!
  * **If array contains negatives or zeros ($nums[i] \le 0$):**
    * The running sum increases and decreases unpredictably.
    * Sliding window fails; the **Prefix Sum + Hash Map approach is the ONLY optimal solution** ($\mathcal{O}(N)$ time, $\mathcal{O}(N)$ space).

* **Time Complexity:** $\mathcal{O}(N)$ average time — a single linear pass with $\mathcal{O}(1)$ hash map lookups.
* **Space Complexity:** $\mathcal{O}(N)$ auxiliary space — storing prefix sums in the hash map.

**File:** [01.py](../../code/sprint-5/day_6_1/01.py)
