# 🔹 Selection Sort

A comprehensive guide, step-by-step breakdown, complexity analysis, and quick-revision interview notes for **Selection Sort**.

---

## Table of Contents

- [1. Intuition](#1-intuition)
- [2. Step-by-Step Approach](#2-step-by-step-approach)
- [3. Python Code Implementation](#3-python-code-implementation)
- [4. Understand the Loops](#4-understand-the-loops)
- [5. Dry Run](#5-dry-run)
- [6. Why `min_index`?](#6-why-min_index)
- [7. Complexity Analysis](#7-complexity-analysis)
- [8. Important Interview Points & FAQs](#8-important-interview-points--faqs)
- [✍️ Short Handwritten Interview Notes](#-short-handwritten-interview-notes)

---

## 1. Intuition

Selection Sort works by conceptually dividing the array into two distinct subarrays:

```text
[ Sorted part | Unsorted part ]
```

At every step of the algorithm:
1. **Find** the smallest (minimum) element in the unsorted part.
2. **Swap** it with the element at the beginning of the unsorted part.
3. **Move the boundary** one step forward, expanding the sorted part and shrinking the unsorted part.
4. **Repeat** until the entire array is sorted.

### Visual Walkthrough

Consider the initial array:

```text
[ 64,  25,  12,  22,  11 ]
   ↑
  Start
```

1. Find the global minimum in the entire array $\rightarrow$ `11`.
2. Swap `11` with `64` (index `0`):

```text
[ 11 | 25,  12,  22,  64 ]
```
> Now `11` is settled in its correct, final sorted position.

Next iteration:

```text
[ 11 | 25,  12,  22,  64 ]
        ↑
   Unsorted start
```

1. Search for the minimum among `[25, 12, 22, 64]` $\rightarrow$ `12`.
2. Swap `12` with `25` (index `1`):

```text
[ 11,  12 | 25,  22,  64 ]
```

Continue this process until only one element remains (which is guaranteed to already be in place).

### 🧠 Mental Model

$$\text{\bf Selection Sort} = \text{\bf Find Minimum} \longrightarrow \text{\bf Select It} \longrightarrow \text{\bf Put It in Front}$$

---

## 2. Step-by-Step Approach

Suppose we are given:

$$\text{nums} = [64, 25, 12, 22, 11]$$

### Step 1 — Start from index $i = 0$
- **Sorted Part:** `[]`
- **Unsorted Part:** `[64, 25, 12, 22, 11]`
- Assume minimum is at index $0$: `nums[0] = 64`.
- Search the remaining array (`i + 1` to `4`):
  ```text
  64,  25,  12,  22,  11
                       ↑ (actual minimum found at index 4)
  ```
- **Actual minimum:** `11` (at index `4`).
- **Swap:** `nums[0]` with `nums[4]` (`64 ↔ 11`).
- **Array becomes:** `[11, 25, 12, 22, 64]`

### Step 2 — Move to index $i = 1$
- **Sorted Part:** `[11]`
- **Unsorted Part:** `[25, 12, 22, 64]`
- Assume minimum is at index $1$: `nums[1] = 25`.
- Search indices $2$ to $4$:
  ```text
  [11 | 25,  12,  22,  64]
              ↑ (minimum found at index 2)
  ```
- **Actual minimum:** `12` (at index `2`).
- **Swap:** `nums[1]` with `nums[2]` (`25 ↔ 12`).
- **Array becomes:** `[11, 12, 25, 22, 64]`

### Step 3 — Move to index $i = 2$
- **Sorted Part:** `[11, 12]`
- **Unsorted Part:** `[25, 22, 64]`
- Assume minimum is at index $2$: `nums[2] = 25`.
- Search indices $3$ to $4$:
  ```text
  [11, 12 | 25,  22,  64]
                  ↑ (minimum found at index 3)
  ```
- **Actual minimum:** `22` (at index `3`).
- **Swap:** `nums[2]` with `nums[3]` (`25 ↔ 22`).
- **Array becomes:** `[11, 12, 22, 25, 64]`

### Step 4 — Move to index $i = 3$
- **Sorted Part:** `[11, 12, 22]`
- **Unsorted Part:** `[25, 64]`
- Assume minimum is at index $3$: `nums[3] = 25`.
- Search index $4$:
  ```text
  [11, 12, 22 | 25,  64]
                ↑ (minimum is already at index 3)
  ```
- **Actual minimum:** `25` (at index `3`).
- Since `min_index == i`, no swap is needed.
- **Array remains:** `[11, 12, 22, 25, 64]`

When $i = n - 1$, the last remaining element `64` is naturally in its correct place. **Sorting is complete!**

---

## 3. Python Code Implementation

```python
def selection_sort(nums):
    n = len(nums)

    # Traverse through all array elements except the last one
    for i in range(n - 1):

        # Assume the current index contains the minimum
        min_index = i

        # Find the actual minimum in the unsorted subarray
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j

        # Swap the found minimum with the first element of unsorted part
        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums


# Driver Code
nums = [64, 25, 12, 22, 11]
sorted_nums = selection_sort(nums)
print(sorted_nums)
```

### Output:

```text
[11, 12, 22, 25, 64]
```

---

## 4. Understand the Loops

Understanding the loops and their boundaries is crucial for interview discussions and code writing.

### The Outer Loop: `for i in range(n - 1):`
- `i` represents the **target position** where the next smallest element must be placed.
  - $i = 0 \longrightarrow$ Place the $1^{\text{st}}$ smallest element at index `0`.
  - $i = 1 \longrightarrow$ Place the $2^{\text{nd}}$ smallest element at index `1`.
  - $i = 2 \longrightarrow$ Place the $3^{\text{rd}}$ smallest element at index `2`.
  - $\dots$
- **Why `n - 1`?** When the first $n - 1$ elements are placed in their correct spots, the $n^{\text{th}}$ element (at index $n - 1$) is guaranteed to be the largest and already correctly positioned. Running an extra iteration for the last element is redundant.

### The Inner Loop: `for j in range(i + 1, n):`
- `j` searches the remaining **unsorted portion** of the array.

```text
[  Sorted Part   |       Unsorted Part       ]
 0, 1, ..., i-1       i,  i+1,  i+2, ..., n-1
                      ↑    ↑
                  min_idx  j scans forward
```

- We initialize `min_index = i`.
- If an element smaller than `nums[min_index]` is found:
  ```python
  if nums[j] < nums[min_index]:
      min_index = j
  ```
- After `j` finishes scanning up to $n - 1$, `min_index` holds the index of the absolute smallest element in the unsorted region.

### The Final Swap:
```python
if min_index != i:
    nums[i], nums[min_index] = nums[min_index], nums[i]
```
- Places the minimum directly at index `i`.
- The condition `min_index != i` avoids an unnecessary self-swap when the current element is already the minimum.

---

## 5. Dry Run

Dry run of Selection Sort on `[64, 25, 12, 22, 11]`:

| Iteration ($i$) | Minimum Found | Elements Swapped | Array State After Iteration |
| :---: | :---: | :---: | :---: |
| **0** | `11` (at index `4`) | `64 ↔ 11` | `[11, 25, 12, 22, 64]` |
| **1** | `12` (at index `2`) | `25 ↔ 12` | `[11, 12, 25, 22, 64]` |
| **2** | `22` (at index `3`) | `25 ↔ 22` | `[11, 12, 22, 25, 64]` |
| **3** | `25` (at index `3`) | *No swap needed* | `[11, 12, 22, 25, 64]` |

**Final Sorted Array:**
`[11, 12, 22, 25, 64]`

---

## 6. Why `min_index`?

Instead of immediately swapping whenever we encounter a smaller element during the scan, we simply **remember its index**.

### Example:

Consider searching the unsorted part of `[64, 25, 12, 22, 11]` at $i = 0$:

```text
Initial: min_index = 0   (nums[0] = 64)
j = 1:   25 < 64  -->  min_index = 1   (nums[1] = 25)
j = 2:   12 < 25  -->  min_index = 2   (nums[2] = 12)
j = 3:   22 > 12  -->  no change
j = 4:   11 < 12  -->  min_index = 4   (nums[4] = 11)
```

Only **after** scanning the entire unsorted region do we perform **a single swap**:
$$\text{nums}[0] \longleftrightarrow \text{nums}[4]$$

### Core Benefit:
- Naive swapping on every comparison leads to unnecessary write operations.
- By tracking `min_index`, Selection Sort guarantees **at most 1 swap per outer loop pass**.

$$\text{\bf Core Idea:} \quad \text{Find Minimum} \longrightarrow \text{Remember Index} \longrightarrow \text{One Swap}$$

---

## 7. Complexity Analysis

### Time Complexity

| Case | Time Complexity | Reason |
| :--- | :---: | :--- |
| **Best Case** | $\mathcal{O}(N^2)$ | Still performs the full nested scan even if the array is already sorted. |
| **Average Case** | $\mathcal{O}(N^2)$ | Random order requires full scans to confirm minimum. |
| **Worst Case** | $\mathcal{O}(N^2)$ | Reverse-sorted array performs full scans in every pass. |

#### Why $\mathcal{O}(N^2)$?
- **Outer loop** runs $(N - 1)$ times.
- **Inner loop** runs:
  - $(N - 1)$ comparisons in pass 1
  - $(N - 2)$ comparisons in pass 2
  - $(N - 3)$ comparisons in pass 3
  - $\dots$
  - $1$ comparison in pass $(N - 1)$

$$\text{Total Comparisons} = (N - 1) + (N - 2) + \dots + 2 + 1 = \frac{N(N - 1)}{2} = \mathcal{O}(N^2)$$

> **Important:** Unlike Bubble Sort (which can terminate early in $\mathcal{O}(N)$ using a swapped flag) or Insertion Sort ($\mathcal{O}(N)$ on sorted input), **Selection Sort always takes $\mathcal{O}(N^2)$ time**, regardless of initial order.

---

### Space Complexity

$$\text{Space Complexity} = \mathcal{O}(1)$$

- Only a few scalar variables (`i`, `j`, `min_index`, `n`) are maintained.
- No auxiliary array or recursive call stack is required.
- Therefore, Selection Sort is an **in-place** sorting algorithm.

---

## 8. Important Interview Points & FAQs

| Question | Answer | Details / Explanation |
| :--- | :---: | :--- |
| **Is Selection Sort stable?** | **No** ❌ | Standard Selection Sort is **unstable**. Swapping over large distances can alter the relative order of duplicate elements. *(Example: In `[4a, 4b, 2]`, `4a` swaps with `2`, placing `4a` after `4b` $\rightarrow$ `[2, 4b, 4a]`)*. |
| **Is it in-place?** | **Yes** ✅ | Operates directly within the input array using $\mathcal{O}(1)$ extra memory. |
| **Does it use an extra array?** | **No** ❌ | Auxiliary space is $\mathcal{O}(1)$. |
| **Number of Swaps?** | **At most $N - 1$** | Makes $\mathcal{O}(N)$ swaps in total. Useful when write operations to memory are significantly more expensive than read operations. |
| **Adaptability?** | **Not adaptive** ❌ | Doesn't speed up on sorted or nearly-sorted data; always takes $\frac{N(N - 1)}{2}$ comparisons. |

---

## ✍️ Short Handwritten Interview Notes

```text
============================================================
                     SELECTION SORT
============================================================

IDEA:
  Divide array into: [ SORTED | UNSORTED ]
  Repeatedly find minimum in unsorted part and place at beginning.

STEPS:
  1. i = starting index of unsorted part (0 to n - 2).
  2. Assume nums[i] is minimum (min_index = i).
  3. Search j from i + 1 to n - 1.
  4. If nums[j] < nums[min_index], update min_index = j.
  5. If min_index != i, swap nums[i] with nums[min_index].
  6. Repeat.

CODE:
  for i in range(n - 1):
      min_index = i
      for j in range(i + 1, n):
          if nums[j] < nums[min_index]:
              min_index = j
      if min_index != i:
          nums[i], nums[min_index] = nums[min_index], nums[i]

COMPLEXITY:
  Time:
    Best    : O(N²)
    Average : O(N²)
    Worst   : O(N²)
  Space:
    O(1) -> In-place

STABILITY:
  No (Standard selection sort is NOT stable)

SWAPS:
  At most O(N) swaps (N - 1 max)

KEY MANTRA:
  FIND MIN  -->  SELECT  -->  SWAP
============================================================
```
