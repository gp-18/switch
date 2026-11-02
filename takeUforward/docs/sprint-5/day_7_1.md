# 🟢 Day 7.1 — Binary Search: Upper Bound (Smallest Index with Element $> X$)

## 1. Upper Bound

Given a sorted array `nums` of size $n$ and an integer `x`, write a program to find the **upper bound** of `x`.

The **upper bound** is defined as the first and smallest index `i` in `nums` such that:
$$nums[i] > x$$

* If no such index exists (i.e., all elements are $\le x$), return the size of the array $n$.

### Example

```text
Input:  nums = [1, 2, 2, 3], x = 2
Output: 3
Explanation:
Index 3 is the smallest index such that nums[3] > 2 (nums[3] = 3 > 2).

Input:  nums = [3, 5, 8, 15, 19], x = 9
Output: 3
Explanation:
Index 3 is the smallest index such that nums[3] > 9 (nums[3] = 15 > 9).

Input:  nums = [3, 5, 8, 15, 19], x = 3
Output: 1
Explanation:
nums[1] = 5 > 3, which is at index 1.

Input:  nums = [1, 2, 3], x = 5  # Edge Case: x is greater than or equal to all elements
Output: 3
Explanation:
No element is strictly greater than 5. Return n = 3.
```

### Think About

* **Lower Bound vs. Upper Bound (The Defining Difference):**
  * **Lower Bound:** Smallest index `i` where $nums[i] \ge x$ (greater than or equal).
  * **Upper Bound:** Smallest index `i` where $nums[i] > x$ (strictly greater).
  * Example on `nums = [1, 2, 2, 3]` with `x = 2`:
    * Lower bound is index `1` (`nums[1] = 2 >= 2`).
    * Upper bound is index `3` (`nums[3] = 3 > 2`).

* **Binary Search Algorithm:**
  1. Initialize `low = 0`, `high = n - 1`.
  2. Initialize `ans = n` (default if no element is strictly greater than $x$).
  3. While `low <= high`:
     * Calculate `mid = low + (high - low) // 2`.
     * **Condition: `nums[mid] > x`**
       * `nums[mid]` is strictly greater than $x$, so `mid` is a valid candidate for upper bound!
       * Record candidate: `ans = mid`.
       * Since we want the **smallest** index, eliminate the right half and search left: `high = mid - 1`.
     * **Condition: `nums[mid] <= x`**
       * `nums[mid]` is less than or equal to $x$, so neither `mid` nor any element to its left can be strictly greater than $x$.
       * Eliminate left half: `low = mid + 1`.
  4. Return `ans`.

* **Standard Library Equivalents:**
  * **Python:** `bisect.bisect_right(nums, x)`
  * **C++:** `std::upper_bound(nums.begin(), nums.end(), x) - nums.begin()`

* **Time Complexity:** $\mathcal{O}(\log N)$ — Search space is halved in every step.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space — Only constant pointer variables used.

**File:** [01.py](../../code/sprint-5/day_7_1/01.py)
