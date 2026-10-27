# 🟢 Day 2 — Arrays: Repeating & Missing Number (Math & XOR Approaches)

## 1. Find the Repeating and Missing Number

Given an integer array `nums` of size $n$ containing values from $[1, n]$ where each value appears exactly once, except for $A$ which appears twice and $B$ which is missing.

Return the values $A$ and $B$ as an array of size 2, where $A$ appears at index 0 and $B$ appears at index 1.

> **Note:** You are not allowed to modify the original array.

### Example

```text
Input:  nums = [3, 5, 4, 1, 1]
Output: [1, 2]
Explanation: 1 appears two times in the array and 2 is missing from nums.

Input:  nums = [1, 2, 3, 6, 7, 5, 7]
Output: [7, 4]
Explanation: 7 appears two times in the array and 4 is missing from nums.

Input:  nums = [6, 5, 7, 1, 8, 6, 4, 3, 2]
Output: [6, 9]
Explanation: Length n = 9. 6 appears twice and 9 is missing from the range [1, 9].

Input:  nums = [2, 2]  # Edge Case: Minimum array length
Output: [2, 1]
Explanation: 2 appears twice and 1 is missing from the range [1, 2].
```

### Think About

* **Optimal Approach 1: Mathematical Equations ($\mathcal{O}(N)$ Time, $\mathcal{O}(1)$ Space):**
  * Let $X$ be the repeating number and $Y$ be the missing number.
  * Let $S_n$ be the expected sum of the first $n$ natural numbers:
    $$S_n = \frac{n(n + 1)}{2}$$
  * Let $S$ be the actual sum of elements in `nums`:
    $$S - S_n = X - Y \quad \text{--- (Equation 1)}$$
  * Let $S_{2n}$ be the expected sum of squares of the first $n$ natural numbers:
    $$S_{2n} = \frac{n(n + 1)(2n + 1)}{6}$$
  * Let $S_2$ be the actual sum of squares of elements in `nums`:
    $$S_2 - S_{2n} = X^2 - Y^2 = (X - Y)(X + Y) \quad \text{--- (Equation 2)}$$
  * Divide Equation 2 by Equation 1 to find $(X + Y)$:
    $$X + Y = \frac{S_2 - S_{2n}}{X - Y}$$
  * Solve the two simultaneous equations:
    $$X = \frac{(X - Y) + (X + Y)}{2}$$
    $$Y = X - (X - Y)$$
  * Return `[int(X), int(Y)]`.

* **Optimal Approach 2: Bit Manipulation / XOR ($\mathcal{O}(N)$ Time, $\mathcal{O}(1)$ Space):**
  * Useful in languages where large $n$ could cause integer overflow with sum of squares.
  * XOR all elements in `nums` and all integers from $1$ to $n$:
    $$XR = (\text{nums}[0] \oplus \dots \oplus \text{nums}[n-1]) \oplus (1 \oplus 2 \dots \oplus n) = X \oplus Y$$
  * Find the lowest differentiating bit between $X$ and $Y$:
    $$\text{diff\_bit} = XR \ \& \ (-XR)$$
  * Divide all elements in `nums` and all integers in $[1, n]$ into two buckets based on whether their `diff_bit` is set.
  * XORing elements in bucket 1 isolates one candidate, and bucket 2 isolates the other.
  * A final linear scan confirms which candidate is in `nums` ($X$, repeating) and which is not ($Y$, missing).

* **Why Is Sorting Not Allowed or Less Efficient?**
  * The problem explicitly forbids mutating the array (*"You are not allowed to modify the original array"*). Sorting in-place violates this constraint, and creating a sorted copy incurs $\mathcal{O}(N)$ extra space.
  * Furthermore, sorting requires $\mathcal{O}(N \log N)$ time, which is asymptotically slower than the $\mathcal{O}(N)$ Math and XOR solutions.

* **Interview Follow-Up (Multiple Duplicates or Missing Values):**
  * If more than one number is duplicated or missing, two equations are insufficient to solve for three or more unknowns without higher-order power sums ($S_3, S_4$).
  * In that case, use a Hash Set or Frequency Array ($\mathcal{O}(N)$ time, $\mathcal{O}(N)$ space), or in-place index negation/cyclic sort if array mutation is permitted.

* **Time Complexity:** $\mathcal{O}(N)$ — A single pass to compute sum and sum of squares (or XOR).
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space — Only scalar arithmetic variables are used; the array is never modified.

**File:** [01.py](../../code/sprint-5/day_2_1/01.py)
