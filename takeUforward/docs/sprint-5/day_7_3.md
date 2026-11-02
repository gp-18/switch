# 🟢 Day 7.3 — Binary Search: Floor and Ceil in Sorted Array

## 1. Floor and Ceil in Sorted Array

Given a sorted integer array `nums` and an integer `x`, find the **floor** and **ceil** of `x` in `nums`:

* **Floor of $x$:** The largest element in `nums` which is smaller than or equal to $x$ ($\text{floor} \le x$).
* **Ceiling of $x$:** The smallest element in `nums` which is greater than or equal to $x$ ($\text{ceil} \ge x$).

If no floor exists (i.e. all elements are $> x$), output `-1`.  
If no ceil exists (i.e. all elements are $< x$), output `-1`.

### Example

```text
Input:  nums = [3, 4, 4, 7, 8, 10], x = 5
Output: Floor = 4, Ceil = 7
Explanation:
- Elements <= 5 are [3, 4, 4]. The largest is 4 (Floor = 4).
- Elements >= 5 are [7, 8, 10]. The smallest is 7 (Ceil = 7).

Input:  nums = [3, 4, 4, 7, 8, 10], x = 8
Output: Floor = 8, Ceil = 8
Explanation: 8 is present in the array, so both Floor and Ceil are 8.

Input:  nums = [2, 4, 6, 8, 10, 12, 14], x = 1
Output: Floor = -1, Ceil = 2
Explanation: No element is <= 1 (Floor = -1). Smallest element >= 1 is 2 (Ceil = 2).

Input:  nums = [2, 4, 6, 8, 10, 12, 14], x = 15
Output: Floor = 14, Ceil = -1
Explanation: Largest element <= 15 is 14 (Floor = 14). No element is >= 15 (Ceil = -1).
```

### Think About

* **Deconstructing Floor and Ceil into Binary Searches:**
  * **Finding the Floor ($\le x$, largest possible):**
    * Initialize `floor = -1`.
    * If `nums[mid] <= x`:
      * `nums[mid]` is a valid candidate for floor!
      * Record candidate: `floor = nums[mid]`.
      * We want the *largest* valid number, so search to the right: `low = mid + 1`.
    * If `nums[mid] > x`:
      * `nums[mid]` is too large, search left: `high = mid - 1`.
  * **Finding the Ceil ($\ge x$, smallest possible):**
    * Notice that **Ceil is identical to Lower Bound!**
    * Initialize `ceil = -1`.
    * If `nums[mid] >= x`:
      * `nums[mid]` is a valid candidate for ceil!
      * Record candidate: `ceil = nums[mid]`.
      * We want the *smallest* valid number, so search to the left: `high = mid - 1`.
    * If `nums[mid] < x`:
      * `nums[mid]` is too small, search right: `low = mid + 1`.

* **Time Complexity:** $2 \times \mathcal{O}(\log N) \approx \mathcal{O}(\log N)$ — Two independent binary searches.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-5/day_7_3/01.py)
