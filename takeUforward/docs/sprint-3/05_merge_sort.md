# 🔹 Merge Sort

A comprehensive guide, step-by-step breakdown, tree visualization, code deep-dive, dry run, complexity analysis, and quick-revision interview notes for **Merge Sort**.

---

## Table of Contents

- [1. Intuition (Divide and Conquer)](#1-intuition-divide-and-conquer)
- [2. Understand the Two Functions](#2-understand-the-two-functions)
  - [A. `mergeSortHelper(arr, low, high)`](#a-mergesorthelperarr-low-high)
  - [B. `merge(arr, low, mid, high)`](#b-mergearr-low-mid-high)
- [3. Python Code Implementation](#3-python-code-implementation)
- [4. Step-by-Step Dry Run & Recursion Tree](#4-step-by-step-dry-run--recursion-tree)
- [5. Deep Dive: Critical Code Nuances](#5-deep-dive-critical-code-nuances)
  - [Why `mid = (low + high) // 2`?](#why-mid--low--high--2)
  - [Why `while left <= mid` and `while right <= high`?](#why-while-left--mid-and-while-right--high)
  - [Why `arr[i] = temp[i - low]`?](#why-arri--tempi---low)
  - [Why `<=` Instead of `<` in `arr[left] <= arr[right]`? (Stability)](#why--instead-of--in-arrleft--arrright-stability)
- [6. Complexity Analysis & Derivation](#6-complexity-analysis--derivation)
- [7. Comparison Table: Selection vs. Bubble vs. Insertion vs. Merge Sort](#7-comparison-table-selection-vs-bubble-vs-insertion-vs-merge-sort)
- [8. Important Interview Points & FAQs](#8-important-interview-points--faqs)
- [9. 5-Minute Quick Revision 🧠](#9-5-minute-quick-revision-)
- [✍️ Short Handwritten Interview Notes](#-short-handwritten-interview-notes)

---

## 1. Intuition (Divide and Conquer)

**Merge Sort** is a classic **Divide and Conquer** sorting algorithm. Unlike simple $\mathcal{O}(N^2)$ algorithms (like Selection Sort and Bubble Sort), Merge Sort runs in guaranteed $\mathcal{O}(N \log N)$ time across all scenarios, making it highly effective for large datasets.

### The Three Phases:

$$\text{\bf Merge Sort} = \text{\bf Divide} \longrightarrow \text{\bf Sort (Recurse)} \longrightarrow \text{\bf Merge}$$

1. **Divide:** Repeatedly split the array into two halves at the midpoint until every subarray contains only a single element.
2. **Sort (Base Case):** A subarray of size $1$ is inherently sorted by definition ($low \ge high$).
3. **Merge:** Combine two adjacent sorted subarrays back together in sorted order into a single larger sorted subarray.

---

### Visual Walkthrough of Dividing and Merging

Consider the array: `[9, 4, 7, 6, 3, 1, 5]`

```text
                     [ 9, 4, 7, 6, 3, 1, 5 ]
                             /      \
               [ 9, 4, 7, 6 ]        [ 3, 1, 5 ]            <-- DIVIDE
                 /        \            /     \
             [ 9, 4 ]    [ 7, 6 ]    [ 3, 1 ]  [ 5 ]
              /    \      /    \      /    \     |
            [9]   [4]   [7]   [6]   [3]   [1]   [5]         <-- BASE CASES (Size 1)
             \    /       \    /      \    /     |
             [ 4, 9 ]    [ 6, 7 ]    [ 1, 3 ]   [ 5 ]       <-- MERGE
                 \        /            \     /
               [ 4, 6, 7, 9 ]        [ 1, 3, 5 ]
                       \                 /
                     [ 1, 3, 4, 5, 6, 7, 9 ]                <-- FULLY SORTED
```

> [!IMPORTANT]
> A single element is already sorted. Merge Sort exploits this fundamental invariant as its recursive base case.

---

## 2. Understand the Two Functions

Merge Sort is split cleanly into two distinct helper operations:

```text
mergeSortHelper()  -->  DIVIDES the array range recursively
merge()            -->  COMBINES two already-sorted adjacent ranges
```

---

### A. `mergeSortHelper(arr, low, high)`

Its sole responsibility is to find the midpoint and delegate work to smaller ranges:

- **`low`**: Starting index of the current range.
- **`high`**: Ending index of the current range.
- **`mid`**: Middle index calculated as `(low + high) // 2`.

```python
# Base case: single element (low == high) or invalid range (low > high)
if low >= high:
    return

mid = (low + high) // 2

# Recursively divide and sort both halves
mergeSortHelper(arr, low, mid)       # Left half:  low -> mid
mergeSortHelper(arr, mid + 1, high)  # Right half: mid + 1 -> high

# Merge the two sorted halves
merge(arr, low, mid, high)
```

---

### B. `merge(arr, low, mid, high)`

Combines two adjacent sorted subarrays:
- **Left half:** indices `low` through `mid`
- **Right half:** indices `mid + 1` through `high`

#### The Two-Pointer Merging Technique:
1. Initialize two pointers:
   - `left = low` (tracks left half)
   - `right = mid + 1` (tracks right half)
2. Compare `arr[left]` and `arr[right]`:
   - Append the smaller element to a temporary array `temp`.
   - Increment the pointer of whichever element was chosen.
3. If one subarray runs out of elements first, copy all remaining elements from the other subarray into `temp`.
4. Copy the sorted elements from `temp` back into `arr[low ... high]`.

---

## 3. Python Code Implementation

```python
class Solution:

    def merge(self, arr, low, mid, high):
        """
        Merges two adjacent sorted subarrays:
        Left:  arr[low ... mid]
        Right: arr[mid + 1 ... high]
        """
        temp = []
        left = low
        right = mid + 1

        # Step 1: Compare elements from both halves and pick the smaller
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        # Step 2: Copy any remaining elements from left half
        while left <= mid:
            temp.append(arr[left])
            left += 1

        # Step 3: Copy any remaining elements from right half
        while right <= high:
            temp.append(arr[right])
            right += 1

        # Step 4: Copy merged elements from temp back into arr[low ... high]
        for i in range(low, high + 1):
            arr[i] = temp[i - low]

    def mergeSortHelper(self, arr, low, high):
        """
        Recursively divides the array and triggers merging.
        """
        # Base case: 1 element or invalid range
        if low >= high:
            return

        mid = (low + high) // 2

        # Divide left and right
        self.mergeSortHelper(arr, low, mid)
        self.mergeSortHelper(arr, mid + 1, high)

        # Merge the two sorted halves
        self.merge(arr, low, mid, high)

    def mergeSort(self, nums):
        """
        Public entry point for Merge Sort.
        """
        n = len(nums)
        if n > 1:
            self.mergeSortHelper(nums, 0, n - 1)
        return nums


# Driver Code
if __name__ == "__main__":
    arr = [9, 4, 7, 6, 3, 1, 5]
    sol = Solution()
    print("Original Array:", arr)
    sorted_arr = sol.mergeSort(arr)
    print("Sorted Array:  ", sorted_arr)
```

### Output:

```text
Original Array: [9, 4, 7, 6, 3, 1, 5]
Sorted Array:   [1, 3, 4, 5, 6, 7, 9]
```

---

## 4. Step-by-Step Dry Run & Recursion Tree

Let us dry run a 4-element array:

$$\text{arr} = [9, 4, 7, 6]$$

### Phase 1: Divide

1. Initial call: `mergeSortHelper(arr, low=0, high=3)`
   - $mid = (0 + 3) // 2 = 1$
   - Divides into:
     - Left branch: `mergeSortHelper(arr, 0, 1)` $\rightarrow [9, 4]$
     - Right branch: `mergeSortHelper(arr, 2, 3)` $\rightarrow [7, 6]$

2. Left branch `[9, 4]` ($low=0, high=1$):
   - $mid = (0 + 1) // 2 = 0$
   - Divides into `[9]` ($low=0, high=0$) and `[4]` ($low=1, high=1$).
   - Both hit base case ($low \ge high$) and return.

3. Right branch `[7, 6]` ($low=2, high=3$):
   - $mid = (2 + 3) // 2 = 2$
   - Divides into `[7]` ($low=2, high=2$) and `[6]` ($low=3, high=3$).
   - Both hit base case and return.

---

### Phase 2: Merge

#### 1. Merge `[9]` and `[4]` ($low=0, mid=0, high=1$)
- Compare $9$ vs $4 \longrightarrow$ append $4$ to `temp`.
- Left pointer has $9$ remaining $\longrightarrow$ append $9$.
- `temp = [4, 9]` copied back to `arr[0...1]`.
- Array becomes: `[4, 9, 7, 6]`

#### 2. Merge `[7]` and `[6]` ($low=2, mid=2, high=3$)
- Compare $7$ vs $6 \longrightarrow$ append $6$ to `temp`.
- Left pointer has $7$ remaining $\longrightarrow$ append $7$.
- `temp = [6, 7]` copied back to `arr[2...3]`.
- Array becomes: `[4, 9, 6, 7]`

#### 3. Top-level Merge: `[4, 9]` and `[6, 7]` ($low=0, mid=1, high=3$)
- Left half: `[4, 9]` (`left = 0`, `mid = 1`)
- Right half: `[6, 7]` (`right = 2`, `high = 3`)

| Step | Comparison | Element Picked | Reason | `temp` Array State | `left` Pointer | `right` Pointer |
| :---: | :---: | :---: | :--- | :--- | :---: | :---: |
| **1** | `arr[0]=4` vs `arr[2]=6` | **`4`** | $4 \le 6$ | `[4]` | $1$ | $2$ |
| **2** | `arr[1]=9` vs `arr[2]=6` | **`6`** | $6 < 9$ | `[4, 6]` | $1$ | $3$ |
| **3** | `arr[1]=9` vs `arr[3]=7` | **`7`** | $7 < 9$ | `[4, 6, 7]` | $1$ | $4$ (exhausted) |
| **4** | Leftover in left half | **`9`** | Right exhausted, copy remaining | `[4, 6, 7, 9]` | $2$ (exhausted) | $4$ |

Copy `temp` back into `arr[0...3]`:
$$\mathbf{[4, 6, 7, 9] \quad \text{Sorted!}}$$

---

## 5. Deep Dive: Critical Code Nuances

### Why `mid = (low + high) // 2`?
- Uses integer floor division to isolate the middle index.
- If the subarray length is even, it divides cleanly into two halves of equal length.
- If the subarray length is odd, the left half will contain one more element than the right half (e.g., $low=0, high=4 \implies mid=2$, so left has indices $0, 1, 2$ [size 3], and right has indices $3, 4$ [size 2]).
- Sizes differ by at most 1.

> [!NOTE]
> In languages like Java or C++ where integer overflow can occur when `low + high > Integer.MAX_VALUE`, you write `mid = low + (high - low) // 2`. In Python, integers have arbitrary precision, but `low + (high - low) // 2` is still good practice.

---

### Why `while left <= mid` and `while right <= high`?
- The left subarray spans the closed interval `[low, mid]`. Since `mid` is part of the left half, `left <= mid` ensures the last element of the left half is not missed.
- The right subarray spans `[mid + 1, high]`. Since `high` is the last valid index, `right <= high` ensures the final right-side element is included.

---

### Why `arr[i] = temp[i - low]`?
```python
for i in range(low, high + 1):
    arr[i] = temp[i - low]
```
- `arr` uses **absolute indices** in the original array (e.g., `low = 4, high = 6`).
- `temp` is a fresh list that always starts at **index `0`**.
- To map absolute index `i` into `temp`, we subtract `low`:
  - When $i = low \implies temp[low - low] = temp[0]$
  - When $i = low + 1 \implies temp[low + 1 - low] = temp[1]$
  - When $i = high \implies temp[high - low]$

---

### Why `<=` Instead of `<` in `arr[left] <= arr[right]`? (Stability)
```python
if arr[left] <= arr[right]:
    temp.append(arr[left])
    left += 1
```
- When two elements are equal (`arr[left] == arr[right]`), the `<=` condition **forces the left element to be picked first**.
- Because the element from the left half originally appeared earlier in the array than the element from the right half, picking it first **preserves their relative order**.
- This makes standard Merge Sort **STABLE** ✅.
- If you used `<` instead of `<=`, equal elements from the right half would be placed first, breaking stability!

---

## 6. Complexity Analysis & Derivation

| Case | Time Complexity | Auxiliary Space | Stable? | In-Place? |
| :--- | :---: | :---: | :---: | :---: |
| **Best Case** | $\mathbf{\mathcal{O}(N \log N)}$ | $\mathcal{O}(N)$ | **Yes** ✅ | **No** ❌ |
| **Average Case** | $\mathbf{\mathcal{O}(N \log N)}$ | $\mathcal{O}(N)$ | **Yes** ✅ | **No** ❌ |
| **Worst Case** | $\mathbf{\mathcal{O}(N \log N)}$ | $\mathcal{O}(N)$ | **Yes** ✅ | **No** ❌ |

---

### Why is the Time Complexity Always $\mathcal{O}(N \log N)$?

We can analyze Merge Sort using the recursion tree:

```text
Level 0:                 [ N ]                   -->  Work = N
                        /     \
Level 1:           [ N/2 ]   [ N/2 ]             -->  Work = N/2 + N/2 = N
                   /   \     /   \
Level 2:       [N/4] [N/4] [N/4] [N/4]           -->  Work = 4 * (N/4) = N
                 ...   ...   ...   ...
Level log N:   [1]   [1]   [1]  ...  [1]         -->  Work = N * 1 = N
```

1. **Number of Levels:**
   - The array of size $N$ is repeatedly halved: $N \rightarrow \frac{N}{2} \rightarrow \frac{N}{4} \rightarrow \dots \rightarrow 1$.
   - The number of times you can divide $N$ by $2$ until reaching $1$ is $\mathbf{\log_2 N}$.
2. **Work Done Per Level:**
   - At every level, all $N$ elements are merged across the various subarrays.
   - Merging two subarrays of sizes $A$ and $B$ takes $\mathcal{O}(A + B)$ time. Across the entire level, the sum of all sizes is exactly $N$.
3. **Total Time:**

$$\text{Total Time} = (\text{Work per level}) \times (\text{Number of levels}) = N \times \log_2 N = \mathbf{\mathcal{O}(N \log N)}$$

> **Recurrence Relation:**
> $$T(N) = 2T\left(\frac{N}{2}\right) + \mathcal{O}(N)$$
> By Master's Theorem: $a=2, b=2, d=1 \implies \log_b a = \log_2 2 = 1 = d \implies \mathbf{T(N) = \mathcal{O}(N \log N)}$.

---

### Space Complexity Breakdown

$$\text{Auxiliary Space} = \mathbf{\mathcal{O}(N)}$$

- **Call Stack Memory:** Depth of recursion is the height of the tree, which is $\mathcal{O}(\log N)$.
- **Temporary Array Memory:** The `temp` buffer created during `merge()` stores up to $N$ elements at the top-level merge.
- Dominant term: $\mathcal{O}(N) + \mathcal{O}(\log N) = \mathbf{\mathcal{O}(N)}$.
- Hence, Merge Sort is **not in-place** for standard array implementations.

---

## 7. Comparison Table: Selection vs. Bubble vs. Insertion vs. Merge Sort

| Property | Selection Sort | Bubble Sort (Optimized) | Insertion Sort | Merge Sort |
| :--- | :---: | :---: | :---: | :---: |
| **Best Time** | $\mathcal{O}(N^2)$ | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | $\mathbf{\mathcal{O}(N \log N)}$ |
| **Average Time** | $\mathcal{O}(N^2)$ | $\mathcal{O}(N^2)$ | $\mathcal{O}(N^2)$ | $\mathbf{\mathcal{O}(N \log N)}$ |
| **Worst Time** | $\mathcal{O}(N^2)$ | $\mathcal{O}(N^2)$ | $\mathcal{O}(N^2)$ | $\mathbf{\mathcal{O}(N \log N)}$ |
| **Auxiliary Space** | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathbf{\mathcal{O}(N)}$ |
| **Stable?** | No ❌ | Yes ✅ | Yes ✅ | **Yes** ✅ |
| **In-place?** | Yes ✅ | Yes ✅ | Yes ✅ | **No** ❌ |
| **Paradigm** | Selection | Adjacent Comparison | Insertion / Shifting | **Divide & Conquer** |
| **Best Use Case** | Minimize writes | Nearly sorted / small | Small or online data | **Large arrays / Linked Lists** |

---

## 8. Important Interview Points & FAQs

| Question | Answer | Explanation |
| :--- | :---: | :--- |
| **Is Merge Sort stable?** | **Yes** ✅ | Because we use `arr[left] <= arr[right]`, whenever duplicate elements appear, the element in the left half is prioritized, preserving relative order. |
| **Is Merge Sort in-place?** | **No** ❌ | Requires $\mathcal{O}(N)$ additional space for the auxiliary merging array. *(In-place merge sort exists theoretically, but has high constant factors and is complex).* |
| **Why is Merge Sort preferred for Linked Lists?** | **Best for LLs** ✅ | In a Linked List, elements can be merged by rewiring pointers in $\mathcal{O}(1)$ extra space! No random access is needed, making Merge Sort $\mathcal{O}(N \log N)$ time and $\mathcal{O}(1)$ auxiliary space on Linked Lists. |
| **What is the worst-case time complexity?** | $\mathcal{O}(N \log N)$ | Guaranteed $\mathcal{O}(N \log N)$. Unlike Quick Sort (which can degrade to $\mathcal{O}(N^2)$ on bad pivots), Merge Sort never degrades. |
| **Does it work on streaming data?** | External sorting | Merge Sort is the foundation of **External Merge Sort**, which is used when dataset sizes exceed RAM capacity (e.g., sorting 1 TB file using 8 GB RAM). |

---

## 9. 5-Minute Quick Revision 🧠

```text
MERGE SORT PIPELINE:
           ┌────────────────────────┐
           │        Array           │
           └───────────┬────────────┘
                       │
             mid = (low + high) // 2
                       │
         ┌─────────────┴─────────────┐
         ▼                           ▼
mergeSortHelper(low, mid)   mergeSortHelper(mid+1, high)
         │                           │
         └─────────────┬─────────────┘
                       ▼
            merge(low, mid, high)
            [Two-Pointer Combine]
                       │
                       ▼
                  Sorted Array!
```

### 🎯 One-Line Memory Trick:
> *"Merge Sort cuts the problem in half until it reaches size 1, then stitches sorted halves together with two pointers."*

### 🔑 Critical Code Lines:
```python
mid = (low + high) // 2
self.mergeSortHelper(arr, low, mid)
self.mergeSortHelper(arr, mid + 1, high)
self.merge(arr, low, mid, high)
```

---

## ✍️ Short Handwritten Interview Notes

```text
============================================================
                        MERGE SORT
============================================================

PARADIGM: Divide and Conquer

CORE IDEA:
  1. Divide: Split range into [low...mid] and [mid+1...high].
  2. Recurse: Recursively sort both halves.
  3. Merge: Combine two sorted halves using 2 pointers.

ALGORITHM:
  mergeSortHelper(arr, low, high):
    if low >= high: return
    mid = (low + high) // 2
    mergeSortHelper(arr, low, mid)
    mergeSortHelper(arr, mid + 1, high)
    merge(arr, low, mid, high)

MERGE LOGIC:
  left = low, right = mid + 1, temp = []
  while left <= mid and right <= high:
      if arr[left] <= arr[right]:  # '<=' ensures STABILITY
          temp.append(arr[left]); left += 1
      else:
          temp.append(arr[right]); right += 1
  append leftovers from left and right halves
  copy temp back: arr[low...high] = temp[:]

COMPLEXITY:
  Time:
    Best    : O(N log N)
    Average : O(N log N)
    Worst   : O(N log N)
  Space:
    O(N) auxiliary space (temp buffer) + O(log N) stack

PROPERTIES:
  - Stable:   YES (with <= check)
  - In-place: NO (requires O(N) temp array)
  - Preferred for: Linked Lists and External Sorting

KEY MANTRA:
  DIVIDE AT MID  -->  RECURSE HALVES  -->  TWO-POINTER MERGE
============================================================
```
