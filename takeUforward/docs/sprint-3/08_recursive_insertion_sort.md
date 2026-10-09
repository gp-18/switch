# 🔹 Recursive Insertion Sort

A comprehensive guide, recursion mechanics, dry run, invariant analysis, iterative vs. recursive comparison, and quick-revision interview notes for **Recursive Insertion Sort**.

---

## Table of Contents

- [1. Intuition (Replacing the Outer Loop with Recursion)](#1-intuition-replacing-the-outer-loop-with-recursion)
- [2. How Does It Work? (Visual Walkthrough)](#2-how-does-it-work-visual-walkthrough)
- [3. Python Code Implementation](#3-python-code-implementation)
- [4. Deep Dive: Anatomy of the Recursive Call](#4-deep-dive-anatomy-of-the-recursive-call)
  - [The Base Case (`i >= n`)](#the-base-case-i--n)
  - [The Invariant: Sorted Prefix `nums[0 ... i - 1]`](#the-invariant-sorted-prefix-nums0--i---1)
  - [Shifting and Key Insertion](#shifting-and-key-insertion)
  - [Tail Recursive Step (`i + 1`)](#tail-recursive-step-i--1)
  - [Alternative Formulation: Head Recursion on Size $n$](#alternative-formulation-head-recursion-on-size-n)
- [5. Detailed Dry Run & Call Stack Trace](#5-detailed-dry-run--call-stack-trace)
- [6. Complexity Analysis](#6-complexity-analysis)
- [7. Iterative Insertion Sort vs. Recursive Insertion Sort](#7-iterative-insertion-sort-vs-recursive-insertion-sort)
- [8. Important Interview Points & FAQs](#8-important-interview-points--faqs)
- [9. 5-Minute Quick Revision 🧠](#9-5-minute-quick-revision-)
- [✍️ Short Handwritten Interview Notes](#-short-handwritten-interview-notes)

---

## 1. Intuition (Replacing the Outer Loop with Recursion)

In **Iterative Insertion Sort**, we use an outer loop `for i in range(1, n)` to pick elements one by one and insert them into the already-sorted prefix `nums[0 ... i - 1]`.

In **Recursive Insertion Sort**, recursion takes charge of incrementing the boundary index $i$:
- The recursive function receives the current index `i` (starting at $1$).
- At each step, it stores `key = nums[i]`, shifts all elements in the sorted prefix `nums[0 ... i - 1]` that are greater than `key` to the right, and inserts `key`.
- After insertion, the sorted subarray expands to `nums[0 ... i]`.
- The function then makes a recursive call for the next element: `i + 1`.

$$\text{\bf Recursive Insertion Sort} = \text{\bf Insert } \text{nums}[i] \text{ into Sorted Prefix } \longrightarrow \text{\bf Recurse on } i + 1$$

---

## 2. How Does It Work? (Visual Walkthrough)

Consider:

$$\text{nums} = [13, 46, 24, 52, 20, 9], \quad n = 6$$

We begin at index $i = 1$:

---

### Call 1: `recursive_insertion_sort(nums, i = 1, n = 6)`
- Sorted prefix: `[13]`
- `key = nums[1] = 46`
- $46 > 13 \longrightarrow$ No shifts. Insert at index $1$.
- Sorted prefix becomes: `[13, 46]`
- Recurse: `i = 2`.

---

### Call 2: `recursive_insertion_sort(nums, i = 2, n = 6)`
- Sorted prefix: `[13, 46]`
- `key = nums[2] = 24`
- $24 < 46 \longrightarrow$ Shift $46$ right.
- $24 > 13 \longrightarrow$ Stop. Insert $24$ at index $1$.
- Sorted prefix becomes: `[13, 24, 46]`
- Recurse: `i = 3`.

---

### Call 3: `recursive_insertion_sort(nums, i = 3, n = 6)`
- Sorted prefix: `[13, 24, 46]`
- `key = nums[3] = 52`
- $52 > 46 \longrightarrow$ No shifts. Insert at index $3$.
- Sorted prefix becomes: `[13, 24, 46, 52]`
- Recurse: `i = 4`.

---

### Call 4: `recursive_insertion_sort(nums, i = 4, n = 6)`
- Sorted prefix: `[13, 24, 46, 52]`
- `key = nums[4] = 20`
- Shift $52$, shift $46$, shift $24$. Stop before $13$.
- Insert $20$ at index $1$.
- Sorted prefix becomes: `[13, 20, 24, 46, 52]`
- Recurse: `i = 5`.

---

### Call 5: `recursive_insertion_sort(nums, i = 5, n = 6)`
- Sorted prefix: `[13, 20, 24, 46, 52]`
- `key = nums[5] = 9`
- Shift $52, 46, 24, 20, 13$. Insert $9$ at index $0$.
- Sorted prefix becomes: `[9, 13, 20, 24, 46, 52]`
- Recurse: `i = 6`.

---

### Call 6: `recursive_insertion_sort(nums, i = 6, n = 6)`
- $i \ge n \longrightarrow$ **Base Case Reached!**
- Returns fully sorted array: `[9, 13, 20, 24, 46, 52]`. ✅

---

## 3. Python Code Implementation

```python
def recursive_insertion_sort(nums, i, n):
    """
    Recursively sorts nums by inserting nums[i] into the sorted prefix nums[0 ... i - 1].
    """
    # Base Case: All elements from index 1 to n - 1 have been inserted
    if i >= n:
        return nums

    key = nums[i]
    j = i - 1

    # Shift elements strictly greater than key one position to the right
    while j >= 0 and nums[j] > key:
        nums[j + 1] = nums[j]
        j -= 1

    # Place key in its correct position
    nums[j + 1] = key

    # Recurse for the next index i + 1
    return recursive_insertion_sort(nums, i + 1, n)


# Driver Code
if __name__ == "__main__":
    nums = [13, 46, 24, 52, 20, 9]
    print("Original Array:", nums)
    sorted_nums = recursive_insertion_sort(nums, 1, len(nums))
    print("Sorted Array:  ", sorted_nums)
```

### Output:

```text
Original Array: [13, 46, 24, 52, 20, 9]
Sorted Array:   [9, 13, 20, 24, 46, 52]
```

---

## 4. Deep Dive: Anatomy of the Recursive Call

### The Base Case (`i >= n`)
- Indexing begins at $i = 1$ because a single element `nums[0]` is sorted by definition.
- When $i = n$, every element up to index $n - 1$ has been inserted into its proper place.
- The recursion stops and returns the array.

---

### The Invariant: Sorted Prefix `nums[0 ... i - 1]`
- When `recursive_insertion_sort(nums, i, n)` is called, the prefix `nums[0 ... i - 1]` is **strictly sorted**.
- The current call's job is to insert `nums[i]` into that sorted prefix.
- Once inserted, the prefix `nums[0 ... i]` is sorted, maintaining the invariant for call `i + 1`.

---

### Shifting and Key Insertion
```python
while j >= 0 and nums[j] > key:
    nums[j + 1] = nums[j]
    j -= 1
nums[j + 1] = key
```
- Shifting values rightwards creates a slot for `key`.
- Using `nums[j] > key` (strictly greater) guarantees **Stability** because equal elements are never shifted past each other.

---

### Alternative Formulation: Head Recursion on Size $n$
Another way interviewers write Recursive Insertion Sort is top-down (head recursion):
```python
def recursive_insertion_sort_head(arr, n):
    # Base case
    if n <= 1:
        return

    # Sort first n - 1 elements first
    recursive_insertion_sort_head(arr, n - 1)

    # Insert last element into sorted array
    key = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
```
- **Forward version (tail-like):** Inserts from index $1 \to n - 1$.
- **Backward version (head-like):** Recursively sorts $n - 1$ first, then inserts the $n^{\text{th}}$ element on the return journey. Both achieve the exact same result!

---

## 5. Detailed Dry Run & Call Stack Trace

Call stack trace for `nums = [13, 46, 24, 52, 20, 9]` with $n = 6$:

```text
Call 1: recursive_insertion_sort(nums, i=1, n=6)
 │      --> key = 46. No shift. Array: [13, 46, 24, 52, 20, 9]
 ▼
Call 2: recursive_insertion_sort(nums, i=2, n=6)
 │      --> key = 24. Shifts 46. Array: [13, 24, 46, 52, 20, 9]
 ▼
Call 3: recursive_insertion_sort(nums, i=3, n=6)
 │      --> key = 52. No shift. Array: [13, 24, 46, 52, 20, 9]
 ▼
Call 4: recursive_insertion_sort(nums, i=4, n=6)
 │      --> key = 20. Shifts 52, 46, 24. Array: [13, 20, 24, 46, 52, 9]
 ▼
Call 5: recursive_insertion_sort(nums, i=5, n=6)
 │      --> key = 9. Shifts 52, 46, 24, 20, 13. Array: [9, 13, 20, 24, 46, 52]
 ▼
Call 6: recursive_insertion_sort(nums, i=6, n=6)
        --> Base Case hit (i >= 6)! Returns nums.
```

---

## 6. Complexity Analysis

| Case | Time Complexity | Call Stack Space | Stable? |
| :--- | :---: | :---: | :---: |
| **Best Case** | $\mathbf{\mathcal{O}(N)}$ *(already sorted)* | $\mathcal{O}(N)$ frames | **Yes** ✅ |
| **Average Case** | $\mathbf{\mathcal{O}(N^2)}$ | $\mathcal{O}(N)$ frames | **Yes** ✅ |
| **Worst Case** | $\mathbf{\mathcal{O}(N^2)}$ *(reverse sorted)* | $\mathcal{O}(N)$ frames | **Yes** ✅ |

### Space Complexity Note:
- While **Iterative Insertion Sort** takes $\mathcal{O}(1)$ space, the recursive version allocates **$\mathcal{O}(N)$ frames on the call stack**.

---

## 7. Iterative Insertion Sort vs. Recursive Insertion Sort

| Metric | Iterative Insertion Sort | Recursive Insertion Sort |
| :--- | :--- | :--- |
| **Outer Loop** | `for i in range(1, n)` | Recursive parameter `i + 1` |
| **Inner Loop** | `while j >= 0 and nums[j] > key:` | Same `while` loop inside each call |
| **Time Complexity** | Best: $\mathcal{O}(N)$, Worst: $\mathcal{O}(N^2)$ | Best: $\mathcal{O}(N)$, Worst: $\mathcal{O}(N^2)$ |
| **Space Complexity** | **$\mathcal{O}(1)$** (In-place) | **$\mathcal{O}(N)$** (Stack frames) |
| **Stability** | **Stable** ✅ | **Stable** ✅ |
| **When to Use?** | Production / small arrays / Timsort | Interviews evaluating recursion fundamentals |

---

## 8. Important Interview Points & FAQs

| Question | Answer | Details |
| :--- | :---: | :--- |
| **Is Recursive Insertion Sort stable?** | **Yes** ✅ | `nums[j] > key` strictly avoids shifting equal elements, preserving initial order. |
| **Is it in-place?** | Modifies array in-place | Array is modified in-place, but auxiliary stack uses $\mathcal{O}(N)$ memory. |
| **Is it adaptive?** | **Yes** ✅ | On sorted inputs, the while loop never executes, achieving $\mathcal{O}(N)$ total comparisons. |

---

## 9. 5-Minute Quick Revision 🧠

```text
RECURSIVE INSERTION SORT FLOW:
  recursive_insertion_sort(nums, i, n)
                 │
            Is i >= n?
           /          \
        YES            NO
         │              │
     Return nums    key = nums[i]
                    j = i - 1
                    Shift elements > key right
                    nums[j + 1] = key
                        │
                    Recurse on i + 1
```

### 🎯 One-Line Memory Trick:
> *"Recursive Insertion Sort steps pointer $i$ forward via recursion while a while-loop shifts larger elements right to insert each key."*

---

## ✍️ Short Handwritten Interview Notes

```text
============================================================
                RECURSIVE INSERTION SORT
============================================================

CORE CONCEPT:
  Outer loop i (1 to n - 1) replaced by recursion.
  Each call inserts nums[i] into sorted prefix nums[0 ... i - 1]
  and then recurses on i + 1.

BASE CASE:
  if i >= n: return nums

ALGORITHM:
  def recursive_insertion_sort(nums, i, n):
      if i >= n: return nums
      key = nums[i]
      j = i - 1
      while j >= 0 and nums[j] > key:
          nums[j + 1] = nums[j]
          j -= 1
      nums[j + 1] = key
      return recursive_insertion_sort(nums, i + 1, n)

COMPLEXITY:
  Time:
    Best    : O(N)   (already sorted)
    Average : O(N²)
    Worst   : O(N²)  (reverse sorted)
  Space:
    O(N) recursion call stack depth

PROPERTIES:
  - Stable:   YES (nums[j] > key)
  - Adaptive: YES (O(N) best case)
  - Type:     Tail Recursive

KEY MANTRA:
  INSERT KEY INTO SORTED PREFIX  -->  RECURSE (i + 1)
============================================================
```
