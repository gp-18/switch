# 🟢 Day 5.1 — Arrays: Longest Consecutive Sequence in an Array (HashSet Sequence Starting Point)

## 1. Longest Consecutive Sequence in an Array

Given an unsorted array of integers `nums` of size $n$, return the length of the longest sequence of consecutive integers.

The integers in this sequence can appear in any order in the original array. You must write an algorithm that runs in $\mathcal{O}(N)$ time complexity.

### Example

```text
Input:  nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation:
The longest consecutive elements sequence is [1, 2, 3, 4]. Its length is 4.

Input:  nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
Output: 9
Explanation:
The longest consecutive elements sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8]. Its length is 9.

Input:  nums = [1, 9, 3, 10, 4, 20, 2]
Output: 4
Explanation:
The consecutive sequences present are:
- [1, 2, 3, 4] (length 4)
- [9, 10] (length 2)
- [20] (length 1)
Maximum length is 4.

Input:  nums = []  # Edge Case: Empty array
Output: 0
Explanation: Array is empty, consecutive sequence length is 0.

Input:  nums = [1, 2, 0, 1]  # Edge Case: Duplicates present
Output: 3
Explanation: Consecutive sequence is [0, 1, 2] of length 3. Duplicate values do not extend the sequence.
```

### Think About

* **Why Brute Force and Sorting Fall Short:**
  * **Brute Force ($\mathcal{O}(N^2)$ or $\mathcal{O}(N^3)$):** For every element $x$, perform linear searches in `nums` to check for $x + 1, x + 2, \dots$. This repeated traversal is too slow for $N = 10^5$.
  * **Sorting ($\mathcal{O}(N \log N)$ Time, $\mathcal{O}(1)$ or $\mathcal{O}(N)$ Space):**
    * Sorting brings consecutive numbers adjacent: `[1, 2, 3, 4, 100, 200]`.
    * We can then do a single pass tracking `last_smaller`, `curr_count`, and ignoring duplicates (`if nums[i] == nums[i-1]`).
    * However, sorting takes $\mathcal{O}(N \log N)$ time, which fails the strict $\mathcal{O}(N)$ constraint expected in interviews.

* **The Key Insight: Intelligent Sequence Starters with HashSet ($\mathcal{O}(N)$ Time):**
  * When does a number `x` represent the **start** of a consecutive sequence?
    * A number `x` can **only** be a sequence starting point if `x - 1` does **not** exist in the array!
  * If `x - 1` *does* exist in the array, then `x` is simply a continuation of an earlier sequence. Exploring from `x` would redundantly re-check numbers that will already be traversed from the true sequence starter.
  * Therefore:
    1. Insert all numbers into a `set` for $\mathcal{O}(1)$ average lookup time.
    2. Iterate through each unique number `it` in the set:
       * Check if `it - 1 not in set`:
         * If `True`: `it` is the head of a new sequence!
         * Start counting: `cnt = 1`, `x = it`.
         * While `x + 1 in set`: increment `x += 1` and `cnt += 1`.
         * Update `longest = max(longest, cnt)`.
       * If `False`: Skip immediately (`it` is not a starting element).

* **Why the Nested While Loop is Strictly $\mathcal{O}(N)$ (Amortized Analysis):**
  * It might look like nested loops could yield $\mathcal{O}(N^2)$, but that never happens!
  * Every number in the set is traversed:
    1. Once in the outer loop condition check (`it - 1 not in set`).
    2. At most once inside the `while (x + 1 in set)` loop because only the smallest element of any continuous sequence can enter the `while` loop.
  * Across all consecutive chains, each element is visited at most twice.
  * Total time: $\mathcal{O}(N)$ to build set $+ \mathcal{O}(N)$ for outer checks $+ \mathcal{O}(N)$ for inner while expansions $\approx \mathcal{O}(N)$.

* **Handling Duplicates & Negative Numbers:**
  * Converting `nums` to a `set` automatically eliminates duplicates in $\mathcal{O}(N)$ time.
  * Negative numbers work identically since hash lookups and arithmetic $x + 1, x - 1$ operate seamlessly across all integer values.

* **Time Complexity:** $\mathcal{O}(N)$ average time — building the set takes $\mathcal{O}(N)$ and traversing sequence elements takes $\mathcal{O}(N)$.
* **Space Complexity:** $\mathcal{O}(N)$ auxiliary space — required to store elements in the hash set.

**File:** [01.py](../../code/sprint-5/day_5_1/01.py)
