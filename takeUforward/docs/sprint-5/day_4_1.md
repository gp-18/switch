# 🟢 Day 4 — Arrays: Maximum Product Subarray (Prefix-Suffix & Modified Kadane)

## 1. Maximum Product Subarray

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest product, and return that product.

A **subarray** is a contiguous non-empty sequence of elements within an array.

### Example

```text
Input:  nums = [4, 5, 3, 7, 1, 2]
Output: 840
Explanation: All numbers are positive; the maximum product is the product of the entire array: 4 * 5 * 3 * 7 * 1 * 2 = 840.

Input:  nums = [-5, 0, -2]
Output: 0
Explanation: The largest product is 0, formed by subarrays [0], [-5, 0], [0, -2], or [-5, 0, -2].

Input:  nums = [1, -2, 3, 4, -4, -3]
Output: 144
Explanation:
There are 3 negative numbers (odd count). To maximize product, exclude the first negative number (-2):
Subarray [3, 4, -4, -3] yields: 3 * 4 * (-4) * (-3) = 144.

Input:  nums = [-2]  # Edge Case: Single negative element
Output: -2
Explanation: The only possible subarray is [-2] with product = -2.
```

### Think About

* **Why Kadane's Algorithm for Maximum Sum Fails Directly for Maximum Product:**
  * In maximum subarray sum, adding a negative number always diminishes the sum, so we simply discard negative running sums by resetting to 0.
  * In multiplication, signs flip! A large negative product multiplied by another negative number becomes a **huge positive product**. Therefore, a minimum running product can instantly become the maximum running product upon encountering another negative value.

* **Key Mathematical Properties of Multiplication in Arrays:**
  1. **All positive elements:** The maximum product is simply the product of the entire array.
  2. **Even count of negative numbers:** Negative signs cancel in pairs $(- \times - = +)$, so the product of the entire array is positive and maximal.
  3. **Odd count of negative numbers:** One negative number must be left out to obtain a positive product. Since the subarray must remain contiguous, the excluded negative number must be either:
     * The **first negative number from the left** (leaving a suffix subarray), OR
     * The **last negative number from the right** (leaving a prefix subarray).
     * Therefore, the optimal subarray is guaranteed to be either a **prefix product** or a **suffix product** of the array!
  4. **Zeros in the array:** Multiplication by 0 resets the running product. Zeros act as subarray splitters. Whenever a running product becomes 0, reset it to 1 to begin considering a fresh contiguous subarray.

* **Optimal Approach 1: Prefix & Suffix Two-Way Traversal ($\mathcal{O}(N)$ Time, $\mathcal{O}(1)$ Space):**
  * Maintain two running products:
    * `prefix`: accumulates products from left to right (`nums[i]`).
    * `suffix`: accumulates products from right to left (`nums[n - i - 1]`).
  * In a single loop from `i = 0` to `n - 1`:
    * If `prefix == 0`: reset `prefix = 1` (starting past a zero boundary).
    * If `suffix == 0`: reset `suffix = 1` (starting past a zero boundary).
    * `prefix *= nums[i]`
    * `suffix *= nums[n - i - 1]`
    * `ans = max(ans, prefix, suffix)`
  * Return `ans`.

* **Optimal Approach 2: Modified Kadane (Tracking `max_prod` & `min_prod`):**
  * Maintain `cur_max` and `cur_min` initialized to `nums[0]`.
  * For each subsequent element `num`:
    * If `num < 0`: swap `cur_max` and `cur_min`.
    * `cur_max = max(num, cur_max * num)`
    * `cur_min = min(num, cur_min * num)`
    * `ans = max(ans, cur_max)`
  * Also runs in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

* **Interview Follow-Up (Printing the Subarray):**
  * By tracking the start and end indices whenever `ans` is updated during the prefix or suffix pass, the actual subarray yielding the maximum product can be retrieved without additional asymptotic cost.

* **Time Complexity:** $\mathcal{O}(N)$ — A single linear scan through the array of length $N$.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space — Only constant scalar variables (`prefix`, `suffix`, `ans`).

**File:** [01.py](../../code/sprint-5/day_4_1/01.py)
