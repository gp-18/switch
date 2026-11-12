# 🟢 Day 4.1 — Strings: Maximum Nesting Depth of the Parentheses

## 1. Maximum Nesting Depth of the Parentheses

A string `s` is a **valid parentheses string (VPS)** if it meets the following conditions:
1. It contains only digits `0-9`, arithmetic operators `+`, `-`, `*`, `/`, and parentheses `(`, `)`.
2. All parentheses are balanced and correctly nested.

Compute the **maximum nesting depth** of parentheses in `s`. The nesting depth is the highest number of parentheses that are open simultaneously at any point in the string.

You must write an algorithm that runs in $\mathcal{O}(N)$ time complexity.

### Example

```text
Input:  s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation:
The deepest nested sub-expression is ((8)/4), which sits inside 3 layers of open parentheses.

Input:  s = "(1)+((2))+(((3)))"
Output: 3
Explanation:
Digit '3' is enclosed inside 3 pairs of parentheses.

Input:  s = "()(())((()()))"
Output: 3

Input:  s = "1+2*3"  # Edge Case: No parentheses
Output: 0
```

### Think About

* **Tracking Nesting Depth Without a Stack ($\mathcal{O}(1)$ Space):**
  * Because `s` is guaranteed to be a valid parentheses string, we do not need a stack to track or match opening and closing bracket positions.
  * A single integer counter `depth` suffices to track how many parentheses are currently open at each character index.

* **Single Linear Scan Algorithm:**
  1. Initialize `depth = 0` and `max_depth = 0`.
  2. Traverse each character `c` in `s`:
     * **If `c == '('`:**
       * A new nesting layer opens: increment `depth += 1`.
       * Update peak depth encountered so far: `max_depth = max(max_depth, depth)`.
     * **Else if `c == ')'`:**
       * The innermost active layer closes: decrement `depth -= 1`.
     * **Other characters (digits, operators):**
       * Ignored, as they do not change the parenthesis nesting depth.
  3. Return `max_depth`.

* **Time Complexity:** $\mathcal{O}(N)$
  * Single pass over all $N$ characters in `s`.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

**File:** [01.py](../../code/sprint-7/day_4_1/01.py)
