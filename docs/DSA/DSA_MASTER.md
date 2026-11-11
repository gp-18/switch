# 🧠 DSA Master — Pattern-Wise Interview Preparation System

> **One file. One source of truth.** Everything you need to go from "I can't even understand the question" to "I recognise the pattern, derive the solution, and explain it calmly in an interview."
>
> Language: **Python 3** · Target: **Product-based company backend interviews** · Question spine: **[dsacourse Top 150](https://dsacourse.com/top-150)** (free) + carefully chosen LeetCode extras.

---

## 📍 Table of Contents

**Part I — How to use this system**
- [0.1 Read this first](#01-read-this-first)
- [0.2 The mentor protocol (how to use this with an AI or a friend)](#02-the-mentor-protocol)
- [0.3 Master roadmap & dependency graph](#03-master-roadmap--dependency-graph)
- [0.4 Realistic 24-week study plan](#04-realistic-24-week-study-plan)

**Part II — Foundations**
- [1. Phase 0: Programming & complexity fundamentals](#1-phase-0-programming--complexity-fundamentals)
- [2. The Python DSA toolkit](#2-the-python-dsa-toolkit)
- [3. The universal 15-step problem-solving framework](#3-the-universal-15-step-problem-solving-framework)
- [4. 🔎 The Pattern Identification System (most important section)](#4--the-pattern-identification-system)

**Part III — Patterns (study in this order)**
| # | Pattern | # | Pattern |
|---|---|---|---|
| P1 | [Array fundamentals](#p1-array-fundamentals) | P13 | [Recursion & Backtracking](#p13-recursion--backtracking) |
| P2 | [Hashing & Frequency Counting](#p2-hashing--frequency-counting) | P14 | [Trees & BST](#p14-trees--binary-search-trees) |
| P3 | [Two Pointers](#p3-two-pointers) | P15 | [Tries](#p15-tries) |
| P4 | [Sliding Window](#p4-sliding-window) | P16 | [Heap / Priority Queue](#p16-heap--priority-queue) |
| P5 | [Prefix Sum & Difference Array](#p5-prefix-sum--difference-array) | P17 | [Graphs: BFS / DFS / Topo / DSU](#p17-graphs) |
| P6 | [Sorting](#p6-sorting) | P18 | [Advanced Graphs: Dijkstra, Bellman-Ford, MST](#p18-advanced-graphs) |
| P7 | [Intervals](#p7-intervals) | P19 | [Greedy](#p19-greedy) |
| P8 | [Kadane's Algorithm](#p8-kadanes-algorithm) | P20 | [Dynamic Programming](#p20-dynamic-programming) |
| P9 | [Binary Search (incl. on Answer)](#p9-binary-search) | P21 | [Bit Manipulation](#p21-bit-manipulation) |
| P10 | [Stack & Monotonic Stack](#p10-stack--monotonic-stack) | P22 | [Matrix & Math](#p22-matrix--math) |
| P11 | [Monotonic Queue / Deque](#p11-monotonic-queue--deque) | P23 | [Cyclic Sort / Index Placement](#p23-cyclic-sort--index-placement) |
| P12 | [Linked List](#p12-linked-list) | P24 | [Advanced: String algos, Segment/Fenwick tree](#p24-advanced-dsa) |

**Part IV — Systems**
- [5. Pattern comparisons (look-alike patterns)](#5-pattern-comparisons)
- [6. Master question bank (all questions in one table)](#6-master-question-bank)
- [7. Mastery & spaced-revision system](#7-mastery--spaced-revision-system)
- [8. Trackers (Markdown + CSV)](#8-trackers)
- [9. Interview preparation & mock interviews](#9-interview-preparation)
- [10. Motivation & consistency system](#10-motivation--consistency-system)
- [11. Appendix: cheat sheets](#11-appendix-cheat-sheets)

---

# PART I — HOW TO USE THIS SYSTEM

## 0.1 Read this first

### The core belief of this guide

You are **not** trying to solve 150 problems. You are trying to learn **~20 ideas** so well that the 150 problems become *examples* of those ideas.

```
Memorising solutions          →  Works for problems you've seen. Fails on everything else.
Understanding patterns        →  Works for problems you've never seen.
```

Every problem in an interview is built from a small set of reusable moves:

> "remember what I've seen" (hashing) · "move two indices with a rule" (two pointers) · "maintain a contiguous range" (sliding window) · "precompute cumulative info" (prefix sum) · "throw away half the search space" (binary search) · "remember unfinished items" (stack) · "always take the best next item" (heap) · "try all choices and undo" (backtracking) · "reuse answers to smaller subproblems" (DP) · "explore neighbours" (graph BFS/DFS) · "make the locally best choice that is provably safe" (greedy)

### The learning loop for every pattern

```
1. UNDERSTAND   → read the pattern section: analogy, why it exists, intuition from brute force
2. RECOGNISE    → study the "How to recognise" clues and the misleading-keyword traps
3. TEMPLATE     → derive the template yourself on paper, then compare with the guide
4. GUIDED       → solve the worked example with the dry-run table
5. PRACTICE     → Level 1 → Level 5 questions, using progressive hints (never jump to the editorial)
6. EXPLAIN      → say the solution out loud in interview format (2 minutes)
7. REVISE       → day 1, 3, 7, 21 re-solves (see Section 7)
8. MASTER       → solve an unseen problem of that pattern independently
```

### Rules of this guide

1. **Never read a solution before 25 minutes of honest effort** (for Easy: 15 minutes). Use the hint ladder instead.
2. **Write code by hand (or in a plain editor) first**, then run it.
3. **Dry-run before you submit.** A table on paper beats ten failed submissions.
4. **A problem is "solved" only if you could re-solve it from scratch in 3 days.** Otherwise it goes to the revision queue.
5. **Count mastered patterns, not solved questions.**

### Legend used in question lists

| Symbol | Meaning |
|---|---|
| ⭐ | **Must solve** — core of the pattern |
| ✅ | **Recommended** — strengthens variations |
| 🚀 | **Optional advanced** — only after the pattern feels comfortable |
| 🟢 / 🟡 / 🔴 | Easy / Medium / Hard |
| `DSA150` | Question is from [dsacourse Top 150](https://dsacourse.com/top-150) |
| `LC` | Extra question from LeetCode (added where Top 150 doesn't cover a variation) |

---

## 0.2 The mentor protocol

This guide is designed so you can paste any problem into a chat with an AI (or a study buddy) and get *mentored*, not *spoon-fed*. Copy this prompt:

```text
I'm practising <PATTERN> using my DSA Master README.
Problem: <paste problem>
Act as my DSA mentor. Do NOT give me code.
Ask me first: what are the input/output, constraints, and my brute force?
Then give me hints one at a time ONLY when I ask "next hint":
  Hint 1 – the key observation
  Hint 2 – which pattern and why
  Hint 3 – the algorithm in words
  Hint 4 – pseudocode
  Hint 5 – help debugging MY code
After I solve it, make me dry-run it in a table, state the complexity,
and give me one follow-up question an interviewer would ask.
```

### The hint ladder (use it on yourself too)

| Stuck for… | Do this |
|---|---|
| 0–10 min | Re-read the problem. Write 2 examples by hand. Write brute force in words. |
| 10–20 min | Open this guide's **recognition clues** for the suspected pattern. |
| 20–25 min | Take **Hint 1** (observation only). |
| +10 min each | Take Hint 2, 3, 4 in order. |
| Still stuck after Hint 4 | Read the editorial **idea only**, close it, and code it yourself. Mark the question **🔁 Needs Revision**. |

---

## 0.3 Master roadmap & dependency graph

### Why this order?

Each pattern uses the previous ones. Sliding window needs hashing (to track window contents). Binary search on answer needs greedy feasibility checks. Trees need recursion. Graphs need trees + queues. DP needs recursion + memoisation (hashing). Learning out of order is why most people feel "DSA doesn't make sense".

```text
PHASE 0  ─ Python, Big-O, recursion basics, dry-running
   │
PHASE 1  ─ LINEAR DATA (the "array brain")
   │   P1 Arrays ──► P2 Hashing/Frequency ──► P3 Two Pointers ──► P4 Sliding Window
   │                        │                                          │
   │                        └──► P5 Prefix Sum (+ hash map) ◄──────────┘
   │   P6 Sorting ──► P7 Intervals        P8 Kadane (DP preview)
   │   P9 Binary Search ──► Binary Search on Answer
   │
PHASE 2  ─ LINEAR STRUCTURES WITH MEMORY
   │   P10 Stack ──► Monotonic Stack ──► P11 Monotonic Deque
   │   P12 Linked List (pointers, fast/slow, dummy node) ──► LRU Cache
   │
PHASE 3  ─ RECURSIVE THINKING
   │   P13 Recursion ──► Backtracking (subsets, permutations, pruning)
   │   P14 Trees (DFS/BFS) ──► BST ──► P15 Tries
   │   P16 Heap (needs arrays + trees intuition)
   │
PHASE 4  ─ NETWORKS
   │   P17 Graphs: BFS/DFS, components, cycles, topo sort, DSU
   │   P18 Advanced graphs: Dijkstra, Bellman-Ford, MST (needs heap + DSU)
   │
PHASE 5  ─ OPTIMISATION
   │   P19 Greedy (needs sorting + heap + intervals)
   │   P20 Dynamic Programming (needs recursion + hashing; 1D → 2D → knapsack → strings → intervals)
   │
PHASE 6  ─ SPECIALISED
       P21 Bits · P22 Matrix/Math · P23 Cyclic sort · P24 KMP / Rabin-Karp / Segment & Fenwick tree
```

### What each phase unlocks in interviews

| Phase | After finishing, you can handle… | Approx. share of real PBC rounds |
|---|---|---|
| 1 | Most "Easy/Medium array & string" screening rounds | ~40% |
| 2 | Stack/linked list rounds, design-ish problems (LRU, Min Stack) | ~15% |
| 3 | Tree rounds, recursion, top-K | ~20% |
| 4 | Graph rounds (very common at product companies) | ~10–15% |
| 5 | DP & greedy (often the "hard" round) | ~10–15% |
| 6 | Rare; nice-to-have | <5% |

*(Shares are a rough planning guide, not data. Arrays/strings/hashing dominate early rounds everywhere.)*

---

## 0.4 Realistic 24-week study plan

Designed for a **working professional** who also spends ~1 hour/day on system design.

| Day type | DSA time | Content |
|---|---|---|
| Weekday (Mon–Fri) | **60–90 min** | 15 min revision queue · 45–60 min new problem(s) · 5 min log |
| Saturday | **2–3 hrs** | New pattern theory + 2–3 problems |
| Sunday | **1.5–2 hrs** | Weekly review, re-solve 3 old problems, 1 timed mock |
| Low-energy day | **30 min** | [Minimum Viable Study Day](#b-minimum-viable-study-day) |

| Weeks | Focus | Patterns | Exit criteria |
|---|---|---|---|
| 1 | Phase 0 | Big-O, Python toolkit, recursion basics | Can state complexity of any loop nest; knows `dict`, `set`, `deque`, `heapq`, `Counter` |
| 2 | Arrays & Hashing | P1, P2 | Solves Two Sum, Group Anagrams, Longest Consecutive without help |
| 3 | Two Pointers | P3 | 3Sum + Container With Most Water independently |
| 4–5 | Sliding Window | P4 | Fixed & variable windows; Minimum Window Substring with ≤ 2 hints |
| 6 | Prefix Sum + Sorting + Intervals + Kadane | P5–P8 | Subarray Sum Equals K; Merge Intervals; Max Subarray |
| 7–8 | Binary Search | P9 | Classic + rotated + on-answer (Koko, Ship Packages) |
| 9 | Stack, Monotonic Stack/Deque | P10, P11 | Daily Temperatures, Largest Rectangle with hints |
| 10 | Linked List | P12 | Reverse, cycle, merge, LRU Cache |
| 11–12 | Recursion & Backtracking | P13 | Subsets, Permutations, Combination Sum, Word Search |
| 13–14 | Trees + Tries | P14, P15 | Any tree Easy in 10 min; LCA, Validate BST, Serialize |
| 15 | Heap | P16 | Top K, K-way merge, Median from stream |
| 16–17 | Graphs | P17 | Islands, Rotting Oranges, Course Schedule, DSU |
| 18 | Advanced Graphs + Greedy | P18, P19 | Dijkstra, MST; Jump Game, Gas Station |
| 19–21 | Dynamic Programming | P20 | 1D, 2D grid, knapsack, LCS, Edit Distance |
| 22 | Bits, Matrix, Cyclic Sort | P21–P23 | Full sets done |
| 23–24 | Mock interviews + weak-pattern repair | All | 2 mocks/week; every pattern ≥ "Comfortable" |

> If you fall behind: **don't skip patterns, shrink the question list** (do only ⭐ questions). Falling behind is normal; quitting is the only real failure.

---

# PART II — FOUNDATIONS

## 1. Phase 0: Programming & complexity fundamentals

You already write Python professionally, so this section focuses on the **DSA view** of things you know: how fast is it, how much memory, and how do I trace it by hand.

### 1.1 What "time complexity" actually means

Time complexity answers: **"If the input gets 10× bigger, how much slower does my code get?"** We count *basic operations* (comparisons, assignments, arithmetic, dict lookups) as a function of input size `n`, and keep only the fastest-growing term.

```python
def f(nums):            # n = len(nums)
    total = 0           # 1 op
    for x in nums:      # loop runs n times
        total += x      #   1 op each → n ops
    return total        # 1 op
# total ≈ n + 2  →  O(n)
```

**Rules for simplifying:**
1. Drop constants: `3n + 5` → `O(n)`.
2. Keep the dominant term: `n² + n` → `O(n²)`.
3. Sequential blocks **add**: loop then loop → `O(n + m)`.
4. Nested blocks **multiply**: loop inside loop → `O(n · m)`.
5. Halving each step → `O(log n)`.

### 1.2 The complexity ladder (memorise the feel, not the math)

| Big-O | Name | Example | n = 10⁵ → ops |
|---|---|---|---|
| O(1) | constant | dict lookup, `arr[i]` | 1 |
| O(log n) | logarithmic | binary search | ~17 |
| O(n) | linear | one loop | 10⁵ |
| O(n log n) | linearithmic | sorting | ~1.7 × 10⁶ |
| O(n²) | quadratic | nested loops over same array | 10¹⁰ ❌ too slow |
| O(2ⁿ) | exponential | all subsets | impossible for n > ~25 |
| O(n!) | factorial | all permutations | impossible for n > ~10 |

### 1.3 🔑 Constraints tell you the intended complexity

Online judges allow roughly **10⁷–10⁸ simple operations per second** (Python is on the slower end, so aim for ≤ 10⁷). **Read the constraints FIRST** — they leak the intended solution.

| If `n` is up to… | Target complexity | Likely patterns |
|---|---|---|
| ≤ 10 | O(n!) / O(2ⁿ · n) | Permutations, backtracking |
| ≤ 20–25 | O(2ⁿ) | Subsets, bitmask, backtracking |
| ≤ 100 | O(n³) | 3 nested loops, Floyd-Warshall, interval DP |
| ≤ 1,000–5,000 | O(n²) | 2D DP, nested loops |
| ≤ 10⁵ – 10⁶ | O(n log n) or O(n) | Sorting, heap, binary search, hashing, two pointers, sliding window, prefix sum |
| ≤ 10⁹ or more (a value, not array size) | O(log n) or O(√n) | Binary search on answer, math |

> 💡 Example: "1 ≤ nums.length ≤ 10⁵" → your O(n²) brute force will TLE. The interviewer *expects* O(n) or O(n log n). That alone eliminates half the possible approaches.

### 1.4 Space complexity

- **Auxiliary space** = extra memory your algorithm uses, *excluding the input*. This is what interviewers usually mean.
- A dict/set of up to `n` items → O(n). A fixed-size array of 26 letters → O(1) (constant, doesn't grow with n).
- **Recursion uses stack space**: recursion depth `d` → O(d) space even with no data structures. A recursive DFS on a skewed tree of n nodes uses O(n) stack.
- The output array usually doesn't count (say so explicitly in interviews: "O(1) extra space, not counting the output").

### 1.5 Complexity of common Python operations (know these cold)

| Operation | Cost | Trap |
|---|---|---|
| `lst[i]`, `lst.append(x)`, `lst.pop()` | O(1) | — |
| `lst.pop(0)`, `lst.insert(0, x)` | **O(n)** | Use `collections.deque` for queues |
| `x in lst` | **O(n)** | Use a `set` for membership |
| `x in set`, `x in dict`, `d[k] = v` | O(1) average | Keys must be hashable (no lists → use tuples) |
| `lst[a:b]` slicing | O(b − a) | Slicing inside a loop silently makes it O(n²) |
| `s + t` string concat | O(len(s) + len(t)) | Building strings in a loop → collect in list, `"".join(...)` |
| `sorted(lst)`, `lst.sort()` | O(n log n) | — |
| `min(lst)`, `max(lst)`, `sum(lst)` | O(n) | Calling these inside a loop → O(n²) |
| `heapq.heappush/heappop` | O(log n) | Min-heap only; negate for max-heap |
| `heapq.heapify(lst)` | O(n) | — |
| `deque.append/appendleft/pop/popleft` | O(1) | — |
| `bisect.bisect_left(lst, x)` | O(log n) | List must be sorted |
| `Counter(iterable)` | O(n) | — |
| `str.count`, `str.find`, `str.index` | O(n) | Hidden loop |

### 1.6 Recursion basics (enough to start; full treatment in P13)

A recursive function = **base case** (when to stop) + **recursive case** (solve a smaller version and combine).

```python
def factorial(n):
    if n <= 1:                 # base case: smallest problem, answered directly
        return 1
    return n * factorial(n-1)  # trust that factorial(n-1) is correct ("leap of faith")
```

Call stack for `factorial(3)`:
```
factorial(3) waits for factorial(2)
  factorial(2) waits for factorial(1)
    factorial(1) returns 1           ← base case
  factorial(2) returns 2 * 1 = 2
factorial(3) returns 3 * 2 = 6
```
Python's default recursion limit is ~1000. For deep recursion use `sys.setrecursionlimit(10**6)` (LeetCode-style) or convert to iteration.

### 1.7 How to dry-run code (the most underrated skill)

1. Pick a **small** input (4–6 elements) that exercises the interesting case.
2. Draw a table: one column per variable that changes, one row per loop iteration.
3. Update **only** what the code says, line by line. Don't "know" what should happen — *execute*.
4. Check the final row against the expected output.

```python
def max_val(nums):
    best = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > best:
            best = nums[i]
    return best
```
Dry run on `[3, 7, 2, 9]`:

| i | nums[i] | nums[i] > best? | best after |
|---|---|---|---|
| start | — | — | 3 |
| 1 | 7 | 7 > 3 ✅ | 7 |
| 2 | 2 | 2 > 7 ❌ | 7 |
| 3 | 9 | 9 > 7 ✅ | 9 |

Return 9 ✅.

### 1.8 Edge-case checklist (run through this for EVERY problem)

- Empty input (`[]`, `""`) · Single element · Two elements
- All elements equal · Already sorted / reverse sorted
- Negative numbers · Zeros · Very large values (overflow isn't an issue in Python, but it is in Java/C++ — mention it)
- Duplicates · Target not present · Answer at index 0 or at the last index
- k = 0, k = n, k > n

---

## 2. The Python DSA toolkit

```python
from collections import defaultdict, Counter, deque, OrderedDict
import heapq, bisect, math
from functools import lru_cache, cache   # cache = Python 3.9+
```

### 2.1 dict / defaultdict / Counter

```python
seen = {}                         # value -> index
seen[5] = 0
seen.get(7, -1)                   # -1 if missing (no KeyError)

groups = defaultdict(list)        # auto-creates [] for new keys
groups["eat"].append("tea")

freq = Counter("banana")          # Counter({'a': 3, 'n': 2, 'b': 1})
freq.most_common(2)               # [('a', 3), ('n', 2)]
freq["z"]                         # 0 (missing keys return 0, no error)
Counter("abc") == Counter("cab")  # True → anagram check
```

### 2.2 set

```python
s = set()
s.add(3); 3 in s                  # O(1)
s.discard(10)                     # no error if missing (remove() raises)
a & b, a | b, a - b               # intersection, union, difference
```

### 2.3 deque (queue / both-ends)

```python
q = deque([1, 2])
q.append(3); q.appendleft(0)      # O(1) both ends
q.popleft(); q.pop()              # O(1)
q[0], q[-1]                       # peek front / back
```

### 2.4 heapq (min-heap)

```python
h = []
heapq.heappush(h, 5)
heapq.heappush(h, 1)
h[0]                              # peek smallest → 1
heapq.heappop(h)                  # → 1
heapq.heappush(h, -x)             # max-heap trick: push negatives, negate on pop
heapq.heappush(h, (dist, node))   # tuples compare by first item, then second...
heapq.nlargest(k, nums)           # convenience, O(n log k)
```

### 2.5 bisect (binary search on sorted lists)

```python
arr = [1, 3, 3, 5]
bisect.bisect_left(arr, 3)        # 1 → first index where 3 could be inserted (first >= 3)
bisect.bisect_right(arr, 3)       # 3 → first index > 3
bisect.insort(arr, 4)             # insert keeping sorted (O(n) due to shifting)
```

### 2.6 Sorting with keys

```python
intervals.sort(key=lambda x: x[0])               # by start
words.sort(key=lambda w: (-freq[w], w))           # by freq desc, then alphabetically
```

### 2.7 Common idioms

```python
for i, x in enumerate(nums): ...                  # index + value
for a, b in zip(s, t): ...                        # parallel iteration
grid = [[0] * cols for _ in range(rows)]          # ✅ correct 2D list
grid = [[0] * cols] * rows                        # ❌ BUG: all rows are the same object
float('inf'), float('-inf')                       # sentinels
ord('c') - ord('a')                               # letter → 0..25
divmod(17, 5)                                     # (3, 2)
```

### 2.8 Linked-list and tree node definitions (LeetCode style)

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right
```

---

## 3. The universal 15-step problem-solving framework

Use this on **every** problem until it's automatic. In interviews, steps 1–10 are spoken out loud *before* coding.

| # | Step | What you actually do | Interview time |
|---|---|---|---|
| 1 | **Read** | Read twice. Underline input, output, and every constraint. | 1 min |
| 2 | **Restate** | "So I'm given X and need to return Y such that Z." | 30 s |
| 3 | **Constraints** | Size of n → target complexity (table 1.3). Negatives? Sorted? Duplicates? | 30 s |
| 4 | **Examples** | Make your own small example and solve it **by hand**. Notice *how your brain* solved it. | 2 min |
| 5 | **Edge cases** | Empty, single, duplicates, negatives, all same (checklist 1.8). | 1 min |
| 6 | **Brute force** | The most obvious correct solution, even if slow. | 1–2 min |
| 7 | **Brute complexity** | State it. Compare to the target from constraints. | 15 s |
| 8 | **Bottleneck** | Which part repeats wasted work? (re-scanning, re-computing, re-searching) | 1 min |
| 9 | **Pattern** | Use the identification system (Section 4) to pick a tool that removes the bottleneck. | 1–2 min |
| 10 | **Optimise** | Describe the new algorithm in plain English. Get interviewer buy-in. | 2 min |
| 11 | **Correctness** | Why does it never miss the answer? (invariant / exchange argument / exhaustive cover) | 1 min |
| 12 | **Implement** | Clean code, good names, talk while typing. | 10–15 min |
| 13 | **Dry-run** | Trace your example through *your code*, not your idea. | 3 min |
| 14 | **Complexity** | Time and space, with justification. | 30 s |
| 15 | **Explain / follow-ups** | Summarise; discuss trade-offs and follow-ups. | 2 min |

### Worked example of the framework — "Two Sum"

> Given `nums` and `target`, return indices of two numbers adding to `target`. Exactly one answer exists. `2 ≤ n ≤ 10⁴`.

1–2. **Restate:** find `i ≠ j` with `nums[i] + nums[j] == target`; return `[i, j]`.
3. **Constraints:** n ≤ 10⁴ → O(n²) = 10⁸ is borderline; O(n) or O(n log n) intended. Not sorted. Negatives allowed.
4. **Example:** `[2, 7, 11, 15], target = 9`. By hand: "I look at 2, I need 7… oh 7 is right there."
5. **Edges:** duplicates like `[3, 3], 6` → indices must differ.
6. **Brute force:** check every pair `(i, j)`, `j > i`.
7. **Complexity:** O(n²) time, O(1) space.
8. **Bottleneck:** for every `i`, I *search* the whole array for `target − nums[i]`. Searching is the repeated work.
9. **Pattern:** "fast lookup of something I've already seen" → **Hashing** (complement lookup).
10. **Optimise:** walk once; for each `x`, check if `target − x` is in a dict of `value → index` seen so far; else store `x`.
11. **Correctness:** when we reach the second element of the answer pair, the first is already in the dict, so we always find it. Checking *before* inserting handles `[3,3]`.
12. **Implement:**
```python
def twoSum(nums, target):
    seen = {}                          # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
```
13. **Dry-run** `[2,7,11,15], 9`:

| i | x | need | need in seen? | seen after |
|---|---|---|---|---|
| 0 | 2 | 7 | ❌ | {2:0} |
| 1 | 7 | 2 | ✅ → return [0, 1] | — |

14. **Complexity:** O(n) time (one pass, O(1) dict ops), O(n) space.
15. **Follow-ups:** "What if sorted?" → two pointers, O(1) space. "What if we need all pairs?" → handle duplicates with counts.

---

## 4. 🔎 The Pattern Identification System

> **Pattern recognition is not keyword matching.** "Subarray" does not *mean* sliding window. You identify a pattern by asking **what structure the problem has** and **what work the brute force wastes**. Keywords are only hints that point you at the right structural question.

### 4.1 The three questions that identify 90% of problems

**Q1. What is the shape of the input?**
- Linear sequence (array / string / linked list)? Tree? Graph/grid? A single number? A set of intervals?

**Q2. What is the shape of the answer?**
- A single value (max/min/count/bool)? A pair/triplet? A contiguous piece (subarray/substring)? A non-contiguous selection (subset/subsequence)? An ordering? A path?

**Q3. What does brute force waste?**
- Re-**searching** for something → hashing / binary search / sorting
- Re-**computing** sums over ranges → prefix sum / sliding window
- Re-**scanning** to find the next bigger/smaller → monotonic stack
- Re-**finding** min/max repeatedly → heap / monotonic deque
- Re-**solving** the same subproblem → DP (memoisation)
- Trying **every** candidate answer value → binary search on answer
- Exploring **every** choice combination → backtracking (if all are needed) or DP (if only the best/count is needed)

### 4.2 Master decision tree

```text
START: read constraints → estimate target complexity (Section 1.3)
│
├─ Input is a GRAPH / GRID / "connections" / "dependencies" / "network"?
│    ├─ shortest path, unweighted ............................ BFS
│    ├─ shortest path, non-negative weights .................. Dijkstra (heap)
│    ├─ shortest path, negative weights or ≤ K edges ......... Bellman-Ford
│    ├─ ordering with prerequisites ........................... Topological sort
│    ├─ "are these connected / groups / merge sets" .......... DSU or DFS
│    ├─ cheapest way to connect everything ................... MST (Kruskal/Prim)
│    └─ explore regions / count islands ...................... DFS/BFS flood fill
│
├─ Input is a TREE?
│    ├─ answer depends on children's answers ................. DFS post-order (return values)
│    ├─ level-by-level / nearest / "view" .................... BFS with queue
│    ├─ BST → sorted order ................................... in-order traversal / BST property
│    └─ prefixes of words .................................... Trie
│
├─ Need ALL combinations / subsets / permutations / arrangements?
│    └─ n small (≤ 20) ....................................... Backtracking
│
├─ Need the BEST / COUNT over choices, and choices overlap?
│    ├─ "number of ways", "min cost", "max profit", "can we reach"
│    │   and greedy has a counter-example ................... Dynamic Programming
│    └─ a locally best choice is provably safe .............. Greedy
│
├─ LINEAR input (array / string)?
│    ├─ Answer is CONTIGUOUS (subarray / substring)?
│    │    ├─ window validity changes monotonically as it grows
│    │    │   (all positives / "at most K distinct" / no repeats) ... Sliding Window
│    │    ├─ exact sum = K, negatives allowed ...................... Prefix Sum + Hash Map
│    │    ├─ many range-sum queries ................................ Prefix Sum
│    │    ├─ max/min subarray sum ................................. Kadane
│    │    └─ max/min inside every window of size k ................ Monotonic Deque
│    ├─ Need to find PAIRS / TRIPLETS with a target?
│    │    ├─ sorted (or sortable without losing info) ............ Two Pointers
│    │    └─ unsorted, need original indices ...................... Hashing
│    ├─ Need fast "have I seen X?" / counts / grouping ............. Hashing
│    ├─ SORTED input, or "find min value that works" (monotonic) .. Binary Search
│    ├─ "next greater / smaller", "span", "histogram" ............. Monotonic Stack
│    ├─ nested structure, matching brackets, undo ................. Stack
│    ├─ repeatedly need k-th largest / smallest / top-K ............ Heap
│    ├─ intervals with start/end ................................... Sort + Intervals
│    ├─ values in range [1, n], find missing/duplicate in O(1) space . Cyclic Sort
│    ├─ in-place modification, remove/partition .................... Two Pointers (read/write)
│    └─ pairs/XOR/"appears once" with O(1) space .................. Bit Manipulation
│
└─ LINKED LIST?
     ├─ middle / cycle / k-th from end ........................... Fast & slow pointers
     ├─ reverse a part ............................................ Pointer reversal
     └─ merge / reorder / insert at head .......................... Dummy node
```

### 4.3 Pattern identification cheat sheet (structural clues)

| Pattern | Structural signal (the real reason) | Common wording | Brute force it replaces |
|---|---|---|---|
| **Hashing** | You repeatedly ask "does X exist?" or "how many X?" | duplicate, anagram, frequency, pair sum, group, first unique | Nested loop searching |
| **Two Pointers** | Sorted order lets you discard one candidate per step | sorted, pair, triplet, palindrome, in-place, partition | O(n²) pair check |
| **Sliding Window** | Contiguous range + validity is *monotonic* (if a window is invalid, every bigger window containing it is too) | longest/shortest substring, at most K, without repeating | Check all O(n²) subarrays |
| **Prefix Sum** | Sum/count over a range = difference of two cumulative values | range sum, subarray sum equals K, equal 0s/1s | Re-summing each range |
| **Difference Array** | Many range *updates*, then read final values | add v to [l, r] many times | Updating each range element |
| **Kadane** | Best contiguous sum; "extend or restart" decision | maximum subarray | All subarrays |
| **Sorting** | Order makes the answer easier (neighbours become relevant) | arrange, merge, closest, meeting | — |
| **Intervals** | Objects with start/end that may overlap | meeting, schedule, merge, overlap | Compare all pairs |
| **Binary Search** | Search space is sorted, or a yes/no condition flips once (F F F T T T) | sorted, minimum capacity/speed/days, rotated, log n | Linear scan of indices or answers |
| **Stack** | Last-opened must be first-closed; nested structure | parentheses, decode, evaluate, undo | — |
| **Monotonic Stack** | Each element waits for the first bigger/smaller element to its right/left | next greater, warmer, span, histogram, visible | For each i, scan right |
| **Monotonic Deque** | Max/min of a *sliding* window | sliding window maximum | Recompute max of each window |
| **Linked List** | Pointer rewiring; no random access | reverse, cycle, middle, merge, reorder | Copy to array |
| **Heap** | Need current smallest/largest repeatedly while data changes | top K, kth largest, closest, schedule, median, merge k | Sort repeatedly |
| **Backtracking** | Must enumerate all valid configurations | all subsets, permutations, combinations, place queens | — (it *is* the smart brute force) |
| **Trees DFS** | Answer at node = f(answers of children) | height, diameter, path sum, balanced, LCA | — |
| **Trees BFS** | Level-wise or closest-first | level order, right view, minimum depth | — |
| **Trie** | Many words sharing prefixes | prefix, autocomplete, word search with many words | Compare each word |
| **Graph BFS** | Fewest steps in unweighted graph; spreading simultaneously | minimum steps, spread, rotting, nearest | — |
| **Graph DFS** | Explore all reachable; components | islands, regions, connected, clone | — |
| **Topological Sort** | Dependencies must come first | prerequisites, order, schedule courses, alien dictionary | — |
| **DSU** | Dynamic merging of groups; "are a and b connected?" | union, redundant connection, accounts merge | Repeated DFS |
| **Dijkstra** | Weighted shortest path, weights ≥ 0 | minimum cost/time/effort path | — |
| **Greedy** | A local choice can be proven never to hurt | maximum number of non-overlapping, jump, gas | Try all choices |
| **DP** | Optimal/count over choices; subproblems overlap | number of ways, min cost, longest, can partition | Exponential recursion |
| **Bit Manipulation** | Parity, XOR cancellation, subsets as masks | single number, power of two, count bits | Hash set |
| **Cyclic Sort** | Values in range [1..n] or [0..n] map to indices | missing number, duplicate, first missing positive (O(1) space) | Hash set |

### 4.4 ⚠️ Misleading keywords (traps)

| Keyword | Looks like | But check… |
|---|---|---|
| "subarray sum equals K" | Sliding window | With **negatives**, shrinking the window doesn't reliably reduce the sum → **prefix sum + hash map** |
| "subsequence" | Sliding window | Subsequence is **not contiguous** → DP or two pointers on two strings, never a window |
| "sorted" | Binary search | If you need pairs, it's often **two pointers**; if you need all elements anyway, it's just a merge |
| "maximum" | Heap | If it's the max in a moving window → **monotonic deque**; if it's max sum → Kadane/DP |
| "minimum number of steps" | DP | In an unweighted graph/grid → **BFS** is simpler and correct |
| "pairs" | Two pointers | If you must return **original indices** of an unsorted array → **hashing** (sorting loses indices) |
| "top K" | Sorting | Works, but heap is O(n log k); bucket sort can be O(n) |
| "find the duplicate" | Hashing | If O(1) space and values in [1..n] → **cyclic sort** or **Floyd's cycle detection** |
| "longest increasing" | Sliding window | "Longest increasing **subsequence**" → DP/binary search; "longest increasing **subarray**" → simple scan |
| "intervals" | Sorting by start | "Max non-overlapping" is greedy by **end** time, not start |
| "all paths" | BFS | Need every path → DFS/backtracking; need shortest → BFS |

### 4.5 Constraint-based shortcut

| Clue in constraints | Strong hint |
|---|---|
| `n ≤ 20` | Exponential is fine → backtracking / bitmask |
| `n ≤ 1000` with two sequences | 2D DP O(n·m) |
| `n ≤ 10⁵`, values up to 10⁹ | O(n log n) → sort / heap / binary search |
| "answer fits in range [1, 10⁹]" and a "can we do it with X?" check is easy | **Binary search on answer** |
| "O(1) extra space" | Two pointers, in-place, cyclic sort, bit tricks, Floyd |
| "values are lowercase letters" | 26-size array instead of dict; O(1) space |
| "return modulo 10⁹+7" | Counting DP / combinatorics |

### 4.6 Practice drill: identify without solving

For each problem, cover the right column and decide the pattern + **reason** in 60 seconds.

| Problem | Pattern | Why (structure) |
|---|---|---|
| Contains Duplicate | Hashing | "Seen before?" lookup |
| Longest Substring Without Repeating Characters | Sliding window + set | Contiguous; once a window has a repeat, larger ones do too |
| Subarray Sum Equals K (negatives) | Prefix sum + hash map | Exact range sums; window not monotonic with negatives |
| Koko Eating Bananas | Binary search on answer | Speed k works ⇒ any bigger k works (monotonic) |
| Daily Temperatures | Monotonic stack | Each day waits for the next warmer day |
| Course Schedule | Topological sort | Prerequisite dependencies; detect cycle |
| Coin Change | DP | Min over choices; greedy fails (coins [1,3,4], amount 6) |
| Merge K Sorted Lists | Heap | Repeatedly pick smallest of k heads |
| Rotting Oranges | Multi-source BFS | Simultaneous spreading, minutes = levels |
| Non-overlapping Intervals | Greedy (sort by end) | Keeping the earliest-ending interval never hurts |
| Find the Duplicate Number | Floyd cycle / binary search | O(1) space, values 1..n act as pointers |

---

# PART III — PATTERNS

> **Every pattern follows the same structure:**
> A. Introduction · B. How to recognise · C. Intuition from scratch · D. Variations · E. Template (derived, explained) · F. Dry run · G. Complexity & when NOT to use · H. Common mistakes · I. Interview thinking · J. Practice questions (Level 1→5) · K. Revision card & mastery criteria

---

## P1. Array Fundamentals

### A. Introduction
An array is a row of numbered lockers. You can open locker `i` instantly (O(1) random access), but inserting a new locker in the middle means shifting everyone after it (O(n)). Strings in Python behave like **immutable** arrays of characters.

Almost every DSA pattern is a smarter way of *traversing* an array. Before patterns, you must be fluent in the four basic traversals:

| Traversal | Code shape | Used for |
|---|---|---|
| Forward | `for i in range(n)` | Running totals, first occurrence |
| Backward | `for i in range(n-1, -1, -1)` | Suffix info, "next" relations |
| Both ends | `l, r = 0, n-1; while l < r` | Palindromes, reversal (→ Two Pointers) |
| All pairs | `for i: for j in range(i+1, n)` | **Brute force** (what patterns try to eliminate) |

### B. How to recognise "just an array scan"
- You can answer by **looking at each element once** while remembering a **small amount of state** (best so far, count, previous element).
- Ask: *"If I walk left to right, what do I need to remember from the past to decide about the current element?"* If the answer is "one or two variables" → plain scan. If it's "everything I've seen" → hashing. If it's "the unresolved elements" → stack.

### C. Intuition: the "running state" idea
Problem: *Find the length of the longest run of consecutive 1s in a binary array.*

- Brute force: for each start index, count 1s until a 0 → O(n²).
- Observation: when I'm inside a run, the run length at `i` is just `run length at i-1 + 1`. When I see a 0, the run resets. I never need to look back.
- So keep `current` and `best`:

```python
def findMaxConsecutiveOnes(nums):
    current = best = 0
    for x in nums:
        current = current + 1 if x == 1 else 0   # extend or reset
        best = max(best, current)
    return best
```
This "extend or reset" idea comes back later as **Kadane's algorithm** (P8).

### D. Variations
- Running state (max, min, count, sum)
- Prefix/suffix arrays (precompute left info and right info separately) → leads to P5
- In-place reversal / rotation
- Simulation (follow rules step by step: Plus One, Spiral Matrix)

### E. Template: one pass with state
```python
def scan(nums):
    state = initial_value            # what you must remember about the past
    answer = initial_answer
    for x in nums:
        state = update(state, x)     # absorb current element
        answer = combine(answer, state)
    return answer
```
**Deriving it:** solve by hand, notice what you keep in your head while moving right — that's `state`.

**Rotate array by k (in-place) — the reversal trick:**
```python
def rotate(nums, k):
    n = len(nums); k %= n                 # k could exceed n
    def rev(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1; r -= 1
    rev(0, n - 1)        # [1,2,3,4,5,6,7], k=3 → [7,6,5,4,3,2,1]
    rev(0, k - 1)        # → [5,6,7,4,3,2,1]
    rev(k, n - 1)        # → [5,6,7,1,2,3,4] ✅
```
**Why it works:** rotating right by k moves the last k elements to the front. Reversing all puts them at the front (but backwards); reversing each part fixes the internal order.

### G. Complexity
One pass: O(n) time, O(1) space.

### H. Common mistakes
- Off-by-one in `range(n-1, -1, -1)`.
- Forgetting `k %= n` in rotations.
- Modifying a list while iterating over it.
- `[[0]*m]*n` aliasing bug.

### I. Interview thinking
Say: *"I'll scan once, keeping X as running state, because the answer at position i only depends on X and nums[i]."*

### J. Practice questions

**Level 1 — Fundamentals**
| Pri | Problem | Diff | Learn / Focus | Trap |
|---|---|---|---|---|
| ⭐ | [Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) `LC` | 🟢 | Running state; first prefix sum | Creating a new sum each time (O(n²)) |
| ⭐ | [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) `LC` | 🟢 | Extend-or-reset | Forgetting to update best at the end |
| ✅ | [Third Maximum Number](https://leetcode.com/problems/third-maximum-number/) `LC` | 🟢 | Tracking top-3 state with distinct values | Duplicates counting as different maxima |
| ⭐ | [Plus One](https://dsacourse.com/top-150/plus-one) `DSA150` | 🟢 | Simulation with carry, backward traversal | All 9s → new leading 1 |

**Level 2–3 — Application / Variations**
| Pri | Problem | Diff | Learn / Focus | Trap |
|---|---|---|---|---|
| ⭐ | [Rotate Array](https://leetcode.com/problems/rotate-array/) `LC` | 🟡 | Reversal trick, in-place | k > n |
| ✅ | [Check if Array Is Sorted and Rotated](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/) `LC` | 🟢 | Count "drops" circularly | Forgetting wrap-around comparison |
| ⭐ | [Encode and Decode Strings](https://dsacourse.com/top-150/encode-decode-strings) `DSA150` | 🟡 | Length-prefix encoding (`"4#abcd"`) | Using a delimiter that can appear in the data |

### K. Revision card
- **Core idea:** remember only what the future needs.
- **Mastered when:** you can write any single-pass scan without bugs and state its complexity instantly.

---

## P2. Hashing & Frequency Counting

### A. Introduction
**Analogy:** a library catalogue. Instead of walking every shelf to find a book (O(n)), you look it up by title and go straight to it (O(1)).

A **hash map** (`dict`) stores `key → value` and finds any key in O(1) average time. A **hash set** (`set`) stores just keys. Hashing exists to kill the most common bottleneck in brute force: **searching**.

| | |
|---|---|
| **Solves** | "Have I seen X?", "How many X?", "Where was X?", "Which items belong together?" |
| **Advantages** | O(1) lookup; works on unsorted data; preserves original indices |
| **Limitations** | O(n) extra memory; no ordering (can't ask "smallest key" quickly); keys must be hashable |
| **Data structures** | `dict`, `set`, `Counter`, `defaultdict`, fixed `[0]*26` arrays for letters |
| **Prerequisites** | Arrays, Big-O |

### B. How to recognise
Ask: **"Is my brute force an inner loop that SEARCHES for something?"** If yes, a hash map can usually replace the inner loop.

Clues:
- Check if an element already exists / duplicates.
- Count occurrences / frequencies / majority.
- Find a **complement** (`target − x`).
- **Group** items by a shared signature (anagrams, same pattern).
- Map between two things (isomorphism, index of value).
- Need O(1) lookup in a design problem (LRU, RandomizedSet).

Misleading: "pair with sum" on a **sorted** array → two pointers is better (O(1) space).

### C. Intuition from scratch — Contains Duplicate
> Return True if any value appears at least twice.

1. **By hand:** `[1, 2, 3, 1]`. You'd look at each number and think "have I seen this?" Your brain is *remembering*.
2. **Naive:** compare every pair → O(n²).
3. **Bottleneck:** for each element, we search all previous elements.
4. **Observation:** we only need to answer "is x among the things I've seen?" — a membership question.
5. **Pattern:** a set answers membership in O(1).
```python
def containsDuplicate(nums):
    seen = set()
    for x in nums:
        if x in seen:       # O(1) instead of scanning
            return True
        seen.add(x)
    return False
```
6. **Why it works:** when we reach the second copy of a duplicate, the first copy is already in `seen`.

### D. Variations (with mini-templates)

**1. Membership lookup** — `set` (Contains Duplicate, Longest Consecutive Sequence)

**2. Frequency map** — count, then use the counts
```python
freq = Counter(s)                     # or manual: freq[c] = freq.get(c, 0) + 1
```

**3. Frequency comparison** (anagrams, ransom note)
```python
def isAnagram(s, t):
    if len(s) != len(t): return False
    count = [0] * 26
    for a, b in zip(s, t):
        count[ord(a) - 97] += 1
        count[ord(b) - 97] -= 1
    return all(c == 0 for c in count)   # every letter balanced
```

**4. Complement lookup** — store what you've seen, ask for `target − x` (Two Sum)

**5. Grouping by signature** — build a key that is identical for items in the same group
```python
def groupAnagrams(strs):
    groups = defaultdict(list)
    for w in strs:
        key = [0] * 26
        for c in w:
            key[ord(c) - 97] += 1
        groups[tuple(key)].append(w)     # list isn't hashable → tuple
    return list(groups.values())
```
Signature choices: `tuple(sorted(w))` (O(k log k)) or count tuple (O(k)).

**6. Index mapping** — `value → index` (Two Sum), `value → last seen index` (sliding window later)

**7. Bijection / two-way mapping** (Isomorphic Strings) — two dicts, check both directions.

**8. Prefix sum + hash map** — covered in P5 (counts subarrays with a given sum).

**9. Bucket by frequency** (Top K Frequent in O(n))
```python
def topKFrequent(nums, k):
    freq = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]   # index = frequency
    for num, f in freq.items():
        buckets[f].append(num)
    res = []
    for f in range(len(buckets) - 1, 0, -1):       # high freq → low
        for num in buckets[f]:
            res.append(num)
            if len(res) == k:
                return res
```
**Why:** a frequency can never exceed n, so frequencies themselves are small indices → no sort needed.

### E. Template (derive, don't memorise)
```python
def hashing_template(nums):
    table = {}                       # 1. Decide: what KEY do I search by? what VALUE do I need back?
    for i, x in enumerate(nums):
        key = transform(x)           # 2. The thing I'll be searching for later (x, target-x, signature...)
        if query(key) in table:      # 3. QUERY before INSERT (so an element doesn't match itself)
            use(table[query(key)], i)
        table[key] = update(i)       # 4. INSERT current info for future elements
    return answer
```
Decisions to make:
- **Key:** value? complement? sorted signature? prefix sum?
- **Value:** index? count? list of items?
- **Order:** query-then-insert (pairs with earlier elements) vs. insert-all-then-query (frequency-based).

### C2. Worked medium — Longest Consecutive Sequence (O(n))
> Unsorted array; length of the longest run of consecutive integers. `[100, 4, 200, 1, 3, 2]` → 4 (1,2,3,4).

- **Brute force:** sort → O(n log n). Or for each x, count x+1, x+2… by scanning → O(n²) or worse.
- **Observation 1:** with a set, "does x+1 exist?" is O(1).
- **Observation 2:** if we start counting from *every* number, we redo work (from 2 we count 2,3,4; from 3 we recount 3,4). Only start counting from a **sequence start**: x where `x−1` is NOT in the set.
```python
def longestConsecutive(nums):
    s = set(nums)
    best = 0
    for x in s:
        if x - 1 not in s:              # x is the start of a run
            length = 1
            while x + length in s:
                length += 1
            best = max(best, length)
    return best
```
**Dry run** `s = {100, 4, 200, 1, 3, 2}`:

| x | x−1 in s? | Start? | Count up | length | best |
|---|---|---|---|---|---|
| 100 | 99 ❌ | ✅ | 101 ❌ | 1 | 1 |
| 4 | 3 ✅ | ❌ skip | — | — | 1 |
| 200 | 199 ❌ | ✅ | 201 ❌ | 1 | 1 |
| 1 | 0 ❌ | ✅ | 2 ✅ 3 ✅ 4 ✅ 5 ❌ | 4 | 4 |
| 3 | 2 ✅ | ❌ skip | — | — | 4 |
| 2 | 1 ✅ | ❌ skip | — | — | 4 |

**Why O(n)?** Each number is visited by the `while` loop at most once overall (only from its run's start). Total work ≈ 2n. *This "amortised" argument is a classic interview follow-up — practise saying it.*

### G. Complexity & when NOT to use
- Typically O(n) time, O(n) space.
- **Don't use hashing when:** the array is sorted and O(1) space is required (→ two pointers); you need order/min/max of keys (→ heap / sorted structure); keys are tiny range (→ plain array is faster and simpler).

### H. Common mistakes
- Inserting before querying (element pairs with itself: Two Sum `[3], target 6`).
- Using a `list` as a dict key (unhashable) → use `tuple`.
- `x in list` instead of `x in set` (silent O(n)).
- Forgetting to decrement/remove counts when they hit zero (matters in sliding window).
- Assuming dict iteration order equals sorted order (it's insertion order).

### I. Interview thinking
- **30-second ID:** "My brute force has an inner search loop → replace it with a hash lookup."
- **Explain:** "I trade O(n) space for O(1) lookups, bringing O(n²) down to O(n)."
- **Follow-ups:** "Can you do it in O(1) space?" (sort + two pointers, O(n log n)); "What about hash collisions?" (average O(1), worst O(n); Python handles collisions internally via open addressing); "What if data doesn't fit in memory?" (partition by hash into files — backend-style answer that impresses).

### J. Practice questions

**Level 1 — Fundamentals**
| Pri | Problem | Diff | Variation | Learn / Focus | Trap |
|---|---|---|---|---|---|
| ⭐ | [Contains Duplicate](https://dsacourse.com/top-150/contains-duplicate) `DSA150` | 🟢 | Membership | set vs list lookup | Sorting works but O(n log n) |
| ⭐ | [Valid Anagram](https://dsacourse.com/top-150/valid-anagram) `DSA150` | 🟢 | Frequency compare | 26-array vs Counter | Different lengths |
| ⭐ | [Two Sum](https://dsacourse.com/top-150/two-sum) `DSA150` | 🟢 | Complement lookup | Query before insert | Using same element twice |
| ✅ | [Ransom Note](https://leetcode.com/problems/ransom-note/) `LC` | 🟢 | Frequency subtraction | Counts going negative | Checking presence, not count |

**Level 2 — Application**
| Pri | Problem | Diff | Variation | Learn / Focus | Trap |
|---|---|---|---|---|---|
| ✅ | [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/) `LC` | 🟢 | Bijection | Two-way mapping | Only checking one direction (`"badc"`,`"baba"`) |
| ✅ | [Majority Element](https://leetcode.com/problems/majority-element/) `LC` | 🟢 | Frequency → then Boyer-Moore | Follow-up O(1) space voting | — |
| ⭐ | [Group Anagrams](https://dsacourse.com/top-150/anagram-groups) `DSA150` | 🟡 | Grouping by signature | Designing a hashable key | List as key |

**Level 3–4 — Variations / Interview Mediums**
| Pri | Problem | Diff | Variation | Learn / Focus | Trap |
|---|---|---|---|---|---|
| ⭐ | [Top K Frequent Elements](https://dsacourse.com/top-150/top-k-frequent-elements) `DSA150` | 🟡 | Freq + bucket / heap | O(n) bucket sort idea | Sorting all = O(n log n) (acceptable but mention better) |
| ⭐ | [Valid Sudoku](https://dsacourse.com/top-150/valid-sudoku) `DSA150` | 🟡 | Multiple sets | Box index `(r//3, c//3)` | Forgetting to skip `"."` |
| ⭐ | [Longest Consecutive Sequence](https://dsacourse.com/top-150/longest-consecutive-sequence) `DSA150` | 🟡 | Set + start detection | Amortised O(n) argument | Counting from every element (O(n²)) |
| ✅ | [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) `LC` | 🟡 | Dict + list design | Swap-with-last deletion | Forgetting to update moved element's index |

### K. Revision card
```
HASHING
Clue:     brute force has an inner SEARCH loop / need counts / grouping
Template: for x: query(table) → act → insert(x)
Keys:     value | target-x | signature tuple | prefix sum
Cost:     O(n) time, O(n) space
Traps:    insert-before-query, list keys, `in list`
Say:      "Trade space for O(1) lookups."
```
**Mastery criteria:** solve Group Anagrams + Longest Consecutive Sequence from scratch in < 15 min each, and explain why the latter is O(n).

---

## P3. Two Pointers

### A. Introduction
**Analogy:** two people searching a sorted bookshelf for two books whose prices add to ₹500 — one starts at the cheap end, one at the expensive end. If the total is too high, the expensive-end person steps left; too low, the cheap-end person steps right. They never need to revisit a book.

Two pointers = **two indices that move according to a rule, where each move safely discards candidates**. It turns O(n²) pair-checking into O(n).

| | |
|---|---|
| **Solves** | Pair/triplet search in sorted data, palindromes, in-place filtering/partitioning, merging sorted sequences |
| **Advantages** | O(n) time, usually O(1) space |
| **Limitations** | Needs an *ordering* or a clear movement rule; sorting destroys original indices |
| **Prerequisites** | Arrays, sorting basics |

### B. How to recognise
The real test: **"Can I prove that moving one pointer never skips a valid answer?"**
- Input sorted (or can be sorted without losing what you need).
- Looking for a pair/triplet meeting a condition (sum, difference, area).
- Comparing from both ends (palindrome, reversing).
- In-place: remove/move/compact elements with O(1) space.
- Two sorted sequences to merge or intersect.

### C. Intuition from scratch — Two Sum II (sorted)
> `numbers = [2, 7, 11, 15], target = 9`, sorted ascending. Return 1-indexed positions.

1. **Brute force:** all pairs, O(n²).
2. **Observation:** take smallest `L` and largest `R`.
   - If `L + R > target`: R paired with *anything* (all ≥ L) is still too big → **R can never be in the answer** → discard R (`r -= 1`).
   - If `L + R < target`: L paired with *anything* (all ≤ R) is too small → discard L (`l += 1`).
3. Every step eliminates one element **with proof**, so ≤ n steps.
```python
def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l + 1, r + 1]
        if s > target:
            r -= 1          # numbers[r] too big for ANY remaining partner
        else:
            l += 1          # numbers[l] too small for ANY remaining partner
```
**Dry run** `[2, 7, 11, 15], 9`:

| l | r | nums[l] | nums[r] | sum | Action |
|---|---|---|---|---|---|
| 0 | 3 | 2 | 15 | 17 | > 9 → r-- |
| 0 | 2 | 2 | 11 | 13 | > 9 → r-- |
| 0 | 1 | 2 | 7 | 9 | ✅ return [1, 2] |

### D. Variations

**1. Opposite direction (converging)** — pair sum, palindrome, container, trapping water.
```python
l, r = 0, n - 1
while l < r:
    if condition(l, r): ...; l += 1; r -= 1
    elif need_bigger: l += 1
    else: r -= 1
```

**2. Same direction — read/write (slow/fast)** — in-place filtering.
```python
def moveZeroes(nums):
    write = 0                                  # next position for a non-zero
    for read in range(len(nums)):              # read scans everything
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1
```
Invariant: everything before `write` is final (non-zero, in original order).

**3. Merge pointers** — one pointer per sorted array (Merge Sorted Array: fill **from the back** to avoid overwriting).

**4. Partition (Dutch National Flag)** — three regions with `low`, `mid`, `high`.
```python
def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]; low += 1; mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]; high -= 1   # don't move mid: new value unchecked
```
Invariant: `[0, low)` = 0s, `[low, mid)` = 1s, `(high, n-1]` = 2s, `[mid, high]` = unknown.

**5. Fix one + two pointers** — 3Sum, 4Sum (loop over the first element, two-pointer the rest).

**6. Fast & slow (Floyd)** — cycle detection; covered in P12.

### E. Template — 3Sum (the most important two-pointer medium)
```python
def threeSum(nums):
    nums.sort()                                   # 1. sorting enables pointer logic & dedup
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:      # 2. skip duplicate first elements
            continue
        if nums[i] > 0: break                     # 3. smallest is positive → no zero sum possible
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1; r -= 1
                while l < r and nums[l] == nums[l - 1]:   # 4. skip duplicate second elements
                    l += 1
    return res
```
**Derivation:** 3Sum = "for each `a`, find pairs `b + c = −a`" → Two Sum II inside a loop → O(n²). Duplicates are adjacent after sorting, so skipping equal neighbours removes duplicate triplets.

### C2. Worked medium — Container With Most Water
Area = `min(h[l], h[r]) * (r − l)`. Start widest. **Which pointer to move?** The shorter wall limits the area. Moving the **taller** wall inward: width shrinks, height is still capped by the shorter wall → area can only decrease. So the shorter wall's best possible container *is the current one* → discard it.
```python
def maxArea(height):
    l, r, best = 0, len(height) - 1, 0
    while l < r:
        best = max(best, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]: l += 1
        else: r -= 1
    return best
```

### G. Complexity & when NOT to use
- O(n) after sorting → overall O(n log n) if you sort; O(1) extra space (sorting in Python uses O(n) internally — mention honestly if asked).
- **Don't use** when you need original indices of an unsorted array (→ hashing), or the movement rule can't be proven (e.g., subarray sum with negatives).

### H. Common mistakes
- `while l <= r` when the two pointers must be different elements (use `<`).
- Forgetting duplicate skipping in 3Sum → duplicate triplets.
- Moving both pointers when only one is justified.
- In Dutch flag, advancing `mid` after swapping with `high`.

### I. Interview thinking
- **ID:** "It's sorted and I need a pair → each comparison lets me discard one end."
- **Correctness line:** "If the sum is too big, the right element is too big even with the smallest partner, so it can't be part of any answer."
- **Follow-ups:** 3Sum closest; 4Sum (another loop, O(n³)); "what if not sorted?" (sort or hash).

### J. Practice questions
| Lvl | Pri | Problem | Diff | Variation | Learn / Focus | Trap |
|---|---|---|---|---|---|---|
| 1 | ⭐ | [Valid Palindrome](https://dsacourse.com/top-150/valid-palindrome) `DSA150` | 🟢 | Opposite | Skip non-alphanumerics with inner whiles | Case sensitivity |
| 1 | ⭐ | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) `LC` | 🟢 | Read/write | Invariant of `write` | Extra array |
| 1 | ✅ | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) `LC` | 🟢 | Read/write | Compare with last written | Returning wrong length |
| 1 | ✅ | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) `LC` | 🟢 | Merge from back | Why fill from the end | Overwriting nums1 |
| 2 | ✅ | [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) `LC` | 🟢 | Opposite, fill from back | Largest square is at an end | Negatives |
| 2 | ⭐ | [Two Sum II — Sorted Input](https://dsacourse.com/top-150/pair-with-target-sum) `DSA150` | 🟡 | Opposite | Elimination proof | 1-indexed output |
| 3 | ⭐ | [Sort Colors](https://dsacourse.com/top-150/sort-colors) `DSA150` | 🟡 | 3-way partition | Invariants of 3 regions | Advancing mid after high swap |
| 3 | ✅ | [Boats to Save People](https://leetcode.com/problems/boats-to-save-people/) `LC` | 🟡 | Sort + opposite (greedy) | Pair heaviest with lightest | — |
| 4 | ⭐ | [3Sum](https://dsacourse.com/top-150/3sum) `DSA150` | 🟡 | Fix one + pair | Dedup logic | Duplicates |
| 4 | ⭐ | [Container With Most Water](https://dsacourse.com/top-150/container-with-most-water) `DSA150` | 🟡 | Opposite, greedy move | Why move the shorter wall | Moving the taller |
| 4 | 🚀 | [4Sum](https://leetcode.com/problems/4sum/) `LC` | 🟡 | Two fixed + pair | Generalising k-sum | Dedup at two levels |
| 5 | ⭐ | [Trapping Rain Water](https://dsacourse.com/top-150/trapping-rain-water) `DSA150` | 🔴 | Opposite with leftMax/rightMax | Water at i = min(maxL, maxR) − h[i] | Can also be prefix max / stack |

**Trapping Rain Water key insight:** process the side with the smaller max, because that side's water level is already determined (the other side has something at least as tall).
```python
def trap(height):
    l, r = 0, len(height) - 1
    left_max = right_max = water = 0
    while l < r:
        if height[l] < height[r]:
            left_max = max(left_max, height[l])
            water += left_max - height[l]
            l += 1
        else:
            right_max = max(right_max, height[r])
            water += right_max - height[r]
            r -= 1
    return water
```

### K. Revision card
```
TWO POINTERS
Clue:   sorted / pairs / both ends / in-place / merge
Rule:   each move must DISCARD a provably useless candidate
Types:  opposite | read-write | merge | 3-way partition | fix-one + pair | fast-slow
Cost:   O(n) (+ sort O(n log n)), O(1) space
Traps:  l<r vs l<=r, duplicate skipping, wrong pointer moved
```
**Mastery:** 3Sum and Container With Most Water from scratch, with the "why this pointer moves" proof spoken aloud.

---

## P4. Sliding Window

### A. Introduction
**Analogy:** a train window. As the train moves, one new tree enters on the right and one old tree leaves on the left. You don't re-count all trees — you update by what entered and what left.

A sliding window is a **contiguous range `[l, r]`** that you grow by moving `r` and shrink by moving `l`, maintaining some **state** about its contents incrementally. It's a special form of same-direction two pointers.

| | |
|---|---|
| **Solves** | Longest/shortest/count of contiguous subarrays/substrings satisfying a condition |
| **Advantages** | O(n): each element enters once and leaves once |
| **Limitations** | Requires **monotonic validity**: shrinking a window must move it toward validity (and growing away from it). Fails with negative numbers for sum targets. |
| **Data structures** | Counters/dicts/sets for window contents, deque for window max |
| **Prerequisites** | Hashing, two pointers |

### B. How to recognise
1. Answer is **contiguous** (subarray/substring). If not contiguous → not a window.
2. A **condition** must hold inside the window (no repeats, sum ≥ target, ≤ k distinct, contains all of t).
3. **Monotonicity check (the real test):** *"If window [l, r] is invalid, is every larger window containing it also invalid?"* (for "longest" problems), or *"If [l, r] is valid, is every larger window also valid?"* (for "shortest" problems). If yes → sliding window works. If no (e.g., sums with negatives) → prefix sum + hashing.

| Wording | Window type |
|---|---|
| "subarray of size k", "every k consecutive" | Fixed |
| "longest substring with …", "at most k …" | Variable, maximise |
| "minimum length subarray with sum ≥ …", "smallest window containing" | Variable, minimise |
| "number of subarrays with …" | Variable, count (`r − l + 1` trick) |
| "exactly k …" | atMost(k) − atMost(k − 1) |

### C. Intuition from scratch — fixed window
> Max sum of any 3 consecutive elements in `[2, 1, 5, 1, 3, 2]`.

- Brute: sum every window of 3 → O(n·k).
- Observation: window `[1..3]` = window `[0..2]` − `nums[0]` + `nums[3]`. Adjacent windows share k−1 elements!
```python
def max_sum_k(nums, k):
    window = sum(nums[:k]); best = window
    for r in range(k, len(nums)):
        window += nums[r] - nums[r - k]     # add entering, remove leaving
        best = max(best, window)
    return best
```

### C2. Intuition — variable window: Longest Substring Without Repeating Characters
> `s = "abcabcbb"` → 3 (`"abc"`)

- Brute: check all O(n²) substrings, each O(n) to verify → O(n³).
- Observation 1: if `s[l..r]` has a repeat, any longer substring containing it also has a repeat → once invalid, **move l** instead of restarting.
- Observation 2: `r` never needs to go backward.
```python
def lengthOfLongestSubstring(s):
    window = set()
    l = best = 0
    for r, c in enumerate(s):
        while c in window:          # shrink until c can enter validly
            window.remove(s[l])
            l += 1
        window.add(c)
        best = max(best, r - l + 1)
    return best
```
**Dry run** `"abcabcbb"`:

| r | c | while c in window → removals | window after add | l | len | best |
|---|---|---|---|---|---|---|
| 0 | a | — | {a} | 0 | 1 | 1 |
| 1 | b | — | {a,b} | 0 | 2 | 2 |
| 2 | c | — | {a,b,c} | 0 | 3 | 3 |
| 3 | a | remove a (l→1) | {b,c,a} | 1 | 3 | 3 |
| 4 | b | remove b (l→2) | {c,a,b} | 2 | 3 | 3 |
| 5 | c | remove c (l→3) | {a,b,c} | 3 | 3 | 3 |
| 6 | b | remove a (l→4), remove b (l→5) | {c,b} | 5 | 2 | 3 |
| 7 | b | remove c (l→6), remove b (l→7) | {b} | 7 | 1 | 3 |

**Why O(n)?** `l` and `r` each move at most n times total. The inner `while` is not "n per iteration" — it's n *across the whole run* (amortised).

### D. Variations
1. **Fixed size k** — add right, remove `nums[r-k]`.
2. **Longest valid** — shrink *while invalid*, then record.
3. **Shortest valid** — shrink *while valid*, recording inside the loop.
4. **Count subarrays** — for "at most" conditions, every valid window ending at `r` contributes `r − l + 1` subarrays.
5. **Exactly K** — `atMost(K) − atMost(K−1)`.
6. **Frequency-matching window** — compare window counts to a target count (anagrams, permutation in string, minimum window substring) using a `need`/`have` counter.
7. **Window with replacement budget** — valid if `window_len − max_freq ≤ k`.
8. **Window max/min** — monotonic deque (P11).

### E. Templates
```python
# LONGEST valid window
def longest(arr):
    state = Counter(); l = best = 0
    for r, x in enumerate(arr):
        state[x] += 1                         # 1. expand: include arr[r]
        while not valid(state):               # 2. shrink until valid again
            state[arr[l]] -= 1
            if state[arr[l]] == 0: del state[arr[l]]
            l += 1
        best = max(best, r - l + 1)           # 3. window [l, r] is the best ending at r
    return best

# SHORTEST valid window
def shortest(arr):
    state = ...; l = 0; best = float('inf')
    for r, x in enumerate(arr):
        add(x)
        while valid(state):                   # while valid, try to shrink further
            best = min(best, r - l + 1)       # record BEFORE removing
            remove(arr[l]); l += 1
    return best if best != float('inf') else 0

# COUNT windows (at most K)
def count_at_most(arr, K):
    l = count = 0
    for r in range(len(arr)):
        add(arr[r])
        while invalid(K): remove(arr[l]); l += 1
        count += r - l + 1                    # subarrays ending at r: [l..r], [l+1..r], ..., [r..r]
    return count
```
**How to derive instead of memorise:** ask (1) what state do I keep about the window? (2) what makes it invalid? (3) do I record when valid (longest) or while shrinking (shortest)?

### C3. Worked hard — Minimum Window Substring
> Smallest substring of `s` containing all characters of `t` (with multiplicity).

State: `need = Counter(t)`, `have` = number of distinct chars whose requirement is met.
```python
def minWindow(s, t):
    if not t: return ""
    need = Counter(t); window = Counter()
    required = len(need); formed = 0
    l = 0; best = (float('inf'), 0, 0)
    for r, c in enumerate(s):
        window[c] += 1
        if c in need and window[c] == need[c]:
            formed += 1                                   # one more char fully satisfied
        while formed == required:                         # valid → try to shrink
            if r - l + 1 < best[0]:
                best = (r - l + 1, l, r)
            lc = s[l]
            window[lc] -= 1
            if lc in need and window[lc] < need[lc]:
                formed -= 1                               # broke a requirement
            l += 1
    return "" if best[0] == float('inf') else s[best[1]:best[2] + 1]
```

### C4. Worked medium — Longest Repeating Character Replacement
Window is valid if `len − (count of most frequent char) ≤ k` (we can replace the rest).
```python
def characterReplacement(s, k):
    count = Counter(); l = maxf = best = 0
    for r, c in enumerate(s):
        count[c] += 1
        maxf = max(maxf, count[c])
        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1; l += 1
        best = max(best, r - l + 1)
    return best
```
*Subtle point:* `maxf` is never decreased. This is safe because the answer only grows when a window with a **larger** maxf appears; a stale maxf can only make us keep a window of an already-achieved size. Great follow-up to explain.

### G. Complexity & when NOT to use
- O(n) time; space O(k) or O(alphabet).
- **Don't use** when: not contiguous (subsequence → DP), sums with negatives (→ prefix sum + hash), need max per window with plain variables (→ deque).

### H. Common mistakes
- Using `if` instead of `while` for shrinking (window stays invalid).
- Recording the answer at the wrong moment (shortest vs longest).
- Not deleting zero-count keys when the condition uses `len(counter)` (distinct count).
- Off-by-one in window length: it's `r − l + 1`.
- Applying a window to "sum = k" with negatives.

### I. Interview thinking
- **ID in 30 s:** "Contiguous + condition that breaks monotonically → window."
- **Explain:** "Each index enters and leaves the window once, so it's O(n) even with the inner while."
- **Follow-ups:** "What if numbers can be negative?" (prefix sum); "What if we need the count instead of longest?" (`r − l + 1`); "exactly k?" (atMost difference).

### J. Practice questions
| Lvl | Pri | Problem | Diff | Variation | Learn / Focus | Trap |
|---|---|---|---|---|---|---|
| 1 | ⭐ | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) `LC` | 🟢 | Fixed | Add-entering/remove-leaving | Recomputing sums |
| 1 | ⭐ | [Best Time to Buy and Sell Stock](https://dsacourse.com/top-150/best-time-to-buy-and-sell-stock) `DSA150` | 🟢 | Running min (window from min to r) | Track min so far | Selling before buying |
| 2 | ⭐ | [Longest Substring Without Repeating Characters](https://dsacourse.com/top-150/longest-substring-without-repeating-characters) `DSA150` | 🟡 | Longest, set | Shrink while invalid | `if` instead of `while` |
| 2 | ⭐ | [Minimum Size Subarray Sum](https://dsacourse.com/top-150/minimum-size-subarray-sum) `DSA150` | 🟡 | Shortest | Record while valid | Works because all positive |
| 2 | ✅ | [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) `LC` | 🟡 | Longest, budget k | Count zeros in window | — |
| 3 | ⭐ | [Permutation in String](https://dsacourse.com/top-150/permutation-in-string) `DSA150` | 🟡 | Fixed + frequency match | Compare 26-count arrays | Rebuilding counts each step |
| 3 | ✅ | [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) `LC` | 🟡 | Fixed + frequency | Collect all start indices | — |
| 3 | ✅ | [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) `LC` | 🟡 | At most 2 distinct | Delete zero-count keys | `len(counter)` wrong |
| 3 | ✅ | [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/) `LC` | 🟡 | Count | `r − l + 1` counting | k ≤ 1 edge case |
| 4 | ⭐ | [Longest Repeating Character Replacement](https://dsacourse.com/top-150/longest-repeating-character-replacement) `DSA150` | 🟡 | Budget via maxf | `len − maxf ≤ k` | Why stale maxf is fine |
| 4 | ✅ | [Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/) `LC` | 🟡 | Exactly K | atMost(k) − atMost(k−1) | — |
| 5 | ⭐ | [Minimum Window Substring](https://dsacourse.com/top-150/minimum-window-substring) `DSA150` | 🔴 | Shortest + freq match | `formed/required` counter | Multiplicity of chars in t |
| 5 | 🚀 | [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/) `LC` | 🔴 | Exactly K | Same trick, harder state | — |
| 5 | ⭐ | [Sliding Window Maximum](https://dsacourse.com/top-150/sliding-window-maximum) `DSA150` | 🔴 | Window + deque | **Do after P11** | Heap = O(n log n) |

### K. Revision card
```
SLIDING WINDOW
Clue:    CONTIGUOUS + condition with MONOTONIC validity
Loop:    for r: add(r); while bad: remove(l), l++; record
Longest: shrink while INVALID, record after
Shortest:shrink while VALID, record inside
Count:   += r-l+1 ;  exactly K = atMost(K) - atMost(K-1)
Fails:   negatives with sum targets → prefix sum + hashmap
Cost:    O(n) amortised
```
**Mastery:** Minimum Window Substring with ≤ 1 hint; explain the monotonicity requirement and why negatives break it.

---

## P5. Prefix Sum & Difference Array

### A. Introduction
**Analogy:** a car's odometer. To know how far you drove between Pune and Mumbai, you don't re-drive the route — you subtract the odometer reading at Pune from the reading at Mumbai.

`prefix[i]` = sum of the first `i` elements. Then **sum of `nums[l..r]` = `prefix[r+1] − prefix[l]`** in O(1).

| | |
|---|---|
| **Solves** | Range sums, subarray sums equal to K (even with negatives), balance problems (equal 0s/1s), range updates (difference array) |
| **Advantages** | O(1) range queries after O(n) preprocessing; handles negatives (unlike windows) |
| **Limitations** | Static data (updates require rebuilding → Fenwick/segment tree in P24) |
| **Prerequisites** | Arrays, hashing |

### B. How to recognise
- "Sum/count of elements between i and j", many queries.
- "Number of subarrays whose sum equals K" (esp. with negatives or zeros).
- "Longest subarray with sum K / equal number of X and Y" (map to +1/−1).
- "Subarray sum divisible by K" (prefix mod K).
- "Product of all except self" (prefix × suffix).
- Many **range updates** then final values → **difference array**.

### C. Intuition from scratch
Build the prefix array with a leading 0 (this removes all special cases for `l = 0`):
```python
nums   = [3, 1, 4, 1, 5]
prefix = [0, 3, 4, 8, 9, 14]      # prefix[i] = sum(nums[:i])
# sum(nums[1..3]) = prefix[4] - prefix[1] = 9 - 3 = 6  → 1+4+1 ✅
```
```python
prefix = [0] * (len(nums) + 1)
for i, x in enumerate(nums):
    prefix[i + 1] = prefix[i] + x
```

### C2. The big one — Prefix Sum + Hash Map (Subarray Sum Equals K)
> Count subarrays with sum exactly `k`. Values can be negative.

- **Brute:** all (l, r) pairs with running sums → O(n²).
- **Why not sliding window?** With negatives, adding an element can *decrease* the sum, so "shrink when too big" isn't valid.
- **Observation:** subarray `(j, i]` has sum `k` ⇔ `prefix[i] − prefix[j] = k` ⇔ `prefix[j] = prefix[i] − k`. So at each `i`, **count how many earlier prefixes equal `prefix[i] − k`** → that's Two Sum on prefix sums!
```python
def subarraySum(nums, k):
    count = {0: 1}          # empty prefix: lets subarrays starting at index 0 be counted
    cur = res = 0
    for x in nums:
        cur += x
        res += count.get(cur - k, 0)      # earlier prefixes that complete a sum-k subarray
        count[cur] = count.get(cur, 0) + 1
    return res
```
**Dry run** `nums = [1, 2, 3], k = 3`:

| x | cur | cur − k | count[cur−k] | res | count after |
|---|---|---|---|---|---|
| — | 0 | — | — | 0 | {0:1} |
| 1 | 1 | −2 | 0 | 0 | {0:1, 1:1} |
| 2 | 3 | 0 | 1 → subarray [1,2] | 1 | {0:1, 1:1, 3:1} |
| 3 | 6 | 3 | 1 → subarray [3] | 2 | {…, 6:1} |

### D. Variations
| Variation | Key stored in map | Value | Example |
|---|---|---|---|
| Count subarrays sum = k | prefix sum | count | Subarray Sum Equals K |
| Longest subarray sum = k | prefix sum | **first** index seen | Contiguous Array (0→−1, k = 0) |
| Divisible by k | prefix % k | count / first index | Continuous Subarray Sum |
| Range query | — (just array) | — | Range Sum Query |
| Prefix × suffix | — | — | Product of Array Except Self |
| Equilibrium | total − left − nums[i] == left | — | Find Pivot Index |
| 2D prefix | `P[r+1][c+1] = P[r][c+1] + P[r+1][c] − P[r][c] + grid[r][c]` | — | Range Sum Query 2D |

**Product of Array Except Self (no division, O(1) extra):**
```python
def productExceptSelf(nums):
    n = len(nums); res = [1] * n
    left = 1
    for i in range(n):              # res[i] = product of everything LEFT of i
        res[i] = left; left *= nums[i]
    right = 1
    for i in range(n - 1, -1, -1):  # multiply by product of everything RIGHT of i
        res[i] *= right; right *= nums[i]
    return res
```

### D2. Difference Array (range updates)
To add `v` to every element of `[l, r]` many times, mark `diff[l] += v` and `diff[r+1] −= v`, then take a prefix sum at the end.
```python
def apply_updates(n, updates):          # updates: (l, r, v)
    diff = [0] * (n + 1)
    for l, r, v in updates:
        diff[l] += v
        diff[r + 1] -= v                # stop the effect after r
    res, run = [], 0
    for i in range(n):
        run += diff[i]
        res.append(run)
    return res
```
Each update O(1) instead of O(r − l + 1). Used in Car Pooling, Corporate Flight Bookings, "minimum platforms" style questions.

### G. Complexity & when NOT to use
- Build O(n); query O(1); prefix+hash O(n) time & space.
- **Don't use** when values change between queries (→ Fenwick/segment tree) or when all numbers are positive and you need longest/shortest (sliding window is O(1) space).

### H. Common mistakes
- Forgetting `count = {0: 1}` (misses subarrays starting at index 0).
- For "longest", overwriting the first index (store only if key not present).
- Off-by-one: `prefix[r+1] − prefix[l]`.
- Negative modulo: Python's `%` is already non-negative for positive k (unlike Java/C++ — mention).

### J. Practice questions
| Lvl | Pri | Problem | Diff | Variation | Learn / Focus | Trap |
|---|---|---|---|---|---|---|
| 1 | ⭐ | [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) `LC` | 🟢 | Range query | Leading-zero prefix | Off-by-one |
| 1 | ⭐ | [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) `LC` | 🟢 | Left vs right sums | total − left − x | — |
| 2 | ⭐ | [Product of Array Except Self](https://dsacourse.com/top-150/product-except-self) `DSA150` | 🟡 | Prefix × suffix | Two passes, O(1) extra | Division with zeros |
| 3 | ⭐ | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) `LC` | 🟡 | Prefix + count map | Two Sum on prefixes | Missing `{0:1}` |
| 3 | ✅ | [Contiguous Array](https://leetcode.com/problems/contiguous-array/) `LC` | 🟡 | Longest, first index | 0 → −1 mapping | Overwriting first index |
| 4 | ✅ | [Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/) `LC` | 🟡 | Prefix mod k | Length ≥ 2 condition | `{0: -1}` init |
| 4 | ✅ | [Car Pooling](https://leetcode.com/problems/car-pooling/) `LC` | 🟡 | Difference array | Drop-off at `to` (not to+1) | Off-by-one |
| 4 | ✅ | [Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/) `LC` | 🟡 | Difference array | 1-indexed ranges | — |

### K. Revision card
```
PREFIX SUM
sum(l..r) = P[r+1] - P[l]          (P has leading 0)
Subarray sum k: count prefixes == cur - k   (init {0:1})
Longest:        store FIRST index of each prefix
Mod k:          key = prefix % k
Range updates:  diff[l]+=v, diff[r+1]-=v, then prefix
Use over window when NEGATIVES exist.
```
**Mastery:** Subarray Sum Equals K + Contiguous Array without hints; explain why sliding window fails with negatives.

---

## P6. Sorting

### A. Introduction
**Analogy:** arranging cards in your hand before playing — once sorted, you instantly see pairs, runs, and gaps.

Sorting is rarely the *answer*; it's the **preprocessing step that makes another pattern possible** (two pointers, intervals, greedy, binary search, dedup). You must also know merge sort and quickselect because interviewers ask about them and they unlock "divide and conquer" problems.

### B. How to recognise
- Order would make neighbours meaningful (closest pair, merge overlaps, group duplicates).
- Greedy needs to process items in a specific order (by end time, by deadline, by ratio).
- "Kth largest/smallest" → sort (O(n log n)), heap (O(n log k)), or quickselect (O(n) avg).
- Custom ordering ("largest number formed", "sort by frequency then value").

### C. Core algorithms you must be able to write

**Merge sort** — divide in half, sort each, merge. Stable, O(n log n) always, O(n) space.
```python
def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left, right = merge_sort(a[:mid]), merge_sort(a[mid:])
    res, i, j = [], 0, 0
    while i < len(left) and j < len(right):        # merge two sorted lists (two pointers!)
        if left[i] <= right[j]:                    # <= keeps it stable
            res.append(left[i]); i += 1
        else:
            res.append(right[j]); j += 1
    res.extend(left[i:]); res.extend(right[j:])
    return res
```
Merge sort is the basis of "count inversions" / Reverse Pairs: during merge, when `right[j] < left[i]`, all remaining left elements form inversions with `right[j]`.

**Quickselect** — find the k-th largest in O(n) average.
```python
import random
def findKthLargest(nums, k):
    target = len(nums) - k                          # index in ascending order
    def select(lo, hi):
        pivot = nums[random.randint(lo, hi)]
        lt, i, gt = lo, lo, hi                      # 3-way partition (handles duplicates)
        while i <= gt:
            if nums[i] < pivot: nums[lt], nums[i] = nums[i], nums[lt]; lt += 1; i += 1
            elif nums[i] > pivot: nums[i], nums[gt] = nums[gt], nums[i]; gt -= 1
            else: i += 1
        if target < lt: return select(lo, lt - 1)
        if target > gt: return select(gt + 1, hi)
        return pivot                                # target falls in the "== pivot" block
    return select(0, len(nums) - 1)
```

**Counting / bucket sort** — when values are in a small range (0..k): O(n + k).

**Custom comparator** — Largest Number:
```python
from functools import cmp_to_key
def largestNumber(nums):
    s = list(map(str, nums))
    s.sort(key=cmp_to_key(lambda a, b: -1 if a + b > b + a else (1 if a + b < b + a else 0)))
    res = "".join(s)
    return "0" if res[0] == "0" else res
```

### D. Sorting algorithm comparison
| Algorithm | Time (avg / worst) | Space | Stable | When |
|---|---|---|---|---|
| Python `sort` (Timsort) | O(n log n) / O(n log n) | O(n) | ✅ | Default always |
| Merge sort | O(n log n) / O(n log n) | O(n) | ✅ | Linked lists, inversions |
| Quick sort | O(n log n) / O(n²) | O(log n) | ❌ | In-place; randomise pivot |
| Heap sort | O(n log n) / O(n log n) | O(1) | ❌ | Memory-tight |
| Counting sort | O(n + k) | O(k) | ✅ | Small integer range |
| Insertion sort | O(n²) | O(1) | ✅ | Nearly sorted, tiny n |

### H. Common mistakes
- Sorting when you need original indices (store `(value, index)` pairs).
- Forgetting sorting costs O(n log n) in your final complexity.
- Comparator returning bool instead of −1/0/1 with `cmp_to_key`.
- Largest Number: all zeros → return `"0"`.

### J. Practice questions
| Lvl | Pri | Problem | Diff | Learn / Focus | Trap |
|---|---|---|---|---|---|
| 1 | ⭐ | [Sort an Array](https://leetcode.com/problems/sort-an-array/) `LC` | 🟡 | Write merge sort yourself | Using built-in sort defeats the purpose |
| 2 | ✅ | [Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/) `LC` | 🟡 | Counter + sort / bucket | — |
| 3 | ⭐ | [Kth Largest Element in an Array](https://dsacourse.com/top-150/kth-largest-element) `DSA150` | 🟡 | Quickselect vs heap vs sort | Index `n − k` |
| 3 | ✅ | [Largest Number](https://leetcode.com/problems/largest-number/) `LC` | 🟡 | Custom comparator `a+b` vs `b+a` | All zeros |
| 5 | 🚀 | [Reverse Pairs](https://leetcode.com/problems/reverse-pairs/) `LC` | 🔴 | Merge sort counting | Counting before merging |

### K. Revision card
```
SORTING = preprocessing for two pointers / greedy / intervals / binary search
Know by heart: merge sort, quickselect (avg O(n)), cmp_to_key
Kth largest: sort O(n log n) | heap O(n log k) | quickselect O(n) avg
Keep indices: sort (value, index) pairs
```

---

## P7. Intervals

### A. Introduction
**Analogy:** your Google Calendar. Meetings are `[start, end]`. Questions: which meetings clash? How many rooms do we need? Can I merge back-to-back blocks?

### B. How to recognise
Input is a list of `[start, end]` pairs (meetings, bookings, ranges, balloons). Almost always step 1 is **sort**.

| Goal | Sort by | Technique |
|---|---|---|
| Merge overlapping | start | Compare with last merged |
| Insert into sorted list | (already sorted) | Three phases: before / overlap / after |
| Max non-overlapping (or min removals) | **end** | Greedy: keep earliest-ending |
| Min arrows / points to cover | end | Same greedy |
| Intersection of two lists | (both sorted) | Two pointers |
| Max simultaneous (rooms/platforms) | start & end separately | Sweep line or min-heap of end times |

**Overlap test:** `a` and `b` overlap iff `a.start <= b.end and b.start <= a.end` (check whether touching endpoints count as overlap — clarify!).

### C. Intuition — Merge Intervals
After sorting by start, any interval that overlaps the current merged block must come **right after it** (nothing earlier can start later). So compare only with the last merged interval.
```python
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:                       # overlaps last block
            merged[-1][1] = max(merged[-1][1], end)      # extend (max! it may be contained)
        else:
            merged.append([start, end])
    return merged
```
**Dry run** `[[1,3],[8,10],[2,6],[15,18]]` → sorted `[[1,3],[2,6],[8,10],[15,18]]`:

| Current | Last merged | start ≤ last.end? | merged after |
|---|---|---|---|
| — | — | — | [[1,3]] |
| [2,6] | [1,3] | 2 ≤ 3 ✅ | [[1,6]] |
| [8,10] | [1,6] | 8 ≤ 6 ❌ | [[1,6],[8,10]] |
| [15,18] | [8,10] | 15 ≤ 10 ❌ | [[1,6],[8,10],[15,18]] |

### D. Key variations

**Non-overlapping Intervals (min removals) — greedy by end:**
```python
def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])
    removed, prev_end = 0, float('-inf')
    for s, e in intervals:
        if s >= prev_end: prev_end = e      # keep it: ends earliest, leaves most room
        else: removed += 1                  # overlaps → drop the current (it ends later)
    return removed
```
**Why by end?** The interval that ends first leaves the most room for the rest — an *exchange argument*: swapping any optimal solution's first choice with the earliest-ending interval never makes it worse.

**Meeting Rooms II — sweep line:**
```python
def minMeetingRooms(intervals):
    starts = sorted(i[0] for i in intervals)
    ends = sorted(i[1] for i in intervals)
    rooms = best = e = 0
    for s in starts:
        while e < len(ends) and ends[e] <= s:   # meetings that ended free a room
            rooms -= 1; e += 1
        rooms += 1
        best = max(best, rooms)
    return best
```
(Alternative: min-heap of end times; heap size = rooms in use.)

### H. Common mistakes
- Forgetting `max()` when extending (contained intervals like `[1,10],[2,3]`).
- Sorting by start for max-non-overlapping (must be end).
- Not clarifying whether `[1,2]` and `[2,3]` overlap.

### J. Practice questions
| Lvl | Pri | Problem | Diff | Variation | Trap |
|---|---|---|---|---|---|
| 2 | ⭐ | [Merge Intervals](https://dsacourse.com/top-150/merge-intervals) `DSA150` | 🟡 | Sort by start + merge | Contained intervals |
| 2 | ⭐ | [Insert Interval](https://dsacourse.com/top-150/insert-interval) `DSA150` | 🟡 | 3-phase scan | Empty list |
| 3 | ⭐ | [Non-overlapping Intervals](https://dsacourse.com/top-150/non-overlapping-intervals) `DSA150` | 🟡 | Greedy by end | Sorting by start |
| 3 | ✅ | [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) `LC` | 🟡 | Greedy by end | Touching counts as overlap here |
| 3 | ✅ | [Interval List Intersections](https://dsacourse.com/top-150/interval-list-intersections) `DSA150` | 🟡 | Two pointers | Advance the one ending first |
| 4 | ⭐ | [Meeting Rooms II](https://dsacourse.com/top-150/minimum-meeting-rooms) `DSA150` | 🟡 | Sweep / heap | `<=` vs `<` at boundaries |
| 5 | 🚀 | [Minimum Interval to Include Each Query](https://dsacourse.com/top-150/minimum-interval-to-include-each-query) `DSA150` | 🔴 | Sort queries + heap | Return answers in original query order |

### K. Revision card
```
INTERVALS → SORT FIRST
merge/insert: by start | max non-overlap / arrows: by END (greedy)
rooms/platforms: sweep starts & ends, or heap of ends
overlap: a.s <= b.e and b.s <= a.e  (clarify touching)
```

---

## P8. Kadane's Algorithm

### A. Introduction
**Analogy:** a running profit streak. If your accumulated streak goes negative, it's a burden — drop it and start fresh from today.

Kadane finds the **maximum-sum contiguous subarray** in O(n). It's the simplest **dynamic programming** you'll ever see: `best_ending_here[i] = max(nums[i], best_ending_here[i−1] + nums[i])`.

### B. How to recognise
- "Maximum (or minimum) sum/product of a **contiguous** subarray."
- "Extend the previous run or start over" decisions.

### C. Intuition
For each index, the best subarray **ending exactly here** either extends the best one ending at `i−1`, or starts fresh at `i`. Extending is only worth it if the previous best is positive.
```python
def maxSubArray(nums):
    cur = best = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)      # extend or restart
        best = max(best, cur)
    return best
```
**Dry run** `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`:

| x | cur + x | max(x, cur+x) = cur | best |
|---|---|---|---|
| −2 | — | −2 | −2 |
| 1 | −1 | 1 | 1 |
| −3 | −2 | −2 | 1 |
| 4 | 2 | 4 | 4 |
| −1 | 3 | 3 | 4 |
| 2 | 5 | 5 | 5 |
| 1 | 6 | 6 | **6** |
| −5 | 1 | 1 | 6 |
| 4 | 5 | 5 | 6 |

### D. Variations
- **All negatives:** initialising with `nums[0]` (not 0) handles it.
- **Maximum Product Subarray:** a negative × negative becomes big → track both `cur_max` and `cur_min`.
```python
def maxProduct(nums):
    cur_max = cur_min = best = nums[0]
    for x in nums[1:]:
        candidates = (x, cur_max * x, cur_min * x)
        cur_max, cur_min = max(candidates), min(candidates)
        best = max(best, cur_max)
    return best
```
- **Circular array:** answer = max(normal Kadane, total − minimum subarray); if all negative, return normal Kadane.
- **Best Time to Buy and Sell Stock** is Kadane on daily differences.

### J. Practice questions
| Lvl | Pri | Problem | Diff | Learn | Trap |
|---|---|---|---|---|---|
| 2 | ⭐ | [Maximum Subarray](https://dsacourse.com/top-150/max-subarray) `DSA150` | 🟡 | Extend or restart | Init with 0 fails all-negative |
| 3 | ⭐ | [Maximum Product Subarray](https://dsacourse.com/top-150/maximum-product-subarray) `DSA150` | 🟡 | Track max & min | Zeros and sign flips |
| 4 | ✅ | [Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/) `LC` | 🟡 | total − min subarray | All-negative case |

### K. Revision card
```
KADANE: cur = max(x, cur + x); best = max(best, cur)   init with nums[0]
Product: track cur_max & cur_min (negatives swap them)
Circular: max(kadane, total - min_subarray) unless all negative
```

---

## P9. Binary Search

### A. Introduction
**Analogy:** guessing a number between 1 and 100 with "higher/lower" hints. You always guess the middle, so each guess halves the possibilities: at most 7 guesses for 100, ~30 for a billion.

Binary search works on **any search space where a yes/no condition flips exactly once**:
```
index/answer:  0  1  2  3  4  5  6  7
condition:     F  F  F  F  T  T  T  T      ← find the FIRST T
```
This is the most important mental model. A sorted array is just one example: `condition(i) = nums[i] >= target`.

| | |
|---|---|
| **Solves** | Search in sorted data, boundaries (first/last occurrence), rotated arrays, and **optimisation problems via "binary search on answer"** |
| **Advantages** | O(log n) — 10⁹ possibilities in ~30 steps |
| **Limitations** | Requires monotonic condition; off-by-one bugs are notorious |
| **Prerequisites** | Arrays, writing a feasibility check (often greedy) |

### B. How to recognise
1. **Sorted array / matrix** + find something → classic binary search.
2. **"Find the minimum X such that…" / "maximum X such that…"** where checking a given X is easy and **if X works, every larger (or smaller) X also works** → **binary search on answer**.
3. "O(log n)" required in the problem statement.
4. Rotated sorted array, peak element (local monotonic structure).
5. Constraints: answer range up to 10⁹ but n only 10⁵.

**Monotonic test for "binary search on answer":** *"If speed k lets Koko finish, does speed k+1 also?"* Yes → monotonic → binary search.

### C. Intuition — from linear to logarithmic
Koko Eating Bananas: piles `[3, 6, 7, 11]`, `h = 8` hours. Find the minimum eating speed `k`.
- **Brute force:** try k = 1, 2, 3, … until it works → O(max(pile) · n).
- **Observation:** `feasible(k)` = hours needed ≤ h. Hours decrease as k increases → F F F T T T…
- **Pattern:** binary search for the first k where feasible is True.
```python
def minEatingSpeed(piles, h):
    def feasible(k):
        return sum((p + k - 1) // k for p in piles) <= h     # ceil(p/k) hours per pile
    lo, hi = 1, max(piles)                 # answer is surely in [1, max(piles)]
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid                       # mid works → answer is mid or smaller
        else:
            lo = mid + 1                   # mid fails → answer is strictly bigger
    return lo
```
**Dry run:**

| lo | hi | mid | hours = Σ ceil(p/mid) | ≤ 8? | Action |
|---|---|---|---|---|---|
| 1 | 11 | 6 | 1+1+2+2 = 6 | ✅ | hi = 6 |
| 1 | 6 | 3 | 1+2+3+4 = 10 | ❌ | lo = 4 |
| 4 | 6 | 5 | 1+2+2+3 = 8 | ✅ | hi = 5 |
| 4 | 5 | 4 | 1+2+2+3 = 8 | ✅ | hi = 4 |
| 4 | 4 | — | loop ends | — | return **4** |

### D. Variations
| Variation | Condition | Example |
|---|---|---|
| Exact match | `nums[mid] == target` | Binary Search |
| Lower bound (first ≥ target) | `nums[mid] >= target` | Search Insert Position |
| First occurrence | lower bound, then check equality | First and Last Position |
| Last occurrence | (first > target) − 1 | First and Last Position |
| Rotated array | decide which half is sorted | Search in Rotated Sorted Array |
| Minimum in rotated | `nums[mid] > nums[hi]` → min is right | Find Minimum in Rotated |
| Peak | `nums[mid] < nums[mid+1]` → peak on right | Find Peak Element |
| On answer — minimise | first feasible | Koko, Ship Packages, Split Array (minimise max) |
| On answer — maximise | last feasible | Magnetic Force / Aggressive Cows (maximise min) |
| 2D matrix | treat as flattened array: `r, c = divmod(mid, cols)` | Search a 2D Matrix |
| Partition search | binary search a cut position | Median of Two Sorted Arrays |

### E. Templates — learn TWO and you're done

**Template 1 — exact search (`lo <= hi`):**
```python
def search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:                      # search space [lo, hi] non-empty
        mid = (lo + hi) // 2
        if nums[mid] == target: return mid
        if nums[mid] < target: lo = mid + 1
        else: hi = mid - 1
    return -1
```

**Template 2 — first True (`lo < hi`) — use for EVERYTHING else:**
```python
def first_true(lo, hi, cond):            # answer guaranteed in [lo, hi]
    while lo < hi:
        mid = (lo + hi) // 2             # rounds down → mid < hi, so hi = mid always shrinks
        if cond(mid): hi = mid           # mid might be the answer; keep it
        else: lo = mid + 1               # mid is definitely not the answer
    return lo
```
**Last True (maximise)** — mirror image; round **up** to avoid an infinite loop:
```python
def last_true(lo, hi, cond):
    while lo < hi:
        mid = (lo + hi + 1) // 2         # round UP, otherwise lo = mid can loop forever
        if cond(mid): lo = mid
        else: hi = mid - 1
    return lo
```
**How to derive:** (1) define the search space and confirm the answer is in it, (2) write `cond` and check it's monotonic, (3) decide first-True or last-True, (4) choose rounding so the range always shrinks.

### C2. Worked — Search in Rotated Sorted Array
At any `mid`, **at least one half is sorted**. Check if target lies inside the sorted half; if yes go there, else go to the other half.
```python
def search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target: return mid
        if nums[lo] <= nums[mid]:                       # left half sorted
            if nums[lo] <= target < nums[mid]: hi = mid - 1
            else: lo = mid + 1
        else:                                           # right half sorted
            if nums[mid] < target <= nums[hi]: lo = mid + 1
            else: hi = mid - 1
    return -1
```

### C3. Worked — Maximise the minimum (Aggressive Cows / Magnetic Force)
Place `m` balls in positions to **maximise the minimum distance**. `feasible(d)` = greedily place a ball whenever distance from the last ≥ d; count ≥ m? If distance d works, any smaller d works → last True.
```python
def maxDistance(position, m):
    position.sort()
    def feasible(d):
        count, last = 1, position[0]
        for p in position[1:]:
            if p - last >= d:
                count += 1; last = p
        return count >= m
    lo, hi = 1, position[-1] - position[0]
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if feasible(mid): lo = mid
        else: hi = mid - 1
    return lo
```
**Minimise the maximum** (Allocate Books / Split Array Largest Sum / Ship Packages) is the mirror: `feasible(cap)` = greedily fill groups without exceeding cap; groups ≤ k? → first True with `lo = max(nums)`, `hi = sum(nums)`.

### G. Complexity & when NOT to use
- Classic: O(log n). On answer: O(n · log(range)).
- **Don't use** when the condition isn't monotonic (then you need DP or full search).

### H. Common mistakes
- Infinite loop: `lo = mid` with `mid = (lo+hi)//2` (round up instead).
- Wrong initial range (answer outside `[lo, hi]`; e.g., Ship Packages must start at `max(weights)`).
- Mixing templates (`lo <= hi` with `hi = mid`).
- Rotated arrays: `<` vs `<=` on `nums[lo] <= nums[mid]` (needed when lo == mid).
- Integer ceil: use `(p + k - 1) // k`, not `math.ceil(p / k)` (float precision on huge values).

### I. Interview thinking
- **ID:** "The answer range is huge but checking one candidate is O(n), and feasibility is monotonic → binary search the answer."
- **Defend complexity:** "log₂(10⁹) ≈ 30 iterations × O(n) check."
- **Follow-ups:** duplicates in rotated array (worst case O(n), shrink `lo++`/`hi--` when equal); "prove monotonicity".

### J. Practice questions
| Lvl | Pri | Problem | Diff | Variation | Trap |
|---|---|---|---|---|---|
| 1 | ⭐ | [Binary Search](https://dsacourse.com/top-150/binary-search) `DSA150` | 🟢 | Exact | `lo <= hi` |
| 1 | ⭐ | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) `LC` | 🟢 | Lower bound | hi = n (insert at end) |
| 1 | ✅ | [Sqrt(x)](https://leetcode.com/problems/sqrtx/) `LC` | 🟢 | Last true on answer | Overflow (not in Python) |
| 2 | ⭐ | [Find First and Last Position of Element](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) `LC` | 🟡 | Two boundaries | Not found case |
| 2 | ⭐ | [Search a 2D Matrix](https://dsacourse.com/top-150/search-a-2d-matrix) `DSA150` | 🟡 | Flattened index | `divmod(mid, cols)` |
| 3 | ⭐ | [Find Minimum in Rotated Sorted Array](https://dsacourse.com/top-150/find-minimum-in-rotated-sorted-array) `DSA150` | 🟡 | Compare with `nums[hi]` | Comparing with nums[lo] |
| 3 | ⭐ | [Search in Rotated Sorted Array](https://dsacourse.com/top-150/search-in-rotated-sorted-array) `DSA150` | 🟡 | Sorted-half check | Boundary inequalities |
| 3 | ✅ | [Find Peak Element](https://dsacourse.com/top-150/find-peak-element) `DSA150` | 🟡 | Slope direction | — |
| 3 | ✅ | [Single Element in a Sorted Array](https://leetcode.com/problems/single-element-in-a-sorted-array/) `LC` | 🟡 | Index parity condition | — |
| 4 | ⭐ | [Koko Eating Bananas](https://dsacourse.com/top-150/koko-eating-bananas) `DSA150` | 🟡 | Min feasible | Ceil division |
| 4 | ⭐ | [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) `LC` | 🟡 | Minimise max | lo = max(weights) |
| 4 | ✅ | [Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/) `LC` | 🟡 | Min feasible day | Impossible case (m·k > n) |
| 4 | ✅ | [Magnetic Force Between Two Balls](https://leetcode.com/problems/magnetic-force-between-two-balls/) `LC` | 🟡 | Maximise min (Aggressive Cows) | Round up mid |
| 4 | ⭐ | [Time Based Key-Value Store](https://dsacourse.com/top-150/time-based-key-value-store) `DSA150` | 🟡 | `bisect_right` − 1 | Timestamp before all |
| 5 | ✅ | [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) `LC` | 🔴 | Minimise max (Allocate Books) | Range [max, sum] |
| 5 | 🚀 | [Median of Two Sorted Arrays](https://dsacourse.com/top-150/median-of-two-sorted-arrays) `DSA150` | 🔴 | Partition search on smaller array | ±inf sentinels |

### K. Revision card
```
BINARY SEARCH = find the flip point of a monotonic condition  F F F T T T
Exact:      lo<=hi, lo=mid+1 / hi=mid-1
First True: lo<hi, mid=(lo+hi)//2,   T→hi=mid,  F→lo=mid+1
Last True:  lo<hi, mid=(lo+hi+1)//2, T→lo=mid,  F→hi=mid-1
On answer:  range of answers + greedy feasible(x) + monotonic proof
Min max → first True | Max min → last True
```
**Mastery:** Koko + Search in Rotated + Magnetic Force without hints; explain why the condition is monotonic.

---

## P10. Stack & Monotonic Stack

### A. Introduction
**Analogy:** a stack of plates — you add and remove only from the top (LIFO: Last In, First Out).

A stack remembers **unfinished business** in reverse order: the most recently opened bracket must be closed first; the most recent unresolved element is the first to be resolved.

A **monotonic stack** keeps elements in increasing or decreasing order. When a new element breaks the order, it *resolves* the waiting elements it beats (e.g., it is their "next greater element").

### B. How to recognise
**Plain stack:**
- Matching pairs / nesting: brackets, tags, decode `3[a2[c]]`.
- Evaluate expressions (RPN, calculator).
- Undo / backtrack the most recent thing (asteroid collision, simplify path).
- Design: Min Stack (stack of `(val, current_min)`).

**Monotonic stack:**
- "Next / previous **greater / smaller** element."
- "How many days until warmer", "stock span".
- "Largest rectangle", "maximal rectangle", "sum of subarray minimums" (each element's range of influence).
- "Remove k digits to make smallest number" (keep stack increasing).
- Brute force is "for each i, scan right until you find something bigger" → O(n²).

### C. Intuition — Daily Temperatures
> For each day, how many days until a warmer temperature? `[73, 74, 75, 71, 69, 72, 76, 73]` → `[1, 1, 4, 2, 1, 1, 0, 0]`

- Brute: for each day, scan forward → O(n²).
- Observation: days waiting for a warmer day form a **decreasing** sequence (if a later day were warmer, it would have already resolved the earlier one). When a warm day arrives, it resolves the waiting days from the most recent backwards — exactly a stack.
```python
def dailyTemperatures(temps):
    ans = [0] * len(temps)
    stack = []                                   # indices of days still waiting; temps decreasing
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:    # today resolves all colder waiting days
            j = stack.pop()
            ans[j] = i - j
        stack.append(i)
    return ans
```
**Dry run:**

| i | t | Pops (resolved j → ans[j]) | Stack after (temps) |
|---|---|---|---|
| 0 | 73 | — | [73] |
| 1 | 74 | 0 → 1 | [74] |
| 2 | 75 | 1 → 1 | [75] |
| 3 | 71 | — | [75, 71] |
| 4 | 69 | — | [75, 71, 69] |
| 5 | 72 | 4 → 1, 3 → 2 | [75, 72] |
| 6 | 76 | 5 → 1, 2 → 4 | [76] |
| 7 | 73 | — | [76, 73] |

Each index is pushed once and popped once → **O(n)**.

### D. Variations — the 4 monotonic stack directions
| Want | Iterate | Pop while | Stack order |
|---|---|---|---|
| Next **greater** to the right | left → right | `nums[top] < x` | decreasing |
| Next **smaller** to the right | left → right | `nums[top] > x` | increasing |
| Previous greater to the left | left → right, answer = top after popping | `nums[top] <= x` | decreasing |
| Previous smaller to the left | left → right, answer = top after popping | `nums[top] >= x` | increasing |
- **Circular** (Next Greater Element II): iterate `2n` times using `i % n`.
- **Range of influence**: for each element, find previous smaller and next smaller → it's the minimum of `(i − left) × (right − i)` subarrays (Sum of Subarray Minimums; break ties with `<` on one side and `<=` on the other).

### E. Template
```python
def next_greater(nums):
    res = [-1] * len(nums)
    stack = []                            # indices whose answer is unknown
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            res[stack.pop()] = x          # x is the first greater to their right
        stack.append(i)
    return res                            # leftovers have no greater element (-1)
```
Store **indices**, not values — you usually need distances or positions.

### C2. Worked hard — Largest Rectangle in Histogram
For each bar, the widest rectangle using its full height extends until a shorter bar on each side. Keep an increasing stack; when a shorter bar arrives, popped bars have found their right boundary, and their left boundary is where they started.
```python
def largestRectangleArea(heights):
    stack = []                                   # (start_index, height), heights increasing
    best = 0
    for i, h in enumerate(heights + [0]):        # sentinel 0 flushes the stack at the end
        start = i
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            best = max(best, height * (i - idx)) # extends from idx up to i-1
            start = idx                          # current bar can extend back to idx
        stack.append((start, h))
    return best
```

### C3. Plain-stack examples
```python
def isValid(s):                                  # Valid Parentheses
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for c in s:
        if c in pairs:
            if not stack or stack.pop() != pairs[c]:
                return False
        else:
            stack.append(c)
    return not stack                              # leftover openers → invalid

class MinStack:                                   # every entry remembers the min at that time
    def __init__(self): self.st = []
    def push(self, v): self.st.append((v, min(v, self.st[-1][1]) if self.st else v))
    def pop(self): self.st.pop()
    def top(self): return self.st[-1][0]
    def getMin(self): return self.st[-1][1]
```

### H. Common mistakes
- Pushing values when you need indices.
- `<` vs `<=` in the pop condition (matters with duplicates).
- Forgetting to flush the remaining stack (sentinel trick).
- Popping from an empty stack (check `stack` first).

### I. Interview thinking
- **ID:** "Each element is waiting for the first larger/smaller element → monotonic stack."
- **Defend O(n):** "Every index is pushed and popped at most once."

### J. Practice questions
| Lvl | Pri | Problem | Diff | Variation | Trap |
|---|---|---|---|---|---|
| 1 | ⭐ | [Valid Parentheses](https://dsacourse.com/top-150/valid-parentheses) `DSA150` | 🟢 | Matching | Leftover openers |
| 1 | ✅ | [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) `LC` | 🟢 | Two stacks, amortised O(1) | Moving every time |
| 2 | ⭐ | [Min Stack](https://dsacourse.com/top-150/min-stack) `DSA150` | 🟡 | Paired state | — |
| 2 | ⭐ | [Evaluate Reverse Polish Notation](https://dsacourse.com/top-150/evaluate-reverse-polish-notation) `DSA150` | 🟡 | Operand stack | Division truncates toward 0: `int(a / b)` |
| 2 | ✅ | [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) `LC` | 🟢 | Monotonic + hash | — |
| 3 | ⭐ | [Daily Temperatures](https://dsacourse.com/top-150/daily-temperatures) `DSA150` | 🟡 | Next greater (distance) | Values vs indices |
| 3 | ✅ | [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) `LC` | 🟡 | Circular, 2n loop | — |
| 3 | ✅ | [Online Stock Span](https://leetcode.com/problems/online-stock-span/) `LC` | 🟡 | Previous greater, accumulate spans | — |
| 3 | ⭐ | [Asteroid Collision](https://dsacourse.com/top-150/asteroid-collision) `DSA150` | 🟡 | Simulation | Equal sizes both explode |
| 3 | ⭐ | [Decode String](https://dsacourse.com/top-150/decode-string) `DSA150` | 🟡 | Nested state stack | Multi-digit numbers |
| 4 | ⭐ | [Car Fleet](https://dsacourse.com/top-150/car-fleet) `DSA150` | 🟡 | Sort by position + arrival times | Float times |
| 4 | ✅ | [Remove K Digits](https://leetcode.com/problems/remove-k-digits/) `LC` | 🟡 | Increasing stack, greedy | Leading zeros, leftover k |
| 4 | ✅ | [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) `LC` | 🟡 | Stack with precedence | Last number |
| 5 | ⭐ | [Largest Rectangle in Histogram](https://dsacourse.com/top-150/largest-rectangle-in-histogram) `DSA150` | 🔴 | Range of influence | Sentinel |
| 5 | 🚀 | [Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/) `LC` | 🟡 | Contribution technique | Duplicate tie-breaking |
| 5 | 🚀 | [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/) `LC` | 🔴 | Histogram per row | — |

### K. Revision card
```
STACK: nesting / matching / undo / evaluate
MONOTONIC STACK: "next/previous greater/smaller", spans, histograms
for i,x: while st and nums[st[-1]] < x: resolve(st.pop()); st.append(i)
Store INDICES. O(n): each index pushed/popped once. Sentinel to flush.
```

---

## P11. Monotonic Queue / Deque

### A. Introduction
A deque (double-ended queue) lets you add/remove from **both** ends in O(1). A **monotonic deque** keeps candidates for the window maximum in decreasing order: the front is always the current max.

### B. How to recognise
- **Maximum/minimum of every sliding window.**
- Sliding window where the condition depends on max − min.
- DP with "max of the last k states" (e.g., Jump Game VI style).

### C. Intuition — Sliding Window Maximum
If a newer element is **bigger** than an older one, the older one can **never** be a window max again (the newer one is bigger and stays in the window longer). So remove it. What remains is decreasing.
```python
def maxSlidingWindow(nums, k):
    dq, res = deque(), []                      # indices; nums[dq] decreasing
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:        # useless older, smaller elements
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:                     # front slid out of the window
            dq.popleft()
        if i >= k - 1:                         # first full window reached
            res.append(nums[dq[0]])
    return res
```
**Dry run** `nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3`:

| i | x | dq after (values) | window full? | max |
|---|---|---|---|---|
| 0 | 1 | [1] | no | — |
| 1 | 3 | [3] | no | — |
| 2 | −1 | [3, −1] | yes | 3 |
| 3 | −3 | [3, −1, −3] | yes | 3 |
| 4 | 5 | [5] (3 also expired) | yes | 5 |
| 5 | 3 | [5, 3] | yes | 5 |
| 6 | 6 | [6] | yes | 6 |
| 7 | 7 | [7] | yes | 7 |

O(n): each index enters and leaves the deque once. A heap gives O(n log n).

### J. Practice questions
| Lvl | Pri | Problem | Diff | Trap |
|---|---|---|---|---|
| 4 | ⭐ | [Sliding Window Maximum](https://dsacourse.com/top-150/sliding-window-maximum) `DSA150` | 🔴 | Expire by index, not value |
| 4 | ✅ | [Longest Continuous Subarray With Absolute Diff ≤ Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) `LC` | 🟡 | Two deques (max & min) |
| 5 | 🚀 | [Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/) `LC` | 🔴 | Deque over prefix sums (negatives!) |

### K. Revision card
```
MONOTONIC DEQUE = window max/min in O(n)
push: pop back while back <= x; append i
expire: popleft if dq[0] <= i-k
answer: nums[dq[0]]
```

---

## P12. Linked List

### A. Introduction
**Analogy:** a treasure hunt — each clue (node) tells you where the next one is. You can't jump to clue #5; you must follow the chain.

No random access; insertion/deletion is O(1) **if you already hold the previous node**. Interview linked-list problems are about **pointer rewiring without losing references**.

### B. How to recognise & toolbox
| Need | Technique |
|---|---|
| Reverse all / part | Three pointers: `prev, cur, nxt` |
| Middle | Fast & slow (fast moves 2) |
| Cycle exists / cycle start | Floyd's tortoise & hare |
| k-th from end | Gap of k between two pointers |
| Merge / build a new list | **Dummy head** node |
| Reorder | middle + reverse second half + merge |
| Copy with extra pointers | Hash map old → new |
| O(1) get/put with recency | Hash map + doubly linked list (LRU) |
| Merge k lists | Heap |

### C. Core moves (write these until automatic)
```python
def reverseList(head):
    prev, cur = None, head
    while cur:
        nxt = cur.next        # 1. save the rest of the list
        cur.next = prev       # 2. flip the pointer
        prev, cur = cur, nxt  # 3. advance both
    return prev               # new head
```
**Dry run** `1 → 2 → 3`:

| Step | prev | cur | nxt | List state |
|---|---|---|---|---|
| start | None | 1 | — | 1→2→3 |
| 1 | 1 | 2 | 2 | None←1  2→3 |
| 2 | 2 | 3 | 3 | None←1←2  3 |
| 3 | 3 | None | None | None←1←2←3 → return 3 |

```python
def middleNode(head):                 # fast moves 2, slow moves 1 → slow ends at middle
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    return slow

def hasCycle(head):                   # if there's a loop, fast eventually laps slow
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast: return True
    return False

def detectCycleStart(head):          # after meeting, reset one pointer to head; meet again at start
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            slow = head
            while slow is not fast:
                slow, fast = slow.next, fast.next
            return slow
    return None

def mergeTwoLists(a, b):             # dummy node avoids "is the head set yet?" special cases
    dummy = tail = ListNode()
    while a and b:
        if a.val <= b.val: tail.next, a = a, a.next
        else: tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b
    return dummy.next

def removeNthFromEnd(head, n):       # gap technique
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n + 1): fast = fast.next     # fast is n+1 ahead
    while fast: fast, slow = fast.next, slow.next
    slow.next = slow.next.next                  # slow is just before the target
    return dummy.next
```
**Why Floyd's cycle start works (short version):** if the distance from head to cycle start is `a`, and they meet `b` steps into the cycle of length `c`, then `2(a + b) = a + b + kc` → `a = kc − b`. So walking `a` steps from head and `a` steps from the meeting point lands both at the cycle start.

### C2. LRU Cache (most asked design-style question)
```python
class Node:
    def __init__(self, k=0, v=0):
        self.k, self.v, self.prev, self.next = k, v, None, None

class LRUCache:
    def __init__(self, capacity):
        self.cap, self.map = capacity, {}
        self.head, self.tail = Node(), Node()       # sentinels: head.next = most recent
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def _add_front(self, node):
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.map: return -1
        node = self.map[key]
        self._remove(node); self._add_front(node)    # mark as most recently used
        return node.v

    def put(self, key, value):
        if key in self.map: self._remove(self.map[key])
        node = Node(key, value)
        self.map[key] = node; self._add_front(node)
        if len(self.map) > self.cap:
            lru = self.tail.prev                       # least recently used
            self._remove(lru); del self.map[lru.k]
```
*Backend bonus:* mention `collections.OrderedDict` (`move_to_end`, `popitem(last=False)`) as the production shortcut, but implement the DLL in interviews unless told otherwise.

### H. Common mistakes
- Losing the rest of the list (not saving `nxt` before rewiring).
- `while fast.next` without checking `fast` (AttributeError on None).
- Forgetting a dummy node when the head itself can change.
- Comparing nodes with `==` instead of `is` (fine in LeetCode, but be precise).

### J. Practice questions
| Lvl | Pri | Problem | Diff | Technique | Trap |
|---|---|---|---|---|---|
| 1 | ⭐ | [Reverse Linked List](https://dsacourse.com/top-150/reverse-linked-list) `DSA150` | 🟢 | prev/cur/nxt (+ recursive version) | Losing `next` |
| 1 | ⭐ | [Merge Two Sorted Lists](https://dsacourse.com/top-150/merge-two-sorted-lists) `DSA150` | 🟢 | Dummy node | Attaching remainder |
| 1 | ⭐ | [Linked List Cycle](https://dsacourse.com/top-150/linked-list-cycle) `DSA150` | 🟢 | Floyd | Null checks |
| 1 | ✅ | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) `LC` | 🟢 | Fast/slow | Even length → second middle |
| 2 | ✅ | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) `LC` | 🟢 | Middle + reverse | — |
| 2 | ✅ | [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) `LC` | 🟢 | Switch heads trick | — |
| 3 | ⭐ | [Remove Nth Node From End of List](https://dsacourse.com/top-150/remove-nth-node-from-end-of-list) `DSA150` | 🟡 | Gap + dummy | Removing the head |
| 3 | ✅ | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) `LC` | 🟡 | Floyd start | Proof |
| 3 | ⭐ | [Reorder List](https://dsacourse.com/top-150/reorder-list) `DSA150` | 🟡 | Middle + reverse + merge | Cutting the first half |
| 3 | ⭐ | [Add Two Numbers](https://dsacourse.com/top-150/add-two-numbers) `DSA150` | 🟡 | Dummy + carry | Final carry |
| 4 | ⭐ | [Copy List with Random Pointer](https://dsacourse.com/top-150/copy-list-with-random-pointer) `DSA150` | 🟡 | Hash map old→new | None random |
| 4 | ⭐ | [Find the Duplicate Number](https://dsacourse.com/top-150/find-the-duplicate-number) `DSA150` | 🟡 | Floyd on `i → nums[i]` | Seeing array as list |
| 4 | ⭐ | [LRU Cache](https://dsacourse.com/top-150/lru-cache) `DSA150` | 🟡 | Hash + DLL | Updating existing key |
| 4 | ✅ | [Sort List](https://leetcode.com/problems/sort-list/) `LC` | 🟡 | Merge sort on list | Splitting correctly |
| 5 | ⭐ | [Merge K Sorted Lists](https://dsacourse.com/top-150/merge-k-sorted-lists) `DSA150` | 🔴 | Heap (do after P16) | Tuples with nodes: add index tiebreaker |
| 5 | 🚀 | [Reverse Nodes in k-Group](https://dsacourse.com/top-150/reverse-nodes-in-k-group) `DSA150` | 🔴 | Reverse sublists + reconnect | Last partial group |

### K. Revision card
```
LINKED LIST: never lose a reference — save next before rewiring
reverse: prev,cur ; middle/cycle: slow,fast ; kth from end: gap
dummy node whenever head may change ; LRU = dict + doubly linked list
```

---

## P13. Recursion & Backtracking

### A. Introduction
**Recursion analogy:** Russian dolls — to open the big doll, open the smaller doll inside, until you reach the smallest one (base case).

**Backtracking analogy:** exploring a maze — at each junction, choose a path; if it dead-ends, **walk back** to the junction and try the next path.

Backtracking = **choose → explore → unchoose**. It systematically enumerates every configuration, pruning branches that can't lead to a valid answer.

| | |
|---|---|
| **Solves** | All subsets, permutations, combinations, partitions, puzzles (N-Queens, Sudoku), path search in grids |
| **Advantages** | Simple, general, correct by construction |
| **Limitations** | Exponential; only feasible for small n (≈ ≤ 20) |
| **Prerequisites** | Functions, call stack, lists |

### B. How to recognise
- "Return **all** possible…" (subsets, permutations, combinations, partitions, valid arrangements).
- Constraints are tiny (n ≤ 10–20).
- You must build a solution step by step, and each step has several choices.
- If the problem asks only for the **count or best**, and subproblems repeat → it's probably **DP** instead (memoise the recursion).

### C. Recursion thinking: the three questions
1. **What does my function return / do for an input?** (Define it precisely in words.)
2. **What is the smallest input (base case)?**
3. **How do I build the answer for n from the answer for a smaller input?** (Trust the recursive call — the "leap of faith".)

### C2. Intuition — Subsets as a decision tree
For `[1, 2, 3]`, every element gets a decision: **take it or skip it**.
```text
                         []
              take 1 /        \ skip 1
                 [1]            []
           t2 /     \ s2     t2/  \s2
          [1,2]     [1]     [2]    []
        t3/  \s3  t3/ \s3 t3/ \s3 t3/ \s3
  [1,2,3] [1,2] [1,3] [1] [2,3] [2] [3] []     ← 2³ = 8 leaves = 8 subsets
```
```python
def subsets(nums):
    res, path = [], []
    def dfs(i):
        if i == len(nums):              # decided for every element → one subset
            res.append(path[:])         # COPY! path keeps changing
            return
        path.append(nums[i])            # choose: take nums[i]
        dfs(i + 1)                      # explore
        path.pop()                      # unchoose
        dfs(i + 1)                      # explore without nums[i]
    dfs(0)
    return res
```

### D. Variations & the universal template
```python
def backtrack(start, path):
    if is_solution(path):
        res.append(path[:])               # copy the current state
        # return  ← only if solutions can't be extended further
    for i in range(start, len(choices)):  # each candidate for THIS position
        if not valid(choices[i], path):   # PRUNE early
            continue
        path.append(choices[i])           # choose
        backtrack(next_start(i), path)    # explore
        path.pop()                        # unchoose
```
| Problem type | `start` for next call | Duplicate handling | Example |
|---|---|---|---|
| Subsets | `i + 1` | — | Subsets |
| Subsets with dup input | `i + 1` | sort; skip `i > start and nums[i] == nums[i-1]` | Subsets II |
| Combinations, reuse allowed | `i` (same element again) | — | Combination Sum |
| Combinations, no reuse, dup input | `i + 1` | sort + same skip rule | Combination Sum II |
| Permutations | loop over all, track `used[]` | — | Permutations |
| Grid path | neighbours, mark visited in-place | restore cell after | Word Search |
| Placement | try each column, check conflict sets | — | N-Queens |
| Partitioning | try every end index `j` for current piece | — | Palindrome Partitioning |

**Why `i > start` for duplicates?** At the same tree level (same position), picking an equal value twice creates identical branches. But using equal values at *different* levels (deeper positions) is fine — that's why we compare against `start`, not 0.

### E. Worked examples
```python
def combinationSum(candidates, target):
    res, path = [], []
    candidates.sort()
    def dfs(start, remain):
        if remain == 0: res.append(path[:]); return
        for i in range(start, len(candidates)):
            if candidates[i] > remain: break           # prune: sorted, so all later are too big
            path.append(candidates[i])
            dfs(i, remain - candidates[i])             # i, not i+1 → reuse allowed
            path.pop()
    dfs(0, target)
    return res

def permute(nums):
    res, path, used = [], [], [False] * len(nums)
    def dfs():
        if len(path) == len(nums): res.append(path[:]); return
        for i in range(len(nums)):
            if used[i]: continue
            used[i] = True; path.append(nums[i])
            dfs()
            path.pop(); used[i] = False
    dfs()
    return res

def solveNQueens(n):
    res, cols, d1, d2 = [], set(), set(), set()      # d1: r-c, d2: r+c identify diagonals
    board = [["."] * n for _ in range(n)]
    def dfs(r):
        if r == n: res.append(["".join(row) for row in board]); return
        for c in range(n):
            if c in cols or (r - c) in d1 or (r + c) in d2: continue
            cols.add(c); d1.add(r - c); d2.add(r + c); board[r][c] = "Q"
            dfs(r + 1)
            cols.remove(c); d1.remove(r - c); d2.remove(r + c); board[r][c] = "."
    dfs(0)
    return res

def exist(board, word):                               # Word Search
    R, C = len(board), len(board[0])
    def dfs(r, c, k):
        if k == len(word): return True
        if not (0 <= r < R and 0 <= c < C) or board[r][c] != word[k]: return False
        tmp, board[r][c] = board[r][c], "#"            # mark visited
        found = any(dfs(r + dr, c + dc, k + 1) for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)))
        board[r][c] = tmp                              # restore (unchoose)
        return found
    return any(dfs(r, c, 0) for r in range(R) for c in range(C))
```

### G. Complexity
- Subsets: O(n · 2ⁿ) (2ⁿ subsets, O(n) to copy each).
- Permutations: O(n · n!).
- Word Search: O(R · C · 4^L) worst case (3^L with the visited mark).
- Space: O(n) recursion depth + output.

### H. Common mistakes
- `res.append(path)` instead of `path[:]` → all results end up empty/identical.
- Forgetting to undo (unchoose) → state leaks between branches.
- Wrong duplicate skip (`i > 0` instead of `i > start`).
- No pruning → TLE on Combination Sum-like problems.

### I. Interview thinking
- Draw the **recursion tree** for a tiny input first — interviewers love this.
- State: "Each level decides position k; branching factor b; depth d → O(b^d)."
- Follow-ups: "Return only the count?" → maybe DP; "Iterative version?" → for subsets, `res += [s + [x] for s in res]`.

### J. Practice questions
| Lvl | Pri | Problem | Diff | Variation | Trap |
|---|---|---|---|---|---|
| 1 | ⭐ | [Subsets](https://dsacourse.com/top-150/subsets) `DSA150` | 🟡 | Take/skip | Copying path |
| 2 | ⭐ | [Combination Sum](https://dsacourse.com/top-150/combination-sum) `DSA150` | 🟡 | Reuse (start = i) | Duplicate combos if start = 0 |
| 2 | ⭐ | [Permutations](https://dsacourse.com/top-150/permutations) `DSA150` | 🟡 | used[] | — |
| 2 | ✅ | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) `LC` | 🟡 | Constrained choices (open < n, close < open) | — |
| 3 | ⭐ | [Subsets II](https://dsacourse.com/top-150/subsets-ii) `DSA150` | 🟡 | Dedup same level | `i > start` |
| 3 | ⭐ | [Combination Sum II](https://dsacourse.com/top-150/combination-sum-ii) `DSA150` | 🟡 | No reuse + dedup | Sorting first |
| 3 | ⭐ | [Letter Combinations of a Phone Number](https://dsacourse.com/top-150/letter-combinations-of-a-phone-number) `DSA150` | 🟡 | Position-wise choices | Empty input → [] |
| 4 | ⭐ | [Word Search](https://dsacourse.com/top-150/word-search) `DSA150` | 🟡 | Grid DFS + restore | Not restoring cell |
| 4 | ⭐ | [Palindrome Partitioning](https://dsacourse.com/top-150/palindrome-partitioning) `DSA150` | 🟡 | Partition | — |
| 5 | ⭐ | [N-Queens](https://dsacourse.com/top-150/n-queens) `DSA150` | 🔴 | Constraint sets | Diagonal identification |

### K. Revision card
```
BACKTRACKING: choose → explore → unchoose     res.append(path[:])
subsets: start=i+1 | reuse: start=i | perms: used[] | dup: sort + skip i>start
prune early (sorted → break)   draw the recursion tree first
"all X" + small n → backtracking ;  "count/best" + overlapping → DP
```

---

## P14. Trees & Binary Search Trees

### A. Introduction
**Analogy:** a company org chart — one CEO (root), each manager has reports (children), employees with no reports are leaves.

A binary tree node has ≤ 2 children. Trees are **recursive structures**: each child is the root of a smaller tree. That's why almost every tree solution is "solve for left subtree, solve for right subtree, combine at the current node".

A **BST** adds an ordering rule: everything in the left subtree < node < everything in the right subtree → **in-order traversal yields sorted order**.

### B. How to recognise the sub-pattern
| Question asks | Approach |
|---|---|
| Something about every node that depends on its children (height, size, balanced, diameter, max path) | **DFS post-order, return a value** |
| Something that depends on ancestors (path sum from root, good nodes, valid BST bounds) | **DFS pre-order, pass a parameter down** |
| Level-by-level, leftmost/rightmost per level, minimum depth, zigzag | **BFS with a queue** |
| Sorted order, k-th smallest in BST | **In-order traversal** |
| Compare two trees | DFS on both simultaneously |
| Build tree from traversals | Recursion + index map |

### C. Traversals
```python
def preorder(n):  return [n.val] + preorder(n.left) + preorder(n.right) if n else []   # root, L, R
def inorder(n):   return inorder(n.left) + [n.val] + inorder(n.right) if n else []    # L, root, R
def postorder(n): return postorder(n.left) + postorder(n.right) + [n.val] if n else [] # L, R, root
# (concise for learning; in interviews append to a shared list to stay O(n))

def inorder_iterative(root):          # interviewers often ask this
    res, stack, cur = [], [], root
    while cur or stack:
        while cur:                    # go as far left as possible
            stack.append(cur); cur = cur.left
        cur = stack.pop()
        res.append(cur.val)           # visit
        cur = cur.right               # then the right subtree
    return res

def levelOrder(root):                 # BFS
    if not root: return []
    res, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):       # exactly the nodes of the current level
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level)
    return res
```

### C2. The two DFS styles
**Style 1 — return info up (post-order):**
```python
def maxDepth(root):
    if not root: return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
```
**Style 2 — pass info down (pre-order):**
```python
def goodNodes(root):                  # node is "good" if no ancestor is greater
    def dfs(node, max_so_far):
        if not node: return 0
        good = 1 if node.val >= max_so_far else 0
        m = max(max_so_far, node.val)
        return good + dfs(node.left, m) + dfs(node.right, m)
    return dfs(root, root.val)
```
**Style 3 — return one thing, track another globally** (diameter, max path sum):
```python
def diameterOfBinaryTree(root):
    best = 0
    def height(node):
        nonlocal best
        if not node: return 0
        l, r = height(node.left), height(node.right)
        best = max(best, l + r)       # longest path THROUGH this node (in edges)
        return 1 + max(l, r)          # what the PARENT needs: longest downward path
    height(root)
    return best

def maxPathSum(root):
    best = float('-inf')
    def gain(node):
        nonlocal best
        if not node: return 0
        l = max(gain(node.left), 0)   # negative branches are dropped
        r = max(gain(node.right), 0)
        best = max(best, node.val + l + r)   # path that bends at node
        return node.val + max(l, r)          # path that continues upward can use one side only
    gain(root)
    return best
```
**The key insight to explain:** "What the parent needs" (one-sided path) differs from "the answer at this node" (two-sided path).

### C3. BST & LCA & construction
```python
def isValidBST(root):
    def ok(node, lo, hi):                       # every node must lie in (lo, hi)
        if not node: return True
        if not (lo < node.val < hi): return False
        return ok(node.left, lo, node.val) and ok(node.right, node.val, hi)
    return ok(root, float('-inf'), float('inf'))

def lowestCommonAncestor(root, p, q):          # general binary tree
    if not root or root is p or root is q: return root
    l = lowestCommonAncestor(root.left, p, q)
    r = lowestCommonAncestor(root.right, p, q)
    if l and r: return root                     # p and q found on different sides
    return l or r

def buildTree(preorder, inorder):
    idx = {v: i for i, v in enumerate(inorder)}
    it = iter(preorder)                          # preorder gives roots in order
    def build(lo, hi):                           # build from inorder[lo..hi]
        if lo > hi: return None
        val = next(it)
        node = TreeNode(val)
        node.left = build(lo, idx[val] - 1)      # left must be built first (preorder order)
        node.right = build(idx[val] + 1, hi)
        return node
    return build(0, len(inorder) - 1)
```

### D. Extra topics to know
- **Morris traversal:** in-order in O(1) space by temporarily threading predecessor's right pointer to the current node. Know the idea; rarely coded.
- **Views:** right side view = last node per BFS level; left view = first; top/bottom view = BFS with horizontal distance map.
- **Serialisation:** pre-order with `"N"` for null, then rebuild with an iterator.
- **Tree DP:** House Robber III — return `(rob_this, skip_this)` from each node.

### H. Common mistakes
- Validating BST by checking only immediate children (must use bounds).
- Forgetting the `None` base case.
- Using `len(q)` *inside* the level loop after appending (capture it first — `range(len(q))` does this correctly).
- Diameter in nodes vs edges.
- Recursion depth on skewed trees (mention iterative alternatives).

### J. Practice questions
| Lvl | Pri | Problem | Diff | Style | Trap |
|---|---|---|---|---|---|
| 1 | ⭐ | [Maximum Depth of Binary Tree](https://dsacourse.com/top-150/maximum-depth) `DSA150` | 🟢 | Return up | — |
| 1 | ⭐ | [Invert Binary Tree](https://dsacourse.com/top-150/invert-binary-tree) `DSA150` | 🟢 | Any traversal | — |
| 1 | ⭐ | [Same Tree](https://dsacourse.com/top-150/same-tree) `DSA150` | 🟢 | Parallel DFS | None vs node |
| 1 | ✅ | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) `LC` | 🟢 | Iterative + Morris practice | — |
| 2 | ⭐ | [Diameter of Binary Tree](https://dsacourse.com/top-150/diameter-of-binary-tree) `DSA150` | 🟢 | Return + global | Through root assumption |
| 2 | ⭐ | [Balanced Binary Tree](https://dsacourse.com/top-150/balanced-binary-tree) `DSA150` | 🟢 | Return height or −1 | O(n²) naive |
| 2 | ⭐ | [Subtree of Another Tree](https://dsacourse.com/top-150/subtree-of-another-tree) `DSA150` | 🟢 | Same Tree at each node | — |
| 2 | ✅ | [Path Sum](https://leetcode.com/problems/path-sum/) `LC` | 🟢 | Pass down | Must end at leaf |
| 3 | ⭐ | [Binary Tree Level Order Traversal](https://dsacourse.com/top-150/level-order-traversal) `DSA150` | 🟡 | BFS | Level boundaries |
| 3 | ⭐ | [Binary Tree Right Side View](https://dsacourse.com/top-150/binary-tree-right-side-view) `DSA150` | 🟡 | BFS last per level | — |
| 3 | ⭐ | [Count Good Nodes in Binary Tree](https://dsacourse.com/top-150/count-good-nodes) `DSA150` | 🟡 | Pass down max | — |
| 3 | ✅ | [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) `LC` | 🟡 | BFS + reverse alternate | — |
| 3 | ✅ | [Path Sum II](https://leetcode.com/problems/path-sum-ii/) `LC` | 🟡 | DFS + backtracking | Copy path |
| 4 | ⭐ | [Validate Binary Search Tree](https://dsacourse.com/top-150/validate-bst) `DSA150` | 🟡 | Bounds | Child-only check |
| 4 | ⭐ | [Kth Smallest Element in a BST](https://dsacourse.com/top-150/kth-smallest-bst) `DSA150` | 🟡 | In-order, stop at k | — |
| 4 | ✅ | [Lowest Common Ancestor of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) `LC` | 🟡 | Use BST ordering | — |
| 4 | ⭐ | [Lowest Common Ancestor of a Binary Tree](https://dsacourse.com/top-150/lowest-common-ancestor-binary-tree) `DSA150` | 🟡 | Return found nodes | — |
| 4 | ⭐ | [Construct Binary Tree from Preorder and Inorder](https://dsacourse.com/top-150/build-tree-from-preorder-inorder) `DSA150` | 🟡 | Index map | Build left before right |
| 4 | ✅ | [House Robber III](https://leetcode.com/problems/house-robber-iii/) `LC` | 🟡 | Tree DP pair | — |
| 5 | ⭐ | [Serialize a Binary Tree](https://dsacourse.com/top-150/serialize-binary-tree) `DSA150` | 🟡 | Pre-order + nulls | Delimiters |
| 5 | ⭐ | [Binary Tree Maximum Path Sum](https://dsacourse.com/top-150/binary-tree-maximum-path-sum) `DSA150` | 🔴 | Return one side, record both | All negative nodes |

### K. Revision card
```
TREES: f(node) = combine(f(left), f(right), node)
return-up (height/diameter) | pass-down (bounds, path) | BFS (levels)
global answer ≠ what parent needs (diameter, max path)
BST: in-order = sorted; validate with (lo, hi) bounds
LCA: if l and r → root else l or r
```

---

## P15. Tries

### A. Introduction
**Analogy:** a phone's contact search — typing "Ra" narrows to Rahul, Raj, Ramesh. Each letter is a step down a tree; words sharing a prefix share a path.

### B. How to recognise
- Many words + prefix queries ("starts with", autocomplete).
- Search with wildcards.
- Find many words in a grid at once (Word Search II).
- Maximum XOR pairs (binary trie, advanced).

### E. Template
```python
class TrieNode:
    def __init__(self):
        self.children = {}            # char -> TrieNode
        self.end = False              # a word ends here

class Trie:
    def __init__(self): self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children.setdefault(c, TrieNode())
        node.end = True
    def _walk(self, s):
        node = self.root
        for c in s:
            if c not in node.children: return None
            node = node.children[c]
        return node
    def search(self, word):
        node = self._walk(word); return bool(node and node.end)
    def startsWith(self, prefix):
        return self._walk(prefix) is not None
```
- Insert/search: O(L) per word (L = word length). Space: O(total characters).
- **Wildcard `.`:** DFS over all children at that position.
- **Word Search II:** insert all words in a trie, DFS the board once, walking the trie in parallel; prune when the trie path doesn't exist; delete found words / leaves to avoid TLE.

### J. Practice questions
| Lvl | Pri | Problem | Diff | Trap |
|---|---|---|---|---|
| 3 | ⭐ | [Implement Trie (Prefix Tree)](https://dsacourse.com/top-150/implement-trie) `DSA150` | 🟡 | Forgetting `end` flag |
| 3 | ✅ | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) `LC` | 🟢 | (Simple scan also works — compare approaches) |
| 4 | ⭐ | [Design Add and Search Words](https://dsacourse.com/top-150/wildcard-search) `DSA150` | 🟡 | DFS on `.` |
| 5 | ⭐ | [Word Search II](https://dsacourse.com/top-150/word-search-ii) `DSA150` | 🔴 | Running Word Search per word (TLE) |
| 5 | 🚀 | [Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) `LC` | 🟡 | Binary trie, greedy bits |

---

## P16. Heap / Priority Queue

### A. Introduction
**Analogy:** a hospital emergency room — patients aren't served in arrival order, but by severity. The most critical patient is always next, and new arrivals slot in by priority.

A **binary heap** is a complete binary tree stored in an array, where every parent ≤ its children (min-heap). The minimum is always at index 0.
- Parent of `i`: `(i − 1) // 2`; children: `2i + 1`, `2i + 2`.
- **Push:** append at the end, *sift up* (swap with parent while smaller) → O(log n).
- **Pop:** move the last element to the root, *sift down* (swap with smaller child) → O(log n).
- **Heapify** an array: O(n) (most nodes are near the bottom and move little).

### B. How to recognise
- "K largest / K smallest / K-th / top K / K closest."
- Repeatedly take the min/max **while new items arrive** (streams, simulations).
- Merge K sorted things.
- Scheduling by priority / earliest deadline / earliest finish.
- Running median (two heaps).
- Dijkstra / Prim (P18).
- *Misleading:* max of a **sliding window** → deque is better; one-time sort is fine if no dynamic updates.

### D. Variations & templates

**1. Top K largest → min-heap of size k** (the heap holds the k best so far; its top is the weakest of them)
```python
def kth_largest(nums, k):
    heap = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)       # evict the smallest → keeps k largest
    return heap[0]                    # the k-th largest
```
O(n log k) time, O(k) space. (Top K **smallest** → max-heap of size k via negatives.)

**2. Max-heap in Python:** push `-x`, read `-heap[0]`.

**3. K-way merge:**
```python
def mergeKLists(lists):
    heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
    heapq.heapify(heap)                         # i breaks ties (ListNodes aren't comparable)
    dummy = tail = ListNode()
    while heap:
        val, i, node = heapq.heappop(heap)
        tail.next = node; tail = node
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next
```
O(N log k) for N total nodes.

**4. Two heaps — running median:**
```python
class MedianFinder:
    def __init__(self):
        self.small = []    # max-heap (negated): lower half
        self.large = []    # min-heap: upper half
    def addNum(self, num):
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))  # move small's max to large
        if len(self.large) > len(self.small):                    # keep small >= large in size
            heapq.heappush(self.small, -heapq.heappop(self.large))
    def findMedian(self):
        if len(self.small) > len(self.large): return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
```
Invariant: every element in `small` ≤ every element in `large`; sizes differ by ≤ 1.

**5. Heap + greedy scheduling** (Task Scheduler, IPO, Reorganize String): repeatedly take the most "valuable" available item; items that are cooling down wait in a queue.

### G. Complexity cheat sheet
| Approach for top-k | Time | Space |
|---|---|---|
| Sort | O(n log n) | O(n) |
| Min-heap of size k | O(n log k) | O(k) |
| Heapify all + pop k | O(n + k log n) | O(n) |
| Quickselect | O(n) avg, O(n²) worst | O(1) |
| Bucket (frequencies) | O(n) | O(n) |

### H. Common mistakes
- Using a max-heap of size n when a min-heap of size k suffices.
- Pushing non-comparable objects (ListNode) without a tiebreaker.
- Forgetting to negate back when reading a max-heap.
- `heap[0]` on an empty heap.

### J. Practice questions
| Lvl | Pri | Problem | Diff | Variation | Trap |
|---|---|---|---|---|---|
| 1 | ⭐ | [Kth Largest Element in a Stream](https://dsacourse.com/top-150/kth-largest-element-in-a-stream) `DSA150` | 🟢 | Size-k min-heap | Initial list longer than k |
| 1 | ⭐ | [Last Stone Weight](https://dsacourse.com/top-150/last-stone-weight) `DSA150` | 🟢 | Max-heap simulation | Negation |
| 2 | ⭐ | [K Closest Points to Origin](https://dsacourse.com/top-150/k-closest-to-origin) `DSA150` | 🟡 | Size-k max-heap | No sqrt needed |
| 2 | ⭐ | [Kth Largest Element in an Array](https://dsacourse.com/top-150/kth-largest-element) `DSA150` | 🟡 | Heap vs quickselect | — |
| 3 | ✅ | [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) `LC` | 🟡 | Custom ordering | Lexicographic tiebreak |
| 3 | ✅ | [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) `LC` | 🟡 | K-way merge (or BS on answer) | — |
| 4 | ⭐ | [Task Scheduler](https://dsacourse.com/top-150/task-scheduler) `DSA150` | 🟡 | Heap + cooldown queue (or math formula) | Idle counting |
| 4 | ✅ | [Reorganize String](https://leetcode.com/problems/reorganize-string/) `LC` | 🟡 | Greedy + hold previous | Impossible case |
| 4 | ✅ | [Design Twitter](https://leetcode.com/problems/design-twitter/) `LC` | 🟡 | K-way merge of feeds | — |
| 5 | ⭐ | [Find Median from Data Stream](https://dsacourse.com/top-150/running-median) `DSA150` | 🔴 | Two heaps | Balancing order |
| 5 | 🚀 | [IPO](https://leetcode.com/problems/ipo/) `LC` | 🔴 | Sort + heap greedy | — |

### K. Revision card
```
HEAP: repeated min/max with changing data. heapq = MIN-heap; negate for max.
Top k largest → MIN-heap size k (pop when > k) → O(n log k)
K-way merge → (val, idx, node) tuples
Median → two heaps, small (max) / large (min), sizes differ ≤ 1
```

---

## P17. Graphs

### A. Introduction
**Analogy:** a city map — places are **nodes (vertices)**, roads are **edges**. Roads may be one-way (directed) or two-way (undirected), and may have lengths (weights).

Trees are graphs with no cycles and one path between any two nodes. General graphs can have cycles, so **you must track visited nodes**, or you'll loop forever.

| Term | Meaning |
|---|---|
| Directed / undirected | One-way / two-way edges |
| Weighted | Edges have costs |
| Connected component | Group of nodes reachable from each other |
| Cycle | Path that returns to its start |
| DAG | Directed Acyclic Graph (prerequisites, build systems) |
| Grid graph | Each cell is a node; neighbours are up/down/left/right |

### B. How to recognise
- Explicit: nodes/edges, "connections", "network", "prerequisites", "friends", "flights".
- **Implicit graphs:** grids (islands), word transformations (Word Ladder: words are nodes, one-letter changes are edges), states in a puzzle.
- Ask: *what are the nodes? what are the edges? directed? weighted?* Then pick the algorithm from the decision tree in Section 4.2.

### C. Representation
```python
def build_graph(n, edges, directed=False):
    graph = defaultdict(list)            # adjacency list: node -> [neighbours]
    for u, v in edges:
        graph[u].append(v)
        if not directed:
            graph[v].append(u)
    return graph
```
Adjacency list: O(V + E) space (use this). Adjacency matrix: O(V²) — only for dense graphs or Floyd-Warshall.

### D. Core algorithms

**1. BFS — shortest path in unweighted graphs, level-by-level**
```python
def bfs(start, graph):
    dist = {start: 0}
    q = deque([start])
    while q:
        node = q.popleft()
        for nei in graph[node]:
            if nei not in dist:              # mark when ENQUEUING (not when popping)
                dist[nei] = dist[node] + 1
                q.append(nei)
    return dist
```
Why BFS gives shortest paths: it explores all nodes at distance d before any at distance d+1.

**2. DFS — explore everything reachable (grid flood fill)**
```python
def numIslands(grid):
    R, C = len(grid), len(grid[0])
    def dfs(r, c):
        if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] != "1":
            return
        grid[r][c] = "0"                     # mark visited (sink the land)
        dfs(r + 1, c); dfs(r - 1, c); dfs(r, c + 1); dfs(r, c - 1)
    count = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == "1":
                dfs(r, c); count += 1        # each new DFS start = new island
    return count
```
(For huge grids, use iterative BFS/DFS to avoid recursion limits.)

**3. Multi-source BFS** — start BFS from **all** sources at once (rotting oranges, distance to nearest 0). Each BFS level = one time unit.
```python
def orangesRotting(grid):
    R, C = len(grid), len(grid[0])
    q, fresh = deque(), 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 2: q.append((r, c))
            elif grid[r][c] == 1: fresh += 1
    minutes = 0
    while q and fresh:
        for _ in range(len(q)):                 # one minute = one level
            r, c = q.popleft()
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                    grid[nr][nc] = 2; fresh -= 1; q.append((nr, nc))
        minutes += 1
    return minutes if fresh == 0 else -1
```

**4. Topological sort (Kahn's algorithm)** — order tasks so every prerequisite comes first; also detects cycles in directed graphs.
```python
def canFinish(numCourses, prerequisites):         # Course Schedule
    graph = defaultdict(list)
    indeg = [0] * numCourses
    for course, pre in prerequisites:
        graph[pre].append(course)                  # edge pre → course
        indeg[course] += 1
    q = deque(i for i in range(numCourses) if indeg[i] == 0)   # no prerequisites
    taken = 0
    while q:
        node = q.popleft(); taken += 1
        for nxt in graph[node]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0: q.append(nxt)      # all its prerequisites are done
    return taken == numCourses                     # < n means a cycle blocked some courses
```
(Course Schedule II: record the pop order.)

**5. Cycle detection**
| Graph | Method |
|---|---|
| Undirected | DFS with `parent` (a visited neighbour that isn't the parent → cycle) or DSU (union of two already-connected nodes → cycle) |
| Directed | Kahn's (processed < n) or DFS with 3 colours: 0 = unvisited, 1 = in current path, 2 = done; reaching a "1" → cycle |

**6. Bipartite check** — 2-colour with BFS/DFS; an edge between same colours → not bipartite.

**7. Disjoint Set Union (Union-Find)**
```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   # path compression
        return self.parent[x]
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb: return False                         # already connected → this edge makes a cycle
        if self.rank[ra] < self.rank[rb]: ra, rb = rb, ra
        self.parent[rb] = ra                              # union by rank: attach smaller under larger
        if self.rank[ra] == self.rank[rb]: self.rank[ra] += 1
        return True
```
Nearly O(1) per operation (inverse Ackermann). Use for: number of components, redundant connection, graph valid tree (n−1 edges + no cycle), accounts merge, Kruskal.

**8. Advanced (know the idea):**
- **Bridges / articulation points (Tarjan):** DFS discovery time `tin` and `low` (lowest tin reachable); edge u–v is a bridge if `low[v] > tin[u]`.
- **SCC (Kosaraju):** DFS to get finish order → reverse graph → DFS in reverse finish order; each DFS tree is one SCC.
- **0-1 BFS:** edges of weight 0 or 1 → deque; weight 0 → `appendleft`, weight 1 → `append`.

### H. Common mistakes
- Marking visited when popping instead of when pushing (duplicates in queue, sometimes wrong distances).
- Not handling disconnected graphs (loop over all nodes as starts).
- Wrong edge direction in topological sort.
- Mutating the input grid when the interviewer wants it preserved (ask!).
- Recursion depth on large grids.

### I. Interview thinking
- **First sentence:** "Let me model this as a graph: nodes are …, edges are …, it's (un)directed and (un)weighted."
- Complexity is almost always **O(V + E)** (grid: O(R·C)).
- Follow-ups: "What if the grid is huge / streamed?" (DSU incrementally); "Return the path, not just its length" (store parents).

### J. Practice questions
| Lvl | Pri | Problem | Diff | Technique | Trap |
|---|---|---|---|---|---|
| 1 | ✅ | [Flood Fill](https://leetcode.com/problems/flood-fill/) `LC` | 🟢 | Grid DFS | Same colour → infinite loop |
| 2 | ⭐ | [Number of Islands](https://dsacourse.com/top-150/number-of-islands) `DSA150` | 🟡 | Grid DFS/BFS | Marking visited |
| 2 | ⭐ | [Max Area of Island](https://dsacourse.com/top-150/max-area-of-island) `DSA150` | 🟡 | DFS returning size | — |
| 2 | ⭐ | [Clone Graph](https://dsacourse.com/top-150/clone-graph) `DSA150` | 🟡 | DFS + old→new map | Cycles |
| 2 | ✅ | [Number of Provinces](https://leetcode.com/problems/number-of-provinces/) `LC` | 🟡 | Components (DFS or DSU) | Adjacency matrix input |
| 3 | ⭐ | [Rotting Oranges](https://dsacourse.com/top-150/rotting-oranges) `DSA150` | 🟡 | Multi-source BFS | No fresh oranges → 0 |
| 3 | ✅ | [01 Matrix](https://leetcode.com/problems/01-matrix/) `LC` | 🟡 | Multi-source BFS from zeros | BFS from each cell = TLE |
| 3 | ⭐ | [Pacific Atlantic Water Flow](https://dsacourse.com/top-150/pacific-atlantic-water-flow) `DSA150` | 🟡 | Reverse flow from borders | Forward from every cell = slow |
| 3 | ⭐ | [Surrounded Regions](https://dsacourse.com/top-150/surrounded-regions) `DSA150` | 🟡 | Border DFS, then flip | — |
| 3 | ✅ | [Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) `LC` | 🟡 | 2-colouring | Disconnected graph |
| 4 | ⭐ | [Course Schedule](https://dsacourse.com/top-150/course-schedule) `DSA150` | 🟡 | Kahn / 3-colour DFS | Edge direction |
| 4 | ⭐ | [Course Schedule II](https://dsacourse.com/top-150/topological-order) `DSA150` | 🟡 | Topological order | Return [] on cycle |
| 4 | ✅ | [Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/) `LC` | 🟡 | Reverse topo / colours | — |
| 4 | ⭐ | [Graph Valid Tree](https://dsacourse.com/top-150/graph-valid-tree) `DSA150` | 🟡 | n−1 edges + connected | — |
| 4 | ⭐ | [Number of Connected Components in an Undirected Graph](https://dsacourse.com/top-150/count-components) `DSA150` | 🟡 | DSU | — |
| 4 | ⭐ | [Redundant Connection](https://dsacourse.com/top-150/redundant-connection) `DSA150` | 🟡 | DSU cycle edge | — |
| 4 | ✅ | [Accounts Merge](https://leetcode.com/problems/accounts-merge/) `LC` | 🟡 | DSU on emails | Sorting output |
| 5 | ⭐ | [Word Ladder](https://dsacourse.com/top-150/word-ladder) `DSA150` | 🔴 | BFS on implicit graph (wildcard buckets `h*t`) | Comparing every word pair |
| 5 | 🚀 | [Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/) `LC` | 🔴 | Tarjan bridges | — |

### K. Revision card
```
GRAPH: define nodes, edges, directed?, weighted?
shortest unweighted → BFS (mark on enqueue) | explore/components → DFS or DSU
simultaneous spread → multi-source BFS | dependencies → Kahn topo (cycle if < n)
DSU: find w/ path compression, union by rank; union returns False → cycle
Complexity: O(V + E)
```

---

## P18. Advanced Graphs

### A. When BFS isn't enough
BFS gives shortest paths only when **every edge has the same cost**. With weights, use:

| Situation | Algorithm | Complexity |
|---|---|---|
| Non-negative weights, single source | **Dijkstra** (heap) | O(E log V) |
| Negative weights, or "at most K edges" | **Bellman-Ford** | O(V · E) or O(K · E) |
| All pairs, small V (≤ ~400) | **Floyd-Warshall** | O(V³) |
| Connect all nodes at minimum total cost | **MST: Kruskal** (sort + DSU) or **Prim** (heap) | O(E log E) |
| Minimise the maximum edge on a path | Dijkstra variant (cost = max) or BS + BFS or DSU | O(E log V) |
| Use every edge exactly once | Eulerian path (Hierholzer) | O(E log E) |

### B. Dijkstra
**Idea:** always expand the closest unfinished node. With non-negative edges, once a node is popped with the smallest distance, no later path can be shorter.
```python
def networkDelayTime(times, n, k):
    graph = defaultdict(list)
    for u, v, w in times: graph[u].append((v, w))
    dist = {}
    heap = [(0, k)]                              # (distance, node)
    while heap:
        d, node = heapq.heappop(heap)
        if node in dist: continue                # stale entry: already finalised with a shorter distance
        dist[node] = d
        for nei, w in graph[node]:
            if nei not in dist:
                heapq.heappush(heap, (d + w, nei))
    return max(dist.values()) if len(dist) == n else -1
```
**Why not with negative edges?** A later negative edge could make an already-finalised node cheaper, breaking the "popped = final" guarantee.

### C. Bellman-Ford (with ≤ K edges)
Relax all edges up to K+1 times. Copy distances each round so you don't chain multiple edges in one round.
```python
def findCheapestPrice(n, flights, src, dst, k):
    dist = [float('inf')] * n
    dist[src] = 0
    for _ in range(k + 1):                       # k stops = k+1 edges
        tmp = dist[:]                            # use last round's values only
        for u, v, w in flights:
            if dist[u] + w < tmp[v]:
                tmp[v] = dist[u] + w
        dist = tmp
    return dist[dst] if dist[dst] != float('inf') else -1
```

### D. Floyd-Warshall
```python
for k in range(n):                     # allow k as an intermediate node
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])
```

### E. MST — Prim (heap) and Kruskal (DSU)
```python
def minCostConnectPoints(points):              # Prim on a complete graph
    n = len(points); seen = set(); heap = [(0, 0)]; total = 0
    while len(seen) < n:
        cost, i = heapq.heappop(heap)
        if i in seen: continue
        seen.add(i); total += cost
        for j in range(n):
            if j not in seen:
                d = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                heapq.heappush(heap, (d, j))
    return total
# Kruskal: sort edges by weight; add edge if dsu.union(u, v) succeeds; stop at n-1 edges.
```

### J. Practice questions
| Lvl | Pri | Problem | Diff | Algorithm | Trap |
|---|---|---|---|---|---|
| 3 | ⭐ | [Network Delay Time](https://dsacourse.com/top-150/network-delay-time) `DSA150` | 🟡 | Dijkstra | Unreachable nodes |
| 3 | ✅ | [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) `LC` | 🟡 | BFS 8-directional | Start/end blocked |
| 4 | ⭐ | [Min Cost to Connect All Points](https://dsacourse.com/top-150/min-cost-connect-points) `DSA150` | 🟡 | Prim / Kruskal | — |
| 4 | ⭐ | [Cheapest Flights Within K Stops](https://dsacourse.com/top-150/cheapest-flights-within-k-stops) `DSA150` | 🟡 | Bellman-Ford | Copying dist per round |
| 4 | ✅ | [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) `LC` | 🟡 | Dijkstra (max-edge cost) | — |
| 4 | ✅ | [Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) `LC` | 🟡 | Floyd-Warshall | Tie → larger index |
| 5 | ⭐ | [Swim in Rising Water](https://dsacourse.com/top-150/swim-in-rising-water) `DSA150` | 🔴 | Dijkstra minimax | — |
| 5 | ⭐ | [Alien Dictionary](https://dsacourse.com/top-150/alien-dictionary) `DSA150` | 🔴 | Build edges + topo | Prefix case `"abc"` before `"ab"` → invalid |
| 5 | 🚀 | [Reconstruct Itinerary](https://dsacourse.com/top-150/reconstruct-itinerary) `DSA150` | 🔴 | Hierholzer (Eulerian path) | Greedy lexical DFS gets stuck |

### K. Revision card
```
weights ≥ 0 → Dijkstra (skip stale heap entries) | negative / ≤K edges → Bellman-Ford (copy per round)
all pairs small V → Floyd O(V³) | connect all cheaply → Kruskal (sort+DSU) / Prim (heap)
```

---

## P19. Greedy

### A. Introduction
**Analogy:** giving change with the fewest Indian coins/notes — always use the largest denomination that fits. It works for ₹ denominations… but **fails** for coins `[1, 3, 4]` making 6 (greedy: 4+1+1 = 3 coins; optimal: 3+3 = 2 coins).

Greedy = make the **locally best choice** at each step and never reconsider. It's correct **only when you can prove** the local choice is part of some optimal solution. When greedy fails, you usually need DP.

### B. How to recognise
- Optimisation (max/min) where sorting by one key reveals an obvious "best next" choice.
- Interval scheduling, jumps/reach, resource allocation, "minimum number of …".
- **Always test with a counter-example** before committing. If you can't break it and can argue why, go greedy.

### C. How to prove a greedy (interview-level)
1. **Exchange argument:** take any optimal solution; swap its first choice with the greedy choice; show it's still valid and no worse. Repeat.
2. **Stays ahead:** show that after each step, greedy's partial solution is at least as good as any other's.
3. **Invariant:** something you maintain (like "max reachable index") always describes everything that's possible.

### D. Classic greedy patterns
**Jump Game (max reach invariant):**
```python
def canJump(nums):
    reach = 0
    for i, x in enumerate(nums):
        if i > reach: return False           # can't even stand here
        reach = max(reach, i + x)
    return True
```
**Jump Game II (BFS by levels on indices):**
```python
def jump(nums):
    jumps = cur_end = farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == cur_end:                     # end of current "level" → must jump
            jumps += 1; cur_end = farthest
    return jumps
```
**Gas Station:** if total gas ≥ total cost, a solution exists; the start is just after the last point where the running tank went negative (any start before it would also fail there).
```python
def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost): return -1
    tank = start = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start, tank = i + 1, 0
    return start
```
**Partition Labels:** record each char's last index; extend the current part's end to the max last-index seen; cut when `i == end`.

**Valid Parenthesis String:** track a range `[lo, hi]` of possible open counts; `*` widens it; if `hi < 0` fail; clamp `lo ≥ 0`; valid if `lo == 0` at end.

**Theory classics (no judge links needed, know the idea):**
- **Activity selection:** sort by end, pick if start ≥ last end (= Non-overlapping Intervals).
- **Minimum platforms:** sweep line (= Meeting Rooms II).
- **Fractional knapsack:** sort by value/weight ratio, take greedily (fractions allowed → greedy works; 0/1 knapsack → DP).
- **Job sequencing with deadlines:** sort by profit desc, place each job in the latest free slot ≤ its deadline (DSU speeds up slot finding).

### J. Practice questions
| Lvl | Pri | Problem | Diff | Greedy idea | Trap |
|---|---|---|---|---|---|
| 1 | ✅ | [Assign Cookies](https://leetcode.com/problems/assign-cookies/) `LC` | 🟢 | Sort both, smallest sufficient cookie | — |
| 1 | ✅ | [Lemonade Change](https://leetcode.com/problems/lemonade-change/) `LC` | 🟢 | Prefer giving a 10 first | — |
| 2 | ⭐ | [Jump Game](https://dsacourse.com/top-150/jump-game) `DSA150` | 🟡 | Max reach | — |
| 2 | ✅ | [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) `LC` | 🟡 | Take every positive difference | — |
| 3 | ⭐ | [Jump Game II](https://dsacourse.com/top-150/jump-game-ii) `DSA150` | 🟡 | Level boundaries | Loop to n−2 |
| 3 | ⭐ | [Gas Station](https://dsacourse.com/top-150/gas-station) `DSA150` | 🟡 | Reset start on negative tank | Proof |
| 3 | ⭐ | [Partition Labels](https://dsacourse.com/top-150/partition-labels) `DSA150` | 🟡 | Last occurrence | — |
| 4 | ⭐ | [Hand of Straights](https://dsacourse.com/top-150/hand-of-straights) `DSA150` | 🟡 | Smallest card must start a group | Counter ordering |
| 4 | ⭐ | [Valid Parenthesis String](https://dsacourse.com/top-150/valid-parenthesis-string) `DSA150` | 🟡 | Range of open counts | Clamping lo |

### K. Revision card
```
GREEDY: local best choice + PROOF (exchange / stays-ahead / invariant)
Test a counter-example first; if greedy breaks → DP
Intervals: sort by END | reach problems: track farthest | circuits: reset on negative
```

---

## P20. Dynamic Programming

### A. Introduction
**Analogy:** if someone asks you "what's 1+1+1+1+1+1+1?" you count: 7. If they add "+1", you don't recount — you say 8, because you **remembered** the previous answer. That's DP.

DP = **recursion + remembering answers to subproblems**. It applies when:
1. **Optimal substructure:** the answer is built from answers to smaller versions of the same problem.
2. **Overlapping subproblems:** the same smaller problems are needed again and again.

| | |
|---|---|
| **Solves** | Count ways, min/max cost, longest/shortest, yes/no reachability over choices |
| **Advantages** | Exponential → polynomial |
| **Limitations** | Needs a correct state definition; memory for tables |
| **Prerequisites** | Recursion (P13), hashing (memo), Kadane (P8) as a preview |

### B. How to recognise
- "Number of ways…", "minimum cost/steps…", "maximum profit/sum…", "longest/shortest subsequence…", "can you reach / partition / form…".
- Choices at each step (take/skip, which coin, match/insert/delete), and **greedy has a counter-example**.
- A brute-force recursion exists, and drawing its tree shows **repeated calls**.
- Two strings/sequences compared position by position → 2D DP.
- *Misleading:* "minimum steps" in an unweighted graph/grid → BFS; "all combinations" → backtracking.

### C. Intuition from scratch — the 4-stage evolution (Climbing Stairs)
> Climb n stairs taking 1 or 2 steps at a time. How many distinct ways?

**Stage 1 — Recursion (define the state).** `ways(i)` = ways to reach step i. The last move was either a 1-step from i−1 or a 2-step from i−2:
```python
def ways(i):
    if i <= 1: return 1
    return ways(i - 1) + ways(i - 2)          # O(2^n): ways(3) is computed many times
```
**Stage 2 — Memoisation (top-down).** Cache results:
```python
from functools import cache
@cache
def ways(i):
    if i <= 1: return 1
    return ways(i - 1) + ways(i - 2)          # O(n): each i computed once
```
**Stage 3 — Tabulation (bottom-up).** Fill a table from base cases upward:
```python
def climbStairs(n):
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```
**Stage 4 — Space optimisation.** Only the last two values are needed:
```python
def climbStairs(n):
    a, b = 1, 1                               # dp[i-2], dp[i-1]
    for _ in range(n - 1):
        a, b = b, a + b
    return b
```
**Always go through these stages in order.** In interviews, a correct memoised solution is often enough; offer tabulation/space optimisation as follow-ups.

### D. The DP recipe (use for EVERY DP problem)
1. **State:** what does `dp[i]` (or `dp[i][j]`) mean *in words*? ← 80% of the difficulty.
2. **Transition:** how is `dp[i]` computed from smaller states? (enumerate the last choice)
3. **Base cases:** smallest states answered directly.
4. **Order:** which states must be computed first? (loop direction)
5. **Answer:** which state holds the final answer? (`dp[n]`, `max(dp)`, `dp[0][0]`…)

### C2. Worked — House Robber
> Can't rob adjacent houses. `[2, 7, 9, 3, 1]` → 12 (2 + 9 + 1).

- **State:** `dp[i]` = max money from houses `0..i`.
- **Transition (last choice):** rob house i → `dp[i−2] + nums[i]`; skip it → `dp[i−1]`. `dp[i] = max(dp[i−1], dp[i−2] + nums[i])`.
- **Base:** `dp[0] = nums[0]`, `dp[1] = max(nums[0], nums[1])`.
```python
def rob(nums):
    prev2, prev1 = 0, 0                       # dp[i-2], dp[i-1]
    for x in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + x)
    return prev1
```
| i | x | rob = prev2 + x | skip = prev1 | new prev1 |
|---|---|---|---|---|
| 0 | 2 | 0 + 2 = 2 | 0 | 2 |
| 1 | 7 | 0 + 7 = 7 | 2 | 7 |
| 2 | 9 | 2 + 9 = 11 | 7 | 11 |
| 3 | 3 | 7 + 3 = 10 | 11 | 11 |
| 4 | 1 | 11 + 1 = 12 | 11 | **12** |

**House Robber II (circular):** answer = max(rob(nums[1:]), rob(nums[:-1])) — first and last can't both be robbed.

### E. DP families & templates

**1. Linear 1D DP** — Climbing Stairs, House Robber, Decode Ways, Word Break.
```python
def wordBreak(s, wordDict):
    words = set(wordDict)
    dp = [False] * (len(s) + 1); dp[0] = True          # dp[i]: s[:i] can be segmented
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True; break
    return dp[-1]
```

**2. Unbounded choices (coins)** — Coin Change (min coins):
```python
def coinChange(coins, amount):
    dp = [0] + [float('inf')] * amount                   # dp[a]: min coins for amount a
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
```
**Coin Change II (number of combinations)** — **coins in the outer loop** so each combination is counted once (order doesn't matter):
```python
def change(amount, coins):
    dp = [1] + [0] * amount
    for c in coins:                 # outer: coins → combinations
        for a in range(c, amount + 1):
            dp[a] += dp[a - c]
    return dp[amount]
# Swapping the loops (amount outer, coins inner) counts PERMUTATIONS instead.
```

**3. 0/1 Knapsack (each item at most once)** — Partition Equal Subset Sum, Target Sum. Iterate capacity **backwards** so an item isn't reused in the same round:
```python
def canPartition(nums):
    total = sum(nums)
    if total % 2: return False
    target = total // 2
    dp = [True] + [False] * target            # dp[s]: some subset sums to s
    for x in nums:
        for s in range(target, x - 1, -1):    # backwards!
            dp[s] = dp[s] or dp[s - x]
    return dp[target]
```
| Knapsack type | Capacity loop | Example |
|---|---|---|
| 0/1 (use once) | backwards | Partition Equal Subset Sum, Target Sum |
| Unbounded (reuse) | forwards | Coin Change, Coin Change II |

**Target Sum trick:** choosing signs splits nums into P (plus) and N (minus): `P − N = target`, `P + N = total` → `P = (target + total) / 2` → count subsets with that sum.

**4. LIS (Longest Increasing Subsequence)**
```python
def lengthOfLIS(nums):                        # O(n²) DP
    dp = [1] * len(nums)                      # dp[i]: LIS ending at i
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

def lengthOfLIS_fast(nums):                   # O(n log n) patience sorting
    tails = []                                # tails[k]: smallest tail of an increasing subseq of length k+1
    for x in nums:
        i = bisect.bisect_left(tails, x)
        if i == len(tails): tails.append(x)
        else: tails[i] = x                    # a smaller tail is always better for the future
    return len(tails)
```

**5. Grid DP** — Unique Paths, Minimum Path Sum: `dp[r][c] = f(dp[r−1][c], dp[r][c−1])`.

**6. Two-string DP** — LCS, Edit Distance, Distinct Subsequences, Interleaving String. State: `dp[i][j]` = answer for `s[:i]` and `t[:j]`.
```python
def longestCommonSubsequence(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1           # match: extend diagonal
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) # skip one char from either
    return dp[m][n]
```
LCS table for `a = "abcde"`, `b = "ace"`:

|   | "" | a | c | e |
|---|---|---|---|---|
| "" | 0 | 0 | 0 | 0 |
| a | 0 | **1** | 1 | 1 |
| b | 0 | 1 | 1 | 1 |
| c | 0 | 1 | **2** | 2 |
| d | 0 | 1 | 2 | 2 |
| e | 0 | 1 | 2 | **3** |

```python
def minDistance(w1, w2):                      # Edit Distance
    m, n = len(w1), len(w2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1): dp[i][0] = i       # delete all
    for j in range(n + 1): dp[0][j] = j       # insert all
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if w1[i - 1] == w2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],      # delete
                                   dp[i][j - 1],      # insert
                                   dp[i - 1][j - 1])  # replace
    return dp[m][n]
```

**7. Palindromes** — Longest Palindromic Substring / Palindromic Substrings: **expand around each centre** (2n−1 centres), O(n²) time, O(1) space; DP table `isPal[i][j] = s[i]==s[j] and isPal[i+1][j−1]` also works.

**8. State machine DP (stocks)** — Buy/Sell with Cooldown: states `hold`, `sold`, `rest`:
```python
def maxProfit(prices):
    hold, sold, rest = float('-inf'), 0, 0
    for p in prices:
        hold, sold, rest = max(hold, rest - p), hold + p, max(rest, sold)
    return max(sold, rest)
```

**9. Interval DP** — Burst Balloons, Minimum Cost to Cut a Stick: `dp[l][r]` = best for range; try every **last** split k inside; iterate by increasing length.

**10. DP on grids with DFS + memo** — Longest Increasing Path in a Matrix (DAG implied by strictly increasing values → no cycles → memo works).

**11. Tree DP** — return a tuple of states from each child (House Robber III).

**12. Bitmask DP (advanced)** — state includes a set of used items as a bitmask (n ≤ ~20).
**13. Digit DP (advanced)** — count numbers ≤ N with a property; state = (position, tight, extra).

### G. Complexity
Time = (number of states) × (work per transition). Space = number of states (often reducible to one or two rows).

### H. Common mistakes
- Vague state ("dp[i] = the answer") → define it precisely in words.
- Wrong loop direction in knapsack (forward vs backward).
- Coin Change II with loops swapped (counts permutations).
- Off-by-one between `dp` indices and string indices (`dp[i]` ↔ `s[i−1]`).
- Initialising min-DP with 0 instead of infinity.
- Using `@cache` with mutable (list) arguments — pass indices or tuples.

### I. Interview thinking
1. Start with the recursive brute force and say: "This recomputes the same states — I'll memoise."
2. State the state + transition + base in one breath.
3. Complexity: "n × amount states, each O(k) transition."
4. Offer space optimisation.
**When stuck:** ask "What is the LAST decision?" — the transition is usually "for each possible last decision, combine with the best of the rest."

### J. Practice questions
| Lvl | Pri | Problem | Diff | Family | Trap |
|---|---|---|---|---|---|
| 1 | ⭐ | [Climbing Stairs](https://dsacourse.com/top-150/climbing-stairs) `DSA150` | 🟢 | 1D | — |
| 1 | ✅ | [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) `LC` | 🟢 | Recursion → memo → table | — |
| 1 | ⭐ | [Min Cost Climbing Stairs](https://dsacourse.com/top-150/min-cost-climbing-stairs) `DSA150` | 🟢 | 1D min | Top is beyond last step |
| 2 | ⭐ | [House Robber](https://dsacourse.com/top-150/house-robber) `DSA150` | 🟡 | Take/skip | — |
| 2 | ⭐ | [House Robber II](https://dsacourse.com/top-150/house-robber-circular) `DSA150` | 🟡 | Two linear runs | n = 1 |
| 2 | ⭐ | [Unique Paths](https://dsacourse.com/top-150/unique-paths) `DSA150` | 🟢 | Grid | — |
| 2 | ✅ | [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) `LC` | 🟡 | Grid min | First row/col |
| 2 | ✅ | [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/) `LC` | 🟡 | Grid + obstacles | Obstacle at start |
| 3 | ⭐ | [Longest Palindromic Substring](https://dsacourse.com/top-150/longest-palindromic-substring) `DSA150` | 🟡 | Expand centres | Even-length centres |
| 3 | ⭐ | [Palindromic Substrings](https://dsacourse.com/top-150/count-palindromic-substrings) `DSA150` | 🟡 | Expand centres | — |
| 3 | ⭐ | [Decode Ways](https://dsacourse.com/top-150/decode-ways) `DSA150` | 🟡 | 1D with conditions | '0' handling |
| 3 | ⭐ | [Coin Change](https://dsacourse.com/top-150/coin-change) `DSA150` | 🟡 | Unbounded min | Greedy fails |
| 3 | ⭐ | [Word Break](https://dsacourse.com/top-150/word-break) `DSA150` | 🟡 | Prefix segmentation | — |
| 3 | ⭐ | [Longest Increasing Subsequence](https://dsacourse.com/top-150/longest-increasing-subsequence) `DSA150` | 🟡 | O(n²) → O(n log n) | Subsequence ≠ subarray |
| 4 | ⭐ | [Partition Equal Subset Sum](https://dsacourse.com/top-150/partition-equal-subset-sum) `DSA150` | 🟡 | 0/1 knapsack | Backward loop |
| 4 | ⭐ | [Coin Change II](https://dsacourse.com/top-150/coin-change-ii) `DSA150` | 🟡 | Unbounded count | Loop order |
| 4 | ⭐ | [Target Sum](https://dsacourse.com/top-150/target-sum) `DSA150` | 🟡 | Subset-sum transform | Parity / negative target |
| 4 | ⭐ | [Longest Common Subsequence](https://dsacourse.com/top-150/longest-common-subsequence) `DSA150` | 🟡 | Two strings | Index offset |
| 4 | ⭐ | [Maximal Square](https://dsacourse.com/top-150/maximal-square) `DSA150` | 🟡 | `1 + min(3 neighbours)` | Area vs side |
| 4 | ⭐ | [Best Time to Buy and Sell Stock with Cooldown](https://dsacourse.com/top-150/best-time-stock-cooldown) `DSA150` | 🟡 | State machine | Simultaneous update |
| 4 | ⭐ | [Interleaving String](https://dsacourse.com/top-150/interleaving-string) `DSA150` | 🟡 | Two strings | Length check |
| 4 | ✅ | [Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) `LC` | 🟡 | LCS(s, reverse(s)) / interval | — |
| 5 | ⭐ | [Edit Distance](https://dsacourse.com/top-150/edit-distance) `DSA150` | 🔴 | Two strings | Base rows |
| 5 | ⭐ | [Longest Increasing Path in a Matrix](https://dsacourse.com/top-150/longest-increasing-path-in-matrix) `DSA150` | 🔴 | DFS + memo | Why no visited set needed |
| 5 | ✅ | [Distinct Subsequences](https://dsacourse.com/top-150/distinct-subsequences) `DSA150` | 🔴 | Two strings count | — |
| 5 | 🚀 | [Burst Balloons](https://dsacourse.com/top-150/burst-balloons) `DSA150` | 🔴 | Interval DP (last burst) | Thinking "first burst" |
| 5 | 🚀 | [Minimum Cost to Cut a Stick](https://leetcode.com/problems/minimum-cost-to-cut-a-stick/) `LC` | 🔴 | Interval DP | — |
| 5 | 🚀 | [Regular Expression Matching](https://dsacourse.com/top-150/regular-expression-matching) `DSA150` | 🔴 | Two strings + `*` | Zero occurrences |
| 5 | 🚀 | [Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) `LC` | 🟡 | Bitmask DP / backtracking | — |
| 5 | 🚀 | [Count Numbers with Unique Digits](https://leetcode.com/problems/count-numbers-with-unique-digits/) `LC` | 🟡 | Counting / digit-DP intro | — |

### K. Revision card
```
DP = recursion + memo. Recipe: STATE (in words) → TRANSITION (last choice) → BASE → ORDER → ANSWER
Evolve: recursion → @cache → table → rolling variables
0/1 knapsack: capacity BACKWARD | unbounded: FORWARD | combos: items outer loop
2 strings: dp[i][j] on prefixes, dp size (m+1)(n+1)
LIS fast: tails + bisect_left
Stuck? "What is the LAST decision?"
```
**Mastery:** Coin Change, Partition Equal Subset Sum, LCS, Edit Distance from scratch, explaining the state in words first.

---

## P21. Bit Manipulation

### A. Introduction
Numbers are stored in binary. Bit tricks give O(1)-space answers for parity, uniqueness, and subsets.

### C. Essential facts
| Expression | Meaning |
|---|---|
| `x & 1` | 1 if odd |
| `x >> 1`, `x << 1` | ÷2, ×2 |
| `x & (x - 1)` | Clear lowest set bit (→ power of two check: `x > 0 and x & (x-1) == 0`) |
| `x & -x` | Isolate lowest set bit |
| `a ^ a = 0`, `a ^ 0 = a` | XOR cancels pairs (Single Number) |
| `(x >> i) & 1` | i-th bit |
| `x | (1 << i)`, `x & ~(1 << i)` | Set / clear bit i |
| `bin(x).count('1')` / `x.bit_count()` (3.10+) | Popcount |
| `mask in range(1 << n)` | Enumerate all subsets of n items |

```python
def singleNumber(nums):              # every number appears twice except one
    res = 0
    for x in nums: res ^= x          # pairs cancel
    return res

def countBits(n):                    # DP with bits: i has bits of i>>1 plus its last bit
    dp = [0] * (n + 1)
    for i in range(1, n + 1): dp[i] = dp[i >> 1] + (i & 1)
    return dp

def missingNumber(nums):             # XOR indices 0..n with values
    res = len(nums)
    for i, x in enumerate(nums): res ^= i ^ x
    return res
```
**Python caveat (Sum of Two Integers):** Python ints are unbounded, so simulate 32 bits with `mask = 0xFFFFFFFF` and convert back: `a if a <= 0x7FFFFFFF else ~(a ^ mask)`.

### J. Practice questions
| Lvl | Pri | Problem | Diff | Trick |
|---|---|---|---|---|
| 1 | ⭐ | [Single Number](https://dsacourse.com/top-150/single-number-practice) `DSA150` | 🟢 | XOR cancel |
| 1 | ⭐ | [Number of 1 Bits](https://dsacourse.com/top-150/number-of-1-bits) `DSA150` | 🟢 | `n & (n−1)` loop |
| 1 | ✅ | [Power of Two](https://leetcode.com/problems/power-of-two/) `LC` | 🟢 | Single set bit |
| 2 | ⭐ | [Counting Bits](https://dsacourse.com/top-150/counting-bits) `DSA150` | 🟢 | DP on `i >> 1` |
| 2 | ⭐ | [Reverse Bits](https://dsacourse.com/top-150/reverse-bits) `DSA150` | 🟢 | Shift out / shift in 32 times |
| 2 | ⭐ | [Missing Number](https://dsacourse.com/top-150/missing-number) `DSA150` | 🟢 | XOR or sum formula |
| 2 | ✅ | [Hamming Distance](https://leetcode.com/problems/hamming-distance/) `LC` | 🟢 | popcount(x ^ y) |
| 3 | ✅ | [Single Number III](https://leetcode.com/problems/single-number-iii/) `LC` | 🟡 | Split by lowest differing bit |
| 3 | 🚀 | [Single Number II](https://leetcode.com/problems/single-number-ii/) `LC` | 🟡 | Count each bit mod 3 |
| 4 | ⭐ | [Sum of Two Integers](https://dsacourse.com/top-150/sum-of-two-integers) `DSA150` | 🟡 | XOR = sum w/o carry, AND<<1 = carry; 32-bit mask in Python |

---

## P22. Matrix & Math

### Matrix techniques
| Problem type | Technique |
|---|---|
| Rotate 90° clockwise in place | **Transpose**, then **reverse each row** |
| Spiral order | Shrinking boundaries `top, bottom, left, right` |
| Set zeroes in O(1) space | Use first row/column as markers (+ a flag for column 0) |
| In-place state updates (Game of Life) | Encode old & new state in one cell (e.g., 2 = was alive now dead) |
| Search in row & column sorted matrix | **Staircase**: start top-right; go left if too big, down if too small → O(m + n) |
| Directions | `dirs = [(1,0),(-1,0),(0,1),(0,-1)]`, bounds check `0 <= r < R` |

```python
def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):                      # transpose (swap across diagonal)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()                                  # mirror horizontally

def spiralOrder(m):
    res = []
    top, bottom, left, right = 0, len(m) - 1, 0, len(m[0]) - 1
    while top <= bottom and left <= right:
        for c in range(left, right + 1): res.append(m[top][c])
        top += 1
        for r in range(top, bottom + 1): res.append(m[r][right])
        right -= 1
        if top <= bottom:
            for c in range(right, left - 1, -1): res.append(m[bottom][c])
            bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1): res.append(m[r][left])
            left += 1
    return res
```

### Math techniques
```python
def myPow(x, n):                      # fast exponentiation: O(log n)
    if n < 0: x, n = 1 / x, -n
    res = 1
    while n:
        if n & 1: res *= x            # odd bit → multiply in current power
        x *= x                        # square the base
        n >>= 1
    return res

def gcd(a, b):                        # Euclid (or math.gcd)
    while b: a, b = b, a % b
    return a

def countPrimes(n):                   # Sieve of Eratosthenes: O(n log log n)
    if n < 3: return 0
    is_p = [True] * n; is_p[0] = is_p[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_p[i]:
            for j in range(i * i, n, i): is_p[j] = False
    return sum(is_p)

MOD = 10**9 + 7                       # modular arithmetic: (a+b)%M, (a*b)%M distribute; use pow(a, M-2, M) for inverse when M is prime
```
**Happy Number** = cycle detection (Floyd or a set) on the digit-square sequence.

### J. Practice questions
| Lvl | Pri | Problem | Diff | Technique |
|---|---|---|---|---|
| 1 | ✅ | [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/) `LC` | 🟢 | Row from previous row |
| 1 | ⭐ | [Happy Number](https://dsacourse.com/top-150/happy-number) `DSA150` | 🟢 | Cycle detection |
| 2 | ⭐ | [Rotate Image](https://dsacourse.com/top-150/rotate-image) `DSA150` | 🟡 | Transpose + reverse |
| 2 | ⭐ | [Spiral Matrix](https://dsacourse.com/top-150/spiral-matrix) `DSA150` | 🟡 | Boundaries |
| 3 | ⭐ | [Set Matrix Zeroes](https://dsacourse.com/top-150/set-matrix-zeroes) `DSA150` | 🟡 | First row/col markers |
| 3 | ✅ | [Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/) `LC` | 🟡 | Staircase |
| 3 | ✅ | [Game of Life](https://leetcode.com/problems/game-of-life/) `LC` | 🟡 | State encoding |
| 3 | ⭐ | [Pow(x, n)](https://dsacourse.com/top-150/pow-x-n) `DSA150` | 🟡 | Fast power, negative n |
| 3 | ⭐ | [Multiply Strings](https://dsacourse.com/top-150/multiply-strings) `DSA150` | 🟡 | Grade-school, `res[i+j+1]` |
| 3 | ✅ | [Count Primes](https://leetcode.com/problems/count-primes/) `LC` | 🟡 | Sieve |

---

## P23. Cyclic Sort / Index Placement

### A. Introduction
When values are in the range `[1, n]` (or `[0, n]`), each value has a "home" index (`value − 1`). Swap every value into its home; afterwards, any index whose value doesn't match reveals a **missing** or **duplicate** number — in O(n) time and **O(1) extra space**.

### B. How to recognise
- "Array of n integers in the range [1, n]" (or [0, n]).
- Find missing / duplicate / first missing positive / mismatched numbers.
- O(1) extra space required (otherwise a set works).

### E. Template
```python
def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        home = nums[i] - 1                                 # where nums[i] belongs
        if 0 <= home < len(nums) and nums[i] != nums[home]:
            nums[i], nums[home] = nums[home], nums[i]      # send it home; DON'T advance i
        else:
            i += 1                                         # in place, out of range, or duplicate
    return nums
# Then: for i, x in enumerate(nums): if x != i + 1 → i+1 is missing (and x is a duplicate)
```
Each swap places one number permanently → at most n swaps → O(n).
Compare `nums[i] != nums[home]` (not `i != home`) to avoid infinite loops on duplicates.

### J. Practice questions
| Lvl | Pri | Problem | Diff | Note |
|---|---|---|---|---|
| 1 | ⭐ | [Missing Number](https://dsacourse.com/top-150/missing-number) `DSA150` | 🟢 | Range [0, n] (or XOR) |
| 2 | ⭐ | [Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) `LC` | 🟢 | Classic template |
| 2 | ✅ | [Set Mismatch](https://leetcode.com/problems/set-mismatch/) `LC` | 🟢 | Duplicate + missing |
| 3 | ✅ | [Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/) `LC` | 🟡 | Template or sign-marking |
| 3 | ⭐ | [Find the Duplicate Number](https://dsacourse.com/top-150/find-the-duplicate-number) `DSA150` | 🟡 | Can't modify array → Floyd |
| 5 | ⭐ | [First Missing Positive](https://leetcode.com/problems/first-missing-positive/) `LC` | 🔴 | Ignore values outside [1, n] |

---

## P24. Advanced DSA

> Study only after Phases 1–5 feel comfortable. These appear rarely in backend interviews but help in strong product companies and with string-heavy problems.

### Strings module overview
| Topic | Covered in |
|---|---|
| Character frequency, anagrams, hashing strings | P2 |
| Two pointers / palindrome checks | P3 |
| Sliding window on substrings | P4 |
| Trie | P15 |
| String DP (LCS, edit distance, palindromes) | P20 |
| **Pattern matching (KMP, Rabin-Karp, Z)** | below |

### KMP (Knuth-Morris-Pratt) — find a pattern in O(n + m)
Naive matching restarts from scratch on mismatch (O(n·m)). KMP precomputes `lps[i]` = length of the longest proper prefix of `pattern[:i+1]` that is also a suffix — on mismatch, jump to `lps[j−1]` instead of restarting.
```python
def kmp_search(text, pat):
    lps, length = [0] * len(pat), 0
    for i in range(1, len(pat)):                    # build LPS
        while length and pat[i] != pat[length]:
            length = lps[length - 1]
        if pat[i] == pat[length]: length += 1
        lps[i] = length
    j = 0
    for i, c in enumerate(text):                    # scan text
        while j and c != pat[j]:
            j = lps[j - 1]
        if c == pat[j]: j += 1
        if j == len(pat):
            return i - j + 1                        # first match index
    return -1
```
### Rabin-Karp (rolling hash)
Hash each window of length m in O(1) by removing the leading char and adding the trailing one: `h = (h − ord(out)·B^(m−1))·B + ord(in) mod M`. Compare hashes; verify on equality (collisions). Use for "repeated substrings" and duplicate detection.

### Z-algorithm
`Z[i]` = length of the longest substring starting at i that matches a prefix. Search by computing Z on `pattern + "$" + text`.

### Fenwick Tree (Binary Indexed Tree) — prefix sums with updates, O(log n)
```python
class Fenwick:
    def __init__(self, n): self.t = [0] * (n + 1)
    def update(self, i, delta):           # 1-indexed
        while i < len(self.t):
            self.t[i] += delta; i += i & -i
    def query(self, i):                   # sum of [1..i]
        s = 0
        while i > 0:
            s += self.t[i]; i -= i & -i
        return s
```
### Segment Tree — range queries (sum/min/max) with point updates, O(log n)
```python
class SegTree:
    def __init__(self, nums):
        self.n = len(nums); self.t = [0] * (2 * self.n)
        self.t[self.n:] = nums
        for i in range(self.n - 1, 0, -1): self.t[i] = self.t[2*i] + self.t[2*i+1]
    def update(self, i, val):
        i += self.n; self.t[i] = val
        while i > 1:
            i //= 2; self.t[i] = self.t[2*i] + self.t[2*i+1]
    def query(self, l, r):                # sum of [l, r)
        res = 0; l += self.n; r += self.n
        while l < r:
            if l & 1: res += self.t[l]; l += 1
            if r & 1: r -= 1; res += self.t[r]
            l //= 2; r //= 2
        return res
```
**Lazy propagation** (range updates + range queries): store pending updates at internal nodes and push them down only when needed. **Sparse table**: O(1) range-min queries on static arrays after O(n log n) preprocessing. **Meet in the middle**: split n ≤ 40 items into two halves of 2²⁰ subsets each, combine with sorting/binary search.

### Practice
| Pri | Problem | Diff | Topic |
|---|---|---|---|
| ✅ | [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) `LC` | 🟢 | Implement KMP |
| ✅ | [Repeated DNA Sequences](https://leetcode.com/problems/repeated-dna-sequences/) `LC` | 🟡 | Rolling hash / set |
| 🚀 | [Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/) `LC` | 🔴 | KMP LPS on `s + "#" + reverse(s)` |
| ✅ | [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) `LC` | 🟡 | Fenwick / segment tree |
| 🚀 | [Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) `LC` | 🔴 | Fenwick with coordinate compression / merge sort |
| 🚀 | [Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) `LC` | 🔴 | BFS over (node, mask) |
| 🚀 | [Numbers At Most N Given Digit Set](https://leetcode.com/problems/numbers-at-most-n-given-digit-set/) `LC` | 🔴 | Digit DP |

---

# PART IV — SYSTEMS

## 5. Pattern Comparisons

| Look-alikes | Choose the first when… | Choose the second when… | Why |
|---|---|---|---|
| **Hashing vs Sorting** | You need original indices, O(n) time, or only membership/counts | O(1) extra space matters, or you need order/neighbours | Hash: O(n) time/O(n) space; sort: O(n log n)/O(1)-ish |
| **Two Pointers vs Hashing** (pair sum) | Input is sorted; O(1) space wanted | Unsorted and you must return indices | Sorting would destroy indices |
| **Sliding Window vs Two Pointers** | The *contiguous range between* pointers matters (window state) | Only the two *endpoint elements* matter (pair sum, palindrome) | Window = same-direction pointers + state |
| **Sliding Window vs Prefix Sum** | All values non-negative / validity is monotonic; want longest/shortest | Negatives exist, or exact sum = K counts | Negatives break "shrink to fix" |
| **Prefix Sum vs Difference Array** | Many range **queries** | Many range **updates** | They're inverse operations |
| **Binary Search vs Linear Search** | Sorted or monotonic condition | Unsorted, single pass anyway | log n vs n |
| **Binary Search on Answer vs Greedy** | Hard to construct the optimum directly but easy to *check* a candidate | The best choice at each step is provably safe | BS-on-answer often *uses* a greedy check |
| **Heap vs Sorting** | Data arrives dynamically, or you need only top k | One-time ordering of everything | O(n log k) vs O(n log n) |
| **Heap vs Monotonic Deque** | Arbitrary insertions/removals by priority | Sliding window max/min (FIFO expiry) | Deque O(n) total vs heap O(n log n) |
| **Heap vs Monotonic Stack** | "Repeatedly get k-th/max" | "Next greater/smaller for each element" | Different questions entirely |
| **Monotonic Stack vs Two Pointers** (Trapping Water) | Thinking in "bounded basins" layer by layer | Thinking per column: min(maxL, maxR) | Both O(n); two pointers O(1) space |
| **Kadane vs Sliding Window** | Max-sum subarray with negatives | Constraint-based window (e.g., sum ≤ k, positives) | Kadane is DP, not a window |
| **Backtracking vs DP** | Need **all** solutions (output itself is exponential) | Need **count/best**; subproblems overlap | DP collapses repeated states |
| **Greedy vs DP** | You can prove the local choice (exchange argument) | Counter-example breaks greedy (coins [1,3,4]) | DP explores all choices efficiently |
| **BFS vs DFS** | Shortest path (unweighted), levels, nearest | Explore all, components, paths, cycle checks, backtracking | BFS expands by distance |
| **BFS vs Dijkstra** | All edges equal cost | Different non-negative weights | BFS assumes uniform cost |
| **Dijkstra vs Bellman-Ford** | Weights ≥ 0, speed matters | Negative weights or "at most k edges" | Dijkstra's finalisation breaks with negatives |
| **DSU vs DFS** (connectivity) | Edges arrive over time; repeated "connected?" queries | One-time traversal, need paths | DSU is incremental |
| **Trie vs Hash Set** | Prefix queries, many words sharing prefixes | Exact-match lookups only | Hash can't answer "starts with" efficiently |
| **Cyclic Sort vs Hash Set** | O(1) space, values in [1..n], can modify input | Any range, or input read-only | Index = implicit hash |

---

## 6. Master Question Bank

> **Every one of the 150 dsacourse problems is included below** (some are placed under the pattern that teaches them best — e.g., Maximum Subarray under Kadane, Product of Array Except Self under Prefix Sum). `LC` extras fill gaps in variations. Links are in each pattern's section.
>
> Tick `[x]` when solved **independently**. Add `🔁` if it needs revision.

<details>
<summary><b>Click to expand the full ordered checklist (~210 problems)</b></summary>

**P1 Arrays**
- [ ] ⭐ Running Sum of 1d Array `LC` · [ ] ⭐ Max Consecutive Ones `LC` · [ ] ✅ Third Maximum Number `LC` · [ ] ⭐ Plus One `DSA150`
- [ ] ⭐ Rotate Array `LC` · [ ] ✅ Check if Array Is Sorted and Rotated `LC` · [ ] ⭐ Encode and Decode Strings `DSA150`

**P2 Hashing**
- [ ] ⭐ Contains Duplicate `DSA150` · [ ] ⭐ Valid Anagram `DSA150` · [ ] ⭐ Two Sum `DSA150` · [ ] ✅ Ransom Note `LC`
- [ ] ✅ Isomorphic Strings `LC` · [ ] ✅ Majority Element `LC` · [ ] ⭐ Group Anagrams `DSA150`
- [ ] ⭐ Top K Frequent Elements `DSA150` · [ ] ⭐ Valid Sudoku `DSA150` · [ ] ⭐ Longest Consecutive Sequence `DSA150` · [ ] ✅ Insert Delete GetRandom O(1) `LC`

**P3 Two Pointers**
- [ ] ⭐ Valid Palindrome `DSA150` · [ ] ⭐ Move Zeroes `LC` · [ ] ✅ Remove Duplicates from Sorted Array `LC` · [ ] ✅ Merge Sorted Array `LC`
- [ ] ✅ Squares of a Sorted Array `LC` · [ ] ⭐ Two Sum II `DSA150` · [ ] ⭐ Sort Colors `DSA150` · [ ] ✅ Boats to Save People `LC`
- [ ] ⭐ 3Sum `DSA150` · [ ] ⭐ Container With Most Water `DSA150` · [ ] 🚀 4Sum `LC` · [ ] ⭐ Trapping Rain Water `DSA150`

**P4 Sliding Window**
- [ ] ⭐ Maximum Average Subarray I `LC` · [ ] ⭐ Best Time to Buy and Sell Stock `DSA150` · [ ] ⭐ Longest Substring Without Repeating Characters `DSA150`
- [ ] ⭐ Minimum Size Subarray Sum `DSA150` · [ ] ✅ Max Consecutive Ones III `LC` · [ ] ⭐ Permutation in String `DSA150` · [ ] ✅ Find All Anagrams in a String `LC`
- [ ] ✅ Fruit Into Baskets `LC` · [ ] ✅ Subarray Product Less Than K `LC` · [ ] ⭐ Longest Repeating Character Replacement `DSA150`
- [ ] ✅ Count Number of Nice Subarrays `LC` · [ ] ⭐ Minimum Window Substring `DSA150` · [ ] 🚀 Subarrays with K Different Integers `LC`

**P5 Prefix Sum**
- [ ] ⭐ Range Sum Query - Immutable `LC` · [ ] ⭐ Find Pivot Index `LC` · [ ] ⭐ Product of Array Except Self `DSA150`
- [ ] ⭐ Subarray Sum Equals K `LC` · [ ] ✅ Contiguous Array `LC` · [ ] ✅ Continuous Subarray Sum `LC` · [ ] ✅ Car Pooling `LC` · [ ] ✅ Corporate Flight Bookings `LC`

**P6 Sorting**
- [ ] ⭐ Sort an Array (merge sort) `LC` · [ ] ✅ Sort Characters By Frequency `LC` · [ ] ⭐ Kth Largest Element in an Array `DSA150` · [ ] ✅ Largest Number `LC` · [ ] 🚀 Reverse Pairs `LC`

**P7 Intervals**
- [ ] ⭐ Merge Intervals `DSA150` · [ ] ⭐ Insert Interval `DSA150` · [ ] ⭐ Non-overlapping Intervals `DSA150` · [ ] ✅ Minimum Number of Arrows `LC`
- [ ] ✅ Interval List Intersections `DSA150` · [ ] ⭐ Meeting Rooms II `DSA150` · [ ] 🚀 Minimum Interval to Include Each Query `DSA150`

**P8 Kadane**
- [ ] ⭐ Maximum Subarray `DSA150` · [ ] ⭐ Maximum Product Subarray `DSA150` · [ ] ✅ Maximum Sum Circular Subarray `LC`

**P9 Binary Search**
- [ ] ⭐ Binary Search `DSA150` · [ ] ⭐ Search Insert Position `LC` · [ ] ✅ Sqrt(x) `LC` · [ ] ⭐ First and Last Position `LC` · [ ] ⭐ Search a 2D Matrix `DSA150`
- [ ] ⭐ Find Minimum in Rotated Sorted Array `DSA150` · [ ] ⭐ Search in Rotated Sorted Array `DSA150` · [ ] ✅ Find Peak Element `DSA150` · [ ] ✅ Single Element in a Sorted Array `LC`
- [ ] ⭐ Koko Eating Bananas `DSA150` · [ ] ⭐ Capacity To Ship Packages `LC` · [ ] ✅ Min Days to Make m Bouquets `LC` · [ ] ✅ Magnetic Force Between Two Balls `LC`
- [ ] ⭐ Time Based Key-Value Store `DSA150` · [ ] ✅ Split Array Largest Sum `LC` · [ ] 🚀 Median of Two Sorted Arrays `DSA150`

**P10 Stack**
- [ ] ⭐ Valid Parentheses `DSA150` · [ ] ✅ Implement Queue using Stacks `LC` · [ ] ⭐ Min Stack `DSA150` · [ ] ⭐ Evaluate RPN `DSA150` · [ ] ✅ Next Greater Element I `LC`
- [ ] ⭐ Daily Temperatures `DSA150` · [ ] ✅ Next Greater Element II `LC` · [ ] ✅ Online Stock Span `LC` · [ ] ⭐ Asteroid Collision `DSA150` · [ ] ⭐ Decode String `DSA150`
- [ ] ⭐ Car Fleet `DSA150` · [ ] ✅ Remove K Digits `LC` · [ ] ✅ Basic Calculator II `LC` · [ ] ⭐ Largest Rectangle in Histogram `DSA150` · [ ] 🚀 Sum of Subarray Minimums `LC` · [ ] 🚀 Maximal Rectangle `LC`

**P11 Monotonic Deque**
- [ ] ⭐ Sliding Window Maximum `DSA150` · [ ] ✅ Longest Continuous Subarray With Abs Diff ≤ Limit `LC` · [ ] 🚀 Shortest Subarray with Sum at Least K `LC`

**P12 Linked List**
- [ ] ⭐ Reverse Linked List `DSA150` · [ ] ⭐ Merge Two Sorted Lists `DSA150` · [ ] ⭐ Linked List Cycle `DSA150` · [ ] ✅ Middle of the Linked List `LC`
- [ ] ✅ Palindrome Linked List `LC` · [ ] ✅ Intersection of Two Linked Lists `LC` · [ ] ⭐ Remove Nth Node From End `DSA150` · [ ] ✅ Linked List Cycle II `LC`
- [ ] ⭐ Reorder List `DSA150` · [ ] ⭐ Add Two Numbers `DSA150` · [ ] ⭐ Copy List with Random Pointer `DSA150` · [ ] ⭐ Find the Duplicate Number `DSA150`
- [ ] ⭐ LRU Cache `DSA150` · [ ] ✅ Sort List `LC` · [ ] ⭐ Merge K Sorted Lists `DSA150` · [ ] 🚀 Reverse Nodes in k-Group `DSA150`

**P13 Backtracking**
- [ ] ⭐ Subsets `DSA150` · [ ] ⭐ Combination Sum `DSA150` · [ ] ⭐ Permutations `DSA150` · [ ] ✅ Generate Parentheses `LC` · [ ] ⭐ Subsets II `DSA150`
- [ ] ⭐ Combination Sum II `DSA150` · [ ] ⭐ Letter Combinations of a Phone Number `DSA150` · [ ] ⭐ Word Search `DSA150` · [ ] ⭐ Palindrome Partitioning `DSA150` · [ ] ⭐ N-Queens `DSA150`

**P14 Trees**
- [ ] ⭐ Maximum Depth `DSA150` · [ ] ⭐ Invert Binary Tree `DSA150` · [ ] ⭐ Same Tree `DSA150` · [ ] ✅ Inorder Traversal (iterative) `LC` · [ ] ⭐ Diameter `DSA150`
- [ ] ⭐ Balanced Binary Tree `DSA150` · [ ] ⭐ Subtree of Another Tree `DSA150` · [ ] ✅ Path Sum `LC` · [ ] ⭐ Level Order Traversal `DSA150` · [ ] ⭐ Right Side View `DSA150`
- [ ] ⭐ Count Good Nodes `DSA150` · [ ] ✅ Zigzag Level Order `LC` · [ ] ✅ Path Sum II `LC` · [ ] ⭐ Validate BST `DSA150` · [ ] ⭐ Kth Smallest in BST `DSA150`
- [ ] ✅ LCA of a BST `LC` · [ ] ⭐ LCA of a Binary Tree `DSA150` · [ ] ⭐ Construct from Preorder & Inorder `DSA150` · [ ] ✅ House Robber III `LC`
- [ ] ⭐ Serialize a Binary Tree `DSA150` · [ ] ⭐ Binary Tree Maximum Path Sum `DSA150`

**P15 Tries**
- [ ] ⭐ Implement Trie `DSA150` · [ ] ✅ Longest Common Prefix `LC` · [ ] ⭐ Design Add and Search Words `DSA150` · [ ] ⭐ Word Search II `DSA150` · [ ] 🚀 Maximum XOR of Two Numbers `LC`

**P16 Heap**
- [ ] ⭐ Kth Largest Element in a Stream `DSA150` · [ ] ⭐ Last Stone Weight `DSA150` · [ ] ⭐ K Closest Points to Origin `DSA150` · [ ] ✅ Top K Frequent Words `LC`
- [ ] ✅ Kth Smallest Element in a Sorted Matrix `LC` · [ ] ⭐ Task Scheduler `DSA150` · [ ] ✅ Reorganize String `LC` · [ ] ✅ Design Twitter `LC`
- [ ] ⭐ Find Median from Data Stream `DSA150` · [ ] 🚀 IPO `LC`

**P17 Graphs**
- [ ] ✅ Flood Fill `LC` · [ ] ⭐ Number of Islands `DSA150` · [ ] ⭐ Max Area of Island `DSA150` · [ ] ⭐ Clone Graph `DSA150` · [ ] ✅ Number of Provinces `LC`
- [ ] ⭐ Rotting Oranges `DSA150` · [ ] ✅ 01 Matrix `LC` · [ ] ⭐ Pacific Atlantic Water Flow `DSA150` · [ ] ⭐ Surrounded Regions `DSA150` · [ ] ✅ Is Graph Bipartite? `LC`
- [ ] ⭐ Course Schedule `DSA150` · [ ] ⭐ Course Schedule II `DSA150` · [ ] ✅ Find Eventual Safe States `LC` · [ ] ⭐ Graph Valid Tree `DSA150`
- [ ] ⭐ Number of Connected Components `DSA150` · [ ] ⭐ Redundant Connection `DSA150` · [ ] ✅ Accounts Merge `LC` · [ ] ⭐ Word Ladder `DSA150` · [ ] 🚀 Critical Connections `LC`

**P18 Advanced Graphs**
- [ ] ⭐ Network Delay Time `DSA150` · [ ] ✅ Shortest Path in Binary Matrix `LC` · [ ] ⭐ Min Cost to Connect All Points `DSA150` · [ ] ⭐ Cheapest Flights Within K Stops `DSA150`
- [ ] ✅ Path With Minimum Effort `LC` · [ ] ✅ Find the City… Threshold Distance `LC` · [ ] ⭐ Swim in Rising Water `DSA150` · [ ] ⭐ Alien Dictionary `DSA150` · [ ] 🚀 Reconstruct Itinerary `DSA150`

**P19 Greedy**
- [ ] ✅ Assign Cookies `LC` · [ ] ✅ Lemonade Change `LC` · [ ] ⭐ Jump Game `DSA150` · [ ] ✅ Best Time to Buy and Sell Stock II `LC` · [ ] ⭐ Jump Game II `DSA150`
- [ ] ⭐ Gas Station `DSA150` · [ ] ⭐ Partition Labels `DSA150` · [ ] ⭐ Hand of Straights `DSA150` · [ ] ⭐ Valid Parenthesis String `DSA150`

**P20 Dynamic Programming**
- [ ] ⭐ Climbing Stairs `DSA150` · [ ] ✅ Fibonacci Number `LC` · [ ] ⭐ Min Cost Climbing Stairs `DSA150` · [ ] ⭐ House Robber `DSA150` · [ ] ⭐ House Robber II `DSA150`
- [ ] ⭐ Unique Paths `DSA150` · [ ] ✅ Minimum Path Sum `LC` · [ ] ✅ Unique Paths II `LC` · [ ] ⭐ Longest Palindromic Substring `DSA150` · [ ] ⭐ Palindromic Substrings `DSA150`
- [ ] ⭐ Decode Ways `DSA150` · [ ] ⭐ Coin Change `DSA150` · [ ] ⭐ Word Break `DSA150` · [ ] ⭐ Longest Increasing Subsequence `DSA150` · [ ] ⭐ Partition Equal Subset Sum `DSA150`
- [ ] ⭐ Coin Change II `DSA150` · [ ] ⭐ Target Sum `DSA150` · [ ] ⭐ Longest Common Subsequence `DSA150` · [ ] ⭐ Maximal Square `DSA150` · [ ] ⭐ Stock with Cooldown `DSA150`
- [ ] ⭐ Interleaving String `DSA150` · [ ] ✅ Longest Palindromic Subsequence `LC` · [ ] ⭐ Edit Distance `DSA150` · [ ] ⭐ Longest Increasing Path in a Matrix `DSA150`
- [ ] ✅ Distinct Subsequences `DSA150` · [ ] 🚀 Burst Balloons `DSA150` · [ ] 🚀 Minimum Cost to Cut a Stick `LC` · [ ] 🚀 Regular Expression Matching `DSA150`
- [ ] 🚀 Partition to K Equal Sum Subsets `LC` · [ ] 🚀 Count Numbers with Unique Digits `LC`

**P21 Bits**
- [ ] ⭐ Single Number `DSA150` · [ ] ⭐ Number of 1 Bits `DSA150` · [ ] ✅ Power of Two `LC` · [ ] ⭐ Counting Bits `DSA150` · [ ] ⭐ Reverse Bits `DSA150`
- [ ] ⭐ Missing Number `DSA150` · [ ] ✅ Hamming Distance `LC` · [ ] ✅ Single Number III `LC` · [ ] 🚀 Single Number II `LC` · [ ] ⭐ Sum of Two Integers `DSA150`

**P22 Matrix & Math**
- [ ] ✅ Pascal's Triangle `LC` · [ ] ⭐ Happy Number `DSA150` · [ ] ⭐ Rotate Image `DSA150` · [ ] ⭐ Spiral Matrix `DSA150` · [ ] ⭐ Set Matrix Zeroes `DSA150`
- [ ] ✅ Search a 2D Matrix II `LC` · [ ] ✅ Game of Life `LC` · [ ] ⭐ Pow(x, n) `DSA150` · [ ] ⭐ Multiply Strings `DSA150` · [ ] ✅ Count Primes `LC`

**P23 Cyclic Sort**
- [ ] ⭐ Find All Numbers Disappeared `LC` · [ ] ✅ Set Mismatch `LC` · [ ] ✅ Find All Duplicates in an Array `LC` · [ ] ⭐ First Missing Positive `LC`

**P24 Advanced**
- [ ] ✅ Find the Index of the First Occurrence (KMP) `LC` · [ ] ✅ Repeated DNA Sequences `LC` · [ ] ✅ Range Sum Query - Mutable `LC`
- [ ] 🚀 Shortest Palindrome `LC` · [ ] 🚀 Count of Smaller Numbers After Self `LC` · [ ] 🚀 Shortest Path Visiting All Nodes `LC` · [ ] 🚀 Numbers At Most N Given Digit Set `LC`

</details>

### If you only have limited time: the "⭐ only" path
Do every ⭐ problem in pattern order (~140 problems). Add ✅ problems only for patterns where your confidence is < 4/5.

---

## 7. Mastery & Spaced-Revision System

### 7.1 Solve status codes (use in trackers)
| Code | Meaning | Next action |
|---|---|---|
| 🟢 **I** | Independent: no hints, < target time | Revise at day 7, 30 |
| 🟡 **H** | Solved with hints (note which hint number) | Revise at day 1, 3, 7, 21 |
| 🔴 **E** | Needed the editorial | Re-solve **tomorrow** from scratch, then 3, 7, 21 |
| ⚫ **F** | Failed / gave up | Re-learn the pattern section first, then treat as E |

**Target times:** Easy 15 min · Medium 30 min · Hard 45 min (excluding reading).

### 7.2 Spaced revision schedule
Memory fades fast unless you retrieve it. Re-solving (not re-reading!) at increasing gaps locks it in:
```text
Day 0 (solve) → Day 1 → Day 3 → Day 7 → Day 21 → Day 60
```
- A revision = **re-derive and re-code from a blank file** without looking at your old code.
- If you fail a revision, reset that problem to Day 1.
- Revision time budget: first 15 minutes of every session (revisions come **before** new problems).

### 7.3 The 11-step mastery ladder (per pattern)
| Step | Activity | ✔ |
|---|---|---|
| 1 | Read the pattern section; derive the template on paper | ☐ |
| 2 | Solve the guided example with a dry-run table | ☐ |
| 3 | Solve one Easy independently | ☐ |
| 4 | Solve a second Easy (different variation) | ☐ |
| 5 | Solve one Medium (hints allowed) | ☐ |
| 6 | Solve another Medium without hints | ☐ |
| 7 | Re-solve step 5's problem after 3+ days | ☐ |
| 8 | Solve a similar problem with different wording | ☐ |
| 9 | Explain one solution out loud in 2 minutes (record yourself) | ☐ |
| 10 | Solve an **unseen** Medium of this pattern | ☐ |
| 11 | Pattern marked **MASTERED** | ☐ |

### 7.4 Mastery levels
| Level | Name | Definition |
|---|---|---|
| 0 | Not started | — |
| 1 | Learning | Read theory, solved guided examples |
| 2 | Practising | Easy independently, Medium with hints |
| 3 | Comfortable | Medium independently, can explain |
| 4 | Interview-ready | Unseen Medium < 30 min with clean explanation |
| 5 | Mastered | Recognises it inside mixed problems; handles follow-ups |

### 7.5 Mixed practice (from week 8 onward)
Once you've finished 4+ patterns, do **one random problem from a past pattern** daily *without knowing its pattern in advance*. Recognition is a separate skill from execution — this trains it.

---

## 8. Trackers

### 8.1 Pattern mastery tracker
| Pattern | Level (0–5) | Solved I/H/E | Weak points | Last revised | Next revision | Confidence (1–5) |
|---|---|---|---|---|---|---|
| P1 Arrays | | | | | | |
| P2 Hashing | | | | | | |
| P3 Two Pointers | | | | | | |
| P4 Sliding Window | | | | | | |
| P5 Prefix Sum | | | | | | |
| P6 Sorting | | | | | | |
| P7 Intervals | | | | | | |
| P8 Kadane | | | | | | |
| P9 Binary Search | | | | | | |
| P10 Stack | | | | | | |
| P11 Deque | | | | | | |
| P12 Linked List | | | | | | |
| P13 Backtracking | | | | | | |
| P14 Trees | | | | | | |
| P15 Tries | | | | | | |
| P16 Heap | | | | | | |
| P17 Graphs | | | | | | |
| P18 Adv. Graphs | | | | | | |
| P19 Greedy | | | | | | |
| P20 DP | | | | | | |
| P21 Bits | | | | | | |
| P22 Matrix/Math | | | | | | |
| P23 Cyclic Sort | | | | | | |
| P24 Advanced | | | | | | |

### 8.2 Question log (Markdown)
| Date | Problem | Pattern | Variation | Status (I/H#/E/F) | Time | Key insight (1 line) | Mistake | Next revision |
|---|---|---|---|---|---|---|---|---|
| 2026-11-12 | Two Sum | P2 | Complement | H1 | 18m | Store value→index, query before insert | Inserted before querying | 2026-11-13 |

### 8.3 Question log (CSV — paste into Google Sheets / Excel)
```csv
date,problem,source,link,pattern,variation,difficulty,status,hint_level,time_min,key_insight,mistake,rev1,rev2,rev3,rev4,confidence
2026-11-12,Two Sum,DSA150,https://dsacourse.com/top-150/two-sum,Hashing,Complement lookup,Easy,H,1,18,"value->index, query before insert","inserted before query",2026-11-13,2026-11-15,2026-11-19,2026-12-03,3
```
Useful sheet formulas: next revision `=A2+1`, `=A2+3`, `=A2+7`, `=A2+21`; conditional-format rows where the revision date ≤ `TODAY()`.

### 8.4 Mistake log (the most valuable file you'll keep)
| Date | Problem | Mistake type | What happened | Rule for the future |
|---|---|---|---|---|
| | | Off-by-one / wrong pattern / edge case / complexity / syntax | | |

Mistake types to tag: **Recognition** (picked wrong pattern) · **Logic** (right pattern, wrong idea) · **Edge case** · **Off-by-one** · **Complexity** (TLE) · **Python gotcha**. Review this log every Sunday — your mistakes repeat.

### 8.5 Daily log template
```markdown
## 2026-11-12  (Day 1)
- Revision: <problem> → pass/fail
- New: <problem> → status, time
- Insight of the day:
- Energy (1–5):
```

### 8.6 Weekly review template (Sunday, 20 minutes)
```markdown
## Week N review
- Patterns progressed: P? Level x → y
- Solved independently: _  | with hints: _ | editorial: _
- Revisions done / due: _ / _
- Top 3 mistakes this week (from mistake log):
- Weakest pattern → plan for next week:
- Interview confidence (1–5):
- One thing I'm proud of:
```

---

## 9. Interview Preparation

### 9.1 The 45-minute coding round, minute by minute
| Minutes | Phase | What you say / do |
|---|---|---|
| 0–5 | **Clarify** | Restate. Ask about input size, ranges, negatives, duplicates, sortedness, empty input, return format, multiple answers. |
| 5–8 | **Examples** | Walk a small example; propose an edge case. |
| 8–12 | **Brute force** | "The straightforward way is … O(n²). It works, but n is 10⁵, so let me optimise." |
| 12–18 | **Optimise** | Name the bottleneck → the pattern → the new algorithm. Get a nod before coding. |
| 18–33 | **Code** | Narrate intent, not keystrokes. Use clear names. |
| 33–40 | **Test** | Dry-run your example through *the code*. Then an edge case. Fix bugs calmly. |
| 40–45 | **Analyse & extend** | Time/space with reasons. Discuss follow-ups and trade-offs. |

### 9.2 Clarifying questions checklist
- What's the size of the input? Range of values? Can values be negative / zero?
- Is the input sorted? Can it contain duplicates?
- Can the input be empty? What should I return then?
- Is there always a valid answer? If multiple, return any or a specific one?
- Can I modify the input in place?
- Is it a stream (data arrives over time) or all at once?
- (Graphs) Directed? Weighted? Connected? Can there be self-loops/cycles?
- (Strings) Character set — lowercase only? Unicode? Case-sensitive?

### 9.3 Communication scripts

**Opening the brute force:**
> "Let me start with a simple correct approach so we have a baseline. I'd check every pair, which is O(n²) time and O(1) space."

**Moving to optimisation:**
> "The repeated work is that for each element I search the rest of the array. If I could answer 'have I seen the complement?' in O(1), the whole thing becomes linear — a hash map does that."

**Proving correctness:**
> "The invariant is: everything left of `write` is already in its final state. Each step preserves it, and when the loop ends, the whole array satisfies it."

**Complexity:**
> "Each index enters and leaves the window at most once, so although there's a nested while loop, total work is O(n). Space is O(k) for the window's character counts."

**When stuck (never go silent):**
> "I'm considering two directions — sorting, which costs O(n log n) but enables two pointers, or a hash map for O(n). Let me test the hash map idea on this example… Could I think out loud for a moment?"
>
> If truly stuck: "Could you give me a hint on whether I'm on the right track with X?" — asking well is a **positive** signal, not a failure.

**When you find a bug:**
> "My dry run shows `l` overshoots when the window becomes empty — I need `while` instead of `if` here. Let me fix that and re-trace."

### 9.4 Testing your code (in order)
1. The example from the problem.
2. Smallest input (empty / single element).
3. The tricky case you identified (duplicates, all negatives, target not found).
4. Large input — talk about it (performance), don't trace it.

### 9.5 Off-by-one detection checklist
- Loop bounds: `range(n)` vs `range(n-1)` vs `range(1, n)`?
- Inclusive or exclusive end? Window length `r − l + 1`.
- Binary search: `lo <= hi` or `lo < hi`? `hi = mid` or `mid − 1`?
- Prefix sums: `P[r+1] − P[l]`.
- DP tables of size `n+1`: `dp[i]` refers to `s[i−1]`.
- Reverse loops: `range(n−1, −1, −1)`.

### 9.6 Avoiding unnecessary complexity
- Don't use a heap when a single variable (running max) suffices.
- Don't sort if one pass works.
- Don't write a class when a function works (unless it's a design question).
- Prefer readable code over clever one-liners; interviewers grade clarity.

### 9.7 Pattern-wise conceptual interview questions (with short model answers)
| Question | Model answer |
|---|---|
| Why is hash lookup O(1) average but O(n) worst? | Collisions: many keys in one bucket; good hashing + resizing keep chains short on average. |
| When does sliding window fail? | When validity isn't monotonic (e.g., sums with negatives); use prefix sums + hash map. |
| Why move the shorter wall in Container With Most Water? | The shorter wall caps the area; moving the taller one only shrinks width without raising the cap. |
| How do you know binary search on answer applies? | Feasibility is monotonic in the candidate and checking one candidate is cheap. |
| Why is the monotonic stack O(n) with a nested loop? | Each element is pushed once and popped at most once. |
| BFS vs DFS for shortest path? | BFS explores by distance layers, so the first visit is shortest in unweighted graphs; DFS doesn't guarantee that. |
| Why does Dijkstra fail on negative edges? | A finalised node could later be improved through a negative edge, violating the greedy finalisation. |
| Memoisation vs tabulation? | Same complexity; memo is top-down and computes only needed states; tabulation avoids recursion depth and enables space optimisation. |
| How do you prove a greedy algorithm? | Exchange argument: transform any optimal solution into the greedy one without making it worse. |
| Heap vs sorting for top-k? | Heap O(n log k) with O(k) memory and works on streams; sorting O(n log n). |
| What's amortised complexity? | Average cost per operation over a sequence (e.g., list append is O(1) amortised despite occasional O(n) resizes). |

### 9.8 Mock interview exercises
Do each as a **timed 35-minute session**, speaking out loud (record on your phone). Then compare with the model outline.

**Mock 1 — Hashing (Easy → follow-up).** *Contains Duplicate → "Contains Duplicate within k indices".*
Model: set → O(n). Follow-up: sliding set of last k elements (or dict value → last index); check `i − last[x] ≤ k`.

**Mock 2 — Two Pointers.** *3Sum.*
Model: sort; fix i; two pointers on the rest; skip duplicates at both levels; O(n²) time, O(1) extra (excluding sort). Follow-up: 3Sum Closest — track best `|sum − target|`.

**Mock 3 — Sliding Window.** *Longest Substring with At Most K Distinct Characters.*
Model: Counter of window; shrink while `len(counter) > k`, deleting zero counts; answer `max(r − l + 1)`; O(n). Follow-up: "exactly K" = atMost(K) − atMost(K−1) (for counting).

**Mock 4 — Prefix Sum.** *Subarray Sum Equals K.*
Model: explain why window fails with negatives; prefix counts with `{0: 1}`; O(n)/O(n). Follow-up: longest such subarray → store first index.

**Mock 5 — Binary Search on Answer.** *Capacity To Ship Packages Within D Days.*
Model: range `[max(w), sum(w)]`; greedy `days_needed(cap)`; monotonic; first-True template; O(n log(sum)).

**Mock 6 — Stack.** *Daily Temperatures.*
Model: brute O(n²); decreasing stack of indices; each popped index gets `i − j`; O(n). Follow-up: circular version (2n loop).

**Mock 7 — Linked List / Design.** *LRU Cache.*
Model: dict key → node + doubly linked list with sentinels; get/put O(1); evict `tail.prev`. Follow-up: thread safety (lock around operations), TTL expiry — connect to your Redis experience.

**Mock 8 — Trees.** *Lowest Common Ancestor.*
Model: post-order returns found node; if both sides non-null → current node. O(n)/O(h). Follow-up: BST version O(h) using values; nodes may not exist → return counts.

**Mock 9 — Graphs.** *Course Schedule II.*
Model: nodes = courses, edge pre → course; Kahn's algorithm; return order or [] if cycle; O(V + E).

**Mock 10 — DP.** *Coin Change.*
Model: greedy counter-example; recursion `f(a) = 1 + min f(a − c)`; memo → table; O(amount · coins). Follow-up: count combinations (Coin Change II, loop order).

**Mock 11 — Heap.** *Find Median from Data Stream.*
Model: two heaps with size invariant; add O(log n), median O(1). Follow-up: if all numbers in [0, 100] → counting array; if 99% in range → counts + two overflow heaps.

**Mock 12 — Mixed (pattern unknown).** Ask a friend or an AI to give you a random Medium from the question bank without naming the pattern. Spend the first 3 minutes **only** on identification and justify it.

### 9.9 Backend-flavoured follow-ups (your edge as a backend developer)
Product companies love candidates who connect DSA to real systems:
- LRU Cache ↔ Redis eviction policies (`allkeys-lru`).
- Heap ↔ job schedulers, rate limiting by priority, Kafka consumer lag top-k.
- Sliding window ↔ rate limiters (fixed/sliding window counters).
- Consistent hashing ↔ hashing + sorted ring + binary search.
- Topological sort ↔ dependency resolution, migration ordering, task DAGs (Airflow).
- Trie ↔ autocomplete, route matching in web frameworks.
- DSU ↔ grouping duplicate accounts/entities.
- External sort / hash partitioning ↔ "data doesn't fit in memory" follow-ups.

---

## 10. Motivation & Consistency System

> Motivation is unreliable. **Systems** are reliable. This section is a system, not a pep talk.

### A. Small daily targets
Every day, pick **one** of these as "the win" (anything more is bonus):
- Learn one concept from a pattern section and derive its template on paper.
- Dry-run one example in a table.
- Solve one Easy problem.
- Re-solve one problem from the revision queue.
- Explain one solved problem out loud in 2 minutes.

### B. Minimum Viable Study Day
For tired, busy, or low-mood days. **30 minutes, no more required:**
```text
10 min  → re-solve (or re-read and re-derive) one problem from the revision queue
15 min  → attempt one Easy or continue yesterday's problem (no pressure to finish)
 5 min  → write 2 lines in the daily log: what you did + one insight
```
A minimum day **counts as a full day** for your streak. The goal is to never let the chain break twice in a row.

### C. Weekly progress (track these, not raw problem count)
- Patterns moved up a level
- Problems solved **independently** (🟢 I)
- Revisions completed vs due
- Weak areas (from mistake log)
- Interview confidence (1–5)

### D. Progress visualisation — mastery map
Update weekly. Use the levels from 7.4:
```text
Pattern          0   1   2   3   4   5
P2  Hashing      ■   ■   ■   ■   □   □    ← "Comfortable"
P3  Two Pointers ■   ■   ■   □   □   □
P4  Window       ■   ■   □   □   □   □
...
Interview-ready patterns: 1 / 24   →   Goal: 15+ at level 4 before applying widely
```
Seeing a pattern go from 1 → 4 is far more motivating (and meaningful) than "solved 87 questions".

### E. Anti-frustration rules
| Situation | Rule |
|---|---|
| **I can't solve a problem** | Follow the hint ladder (0.2). Being stuck for 25 minutes *is* the training — your brain is building the pattern. After the editorial, close it and code it yourself; mark 🔁. |
| **I repeatedly forget solutions** | You're memorising code, not ideas. Write a 1-line **key insight** for each problem ("store value→index, query before insert"). Re-derive from the insight, never from code. Follow the spaced schedule. |
| **I struggle with Mediums** | Normal for months 1–3. Mediums are 1–2 patterns + one twist. Go back to the pattern's Level 2–3 problems, then retry. Expect ~50% hint usage at first; it drops. |
| **I feel behind others** | Others post wins, not struggles. Compare only with your own last month's mastery map. Pattern depth beats problem count in interviews. |
| **I lost motivation** | Drop to Minimum Viable Days for a week. Don't add new patterns; just revise. Motivation returns *after* action, not before. |
| **I had a bad study day** | One bad day changes nothing. Log it ("energy 1/5"), do 10 minutes, and close the laptop. Tomorrow is a normal day. |
| **I've been reading editorials too much** | Rule for the next 7 days: no editorial before Hint 3 and 25 minutes. Do more Easies to rebuild independent wins. |
| **I'm stuck on a whole pattern** | Re-read its section C (intuition) and redo the guided example with a dry run. Then do only ⭐ Level 1–2 for that pattern for 3 days. |
| **Interview went badly** | Write the question + what went wrong in the mistake log within 24 hours. It becomes your most valuable practice problem. |

### F. Realistic expectations
- Weeks 1–4: most problems need hints. **This is the expected path**, not a sign you're bad at DSA.
- Weeks 5–10: Easies become routine; first independent Mediums appear.
- Weeks 11–20: you start recognising patterns within a minute; Mediums ~50–70% independent.
- Weeks 20+: interview-ready on most patterns; Hards remain hard for everyone.
- Consistency of **6 days/week at 60–90 minutes** beats weekend marathons every time.

### G. Session ritual (reduces start-up friction)
1. Same time daily (e.g., right after your system design hour, or before work).
2. Open the daily log → read yesterday's insight (1 min).
3. Do revisions first (warm-up wins).
4. New problem with a timer.
5. Log it. Stop on time — stopping while it's still interesting makes tomorrow easier to start.

---

## 11. Appendix: Cheat Sheets

### 11.1 Pattern one-liners
| Pattern | One-liner |
|---|---|
| Hashing | Replace an inner search loop with O(1) lookups |
| Two Pointers | Each move discards a provably useless candidate |
| Sliding Window | Contiguous + monotonic validity → expand right, shrink left |
| Prefix Sum | Range sum = difference of two cumulative sums |
| Difference Array | Range update = two point updates + prefix sum |
| Kadane | Extend the previous run or restart |
| Sorting | Preprocess so neighbours/greedy/two pointers become valid |
| Intervals | Sort by start to merge; by end to maximise non-overlap |
| Binary Search | Find the flip point of a monotonic condition |
| Stack | Most recent unfinished item first |
| Monotonic Stack | Each element waits for its next greater/smaller |
| Monotonic Deque | Window max/min, expire from the front |
| Linked List | Rewire carefully; dummy head; fast/slow |
| Backtracking | Choose → explore → unchoose |
| Trees | f(node) = combine(f(left), f(right)) |
| Trie | Shared prefixes share paths |
| Heap | Repeated min/max on changing data |
| BFS | Shortest path by layers (unweighted) |
| DFS | Explore everything reachable |
| Topo Sort | Remove nodes with zero prerequisites, repeatedly |
| DSU | Merge groups; same root = connected |
| Dijkstra | Expand closest node first (weights ≥ 0) |
| Greedy | Provably safe local choice |
| DP | State + transition + base; reuse subproblem answers |
| Bits | XOR cancels; `x & (x−1)` drops the lowest bit |
| Cyclic Sort | Values 1..n go to index value−1 |

### 11.2 Algorithm complexity reference
| Algorithm / operation | Time | Space |
|---|---|---|
| Binary search | O(log n) | O(1) |
| Sorting (Timsort / merge) | O(n log n) | O(n) |
| Quickselect | O(n) avg | O(1) |
| Heap push/pop | O(log n) | — |
| Heapify | O(n) | O(1) |
| BFS / DFS | O(V + E) | O(V) |
| Topological sort | O(V + E) | O(V) |
| Dijkstra (binary heap) | O((V + E) log V) | O(V + E) |
| Bellman-Ford | O(V · E) | O(V) |
| Floyd-Warshall | O(V³) | O(V²) |
| Kruskal | O(E log E) | O(V) |
| DSU op (path compression + rank) | ~O(1) amortised | O(V) |
| Trie insert/search | O(L) | O(total chars) |
| KMP | O(n + m) | O(m) |
| Fenwick / Segment tree op | O(log n) | O(n) |
| Subsets / permutations | O(n · 2ⁿ) / O(n · n!) | O(n) + output |

### 11.3 Python gotchas in interviews
| Gotcha | Fix |
|---|---|
| `[[0]*m]*n` shares rows | `[[0]*m for _ in range(n)]` |
| `res.append(path)` in backtracking | `res.append(path[:])` |
| `list.pop(0)` is O(n) | `deque.popleft()` |
| `x in list` is O(n) | Use a `set` |
| Max-heap | Push `-x` |
| Heap with uncomparable objects | `(priority, counter, obj)` |
| Integer division toward zero (RPN) | `int(a / b)`, not `a // b` |
| Recursion limit (~1000) | `sys.setrecursionlimit(10**6)` or iterative |
| Mutable default args `def f(x=[])` | Use `None` and create inside |
| String concatenation in loops | Collect in list, `"".join()` |
| `@cache` with list args | Convert to tuple or use indices |
| Floating-point ceil | `(a + b - 1) // b` |

### 11.4 The final checklist before any interview
- [ ] I can state the 15-step framework from memory.
- [ ] I can identify a pattern and **justify** it from structure, not keywords.
- [ ] I can write from scratch: binary search (both templates), sliding window, BFS, DFS, topological sort, DSU, Dijkstra, backtracking template, LRU cache, merge sort, quickselect, knapsack.
- [ ] I can explain amortised O(n) for sliding window and monotonic stack.
- [ ] I've done at least 8 timed mocks out loud.
- [ ] My mistake log has been reviewed this week.

---

> **Remember:** You're not trying to have seen every problem. You're becoming someone who can look at a problem they've never seen, ask *"what does the brute force waste?"*, and know which tool removes that waste. That skill is built one pattern, one dry run, and one honest attempt at a time. Start with [P1](#p1-array-fundamentals) today. 🚀
