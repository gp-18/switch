# 🟢 Day 2.3 — Binary Search: Find the Smallest Divisor Given a Threshold

## 1. Find the Smallest Divisor Given a Threshold

Given an array of integers `nums` and an integer `limit` as a threshold value, find the **smallest positive integer divisor** such that upon dividing all elements of `nums` by this divisor and taking the ceiling of each division result, the total sum is less than or equal to `limit`.

$$\sum_{i=0}^{n-1} \left\lceil \frac{nums[i]}{\text{divisor}} \right\rceil \le limit$$

If no such divisor exists (e.g. `len(nums) > limit`), return `-1`.

### Example

```text
Input:  nums = [1, 2, 3, 4, 5], limit = 8
Output: 3
Explanation:
- Divisor 1: 1 + 2 + 3 + 4 + 5 = 15 > 8
- Divisor 2: 1 + 1 + 2 + 2 + 3 = 9 > 8
- Divisor 3: 1 + 1 + 1 + 2 + 2 = 7 <= 8
3 is the smallest divisor satisfying the threshold.

Input:  nums = [8, 4, 2, 3], limit = 10
Output: 2
Explanation:
- Divisor 1: 8 + 4 + 2 + 3 = 17 > 10
- Divisor 2: 4 + 2 + 1 + 2 = 9 <= 10
Output = 2.

Input:  nums = [8, 4, 2, 3], limit = 4
Output: 8
Explanation:
At divisor 8: ceil(8/8) + ceil(4/8) + ceil(2/8) + ceil(3/8) = 1 + 1 + 1 + 1 = 4 <= 4.

Input:  nums = [1, 2, 3], limit = 2  # Edge Case: limit < len(nums)
Output: -1
Explanation: Even with infinite divisor, minimum sum is 1 + 1 + 1 = 3 > 2. Impossible, return -1.
```

### Think About

* **The Monotonicity Principle (Binary Search on Answers):**
  * As the divisor $d$ **increases**, each term $\lceil nums[i] / d \rceil$ **decreases or stays the same**.
  * Consequently, the total sum is a **monotonically non-increasing** function with respect to $d$:
    $$d_1 < d_2 \implies \text{TotalSum}(d_1) \ge \text{TotalSum}(d_2)$$
  * If a divisor $d$ yields a sum $\le limit$, then all divisors $> d$ will also satisfy the condition.
  * Our objective is to find the **smallest** such divisor $\implies$ binary search!

* **Search Space Boundaries:**
  * **Lower bound (`low = 1`):** The smallest possible positive divisor is $1$.
  * **Upper bound (`high = max(nums)`):** Dividing by $\max(nums)$ turns every element into $1$, yielding the absolute minimum possible sum equal to $N = len(nums)$.
  * **Edge check:** If $N > limit$, return `-1` immediately because the minimum possible sum is $N$.

* **Step-by-Step Binary Search:**
  1. Initialize `low = 1`, `high = max(nums)`, `ans = -1`.
  2. While `low <= high`:
     * Calculate `mid = low + (high - low) // 2`.
     * Compute total sum of $\lceil nums[i] / mid \rceil$.
     * **Condition: `total_sum <= limit`**
       * `mid` is a valid divisor!
       * Record candidate: `ans = mid`.
       * Since we want the **smallest** divisor, search left: `high = mid - 1`.
     * **Condition: `total_sum > limit`**
       * The sum is too large; we need a larger divisor to decrease the sum: `low = mid + 1`.
  3. Return `ans` (or `low`).

* **Integer Math for Ceiling Division (Interview Tip):**
  * In Python, instead of `math.ceil(num / mid)` (which incurs floating-point operations), use pure integer arithmetic:
    $$\left\lceil \frac{a}{b} \right\rceil = \frac{a + b - 1}{b} = (a + b - 1) // b$$
  * This is faster, exact, and prevents precision errors with large numbers.

* **Time Complexity:** $\mathcal{O}(N \times \log(\max(nums)))$
  * Range size is $\max(nums)$, giving $\log(\max(nums))$ binary search steps.
  * In each step, we iterate through the array of length $N$ to compute the sum.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-6/day_2_3/01.py)
