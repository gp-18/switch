# 🟢 Day 4.4 — Binary Search: Aggressive Cows

## 1. Aggressive Cows

Given an array `nums` of size $n$, which denotes the 1D coordinates of stalls, and an integer $k$, which denotes the number of aggressive cows.

Assign stalls to $k$ cows such that the **minimum distance between any two cows is as large as possible** (maximize the minimum distance).

Find the **maximum possible minimum distance**.

You must write an algorithm that runs in $\mathcal{O}(N \log N + N \times \log(\max(nums) - \min(nums)))$ time complexity.

### Example

```text
Input:  n = 6, k = 4, nums = [0, 3, 4, 7, 10, 9]
Output: 3
Explanation:
Sorted stall positions: [0, 3, 4, 7, 9, 10].
Place 4 cows at positions: [0, 3, 7, 10].
Distances between consecutive cows:
- 3 - 0 = 3
- 7 - 3 = 4
- 10 - 7 = 3
The minimum distance is min(3, 4, 3) = 3.
It is impossible to place 4 cows such that all pairwise distances are >= 4.
The maximum possible minimum distance is 3.

Input:  n = 5, k = 2, nums = [4, 2, 1, 3, 6]
Output: 5
Explanation:
Sorted stalls: [1, 2, 3, 4, 6].
Place 2 cows at the two extreme stalls [1, 6].
The distance between them is 6 - 1 = 5.

Input:  n = 5, k = 3, nums = [10, 1, 2, 7, 5]
Output: 4
Explanation:
Sorted stalls: [1, 2, 5, 7, 10].
Place 3 cows at [1, 5, 10].
Distances: 5 - 1 = 4, 10 - 5 = 5. Minimum distance = 4.

Input:  n = 2, k = 2, nums = [1, 100]  # Edge Case: 2 cows at extremes
Output: 99
Explanation:
Distance = 100 - 1 = 99.
```

### Think About

* **Why Sorting the Stalls is Necessary:**
  * The problem requires placing cows along a coordinate line such that all pairwise distances between placed cows are $\ge D$.
  * If the stalls are sorted in non-decreasing order:
    $$nums[0] \le nums[1] \le \dots \le nums[n - 1]$$
    then if each cow placed is at least $D$ units away from the immediately preceding placed cow, it is automatically at least $D$ units away from all earlier cows!
  * Sorting takes $\mathcal{O}(N \log N)$ time and enables greedy left-to-right placement.

* **Minimax Monotonicity (Binary Search on Answers):**
  * Let $D$ be a candidate minimum distance between any two cows.
  * If we **can** place $k$ cows with pairwise distance $\ge D$, then we can also easily place them with any smaller distance $D' < D$.
  * If we **cannot** place $k$ cows with distance $\ge D$, it is impossible to place them with any larger distance $D' > D$.
  * The feasibility predicate is monotonic:
    $$\underbrace{[\text{True}, \text{True}, \dots, \text{True}}_{\text{Feasible distances } \le D^*}, \underbrace{\text{False}, \text{False}, \dots]}_{\text{Infeasible distances } > D^*}$$
  * We want to find the **largest** feasible distance $D^* \implies$ **Binary Search!**

* **Search Space Boundaries:**
  * **Lower bound (`low = 1`):** Minimum possible distance between distinct stalls.
  * **Upper bound (`high = nums[-1] - nums[0]`):** The maximum distance between the first and last stall in the sorted array.
  * Range: $[1, nums[-1] - nums[0]]$.

* **Greedy Placement Check (`canWePlace(nums, dist, cows)`):**
  * To test if separation `dist` is feasible:
    1. Place the first cow at the first stall: `cntCows = 1`, `last = nums[0]`.
    2. Traverse the remaining stalls $i = 1, \dots, n - 1$:
       * If $nums[i] - last \ge dist$:
         * Place the next cow here: `cntCows += 1`, `last = nums[i]`.
         * If `cntCows >= cows`, return `True`.
    3. If traversal finishes and fewer than $k$ cows were placed, return `False`.

* **Step-by-Step Binary Search Algorithm:**
  1. Sort `nums` in ascending order.
  2. Set `low = 1`, `high = nums[-1] - nums[0]`.
  3. While `low <= high`:
     * `mid = low + (high - low) // 2`.
     * If `canWePlace(nums, mid, k)`:
       * Feasible! We can try for an even larger distance:
       * Eliminate left half: `low = mid + 1`.
     * Else:
       * Too far apart, cows don't fit:
       * Eliminate right half: `high = mid - 1`.
  4. At loop termination (`low > high`), `high` points to the maximum feasible distance. Return `high`.

* **Time Complexity:** $\mathcal{O}(N \log N + N \times \log(\max(nums) - \min(nums)))$
  * Sorting takes $\mathcal{O}(N \log N)$.
  * Binary search takes $\mathcal{O}(\log(\text{range}))$ iterations, each making an $\mathcal{O}(N)$ linear scan.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space beyond sorting.

**File:** [01.py](../../code/sprint-6/day_4_4/01.py)

