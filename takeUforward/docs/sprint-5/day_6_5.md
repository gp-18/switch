# 🟢 Day 6.5 — Binary Search: Search X in Sorted Array (Iterative Binary Search)

## 1. Search X in Sorted Array

Given a sorted array of integers `nums` with 0-based indexing and a target integer `target`, find the index of `target`.

* If `target` is found in the array, return its index.
* If `target` is not found, return `-1`.

You must write an algorithm with $\mathcal{O}(\log N)$ runtime complexity.

### Example

```text
Input:  nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
Explanation: The target integer 9 exists in nums at index 4.

Input:  nums = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1
Explanation: 2 does not exist in nums, so return -1.

Input:  nums = [-1, 0, 3, 5, 9, 12], target = -1
Output: 0
Explanation: -1 is at index 0.

Input:  nums = [5], target = 5  # Edge Case: Single element found
Output: 0

Input:  nums = [5], target = 2  # Edge Case: Single element missing
Output: -1
```

### Think About

* **The Binary Search Paradigm (Halving the Search Space):**
  * Because the array is **sorted**, any element `nums[mid]` divides the search space into two ordered partitions:
    1. Every element to the left is $\le nums[mid]$.
    2. Every element to the right is $\ge nums[mid]$.
  * By comparing `nums[mid]` with `target`, we can safely eliminate an entire half of remaining candidates in $\mathcal{O}(1)$ time.

* **Step-by-Step Logic:**
  1. Define the search space boundaries:
     * `low = 0`
     * `high = len(nums) - 1`
  2. While the search space is valid (`low <= high`):
     * Calculate midpoint: `mid = low + (high - low) // 2` (or `(low + high) // 2`).
     * **Case 1 (Match):** If `nums[mid] == target`, return `mid`.
     * **Case 2 (Target is larger):** If `target > nums[mid]`, target must be in the right half $\rightarrow$ eliminate left: `low = mid + 1`.
     * **Case 3 (Target is smaller):** If `target < nums[mid]`, target must be in the left half $\rightarrow$ eliminate right: `high = mid - 1`.
  3. If loop terminates without a match (`low > high`), target is absent $\rightarrow$ return `-1`.

* **Avoiding Integer Overflow (PBC Favorite):**
  * In languages like C++, Java, and Go, calculating `(low + high) / 2` can overflow a 32-bit signed integer if `low + high > 2^31 - 1`.
  * Using `mid = low + (high - low) // 2` avoids overflow while maintaining exact mathematical equivalence. In Python, integers have arbitrary precision, but writing this pattern demonstrates production-grade habits.

* **Iterative vs. Recursive Implementation:**
  * **Iterative:** Uses $\mathcal{O}(1)$ auxiliary space.
  * **Recursive:** Incurs $\mathcal{O}(\log N)$ call-stack memory.
  * In interviews, always default to the **iterative** approach for optimal $\mathcal{O}(1)$ space.

* **Time Complexity:** $\mathcal{O}(\log N)$ — The search space of size $N$ is halved in every step until size is 1.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space — Only two pointer variables (`low`, `high`) are stored.

**File:** [01.py](../../code/sprint-5/day_6_5/01.py)
