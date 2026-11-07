# 🟢 Day 4.1 — Binary Search: Capacity to Ship Packages Within D Days

## 1. Capacity to Ship Packages Within D Days

You are given an array `weights` where `weights[i]` represents the weight of the $i$-th package on a conveyor belt. All the packages must be shipped in the order given from one port to another within `days` days.

Each day, the ship can carry a contiguous sequence of packages, as long as the total weight does not exceed its maximum capacity.

Your task is to find the **minimum possible capacity** of the ship so that all packages can be shipped within the given number of `days`.

You must write an algorithm that runs in $\mathcal{O}(N \times \log(\sum(weights) - \max(weights)))$ time complexity.

### Example

```text
Input:  weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days = 5
Output: 15
Explanation:
Minimum ship capacity = 15. One way to ship all packages in 5 days:
- Day 1: 1 + 2 + 3 + 4 + 5 = 15
- Day 2: 6 + 7 = 13
- Day 3: 8
- Day 4: 9
- Day 5: 10
No day exceeds capacity 15 and all packages are shipped in order in 5 days.

Input:  weights = [3, 2, 2, 4, 1, 4], days = 3
Output: 6
Explanation:
One possible division with capacity 6:
- Day 1: 3 + 2 = 5
- Day 2: 2 + 4 = 6
- Day 3: 1 + 4 = 5
All packages shipped in order within 3 days.

Input:  weights = [10, 50, 50, 10], days = 2
Output: 60
Explanation:
- Day 1: 10 + 50 = 60
- Day 2: 50 + 10 = 60
Total days = 2 <= 2. Capacity = 60.

Input:  weights = [1, 2, 3, 1, 1], days = 4  # Edge Case: days close to len(weights)
Output: 3
Explanation:
Day 1: 1+2=3, Day 2: 3, Day 3: 1, Day 4: 1.
```

### Think About

* **The Monotonicity Principle (Binary Search on Answers):**
  * As the ship's capacity $C$ **increases**, the number of days required to transport all packages **decreases or stays the same**.
  * Consequently, the required days is a **monotonically non-increasing** function of capacity:
    $$C_1 < C_2 \implies \text{Days}(C_1) \ge \text{Days}(C_2)$$
  * If a capacity $C$ allows us to finish within `days` days, any larger capacity will also succeed.
  * If a capacity $C$ fails, any smaller capacity will also fail.
  * Our objective is to find the **smallest** valid capacity $C$ $\implies$ **Binary Search!**

* **Search Space Boundaries:**
  * **Lower bound (`low = max(weights)`):** The ship must at least be able to carry the heaviest individual package. If capacity is less than $\max(weights)$, that package could never be loaded.
  * **Upper bound (`high = sum(weights)`):** In the extreme case of $days = 1$, the ship must transport all packages together in a single day.
  * Thus, the search space is strictly $[\max(weights), \sum(weights)]$.

* **Greedy Feasibility Simulation (`canShip`):**
  * For a candidate capacity `mid`:
    * Start on Day 1 with `curr_load = 0` and `required_days = 1`.
    * Traverse `weights` sequentially:
      * If `curr_load + w > mid`:
        * Package `w` cannot fit today. Start a new day: `required_days += 1`, `curr_load = w`.
      * Else:
        * Pack it onto the current day: `curr_load += w`.
    * If `required_days <= days`, capacity `mid` is feasible.

* **Step-by-Step Binary Search Algorithm:**
  1. Set `low = max(weights)`, `high = sum(weights)`, `ans = high`.
  2. While `low <= high`:
     * `mid = low + (high - low) // 2`.
     * If `canShip(weights, days, mid)` is `True`:
       * `mid` is sufficient! Record `ans = mid`.
       * Search for a smaller capacity on the left: `high = mid - 1`.
     * Else:
       * Capacity `mid` is too small, need more capacity: `low = mid + 1`.
  3. Return `ans` (or `low`).

* **Time Complexity:** $\mathcal{O}(N \times \log(\sum(weights) - \max(weights)))$
  * Range size is at most $\sum(weights) \le 500 \times (5 \times 10^4) = 2.5 \times 10^7$.
  * Binary search takes $\approx \log_2(2.5 \times 10^7) \approx 25$ iterations.
  * Each iteration scans the $N$ packages in $\mathcal{O}(N)$ time.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-6/day_4_1/01.py)

