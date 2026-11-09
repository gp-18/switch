# 🟢 Day 5.4 — Binary Search: Kth Element of 2 Sorted Arrays

## 1. Kth Element of 2 Sorted Arrays

Given two sorted arrays `a` and `b` of size $m$ and $n$ respectively, and an integer $k$ ($1 \le k \le m + n$).

Find the element that would be at the **$k$-th position (1-based index)** of the final sorted array formed by merging both arrays.

You must write an algorithm that runs in $\mathcal{O}(\log(\min(m, n)))$ time complexity.

### Example

```text
Input:  a = [2, 3, 6, 7, 9], b = [1, 4, 8, 10], k = 5
Output: 6
Explanation:
The merged sorted array is [1, 2, 3, 4, 6, 7, 8, 9, 10].
The 5th element is 6.

Input:  a = [100, 112, 256, 349, 770], b = [72, 86, 113, 119, 265, 445, 892], k = 7
Output: 256
Explanation:
Merged array: [72, 86, 100, 112, 113, 119, 256, 265, 349, 445, 770, 892].
The 7th element is 256.

Input:  a = [2, 3, 6], b = [7, 9], k = 4
Output: 7
Explanation:
Merged array: [2, 3, 6, 7, 9]. The 4th element is 7.

Input:  a = [2, 3, 6], b = [7, 9], k = 1  # Edge Case: First element
Output: 2

Input:  a = [2, 3, 6], b = [7, 9], k = 5  # Edge Case: Last element
Output: 9
```

### Think About

* **The Partition Concept for $k$ Elements:**
  * Similar to finding the median, we want to partition the combined array such that the **left half contains exactly $k$ elements**.
  * The $k$-th element in the sorted order will simply be the largest element in this left partition:
    $$\text{ans} = \max(l_1, l_2)$$

* **Search Space Boundaries for $mid_1$:**
  * Ensure array `a` is the smaller array with size $m$ ($m \le n$).
  * If $m > n$, swap the arrays: `kthElement(b, a, k)`.
  * **Lower bound (`low = max(0, k - n)`):**
    * Even if we take all $n$ elements from array `b`, we may still need $k - n$ elements from `a` to make up $k$ elements.
    * If $k < n$, $k - n < 0$, so we take $\max(0, k - n)$.
  * **Upper bound (`high = min(k, m)`):**
    * We cannot take more elements from `a` than its total size $m$.
    * We also cannot take more than $k$ elements total.
    * Therefore, $\text{high} = \min(k, m)$.
  * Search range for binary search: $[\max(0, k - n), \min(k, m)]$.

* **Valid Partition Condition:**
  * For $mid_1$ elements taken from `a`, take $mid_2 = k - mid_1$ elements from `b`.
  * Define border elements:
    * $l_1 = a[mid_1 - 1]$ if $mid_1 > 0$ else $-\infty$
    * $r_1 = a[mid_1]$ if $mid_1 < m$ else $+\infty$
    * $l_2 = b[mid_2 - 1]$ if $mid_2 > 0$ else $-\infty$
    * $r_2 = b[mid_2]$ if $mid_2 < n$ else $+\infty$
  * If $l_1 \le r_2$ and $l_2 \le r_1$:
    * Valid partition found! Return $\max(l_1, l_2)$.
  * If $l_1 > r_2$:
    * Too many elements taken from `a`. Move left: `high = mid1 - 1`.
  * Else ($l_2 > r_1$):
    * Too few elements taken from `a`. Move right: `low = mid1 + 1`.

* **Time Complexity:** $\mathcal{O}(\log(\min(m, n)))$
  * Binary search is performed on the smaller array within a range of length $\le \min(m, n)$.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-6/day_5_4/01.py)

