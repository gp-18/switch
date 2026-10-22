# 🟢 Day 5 — Arrays: Maximum Subarray Sum (Kadane's Algorithm)

## 1. Kadane's Algorithm (Maximum Subarray Sum)

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous non-empty sequence of elements within an array.

### Example

```text
Input:  nums = [2, 3, 5, -2, 7, -4]
Output: 15
Explanation: The subarray [2, 3, 5, -2, 7] from index 0 to 4 has the largest sum = 15.

Input:  nums = [-1, 2, 3, -1, 2, -6, 5]
Output: 6
Explanation: The subarray [2, 3, -1, 2] from index 1 to 4 has the largest sum = 6.

Input:  nums = [-2, -3, -7, -2, -10, -4]  # Edge Case: All negative numbers
Output: -2
Explanation: The single element [-2] (at index 0 or 3) gives the maximum sum.
```

### Think About

* **Optimal Approach (Kadane's Algorithm):**
  * Maintain two variables:
    * `max_sum = float('-inf')`: keeps track of the global maximum subarray sum encountered so far.
    * `current_sum = 0`: tracks the running sum of the current contiguous subarray.
  * Iterate through each element in `nums`:
    * Add `nums[i]` to `current_sum`.
    * Update `max_sum = max(max_sum, current_sum)`.
    * If `current_sum < 0`, reset `current_sum = 0`.
* **Why Reset to 0 When Sum Drops Below Zero?**
  * A prefix subarray with a net negative sum will always diminish the total sum of any subsequent contiguous subarray. Discarding the accumulated negative prefix and starting fresh from the next element is strictly better.
* **Handling All-Negative Arrays:**
  * By initializing `max_sum = float('-inf')` (or `nums[0]`) and updating `max_sum` *before* resetting `current_sum`, the algorithm handles arrays where all numbers are negative by picking the least negative (maximum) single element.
* **Interview Follow-Up (Printing the Subarray):**
  * Maintain `start = 0`, `ans_start = -1`, `ans_end = -1`.
  * When `current_sum == 0`, set `start = i`.
  * When `current_sum > max_sum`, set `ans_start = start` and `ans_end = i`.
* **Time Complexity:** $\mathcal{O}(N)$ — A single linear scan through the array of length $N$.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space — Only constant scalar variables.

**File:** [01.py](../../code/sprint-4/day_5/01.py)

---

## 2. Print Subarray with Maximum Sum (Kadane's Algorithm Follow-up)

Given an integer array `nums`, find the contiguous subarray that yields the largest sum. Print or return the actual subarray elements (along with their starting and ending indices) as well as the maximum sum.

### Example

```text
Input:  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: Subarray: [4, -1, 2, 1], Maximum Sum: 6
Explanation: The subarray from index 3 to index 6 has the largest sum = 4 + (-1) + 2 + 1 = 6.

Input:  nums = [2, 3, 5, -2, 7, -4]
Output: Subarray: [2, 3, 5, -2, 7], Maximum Sum: 15
Explanation: The subarray from index 0 to index 4 has the largest sum = 15.

Input:  nums = [-2, -3, -7, -2, -10, -4]  # Edge Case: All negative numbers
Output: Subarray: [-2], Maximum Sum: -2
Explanation: The single element [-2] at index 0 or index 3 gives the maximum sum.
```

### Think About

* **Tracking Subarray Boundaries:**
  * Rather than storing or copying subarray elements during iteration, maintain only index pointers:
    * `start = 0`: denotes the starting index of the current active subarray candidate.
    * `ans_start = -1` and `ans_end = -1`: store the boundary indices of the best subarray found so far.
* **Core Algorithm Steps:**
  * Initialize `max_sum = float('-inf')`, `current_sum = 0`.
  * Iterate `i` from `0` to `n - 1`:
    * If `current_sum == 0`: set `start = i` (this marks the beginning of a fresh subarray).
    * Add `nums[i]` to `current_sum`.
    * If `current_sum > max_sum`:
      * Update `max_sum = current_sum`.
      * Record best indices: `ans_start = start`, `ans_end = i`.
    * If `current_sum < 0`: reset `current_sum = 0`.
* **Extracting the Subarray:**
  * After the loop, the subarray with the maximum sum is `nums[ans_start : ans_end + 1]`.
* **Time Complexity:** $\mathcal{O}(N)$ — Single pass traversal through the array.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space (excluding space needed to print or return the result subarray).

**File:** [02.py](../../code/sprint-4/day_5/02.py)

