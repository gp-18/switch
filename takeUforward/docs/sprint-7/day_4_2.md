# 🟢 Day 4.2 — Strings: Roman to Integer

## 1. Roman to Integer

Roman numerals are represented by seven different symbols:

| Symbol | `I` | `V` | `X` | `L` | `C` | `D` | `M` |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Value** | 1 | 5 | 10 | 50 | 100 | 500 | 1000 |

Roman numerals are usually written largest to smallest from left to right. However, when a smaller numeral is placed immediately before a larger one, it indicates **subtraction**:
* `I` before `V` (5) and `X` (10) $\rightarrow$ `4` and `9`
* `X` before `L` (50) and `C` (100) $\rightarrow$ `40` and `90`
* `C` before `D` (500) and `M` (1000) $\rightarrow$ `400` and `900`

Given a valid Roman numeral string `s` in the range $[1, 3999]$, convert it to an integer.

You must write an algorithm that runs in $\mathcal{O}(N)$ time complexity.

### Example

```text
Input:  s = "III"
Output: 3
Explanation: III = 1 + 1 + 1 = 3.

Input:  s = "XLII"
Output: 42
Explanation: XL = 40 (50 - 10), II = 2 -> 40 + 2 = 42.

Input:  s = "DCCCXC"
Output: 890
Explanation: D = 500, CCC = 300, XC = 90 (100 - 10) -> 500 + 300 + 90 = 890.

Input:  s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90, IV = 4 -> 1000 + 900 + 90 + 4 = 1994.
```

### Think About

* **The Lookahead Rule (Subtract vs. Add):**
  * Normally, symbols appear in descending order left-to-right, so each symbol's value is simply added to the running total.
  * Whenever a symbol has a **strictly smaller value than the symbol immediately after it**, it forms a subtractive pair (e.g. `IV`, `IX`, `XL`, `XC`, `CD`, `CM`).
  * Instead of special-casing two-character pairs, compare `mp[s[i]]` against `mp[s[i + 1]]`:
    * If `mp[s[i]] < mp[s[i + 1]]`: **subtract** `mp[s[i]]` from `total`.
    * Otherwise: **add** `mp[s[i]]` to `total`.
  * **Example Trace (`"MCMXCIV"`):**
    * `M` (`1000 >= 100`): `+1000`
    * `C` (`100 < 1000`): `-100`
    * `M` (`1000 >= 10`): `+1000` *(net `CM` = `-100 + 1000 = +900`)*
    * `X` (`10 < 100`): `-10`
    * `C` (`100 >= 1`): `+100` *(net `XC` = `-10 + 100 = +90`)*
    * `I` (`1 < 5`): `-1`
    * `V` (last char): `+5` *(net `IV` = `-1 + 5 = +4`)*
    * Total = `1994`.

* **Step-by-Step Algorithm:**
  1. Create a constant lookup dictionary `mp = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}`.
  2. Initialize `total = 0`.
  3. Traverse `i` from `0` to `len(s) - 1`:
     * If `i + 1 < len(s)` and `mp[s[i]] < mp[s[i + 1]]`:
       `total -= mp[s[i]]`
     * Else:
       `total += mp[s[i]]`
  4. Return `total`.

* **Time Complexity:** $\mathcal{O}(N)$
  * Single pass over the string of length $N$ ($N \le 15$), with $\mathcal{O}(1)$ dictionary lookups.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space — Fixed 7-entry symbol map.

**File:** [01.py](../../code/sprint-7/day_4_2/01.py)
