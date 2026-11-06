# 🟢 Day 3.1 — Binary Search: Koko Eating Bananas

## 1. Koko Eating Bananas

A monkey is given $n$ piles of bananas, where the $i$-th pile has `nums[i]` bananas. An integer $h$ represents the total time in hours available to eat all the bananas.

Each hour, the monkey chooses a single non-empty pile of bananas and eats $k$ bananas from it. If the pile contains fewer than $k$ bananas, she eats all the bananas in that pile and does not consume any more bananas during that hour.

Determine the **minimum integer rate $k$** (bananas per hour) such that Koko can eat all the bananas within $h$ hours.

$$\sum_{i=0}^{n-1} \left\lceil \frac{nums[i]}{k} \right\rceil \le h$$

You must write an algorithm that runs in $\mathcal{O}(N \times \log(\max(nums)))$ time complexity.

### Example

```text
Input:  nums = [7, 15, 6, 3], h = 8
Output: 5
Explanation:
- Rate 5 bananas/hr: ceil(7/5) + ceil(15/5) + ceil(6/5) + ceil(3/5) = 2 + 3 + 2 + 1 = 8 hours <= 8.
5 is the minimum rate required to finish within 8 hours.

Input:  nums = [25, 12, 8, 14, 19], h = 5
Output: 25
Explanation:
Since h = len(nums) = 5, Koko must finish each pile in exactly 1 hour.
The rate must at least equal the largest pile: max(nums) = 25.

Input:  nums = [3, 7, 6, 11], h = 8
Output: 4
Explanation:
ceil(3/4) + ceil(7/4) + ceil(6/4) + ceil(11/4) = 1 + 2 + 2 + 3 = 8 <= 8.

Input:  nums = [30], h = 5  # Edge Case: Single pile
Output: 6
Explanation:
ceil(30 / 6) = 5 <= 5.
```

### Think About

* **The Monotonicity Principle (Binary Search on Answers):**
  * As the hourly eating rate $k$ **increases**, the hours required to consume each pile $\lceil nums[i] / k \rceil$ **decreases or stays the same**.
  * Consequently, the total time required is a **monotonically non-increasing** function with respect to $k$:
    $$k_1 < k_2 \implies \text{TotalHours}(k_1) \ge \text{TotalHours}(k_2)$$
  * If an eating rate $k$ yields total hours $\le h$, then every rate $> k$ will also allow Koko to finish within $h$ hours.
  * Our objective is to find the **smallest** feasible integer rate $k$ $\implies$ binary search!

* **Search Space Boundaries:**
  * **Lower bound (`low = 1`):** Koko must eat at least $1$ banana per hour ($k \ge 1$).
  * **Upper bound (`high = max(nums)`):** If Koko eats at a rate equal to $\max(nums)$, she consumes every pile in exactly $1$ hour, finishing all piles in $N$ hours. Since $n \le h$, she can never need a rate higher than $\max(nums)$ because she cannot eat from more than one pile in a single hour.
  * Thus, the search space is strictly $[1, \max(nums)]$.

* **Step-by-Step Binary Search Algorithm:**
  1. Initialize `low = 1`, `high = max(nums)`, `ans = high`.
  2. While `low <= high`:
     * Compute `mid = low + (high - low) // 2`.
     * Calculate total hours needed at rate `mid`:
       $$\text{totalH} = \sum_{i=0}^{n-1} \left\lceil \frac{nums[i]}{mid} \right\rceil$$
     * **Condition 1: `totalH <= h`**
       * `mid` is a feasible eating rate! Koko can finish within $h$ hours.
       * Record candidate: `ans = mid`.
       * Since we want the **minimum** rate, search left: `high = mid - 1`.
     * **Condition 2: `totalH > h`**
       * Koko takes too long at rate `mid`. She must eat faster.
       * Eliminate left half: `low = mid + 1`.
  3. When the loop ends (`low > high`), return `ans` (or `low`).

* **Integer Math for Ceiling Division (Interview Tip):**
  * Instead of floating-point division `math.ceil(x / k)`, use exact integer arithmetic:
    $$\left\lceil \frac{x}{k} \right\rceil = \frac{x + k - 1}{k} = (x + k - 1) // k$$
  * This avoids floating-point precision loss with very large numbers ($10^9$) and runs faster.

* **Avoiding Integer Overflow (PBC Favorite):**
  * In statically typed languages (C++/Java), accumulating `totalH` can overflow a 32-bit signed integer when $nums[i] \approx 10^9$ and $k = 1$ ($10^4 \times 10^9 = 10^{13} > 2^{31} - 1$).
  * Use a 64-bit integer (`long long` in C++, `long` in Java) for `totalH`. In Python, integers have arbitrary precision natively.

* **Time Complexity:** $\mathcal{O}(N \times \log(\max(nums)))$
  * Binary search on the range $[1, \max(nums)]$ takes $\mathcal{O}(\log(\max(nums)))$ iterations.
  * In each iteration, we iterate through the array of length $N$ to compute total hours $\mathcal{O}(N)$.
  * Overall: $\mathcal{O}(N \times \log(\max(nums)))$.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-6/day_3_1/01.py)
