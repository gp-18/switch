# 🟢 Day 3.2 — Arrays: Reverse Pairs (Modified Merge Sort & Two Pointers)

## 1. Reverse Pairs

Given an integer array `nums`, return the total number of **reverse pairs** in the array.

An index pair `(i, j)` is called a **reverse pair** if:
$$0 \le i < j < \text{len}(nums) \quad \text{and} \quad nums[i] > 2 \times nums[j]$$

### Example

```text
Input:  nums = [6, 4, 1, 2, 7]
Output: 3
Explanation:
The 3 reverse pairs (i < j and nums[i] > 2 * nums[j]) are:
1. (0, 2): nums[0] = 6, nums[2] = 1 -> 6 > 2 * 1 (valid)
2. (0, 3): nums[0] = 6, nums[3] = 2 -> 6 > 2 * 2 = 4 (valid)
3. (1, 2): nums[1] = 4, nums[2] = 1 -> 4 > 2 * 1 = 2 (valid)

Input:  nums = [5, 4, 4, 3, 3]
Output: 0
Explanation: No pairs satisfy nums[i] > 2 * nums[j].

Input:  nums = [6, 4, 4, 2, 2]
Output: 2
Explanation:
The 2 reverse pairs are:
1. (0, 3): nums[0] = 6, nums[3] = 2 -> 6 > 2 * 2 = 4
2. (0, 4): nums[0] = 6, nums[4] = 2 -> 6 > 2 * 2 = 4
Note: nums[1] = 4 and nums[3] = 2 gives 4 > 2 * 2 = 4 which is False (not strictly greater).

Input:  nums = [1]  # Edge Case: Single element
Output: 0
Explanation: At least two elements are required to form a pair.
```

### Think About

* **Why Standard Merge Step Counting Fails Here (Classic Interview Trap):**
  * In standard Count Inversions ($nums[i] > nums[j]$), counting and merging are done in the exact same step because $nums[left] > nums[right]$ decides both:
    1. Who enters the merged array first.
    2. How many inversions are contributed by $nums[right]$.
  * In **Reverse Pairs**, the condition is non-unit: $nums[i] > 2 \times nums[j]$.
  * Even if $nums[left] \le 2 \times nums[right]$, it is very common that $nums[left] > nums[right]$ (for example, $4$ vs $3$: $4 \ngtr 2 \times 3$, but $4 > 3$).
  * Trying to count pairs while merging corrupts the sorted order or skips valid reverse pairs.
  * **The Solution:** Decouple counting from merging! First count valid pairs across the two sorted halves using two pointers in $\mathcal{O}(N)$ time, and *then* perform the standard merge in $\mathcal{O}(N)$ time.

* **Two-Pointer Counting Pass (`count_pairs`):**
  * Both halves (`nums[low..mid]` and `nums[mid+1..high]`) are already sorted.
  * Initialize `right = mid + 1`.
  * For each `i` from `low` to `mid`:
    * While `right <= high and nums[i] > 2 * nums[right]`:
      * Increment `right += 1`.
    * All elements in the right half from index `mid + 1` up to `right - 1` satisfy $nums[i] > 2 \times nums[k]$.
    * Add `right - (mid + 1)` to the reverse pair count.
    * **Key Invariant:** Because `nums[low..mid]` is sorted, as `i` advances to `i + 1`, $nums[i + 1] \ge nums[i]$. Any elements in the right half that were smaller than $\frac{nums[i]}{2}$ will automatically be smaller than $\frac{nums[i + 1]}{2}$.
    * Therefore, `right` **never resets backward**. It only advances forward, giving strict linear $\mathcal{O}(N)$ time for the entire counting pass.

* **Integer Overflow & Negative Numbers:**
  * Constraints: $-2^{31} \le nums[i] \le 2^{31} - 1$.
  * In languages like C++ or Java, $2 \times nums[j]$ can overflow a 32-bit signed integer when $nums[j] \ge 2^{30}$ or $nums[j] \le -2^{30}$. Cast to a 64-bit integer (`1LL * nums[j] * 2`). Python natively handles arbitrarily large integers.
  * For negative numbers, standard inequalities apply directly (e.g., $-2 > 2 \times (-3) = -6$ is True).

* **Time Complexity:** $\mathcal{O}(2N \log N) \approx \mathcal{O}(N \log N)$
  * Counting takes $\mathcal{O}(N)$ and merging takes $\mathcal{O}(N)$ at each of the $\log N$ recursion levels.
* **Space Complexity:** $\mathcal{O}(N)$
  * Auxiliary space for the temporary array during the merge operation.

**File:** [01.py](../../code/sprint-5/day_3_2/01.py)
