# 🟢 Day 3.1 — Strings: Remove Outermost Parentheses

## 1. Remove Outermost Parentheses

A valid parentheses string is defined recursively by the following rules:
1. `""` (empty string) is valid.
2. If `A` is valid, then `"(" + A + ")"` is valid.
3. If `A` and `B` are valid, then `A + B` is valid.

A **primitive** valid parentheses string is a non-empty valid string that cannot be split into two or more non-empty valid parentheses strings.

Given a valid parentheses string `s`, consider its primitive decomposition:
$$s = P_1 + P_2 + \dots + P_k$$
where each $P_i$ is a primitive valid parentheses string.

Return `s` after **removing the outermost parentheses of every primitive string** $P_i$ in its decomposition.

You must write an algorithm that runs in $\mathcal{O}(N)$ time complexity.

### Example

```text
Input:  s = "((()))"
Output: "(())"
Explanation:
The string is a single primitive: "((()))".
Removing its outermost '(' and ')' yields "(())".

Input:  s = "()(()())(())"
Output: "()()()"
Explanation:
Primitive decomposition: "()" + "(()())" + "(())"
Removing outermost parentheses of each primitive:
"" + "()()" + "()" = "()()()".

Input:  s = "()(())((()))"
Output: "()(())"
Explanation:
Primitive decomposition: "()" + "(())" + "((()))"
Removing outermost parentheses: "" + "()" + "(())" = "()(())".

Input:  s = "()()"  # Edge Case: Only depth-1 primitives
Output: ""
Explanation:
Primitive decomposition: "()" + "()" -> "" + "" = "".
```

### Think About

* **Tracking Nesting Depth with a Balance Counter ($\mathcal{O}(1)$ Auxiliary State):**
  * We don't need an explicit stack because there is only one type of bracket (`'('` and `')'`).
  * A single integer `balance` tracks our current nesting depth:
    * `'('` opens a level (`balance += 1`).
    * `')'` closes a level (`balance -= 1`).
  * Whenever `balance` transitions from `0 -> 1`, we just encountered the **outermost opening `'('`** of a new primitive.
  * Whenever `balance` transitions from `1 -> 0`, we just encountered the **outermost closing `')'`** of the current primitive.
  * Every character encountered while `balance` remains strictly inside ($> 0$) belongs to the inner content and must be preserved!

* **Order of Operations (Check Before vs. After Update):**
  * **For an opening `'('`:**
    1. Check `if balance > 0:` $\rightarrow$ append `'('` (skip if `balance == 0`, because it's the outermost opener).
    2. Increment `balance += 1`.
  * **For a closing `')'`:**
    1. Decrement `balance -= 1` first.
    2. Check `if balance > 0:` $\rightarrow$ append `')'` (skip if `balance` just dropped to `0`, because it's the outermost closer).

* **Python String Construction Tip ($\mathcal{O}(N)$ vs $\mathcal{O}(N^2)$):**
  * Strings in Python are immutable, so appending directly via `ans += char` inside a loop can incur quadratic $\mathcal{O}(N^2)$ copy overhead.
  * Accumulate characters into a list `res = []` and execute `''.join(res)` once at the end for guaranteed $\mathcal{O}(N)$ runtime.

* **Time Complexity:** $\mathcal{O}(N)$
  * Single linear pass across all $N$ characters of `s`.
* **Space Complexity:** $\mathcal{O}(N)$
  * Required to build and store the returned result string (additional auxiliary space excluding the output buffer is $\mathcal{O}(1)$).

**File:** [01.py](../../code/sprint-7/day_3_1/01.py)
