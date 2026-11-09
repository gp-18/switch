# 🟢 Day 5.1 — Binary Search: Book Allocation Problem

## 1. Book Allocation Problem

Given an array `nums` of $n$ integers, where `nums[i]` represents the number of pages in the $i$-th book, and an integer $m$ representing the number of students.

Allocate all the books to the students subject to the following rules:
1. Each student gets **at least one book**.
2. Each book is allocated to **only one student**.
3. Book allocation must be **contiguous** (a student can only be assigned a contiguous sequence of books).

Allocate the books to $m$ students in such a way that the **maximum number of pages assigned to a student is minimized**.

If the allocation of books is not possible, return `-1`.

You must write an algorithm that runs in $\mathcal{O}(N \times \log(\sum(nums) - \max(nums)))$ time complexity.

### Example

```text
Input:  nums = [12, 34, 67, 90], m = 2
Output: 113
Explanation:
One optimal contiguous allocation:
- Student 1 gets: [12, 34, 67] -> 12 + 34 + 67 = 113 pages
- Student 2 gets: [90]         -> 90 pages
The maximum pages assigned to any student is max(113, 90) = 113.
Any other allocation would result in a larger maximum (e.g. [12, 34] and [67, 90] gives max(46, 157) = 157).

Input:  nums = [25, 46, 28, 49, 24], m = 4
Output: 71
Explanation:
Allocation: [25, 46] | [28] | [49] | [24]
Pages per student: 71, 28, 49, 24.
Maximum pages = max(71, 28, 49, 24) = 71.

Input:  nums = [15, 17, 20], m = 2
Output: 32
Explanation:
Allocation: [15, 17] | [20] -> Pages: 32, 20.
Maximum pages = max(32, 20) = 32.

Input:  nums = [10, 20, 30], m = 4  # Edge Case: m > n (more students than books)
Output: -1
Explanation:
There are 4 students but only 3 books. Since each student must receive at least 1 book,
allocation is impossible. Return -1.
```

### Think About

* **Impossible Edge Case ($m > n$):**
  * Since each student must be allocated at least one book and books cannot be split, if the number of students $m$ exceeds the total number of books $n$, it is impossible.
  * Immediately return `-1`.

* **The Monotonicity Principle (Binary Search on Answers):**
  * Let $P$ be a candidate upper limit on the maximum pages any student is allowed to read.
  * As the page limit $P$ **increases**, each student can take on more pages, so **fewer or equal students** are needed to read all books.
  * Consequently, the number of students required is a **monotonically non-increasing** function of the page limit:
    $$P_1 < P_2 \implies \text{Students}(P_1) \ge \text{Students}(P_2)$$
  * If a page limit $P$ can allocate all books using $\le m$ students, then any limit $> P$ is also feasible.
  * If limit $P$ requires $> m$ students, any smaller limit will also fail.
  * We want to find the **minimum feasible page limit $P$** $\implies$ **Binary Search!**

* **Search Space Boundaries:**
  * **Lower bound (`low = max(nums)`):** The student allocated the thickest book must read at least $\max(nums)$ pages. No valid allocation can have a maximum page limit less than $\max(nums)$.
  * **Upper bound (`high = sum(nums)`):** If $m = 1$, one student must read all books, totaling $\sum(nums)$ pages.
  * Search space range: $[\max(nums), \sum(nums)]$.

* **Greedy Feasibility Simulation (`countStudents`):**
  * Given a limit `mid`:
    * Start with `students = 1` and `pages = 0`.
    * Traverse `nums`:
      * If `pages + book <= mid`, assign this book to the current student: `pages += book`.
      * Else, the current student cannot take more pages. Allocate to a new student:
        `students += 1`, `pages = book`.
    * If `students <= m`, the limit `mid` is feasible.

* **Step-by-Step Binary Search Algorithm:**
  1. Check if $m > n$: return `-1`.
  2. Set `low = max(nums)`, `high = sum(nums)`, `ans = high`.
  3. While `low <= high`:
     * `mid = low + (high - low) // 2`.
     * If `countStudents(nums, mid) <= m`:
       * Feasible! Record `ans = mid`.
       * Search for a smaller maximum on the left: `high = mid - 1`.
     * Else:
       * Requires more than $m$ students; limit is too small: `low = mid + 1`.
  4. Return `ans` (or `low`).

* **Time Complexity:** $\mathcal{O}(N \times \log(\sum(nums) - \max(nums)))$
  * The search space size is $\sum(nums) - \max(nums) \le 10^4 \times 10^5 = 10^9$.
  * Binary search takes $\log_2(10^9) \approx 30$ iterations.
  * In each iteration, we iterate through the $N$ books in $\mathcal{O}(N)$ time.
  * Total time: $\mathcal{O}(N \times \log(\sum(nums) - \max(nums)))$. For $N = 10^4$, total operations $\approx 3 \times 10^5$, running in milliseconds.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-6/day_5_1/01.py)

