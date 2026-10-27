# 🟢 Day 1 — Arrays: Majority Element-II (Extended Boyer-Moore Voting Algorithm)

## 1. Majority Element-II

Given an integer array `nums` of size $n$, return all elements which appear strictly more than $\lfloor n / 3 \rfloor$ times in the array. The output can be returned in any order.

### Example

```text
Input:  nums = [1, 2, 1, 1, 3, 2]
Output: [1]
Explanation: Here, n / 3 = 6 / 3 = 2. The only element appearing 3 or more times is [1].

Input:  nums = [1, 2, 1, 1, 3, 2, 2]
Output: [1, 2]
Explanation: Here, n / 3 = 7 / 3 = 2. The elements appearing 3 or more times are [1, 2].

Input:  nums = [1, 2, 1, 1, 3, 2, 2, 3]
Output: [1, 2]
Explanation: Here, n / 3 = 8 / 3 = 2. 1 appears 3 times, 2 appears 3 times, and 3 appears 2 times. The elements appearing > 2 times are [1, 2].

Input:  nums = [1, 2, 3]  # Edge Case: No majority element
Output: []
Explanation: Here, n / 3 = 3 / 3 = 1. Every element appears exactly 1 time (not > 1).

Input:  nums = [5, 5, 5, 5]  # Edge Case: All identical elements
Output: [5]
Explanation: Here, n / 3 = 4 / 3 = 1. 5 appears 4 times > 1.
```

### Think About

* **Optimal Approach (Extended Boyer-Moore Voting Algorithm):**
  * By mathematical constraint, at most **2** elements can appear strictly more than $\lfloor n / 3 \rfloor$ times.
  * Maintain two candidates (`candidate1 = None`, `candidate2 = None`) and two vote counters (`count1 = 0`, `count2 = 0`).
  * **Pass 1 (Candidate Selection / Triplet Cancellation):**
    * Iterate through each `num` in `nums`:
      * If `num == candidate1`: increment `count1 += 1`.
      * Else if `num == candidate2`: increment `count2 += 1`.
      * Else if `count1 == 0`: set `candidate1 = num` and `count1 = 1`.
      * Else if `count2 == 0`: set `candidate2 = num` and `count2 = 1`.
      * Else: decrement both `count1 -= 1` and `count2 -= 1` (cancelling a triplet of 3 mutually distinct elements).
  * **Pass 2 (Verification Pass):**
    * Boyer-Moore only narrows down potential candidates; it does not guarantee they meet the threshold.
    * Traverse `nums` again to count the actual occurrences of `candidate1` and `candidate2`.
    * If `actual_count1 > n // 3`: append `candidate1` to the result.
    * If `actual_count2 > n // 3`: append `candidate2` to the result.
* **Why Can There Be at Most Two Elements Appearing $> n/3$ Times?**
  * Any element appearing strictly more than $n / 3$ times must appear at least $\lfloor n / 3 \rfloor + 1$ times.
  * If there were $3$ such elements, their total count would be at least:
    $$3 \times \left( \left\lfloor \frac{n}{3} \right\rfloor + 1 \right) > 3 \times \frac{n}{3} = n$$
  * This strictly exceeds the array size $n$, which is impossible. Hence, at most **2** elements can qualify (there could be 0, 1, or 2).
* **Why Is the Verification Pass Mandatory?**
  * In Majority Element-I ($> n / 2$), a majority element was guaranteed to exist.
  * In Majority Element-II, there is no guarantee that any element appears $> n / 3$ times (e.g., `nums = [1, 2, 3]` gives candidates from voting that appear only once). A verification count is strictly required.
* **Why Is Sorting Less Efficient?**
  * Sorting groups identical elements contiguously but costs $\mathcal{O}(N \log N)$ time and either mutates the input array or uses $\mathcal{O}(N)$ extra space.
  * Extended Boyer-Moore runs in strictly linear $\mathcal{O}(N)$ time with $\mathcal{O}(1)$ auxiliary space.
* **Interview Follow-Up (Elements Appearing $> n/k$ Times — Misra-Gries Algorithm):**
  * At most $k - 1$ elements can appear more than $n / k$ times.
  * Maintain $k - 1$ candidate slots and $k - 1$ counters (or a dictionary of capacity $k - 1$).
  * When encountering an element that doesn't match any candidate and no counters are 0, decrement all $k - 1$ counters by 1 (cancelling $k$ distinct elements).
  * Conclude with a verification pass across all $k - 1$ candidates.
* **Time Complexity:** $\mathcal{O}(N)$ — Two linear passes through the array of length $N$.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space — Only constant scalar variables for candidates and counters.

**File:** [01.py](../../code/sprint-5/day_1_1/01.py)
