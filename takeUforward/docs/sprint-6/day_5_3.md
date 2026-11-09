# 🟢 Day 5.3 — Binary Search: Median of 2 Sorted Arrays

## 1. Median of 2 Sorted Arrays

Given two sorted arrays `arr1` and `arr2` of size $m$ and $n$ respectively, return the **median** of the two sorted arrays.

The median is defined as the middle value of a sorted list of numbers:
* If the total number of elements $m + n$ is **odd**, the median is the single middle element.
* If the total number of elements $m + n$ is **even**, the median is the average of the two middle elements.

You must write an algorithm that runs in $\mathcal{O}(\log(\min(m, n)))$ time complexity.

### Example

```text
Input:  arr1 = [2, 4, 6], arr2 = [1, 3, 5]
Output: 3.5
Explanation:
The combined sorted array is [1, 2, 3, 4, 5, 6] (length = 6, even).
The two middle elements are 3 and 4.
Median = (3 + 4) / 2.0 = 3.5.

Input:  arr1 = [2, 4, 6], arr2 = [1, 3]
Output: 3.0
Explanation:
The combined sorted array is [1, 2, 3, 4, 6] (length = 5, odd).
The middle element is 3.
Median = 3.0.

Input:  arr1 = [2, 4, 5], arr2 = [1, 6]
Output: 4.0
Explanation:
The combined sorted array is [1, 2, 4, 5, 6]. Median = 4.0.

Input:  arr1 = [], arr2 = [2]  # Edge Case: One empty array
Output: 2.0
Explanation:
Merged array is [2]. Median = 2.0.

Input:  arr1 = [1, 2], arr2 = [3, 4]  # Edge Case: Disjoint arrays
Output: 2.5
Explanation:
Merged array is [1, 2, 3, 4]. Median = (2 + 3) / 2.0 = 2.5.
```

### Think About

* **The Partition Concept:**
  * The median divides the merged sorted array into two halves of equal size (or left half has 1 extra element if $m + n$ is odd):
    $$\text{left\_size} = \frac{m + n + 1}{2}$$
  * If we choose $mid_1$ elements from `arr1` for the left half, we must take $mid_2 = \text{left\_size} - mid_1$ elements from `arr2`.
  * The boundary elements around the cut are:
    * $l_1 = arr1[mid_1 - 1]$ (or $-\infty$ if $mid_1 = 0$)
    * $r_1 = arr1[mid_1]$ (or $+\infty$ if $mid_1 = m$)
    * $l_2 = arr2[mid_2 - 1]$ (or $-\infty$ if $mid_2 = 0$)
    * $r_2 = arr2[mid_2]$ (or $+\infty$ if $mid_2 = n$)

* **Valid Partition Condition:**
  * For the merged halves to form a valid sorted order, all elements in the left half must be $\le$ all elements in the right half:
    $$l_1 \le r_2 \quad \text{and} \quad l_2 \le r_1$$
  * When this condition holds, we have found the exact median:
    * If $(m + n)$ is **odd**: $\text{median} = \max(l_1, l_2)$
    * If $(m + n)$ is **even**: $\text{median} = \frac{\max(l_1, l_2) + \min(r_1, r_2)}{2.0}$

* **Always Binary Search on the Smaller Array:**
  * If $m > n$, swap `arr1` and `arr2` so that `arr1` is always the shorter array ($m \le n$).
  * This guarantees:
    1. Search space is minimized: $\mathcal{O}(\log(\min(m, n)))$.
    2. $mid_2 = \text{left\_size} - mid_1$ is guaranteed to never be negative or exceed $n$.

* **Binary Search Decisions:**
  * **If $l_1 > r_2$:** We took too many elements from `arr1`. Move left: `high = mid1 - 1`.
  * **If $l_2 > r_1$:** We took too few elements from `arr1` (too many from `arr2`). Move right: `low = mid1 + 1`.

* **Time Complexity:** $\mathcal{O}(\log(\min(m, n)))$
  * Binary search is performed on the smaller array of size $\min(m, n)$.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-6/day_5_3/01.py)

