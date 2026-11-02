# 🟢 Day 6.6 — Binary Search: Lower Bound (Smallest Index with Element $\ge X$)

## 1. Lower Bound

Given a sorted array `nums` of size $n$ and an integer `x`, write a program to find the **lower bound** of `x`.

The **lower bound** algorithm finds the first and smallest index in a sorted array where the value at that index is **greater than or equal to** $x$ (i.e. $nums[index] \ge x$).

* If no such index exists (all elements are strictly smaller than $x$), return the size of the array $n$.

### Example

```text
Input:  nums = [1, 2, 2, 3], x = 2
Output: 1
Explanation:
Index 1 is the smallest index such that nums[1] >= 2.

Input:  nums = [3, 5, 8, 15, 19], x = 9
Output: 3
Explanation:
Index 3 is the smallest index such that nums[3] >= 9 (nums[3] = 15 >= 9).

Input:  nums = [3, 5, 8, 15, 19], x = 3
Output: 0
Explanation:
nums[0] = 3 >= 3, which is at index 0.

Input:  nums = [1, 3, 5, 7], x = 10  # Edge Case: x is greater than all elements
Output: 4
Explanation:
No element is >= 10. Return the length of the array n = 4.
```

### Think About

* **Difference between Binary Search, Lower Bound, and Upper Bound:**
  * **Standard Binary Search:** Looks for exact match $nums[mid] == x$.
  * **Lower Bound:** Looks for the smallest index where $nums[mid] \ge x$.
  * **Upper Bound:** Looks for the smallest index where $nums[mid] > x$.

* **Step-by-Step Binary Search Adaptation:**
  1. Initialize `low = 0`, `high = n - 1`.
  2. Initialize `ans = n` (default answer if no element satisfies $nums[mid] \ge x$).
  3. While `low <= high`:
     * Calculate `mid = low + (high - low) // 2`.
     * **Condition: `nums[mid] >= x`**
       * `nums[mid]` is a valid candidate for the lower bound!
       * Record it: `ans = mid`.
       * Since we want the **smallest / leftmost index**, try searching further left: `high = mid - 1`.
     * **Condition: `nums[mid] < x`**
       * `nums[mid]` is strictly too small to be a lower bound.
       * All elements to the left of `mid` are also too small $\rightarrow$ eliminate left: `low = mid + 1`.
  4. Return `ans`.

* **Direct Applications in Coding & Interviews:**
  * **Search Insert Position (LeetCode 35):** Finding where $x$ should be inserted into a sorted array is mathematically identical to finding its lower bound!
  * **Python / C++ Equivalents:**
    * Python: `bisect.bisect_left(nums, x)`
    * C++: `std::lower_bound(nums.begin(), nums.end(), x) - nums.begin()`
    * Java: `Arrays.binarySearch(nums, x)` (with negative insertion point conversion)

* **Time Complexity:** $\mathcal{O}(\log N)$ — The search space is divided in half at each iteration.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space — Only constant scalar pointer variables (`low`, `high`, `mid`, `ans`).

**File:** [01.py](../../code/sprint-5/day_6_6/01.py)
