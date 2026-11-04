# 🟢 Day 1.1 — Binary Search: Count Occurrences in a Sorted Array

## 1. Count Occurrences in a Sorted Array

Given a sorted array of integers `arr` and an integer `target`, determine how many times `target` appears in `arr`.

Return the total count of occurrences of `target` in the array.

You must write an algorithm that runs in $\mathcal{O}(\log N)$ time complexity.

### Example

```text
Input:  arr = [0, 0, 1, 1, 1, 2, 3], target = 1
Output: 3
Explanation: The target 1 appears 3 times in the array (from index 2 to 4).

Input:  arr = [5, 5, 5, 5, 5, 5], target = 5
Output: 6
Explanation: All 6 elements are equal to 5, so the count is 6.

Input:  arr = [2, 4, 6, 8, 10], target = 3
Output: 0
Explanation: 3 does not appear in the array. Return 0.

Input:  arr = [1, 2, 2, 2, 3, 4], target = 2
Output: 3
Explanation: 2 appears at indices 1, 2, 3 -> count = 3 - 1 + 1 = 3.

Input:  arr = [7], target = 7  # Edge Case: Single element found
Output: 1

Input:  arr = [7], target = 9  # Edge Case: Single element missing
Output: 0
```

### Think About

* **Why Linear Scan is Suboptimal:**
  * Iterating through the entire array takes $\mathcal{O}(N)$ time.
  * For $N = 10^6$, $\mathcal{O}(N)$ time wastes the crucial advantage of the array being **already sorted**.

* **The Contiguity Principle:**
  * In a sorted array, all duplicate occurrences of any number appear **adjacent to each other in a single contiguous block**:
    $$[\dots, \underbrace{\text{target}, \text{target}, \dots, \text{target}}_{\text{from index } first \text{ to } last}, \dots]$$
  * Once we find the **first occurrence** index and the **last occurrence** index:
    $$\text{Total Occurrences} = last - first + 1$$

* **Two Binary Searches Implementation:**
  1. **`firstOccurrence(arr, target)`:**
     * `low = 0, high = n - 1, first = -1`
     * While `low <= high`:
       * `mid = low + (high - low) // 2`
       * If `arr[mid] == target`:
         * Record `first = mid`
         * Search further left: `high = mid - 1`
       * Else if `arr[mid] < target`:
         * `low = mid + 1`
       * Else:
         * `high = mid - 1`
     * Return `first`.
  2. **Early Exit Optimization:**
     * If `first == -1`, `target` does not exist anywhere in `arr`!
     * Immediately return `0` without running the second binary search.
  3. **`lastOccurrence(arr, target)`:**
     * `low = 0, high = n - 1, last = -1`
     * While `low <= high`:
       * `mid = low + (high - low) // 2`
       * If `arr[mid] == target`:
         * Record `last = mid`
         * Search further right: `low = mid + 1`
       * Else if `arr[mid] < target`:
         * `low = mid + 1`
       * Else:
         * `high = mid - 1`
     * Return `last`.
  4. **Compute Count:**
     $$\text{count} = last - first + 1$$

* **Alternative Technique: Upper Bound & Lower Bound:**
  * Recall:
    * `lower_bound`: smallest index with $arr[i] \ge target$.
    * `upper_bound`: smallest index with $arr[i] > target$.
  * If `lower_bound == len(arr)` or `arr[lower_bound] != target`: count is `0`.
  * Otherwise:
    $$\text{count} = \text{upper\_bound}(arr, target) - \text{lower\_bound}(arr, target)$$

* **Time Complexity:** $2 \times \mathcal{O}(\log N) \approx \mathcal{O}(\log N)$ — Two independent binary searches.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-6/day_1_1/01.py)
