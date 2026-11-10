# 🟢 Day 1.1 — Binary Search: Split Array - Largest Sum

## 1. Split Array - Largest Sum

Given an integer array `a` of size $n$ and an integer $k$.

Split the array `a` into **$k$ non-empty contiguous subarrays** such that the **largest sum among all subarrays is minimized**.

Return the minimized largest sum of the split.

You must write an algorithm that runs in $\mathcal{O}(N \times \log(\sum(a) - \max(a)))$ time complexity.

### Example

```text
Input:  a = [1, 2, 3, 4, 5], k = 3
Output: 6
Explanation:
The optimal way to split the array into 3 contiguous subarrays is:
[1, 2, 3] | [4] | [5]
Subarray sums are: 6, 4, 5.
The largest sum among them is max(6, 4, 5) = 6, which is the minimum possible.

Input:  a = [3, 5, 1], k = 3
Output: 5
Explanation:
The only way to split into 3 non-empty subarrays is [3], [5], [1].
The largest sum is max(3, 5, 1) = 5.

Input:  a = [1, 2, 3, 4, 5], k = 2
Output: 9
Explanation:
Optimal split: [1, 2, 3] | [4, 5] -> sums: 6 and 9. Maximum = 9.

Input:  a = [10, 20, 30], k = 1  # Edge Case: k = 1
Output: 60
Explanation:
Only 1 subarray allowed, containing all elements. Sum = 60.
```

### Think About

* **Equivalence to Book Allocation & Painter's Partition:**
  * Splitting an array of $n$ elements into $k$ contiguous non-empty subarrays to minimize the maximum subarray sum is structurally identical to allocating $n$ books to $k$ students to minimize the maximum pages per student.

* **The Monotonicity Principle (Binary Search on Answers):**
  * Let $S$ be a candidate upper limit on the sum of any subarray.
  * As $S$ **increases**, each subarray can pack more elements, requiring **fewer or equal partitions**.
  * If all elements can be partitioned into $\le k$ subarrays with limit $S$, then any limit $> S$ is also feasible (as long as $k \le n$, fewer partitions can always be split further into $k$ non-empty subarrays without increasing the max sum).
  * If limit $S$ requires $> k$ partitions, any smaller limit will also fail.
  * Our objective is to find the **smallest** valid sum limit $S$ $\implies$ **Binary Search!**

* **Search Space Boundaries:**
  * **Lower bound (`low = max(a)`):** Every element must belong to at least one subarray, so no valid split can have a maximum subarray sum smaller than the largest single element $\max(a)$.
  * **Upper bound (`high = sum(a)`):** When $k = 1$, a single subarray covers the entire array with sum $\sum(a)$.
  * Search space range: $[\max(a), \sum(a)]$.

* **Greedy Partition Simulation (`countPartitions`):**
  * Given a candidate limit `maxSum`:
    * Start with `partitions = 1` and `subarraySum = 0`.
    * Traverse `a`:
      * If `subarraySum + a[i] <= maxSum`:
        * Append `a[i]` to the current subarray: `subarraySum += a[i]`.
      * Else:
        * Start a new subarray: `partitions += 1`, `subarraySum = a[i]`.
    * Return total `partitions` formed.

* **Step-by-Step Binary Search Algorithm:**
  1. Initialize `low = max(a)`, `high = sum(a)`.
  2. While `low <= high`:
     * Compute `mid = low + (high - low) // 2`.
     * Compute `partitions = countPartitions(a, mid)`.
     * **If `partitions > k`:**
       * `mid` is too small (forces too many subarrays).
       * Increase limit: `low = mid + 1`.
     * **Else (`partitions <= k`):**
       * `mid` is feasible! Try minimizing the sum further on the left: `high = mid - 1`.
  3. Return `low` (when `low > high`, `low` points to the minimum feasible maximum sum).

* **Time Complexity:** $\mathcal{O}(N \times \log(\sum(a) - \max(a)))$
  * Binary search reduces the range $[\max(a), \sum(a)]$ in logarithmic steps.
  * In each iteration, `countPartitions` performs one linear pass of $\mathcal{O}(N)$.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-7/day_1_1/01.py)
