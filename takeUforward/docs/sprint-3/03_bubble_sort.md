# 🔹 Bubble Sort

A comprehensive guide, step-by-step breakdown, loop analysis, optimization techniques, complexity analysis, and quick-revision interview notes for **Bubble Sort**.

---

## Table of Contents

- [1. What is Bubble Sort?](#1-what-is-bubble-sort)
- [2. How Does It Work? (Visual Walkthrough)](#2-how-does-it-work-visual-walkthrough)
- [3. Python Code Implementation](#3-python-code-implementation)
- [4. Why `n - 1 - i`? (Understanding the Loops)](#4-why-n---1---i-understanding-the-loops)
- [5. Detailed Dry Run Table](#5-detailed-dry-run-table)
- [6. Optimization: The `swapped` Flag ($\mathcal{O}(N)$ Best Case)](#6-optimization-the-swapped-flag-mathcalon-best-case)
- [7. Complexity Analysis](#7-complexity-analysis)
- [8. Important Interview Points & FAQs](#8-important-interview-points--faqs)
- [9. Comparison: Bubble Sort vs. Selection Sort](#9-comparison-bubble-sort-vs-selection-sort)
- [✍️ Short Handwritten Interview Notes](#-short-handwritten-interview-notes)

---

## 1. What is Bubble Sort?

**Bubble Sort** is a comparison-based sorting algorithm that repeatedly compares adjacent elements and swaps them if they are in the wrong order.

### Mental Model

Think of it like air bubbles rising in water:
- The **heaviest (largest) elements** gradually "bubble up" to the end of the array after every pass.
- After Pass 1, the $1^{\text{st}}$ largest element is settled at the last index.
- After Pass 2, the $2^{\text{nd}}$ largest element is settled at the second-to-last index.
- After $k$ passes, the $k$ largest elements are settled at the end in sorted order.

$$\text{\bf Bubble Sort} = \text{\bf Compare Adjacent} \longrightarrow \text{\bf Swap if Out of Order} \longrightarrow \text{\bf Bubble Largest to End}$$

---

## 2. How Does It Work? (Visual Walkthrough)

Suppose we have the array:

$$\text{arr} = [5, 3, 8, 4, 2]$$

We want to sort it in ascending order: `[2, 3, 4, 5, 8]`.

---

### 🔹 Pass 1 (Pushing the largest element to the end)

We compare adjacent pairs from index `0` up to `n - 2`:

1. **Compare $5$ and $3$:**
   - $5 > 3 \longrightarrow$ **Swap**
   - Array: `[3, 5, 8, 4, 2]`

2. **Compare $5$ and $8$:**
   - $5 < 8 \longrightarrow$ **No swap**
   - Array: `[3, 5, 8, 4, 2]`

3. **Compare $8$ and $4$:**
   - $8 > 4 \longrightarrow$ **Swap**
   - Array: `[3, 5, 4, 8, 2]`

4. **Compare $8$ and $2$:**
   - $8 > 2 \longrightarrow$ **Swap**
   - Array: `[3, 5, 4, 2, 8]`

```text
[ 3,  5,  4,  2, | 8 ]
                   ↑
             largest element is now settled!
```
> **Notice:** **`8`** has reached its final sorted position at the end.

---

### 🔹 Pass 2 (Pushing the 2nd largest element)

Now we only need to compare up to index `n - 3` (no need to touch `8`):

1. **Compare $3$ and $5$:**
   - $3 < 5 \longrightarrow$ **No swap**
   - Array: `[3, 5, 4, 2, 8]`

2. **Compare $5$ and $4$:**
   - $5 > 4 \longrightarrow$ **Swap**
   - Array: `[3, 4, 5, 2, 8]`

3. **Compare $5$ and $2$:**
   - $5 > 2 \longrightarrow$ **Swap**
   - Array: `[3, 4, 2, 5, 8]`

```text
[ 3,  4,  2, | 5,  8 ]
               ↑   ↑
            sorted part
```
> **Notice:** **`5`** has reached its correct position.

---

### 🔹 Pass 3 (Pushing the 3rd largest element)

Compare pairs up to index `n - 4`:

1. **Compare $3$ and $4$:**
   - $3 < 4 \longrightarrow$ **No swap**
   - Array: `[3, 4, 2, 5, 8]`

2. **Compare $4$ and $2$:**
   - $4 > 2 \longrightarrow$ **Swap**
   - Array: `[3, 2, 4, 5, 8]`

```text
[ 3,  2, | 4,  5,  8 ]
           ↑   ↑   ↑
          sorted part
```
> **Notice:** **`4`** has reached its correct position.

---

### 🔹 Pass 4 (Final adjacent comparison)

Only one comparison left between the first two elements:

1. **Compare $3$ and $2$:**
   - $3 > 2 \longrightarrow$ **Swap**
   - Array: `[2, 3, 4, 5, 8]`

```text
[ 2,  3,  4,  5,  8 ]
  ===================
    Fully Sorted! ✅
```

---

## 3. Python Code Implementation

### Standard Bubble Sort

```python
def bubble_sort(arr):
    n = len(arr)

    # Outer loop for passes (0 to n - 2)
    for i in range(n - 1):
        # Inner loop for adjacent comparisons
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Swap adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Driver Code
arr = [5, 3, 8, 4, 2]
print("Sorted array:", bubble_sort(arr))
```

### Output:

```text
Sorted array: [2, 3, 4, 5, 8]
```

---

## 4. Why `n - 1 - i`? (Understanding the Loops)

This is one of the most frequently asked questions in DSA interviews regarding Bubble Sort.

### 1. The Outer Loop: `for i in range(n - 1):`
- `i` represents the **pass number** (from $0$ to $n - 2$).
- After pass $i$, exactly $i + 1$ largest elements have been placed at the end of the array.
- An array of size $n$ requires at most $n - 1$ passes, because once $n - 1$ elements are placed in their proper positions, the remaining 1 element must already be in its correct place.

---

### 2. The Inner Loop: `for j in range(n - 1 - i):`
Why is the limit `n - 1 - i`? Let's break it down:

1. **Why `n - 1`?**
   - We compare `arr[j]` with `arr[j + 1]`.
   - If `j` went all the way to `n - 1`, accessing `arr[j + 1]` would evaluate to `arr[n]`, causing an **`IndexError: list index out of range`**.
   - Therefore, the maximum allowable index for `j` is `n - 2`, meaning the range must stop at `n - 1`.

2. **Why `- i`?**
   - After Pass 1 ($i = 0$): The single largest element (`8`) is settled at index $n - 1$. We don't need to check it again.
   - After Pass 2 ($i = 1$): The two largest elements (`5, 8`) are settled at indices $n - 2$ and $n - 1$.
   - After Pass 3 ($i = 2$): The three largest elements (`4, 5, 8`) are settled.

```text
Pass 0 (i = 0):  j goes from 0 to n - 2   -->  (n - 1) comparisons
Pass 1 (i = 1):  j goes from 0 to n - 3   -->  (n - 2) comparisons
Pass 2 (i = 2):  j goes from 0 to n - 4   -->  (n - 3) comparisons
...
Pass i:          j goes from 0 to n - 2 - i --> (n - 1 - i) comparisons
```

> **Takeaway:** Every subsequent pass reduces the comparison window by 1 because the rightmost portion of the array is already sorted.

---

## 5. Detailed Dry Run Table

Dry run of Bubble Sort on `arr = [5, 3, 8, 4, 2]` ($n = 5$):

| Pass ($i$) | Inner Index ($j$) | Adjacent Pair Compared | Condition (`arr[j] > arr[j+1]`) | Action Taken | Array State After Step |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **0** | $0$ | $5$ vs $3$ | $5 > 3$ (True) | Swap $(5, 3)$ | `[3, 5, 8, 4, 2]` |
| **0** | $1$ | $5$ vs $8$ | $5 > 8$ (False) | No swap | `[3, 5, 8, 4, 2]` |
| **0** | $2$ | $8$ vs $4$ | $8 > 4$ (True) | Swap $(8, 4)$ | `[3, 5, 4, 8, 2]` |
| **0** | $3$ | $8$ vs $2$ | $8 > 2$ (True) | Swap $(8, 2)$ | `[3, 5, 4, 2, 8]` *(8 settled)* |
| **1** | $0$ | $3$ vs $5$ | $3 > 5$ (False) | No swap | `[3, 5, 4, 2, 8]` |
| **1** | $1$ | $5$ vs $4$ | $5 > 4$ (True) | Swap $(5, 4)$ | `[3, 4, 5, 2, 8]` |
| **1** | $2$ | $5$ vs $2$ | $5 > 2$ (True) | Swap $(5, 2)$ | `[3, 4, 2, 5, 8]` *(5 settled)* |
| **2** | $0$ | $3$ vs $4$ | $3 > 4$ (False) | No swap | `[3, 4, 2, 5, 8]` |
| **2** | $1$ | $4$ vs $2$ | $4 > 2$ (True) | Swap $(4, 2)$ | `[3, 2, 4, 5, 8]` *(4 settled)* |
| **3** | $0$ | $3$ vs $2$ | $3 > 2$ (True) | Swap $(3, 2)$ | `[2, 3, 4, 5, 8]` *(3 settled)* |

**Final Sorted Result:** `[2, 3, 4, 5, 8]`

---

## 6. Optimization: The `swapped` Flag ($\mathcal{O}(N)$ Best Case)

### The Problem with Standard Bubble Sort
Even if the input array is **already sorted** (e.g., `[1, 2, 3, 4, 5]`), the standard algorithm will blindly continue running all nested loops and execute $\frac{N(N - 1)}{2}$ comparisons.

### The Solution
If a pass completes **without making a single swap**, that means every adjacent pair was already in non-decreasing order:
$$\text{arr}[j] \le \text{arr}[j + 1] \quad \text{for all } j$$
Therefore, the array is already sorted, and we can terminate early!

```python
def bubble_sort_optimized(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped in this pass, array is sorted!
        if not swapped:
            break

    return arr


# Example: Already sorted array takes only 1 pass (O(N) time)
sorted_arr = [1, 2, 3, 4, 5]
print("Optimized sort result:", bubble_sort_optimized(sorted_arr))
```

---

## 7. Complexity Analysis

| Case | Standard Time | Optimized Time | Condition |
| :--- | :---: | :---: | :--- |
| **Best Case** | $\mathcal{O}(N^2)$ | $\mathbf{\mathcal{O}(N)}$ | Array is already sorted; 0 swaps occur in Pass 1 $\rightarrow$ exits early. |
| **Average Case** | $\mathcal{O}(N^2)$ | $\mathcal{O}(N^2)$ | Random order elements. |
| **Worst Case** | $\mathcal{O}(N^2)$ | $\mathcal{O}(N^2)$ | Array is sorted in reverse order; maximum swaps occur. |

### Mathematical Derivation of Comparisons:

$$\text{Total Comparisons} = (N - 1) + (N - 2) + (N - 3) + \dots + 1 = \frac{N(N - 1)}{2} = \mathcal{O}(N^2)$$

### Space Complexity:
$$\text{Space Complexity} = \mathcal{O}(1)$$
- Modifies the array **in-place**.
- Uses only auxiliary loop variables (`i`, `j`, `swapped`). No additional memory is allocated.

---

## 8. Important Interview Points & FAQs

| Question | Answer | Details / Explanation |
| :--- | :---: | :--- |
| **Is Bubble Sort stable?** | **Yes** ✅ | It only swaps when `arr[j] > arr[j + 1]`. If two elements are equal (`arr[j] == arr[j + 1]`), they are **not** swapped, preserving their original relative order. |
| **Is it in-place?** | **Yes** ✅ | Auxiliary space is $\mathcal{O}(1)$. |
| **Is it adaptive?** | **Yes (with flag)** ✅ | The optimized version detects sorted data in $\mathcal{O}(N)$ time. |
| **Worst-case swaps?** | $\frac{N(N - 1)}{2}$ swaps | When the array is reverse sorted, every comparison requires a swap. |
| **Best-case swaps?** | $0$ swaps | When the array is already sorted. |

---

## 9. Comparison: Bubble Sort vs. Selection Sort

| Feature | Bubble Sort | Selection Sort |
| :--- | :--- | :--- |
| **Core Operation** | Repeatedly swaps adjacent out-of-order pairs | Finds minimum in unsorted part and places in front |
| **Best Case Time** | $\mathcal{O}(N)$ *(Optimized with flag)* | $\mathcal{O}(N^2)$ *(Always)* |
| **Worst Case Time** | $\mathcal{O}(N^2)$ | $\mathcal{O}(N^2)$ |
| **Auxiliary Space** | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |
| **Stability** | **Stable** ✅ | **Unstable** ❌ |
| **Number of Swaps** | $\mathcal{O}(N^2)$ in worst case | $\mathcal{O}(N)$ (at most $N - 1$ swaps) |
| **When to prefer?** | When input is almost sorted or stability is needed | When write operations (swapping) are very expensive |

---

## ✍️ Short Handwritten Interview Notes

```text
============================================================
                      BUBBLE SORT
============================================================

IDEA:
  Repeatedly compare adjacent elements (arr[j], arr[j+1]).
  If arr[j] > arr[j+1], SWAP them.
  Largest element "bubbles" to the end on every pass.

STEPS:
  1. Outer loop i from 0 to n - 2 (pass count).
  2. Flag swapped = False.
  3. Inner loop j from 0 to n - 2 - i (reduce search space).
  4. If arr[j] > arr[j + 1]:
       swap(arr[j], arr[j + 1])
       swapped = True
  5. If not swapped:
       break (already sorted).

CODE:
  for i in range(n - 1):
      swapped = False
      for j in range(n - 1 - i):
          if arr[j] > arr[j + 1]:
              arr[j], arr[j + 1] = arr[j + 1], arr[j]
              swapped = True
      if not swapped:
          break

COMPLEXITY:
  Time:
    Best    : O(N)   (with swapped flag)
    Average : O(N²)
    Worst   : O(N²)  (reverse sorted)
  Space:
    O(1) -> In-place

STABILITY:
  YES (Stable) -> preserves order of equal elements

SWAPS:
  Worst: O(N²) swaps
  Best : 0 swaps

KEY MANTRA:
  COMPARE ADJACENT  -->  SWAP  -->  BUBBLE TO END
============================================================
```
