# 🔹 Quick Sort

A comprehensive guide, step-by-step breakdown, partition mechanics, dry run, complexity analysis, Merge Sort vs. Quick Sort comparison, and quick-revision interview notes for **Quick Sort**.

---

## Table of Contents

- [1. Intuition (Divide and Conquer with Partitioning)](#1-intuition-divide-and-conquer-with-partitioning)
- [2. How Does It Work? (Visual Walkthrough)](#2-how-does-it-work-visual-walkthrough)
- [3. Python Code Implementation](#3-python-code-implementation)
- [4. Deep Dive: The Partition Algorithm](#4-deep-dive-the-partition-algorithm)
  - [Why `i <= high - 1` and `j >= low + 1`?](#why-i--high---1-and-j--low--1)
  - [Why Swap `arr[low]` with `arr[j]` (and NOT `arr[i]`)?](#why-swap-arrlow-with-arrj-and-not-arri)
  - [Why `p_index - 1` and `p_index + 1` in Recursive Calls?](#why-p_index---1-and-p_index--1-in-recursive-calls)
- [5. Detailed Dry Run Table](#5-detailed-dry-run-table)
- [6. Complexity Analysis & The Worst-Case Trap](#6-complexity-analysis--the-worst-case-trap)
- [7. Comparison: Quick Sort vs. Merge Sort](#7-comparison-quick-sort-vs-merge-sort)
- [8. Important Interview Points & FAQs](#8-important-interview-points--faqs)
- [9. 5-Minute Quick Revision 🧠](#9-5-minute-quick-revision-)
- [✍️ Short Handwritten Interview Notes](#-short-handwritten-interview-notes)

---

## 1. Intuition (Divide and Conquer with Partitioning)

Like Merge Sort, **Quick Sort** is a **Divide and Conquer** algorithm. However, its strategy is the exact opposite of Merge Sort:
- **Merge Sort:** Divides the array trivially in the middle without checking values, recurses, and does all the heavy work during the **Merge** step.
- **Quick Sort:** Does all the heavy work upfront during the **Partition** step, places a chosen element (the **Pivot**) in its final sorted position, and then trivially recurses on both sides.

### The Core Principle of Partitioning:

$$\text{\bf Quick Sort} = \text{\bf Pick Pivot} \longrightarrow \text{\bf Partition Around Pivot} \longrightarrow \text{\bf Recurse Left \& Right}$$

1. **Pick a Pivot:** Choose any element in the array range (standard convention: `arr[low]`).
2. **Partition:** Rearrange the array such that:
   - All elements **$\le$ Pivot** are shifted to the left of the pivot.
   - All elements **$>$ Pivot** are shifted to the right of the pivot.
   - The pivot is placed at its **exact, final sorted position** (the partition index).
3. **Recurse:** Once the pivot is in its final position, it never needs to be touched again. Recursively sort the left subarray and the right subarray.

```text
       [ Elements <= Pivot ]    [ PIVOT ]    [ Elements > Pivot ]
                 ▲                  ▲                  ▲
          Recursively Sort     Fixed In Place     Recursively Sort
```

---

## 2. How Does It Work? (Visual Walkthrough)

Consider the array:

$$\text{arr} = [4, 6, 2, 5, 7, 9, 1, 3]$$

### Step 1: Choosing the Pivot
- Let `pivot = arr[low] = arr[0] = 4`.
- Initialize two pointers:
  - `i = low = 0` (scans forward looking for elements $> \text{pivot}$)
  - `j = high = 7` (scans backward looking for elements $\le \text{pivot}$)

```text
Index:    0   1   2   3   4   5   6   7
Values: [ 4,  6,  2,  5,  7,  9,  1,  3 ]
          ▲                           ▲
       pivot, i                       j
```

---

### Step 2: Scanning & Swapping
1. **Move `i` forward** until `arr[i] > 4`:
   - At index `1`: `arr[1] = 6 > 4` $\longrightarrow$ `i` stops at `1`.
2. **Move `j` backward** until `arr[j] <= 4`:
   - At index `7`: `arr[7] = 3 <= 4` $\longrightarrow$ `j` stops at `7`.
3. Since $i < j$ ($1 < 7$), **swap `arr[i]` and `arr[j]`** (`6 ↔ 3`):

```text
Index:    0   1   2   3   4   5   6   7
Values: [ 4,  3,  2,  5,  7,  9,  1,  6 ]
              ▲                       ▲
              i                       j
```

4. **Continue scanning:**
   - Advance `i`: `arr[2]=2 <= 4`, `arr[3]=5 > 4` $\longrightarrow$ `i` stops at `3`.
   - Retreat `j`: `arr[7]=6 > 4`, `arr[6]=1 <= 4` $\longrightarrow$ `j` stops at `6`.
5. Since $i < j$ ($3 < 6$), **swap `arr[i]` and `arr[j]`** (`5 ↔ 1`):

```text
Index:    0   1   2   3   4   5   6   7
Values: [ 4,  3,  2,  1,  7,  9,  5,  6 ]
                          ▲   ▲
                          j   i   (pointers have crossed!)
```

6. **Advance `i` and `j` again:**
   - `i` advances until `arr[4] = 7 > 4` $\longrightarrow$ `i` stops at `4`.
   - `j` retreats until `arr[3] = 1 <= 4` $\longrightarrow$ `j` stops at `3`.
7. **Pointers have crossed ($i > j$):**
   - The scanning stops!
   - Now swap the **pivot (`arr[low]`)** with **`arr[j]`** (`4 ↔ 1`):

```text
Index:    0   1   2   3   4   5   6   7
Values: [ 1,  3,  2,  4,  7,  9,  5,  6 ]
          ─────────   ▲   ───────────────
          <= Pivot  PIVOT    > Pivot
```

> **Result:** `4` is now permanently in its correct sorted position (index `3`).
> - Left subarray: `[1, 3, 2]`
> - Right subarray: `[7, 9, 5, 6]`

---

## 3. Python Code Implementation

```python
def partition(arr, low, high):
    """
    Partitions subarray arr[low ... high] around pivot = arr[low].
    Places elements <= pivot on the left and > pivot on the right.
    Returns the final sorted index of the pivot.
    """
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        # Move `i` forward until finding an element strictly greater than pivot
        while arr[i] <= pivot and i <= high - 1:
            i += 1

        # Move `j` backward until finding an element smaller than or equal to pivot
        while arr[j] > pivot and j >= low + 1:
            j -= 1

        # If pointers have not crossed, swap the out-of-order pair
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # Swap pivot into its final sorted position (index j)
    arr[low], arr[j] = arr[j], arr[low]
    return j


def quick_sort_helper(arr, low, high):
    """
    Recursively sorts subarray arr[low ... high] around partition index.
    """
    if low < high:
        # Partition the array and get the pivot's fixed index
        p_index = partition(arr, low, high)

        # Recursively sort elements to the left and right of the pivot
        quick_sort_helper(arr, low, p_index - 1)
        quick_sort_helper(arr, p_index + 1, high)


def quick_sort(nums):
    """
    Main Quick Sort function. Sorts array in-place.
    """
    n = len(nums)
    if n > 1:
        quick_sort_helper(nums, 0, n - 1)
    return nums


# Driver Code
if __name__ == "__main__":
    nums = [4, 6, 2, 5, 7, 9, 1, 3]
    print("Original Array:", nums)
    sorted_nums = quick_sort(nums)
    print("Sorted Array:  ", sorted_nums)
```

### Output:

```text
Original Array: [4, 6, 2, 5, 7, 9, 1, 3]
Sorted Array:   [1, 2, 3, 4, 5, 6, 7, 9]
```

---

## 4. Deep Dive: The Partition Algorithm

### Why `i <= high - 1` and `j >= low + 1`?
- **`i <= high - 1`:** Prevents pointer `i` from walking off the right end of the array if all elements are $\le \text{pivot}$.
- **`j >= low + 1`:** Prevents pointer `j` from walking off the left end of the array if all elements are $> \text{pivot}$.
- Both checks guarantee that array indexing remains safely in bounds.

---

### Why Swap `arr[low]` with `arr[j]` (and NOT `arr[i]`)?
This is one of the most common conceptual interview questions!

- Pointer `i` stops at an element that is **strictly greater than the pivot** (`arr[i] > pivot`).
- Pointer `j` stops at an element that is **smaller than or equal to the pivot** (`arr[j] <= pivot`).
- When the pointers cross, $j < i$. Therefore, `j` is situated in the **left partition**, where every element must be $\le \text{pivot}$.
- If you swapped `arr[low]` with `arr[i]`, a value greater than the pivot would end up at index `low` (the left side), breaking the partition invariant!
- Swapping with `arr[j]` guarantees that the value moving to `low` is $\le \text{pivot}$.

---

### Why `p_index - 1` and `p_index + 1` in Recursive Calls?
```python
quick_sort_helper(arr, low, p_index - 1)
quick_sort_helper(arr, p_index + 1, high)
```
- The element at `p_index` is **already in its permanent, correct sorted position**.
- Including `p_index` in subsequent calls would be redundant and could lead to infinite recursion.
- We strictly exclude it by using `p_index - 1` for the left half and `p_index + 1` for the right half.

---

## 5. Detailed Dry Run Table

Trace of `partition` on `arr = [4, 6, 2, 5, 7, 9, 1, 3]`, with `low = 0, high = 7, pivot = 4`:

| Step | `i` Index (`arr[i]`) | `j` Index (`arr[j]`) | Condition ($i < j$) | Action | Array State |
| :---: | :---: | :---: | :---: | :--- | :--- |
| **Start** | $0$ (`4`) | $7$ (`3`) | — | Initialize | `[4, 6, 2, 5, 7, 9, 1, 3]` |
| **Scan 1** | $1$ (`6 > 4`) | $7$ (`3 <= 4`) | $1 < 7$ (True) | Swap `arr[1]` & `arr[7]` | `[4, 3, 2, 5, 7, 9, 1, 6]` |
| **Scan 2** | $3$ (`5 > 4`) | $6$ (`1 <= 4`) | $3 < 6$ (True) | Swap `arr[3]` & `arr[6]` | `[4, 3, 2, 1, 7, 9, 5, 6]` |
| **Scan 3** | $4$ (`7 > 4`) | $3$ (`1 <= 4`) | $4 < 3$ (False) | Pointers crossed $\rightarrow$ Stop loop | `[4, 3, 2, 1, 7, 9, 5, 6]` |
| **Final** | — | $3$ | — | Swap `arr[low]` with `arr[j]` (`4 ↔ 1`) | `[1, 3, 2, 4, 7, 9, 5, 6]` |

**Returned `p_index`:** `3` (Value `4` is settled!).

---

## 6. Complexity Analysis & The Worst-Case Trap

| Case | Time Complexity | When Does It Occur? | Recurrence Relation |
| :--- | :---: | :--- | :--- |
| **Best Case** | $\mathbf{\mathcal{O}(N \log N)}$ | Pivot consistently splits array into two equal halves. | $T(N) = 2T(N/2) + \mathcal{O}(N)$ |
| **Average Case** | $\mathbf{\mathcal{O}(N \log N)}$ | Random data; pivot splits array in balanced proportions. | $T(N) = T(k) + T(N - k - 1) + \mathcal{O}(N)$ |
| **Worst Case** | $\mathbf{\mathcal{O}(N^2)}$ | Array is already sorted or reverse-sorted, and pivot is chosen as `arr[low]`. | $T(N) = T(N - 1) + \mathcal{O}(N)$ |

### Space Complexity:
$$\text{Auxiliary Space} = \mathcal{O}(1) \quad (\text{In-place array modifications})$$
$$\text{Recursion Call Stack Space} = \begin{cases} \mathcal{O}(\log N) & \text{Best / Average Case} \\ \mathcal{O}(N) & \text{Worst Case} \end{cases}$$

---

### The Worst-Case Trap ($\mathcal{O}(N^2)$)

Suppose the array is already sorted: `[1, 2, 3, 4, 5]`.
- Picking `pivot = arr[0] = 1` yields partitions of size $0$ and size $4$.
- Next call picks `2`, yielding partitions of size $0$ and size $3$.
- The recursion depth becomes $N$ instead of $\log N$, resulting in:

$$\text{Work} = N + (N - 1) + (N - 2) + \dots + 1 = \frac{N(N + 1)}{2} = \mathcal{O}(N^2)$$

### How to Prevent the Worst Case?
1. **Randomized Quick Sort:** Choose a random index between `low` and `high` and swap it with `arr[low]` before partitioning.
2. **Median-of-Three:** Pick the median of `arr[low]`, `arr[mid]`, and `arr[high]` as the pivot.

---

## 7. Comparison: Quick Sort vs. Merge Sort

| Property | Quick Sort | Merge Sort |
| :--- | :--- | :--- |
| **Paradigm** | Divide & Conquer (Work done during **Partition**) | Divide & Conquer (Work done during **Merge**) |
| **Best Time** | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N \log N)$ |
| **Worst Time** | $\mathcal{O}(N^2)$ *(Can be mitigated)* | $\mathbf{\mathcal{O}(N \log N)}$ *(Guaranteed)* |
| **Auxiliary Memory** | $\mathbf{\mathcal{O}(1)}$ *(Only $\mathcal{O}(\log N)$ stack)* | $\mathcal{O}(N)$ *(Requires temporary array)* |
| **In-place?** | **Yes** ✅ | **No** ❌ |
| **Stable?** | **No** ❌ | **Yes** ✅ |
| **Cache Locality** | **Excellent** (Sequentially scans contiguous blocks) | Moderate |
| **Best Suited For** | Arrays / Internal in-memory sorting | Linked Lists / External sorting (Large datasets) |

---

## 8. Important Interview Points & FAQs

| Question | Answer | Details |
| :--- | :---: | :--- |
| **Is Quick Sort stable?** | **No** ❌ | Long-distance swaps around the pivot can change the relative order of duplicate elements. |
| **Why is Quick Sort usually faster than Merge Sort in practice?** | Cache Locality | Quick Sort works strictly in-place and has exceptional memory cache performance (spatial locality) with low constant factors. |
| **Which pivot choice is best?** | Randomized / Median | Avoids the $\mathcal{O}(N^2)$ degenerate case on sorted or reverse-sorted inputs. |
| **Can Quick Sort be used on Linked Lists?** | Possible, but Merge Sort is better | Quick Sort requires random access / backward scanning (`j -= 1`), which is inefficient on singly linked lists. |

---

## 9. 5-Minute Quick Revision 🧠

```text
QUICK SORT PIPELINE:
           ┌────────────────────────┐
           │   arr[low ... high]    │
           └───────────┬────────────┘
                       │
              partition(low, high)
              [Pivot placed at j]
                       │
         ┌─────────────┴─────────────┐
         ▼                           ▼
quick_sort(low, p - 1)      quick_sort(p + 1, high)
  [Left <= Pivot]              [Right > Pivot]
```

### 🎯 One-Line Memory Trick:
> *"Quick Sort puts the pivot in its correct spot, pushes smaller elements left, larger elements right, and recurses."*

### 🔑 Critical Code Pattern:
```python
p_index = partition(arr, low, high)
quick_sort_helper(arr, low, p_index - 1)
quick_sort_helper(arr, p_index + 1, high)
```

---

## ✍️ Short Handwritten Interview Notes

```text
============================================================
                        QUICK SORT
============================================================

PARADIGM: Divide and Conquer

CORE IDEA:
  1. Pick pivot: arr[low].
  2. Partition: Put elements <= pivot on left, > pivot on right.
  3. Place pivot at its final spot (index j).
  4. Recurse on [low ... j - 1] and [j + 1 ... high].

PARTITION ALGORITHM:
  pivot = arr[low]
  i = low, j = high
  while i < j:
      while arr[i] <= pivot and i <= high - 1: i += 1
      while arr[j] > pivot and j >= low + 1:  j -= 1
      if i < j: swap(arr[i], arr[j])
  swap(arr[low], arr[j])
  return j

COMPLEXITY:
  Time:
    Best    : O(N log N)
    Average : O(N log N)
    Worst   : O(N²) (sorted array with bad pivot)
  Space:
    O(1) extra space (in-place)
    O(log N) stack (O(N) worst case)

PROPERTIES:
  - Stable:   NO
  - In-place: YES
  - Cache-friendly: YES

KEY MANTRA:
  PICK PIVOT  -->  PARTITION  -->  RECURSE BOTH SIDES
============================================================
```
