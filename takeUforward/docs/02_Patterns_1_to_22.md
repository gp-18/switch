# Pattern Printing: Questions 1 to 22 (Python)

Source: Striver's A2Z DSA Sheet (takeuforward). This README has the **notes first**, then **only the questions**. Solve every pattern yourself.

---

## Table of Contents
- [Notes: How to Think](#notes-how-to-think)
- [Row-Formula Cheat Sheet](#row-formula-cheat-sheet)
- [Traps and Checklist](#traps-and-checklist)
- [Interview Notes](#interview-notes)
- [Questions: Pattern 1 to 22](#questions)
- [Progress Tracker](#progress-tracker)

---

# Notes: How to Think

## The Universal Method (works for every pattern)

```
[Count rows] -> [Per row: spaces / content / spaces as f(i)]
   -> [One inner loop per part] -> [Dry-run i=0, i=last, N=1]
```

1. **Rows:** find how many rows there are. It is usually `N`, `2N`, or `2N-1`.
2. **Row table:** draw the pattern and write, for row `i`, how many leading spaces, how many content items, and how many trailing spaces.
3. **Content rule:** decide what is printed at column `j`. It could be `*`, `j+1`, `i+1`, a letter, or a value that depends on `min(i, j, ...)`.
4. **Loops:** one outer loop for rows, one inner loop per part of the row, then `print()`.
5. **Verify:** check the first row, the last row and `N=1`. If the formula holds there, it holds for every `N`.

## Python Basics for Patterns

- `print(x, end="")` stays on the same line. `print()` moves to the next line.
- `"*" * k` repeats a string `k` times. If `k <= 0` it gives an empty string.
- Letters: `chr(ord('A') + k)` gives the k-th letter (0-indexed).
- Use **0-indexed** `i`, and convert to 1-indexed only inside the formula.
- Width of a centered shape is constant: `spaces + content + spaces = constant`.

## Three Ideas That Solve Most Patterns

| Idea | Meaning | Used in |
|------|---------|---------|
| Row formula | Count of spaces/stars is a function of `i` | 1 to 11, 12 to 18 |
| Symmetry / mirror | Second half mirrors the first, so reuse the formula | 9, 10, 17, 19, 20, 22 |
| Distance from border | Value at (i, j) = based on distance to the nearest edge | 21, 22 |

---

# Row-Formula Cheat Sheet

`i` is the 0-indexed row, `j` is the 0-indexed column, `N` is the input.

| Pattern | Rows | Per-row idea |
|---|---|---|
| 1 | N | N stars |
| 2 | N | i+1 stars |
| 3 | N | numbers 1 to i+1 |
| 4 | N | number (i+1) printed i+1 times |
| 5 | N | N-i stars |
| 6 | N | numbers 1 to N-i |
| 7 | N | spaces N-i-1, stars 2i+1 |
| 8 | N | spaces i, stars 2N-2i-1 |
| 9 | 2N | Pattern 7 followed by Pattern 8 |
| 10 | 2N-1 | stars i+1 if i<N else 2N-1-i |
| 11 | N | i+1 values, alternate 1/0, start = 1 if i is even |
| 12 | N | numbers 1 to i+1, spaces 2(N-i-1), numbers i+1 to 1 |
| 13 | N | keep a running counter that never resets |
| 14 | N | letters 'A' to (i+1)th letter |
| 15 | N | letters 'A' to (N-i)th letter |
| 16 | N | (i+1)th letter repeated i+1 times |
| 17 | N | spaces N-i-1, ascending letters, then descending letters (2i+1 total) |
| 18 | N | letters from (N-i-1)th letter up to the Nth letter |
| 19 | 2N | stars N-i, spaces 2i, stars N-i (top half), then mirror |
| 20 | 2N-1 | stars, spaces, stars, with i+1 stars on each side (top half), then mirror |
| 21 | N | print `*` on the border, space inside |
| 22 | 2N-1 | value = N - min(distance to any of the 4 edges) |

---

# Traps and Checklist

## Common Mistakes
- Forgetting `print()` after the inner loop, so all rows merge into one line.
- Off-by-one: `range(i)` vs `range(i+1)`.
- Mixing 0-indexed and 1-indexed `i` inside one formula.
- Diamond: using 2N rows when 2N-1 is needed, or repeating the middle row.
- Not testing `N=1` (and `N=2`).
- Letters: going past `'Z'` when `N` is large.
- Pattern 13: resetting the counter every row instead of keeping it global.
- Pattern 22: computing the distance from only one or two edges instead of all four.

## Before You Submit
- [ ] Rows correct (`N`, `2N`, or `2N-1`)?
- [ ] Spaces plus content give the same width in every row?
- [ ] First row, last row and `N=1` checked by hand?
- [ ] Trailing spaces match what the judge expects?

## Complexity (all patterns)
- **Time:** O(N^2), because about N^2 characters are printed.
- **Space:** O(1) extra (one row string is O(N)).
- This is optimal, because the output itself is O(N^2).

---

# Interview Notes

- Pattern questions are a **warm-up** for loop logic, dry-running and edge cases. They rarely come alone at 3.5 years, but they tell the interviewer how you think.
- Say the row formula out loud **before** writing code. It shows structure in your thinking.
- Dry-run `i=0`, `i=last` and `N=1` in front of the interviewer.
- Know both styles: nested loops (clear) and string multiplication (short).
- Be ready for a follow-up: "make it hollow", "make it work with letters", "reduce to one loop".
- The same row/column index logic is used in matrix traversal, spiral order and diagonal problems.

---

# Questions

> Examples use N = 4 unless stated. Print exactly the shape shown for the given N.

## Pattern 1: Square of Stars
Print an N x N square of stars.
```
****
****
****
****
```
[Practice](https://takeuforward.org/practice/dsa/pattern-1)

## Pattern 2: Right-Angled Triangle of Stars
```
*
**
***
****
```
[Practice](https://takeuforward.org/practice/dsa/pattern-2)

## Pattern 3: Right-Angled Triangle of Numbers
```
1
12
123
1234
```
[Practice](https://takeuforward.org/practice/dsa/pattern-3)

## Pattern 4: Row Number Repeated
```
1
22
333
4444
```
[Practice](https://takeuforward.org/practice/dsa/pattern-4)

## Pattern 5: Inverted Right-Angled Triangle of Stars
```
****
***
**
*
```
[Practice](https://takeuforward.org/practice/dsa/pattern-5)

## Pattern 6: Inverted Right-Angled Triangle of Numbers
```
1234
123
12
1
```
[Practice](https://takeuforward.org/practice/dsa/pattern-6)

## Pattern 7: Star Pyramid
```
   *
  ***
 *****
*******
```
[Practice](https://takeuforward.org/practice/dsa/pattern-7)

## Pattern 8: Inverted Star Pyramid
```
*******
 *****
  ***
   *
```
[Practice](https://takeuforward.org/practice/dsa/pattern-8)

## Pattern 9: Diamond Star Pattern
```
   *
  ***
 *****
*******
*******
 *****
  ***
   *
```
[Practice](https://takeuforward.org/practice/dsa/pattern-9)

## Pattern 10: Half Diamond Star Pattern
```
*
**
***
****
***
**
*
```
[Practice](https://takeuforward.org/practice/dsa/pattern-10)

## Pattern 11: Binary Number Triangle
```
1
01
101
0101
```
[Practice](https://takeuforward.org/practice/dsa/pattern-11)

## Pattern 12: Number Crown
```
1      1
12    21
123  321
12344321
```
[Practice](https://takeuforward.org/practice/dsa/pattern-12)

## Pattern 13: Increasing Number Triangle
```
1
2 3
4 5 6
7 8 9 10
```
[Practice](https://takeuforward.org/practice/dsa/pattern-13)

## Pattern 14: Increasing Letter Triangle
```
A
AB
ABC
ABCD
```
[Practice](https://takeuforward.org/practice/dsa/pattern-14)

## Pattern 15: Reverse Letter Triangle
```
ABCD
ABC
AB
A
```
[Practice](https://takeuforward.org/practice/dsa/pattern-15)

## Pattern 16: Alpha-Ramp Pattern
```
A
BB
CCC
DDDD
```
[Practice](https://takeuforward.org/practice/dsa/pattern-16)

## Pattern 17: Alpha-Hill Pattern
```
   A
  ABA
 ABCBA
ABCDCBA
```
[Practice](https://takeuforward.org/practice/dsa/pattern-17)

## Pattern 18: Alpha-Triangle Pattern
```
D
CD
BCD
ABCD
```
[Practice](https://takeuforward.org/practice/dsa/pattern-18)

## Pattern 19: Symmetric-Void Pattern (N = 5)
```
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
```
[Practice](https://takeuforward.org/practice/dsa/pattern-19)

## Pattern 20: Symmetric-Butterfly Pattern (N = 5)
```
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
```
[Practice](https://takeuforward.org/practice/dsa/pattern-20)

## Pattern 21: Hollow Rectangle Pattern
Print an N x N rectangle that is filled with stars only on the border.
```
****
*  *
*  *
****
```
[Practice](https://takeuforward.org/practice/dsa/pattern-21)

## Pattern 22: The Number Pattern (Concentric Squares)
Print a (2N-1) x (2N-1) grid where the outermost layer is N and the value decreases by 1 each layer inward, ending with 1 in the center.
```
4444444
4333334
4322234
4321234
4322234
4333334
4444444
```
[Practice](https://takeuforward.org/practice/dsa/pattern-22)

---

