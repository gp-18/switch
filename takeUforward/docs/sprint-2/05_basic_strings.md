# 🟢 LEVEL 1 — Basic Traversals & Character Counting

## 1. Reverse a String

Given a string `s`, return a new string with its characters reversed.

### Example

```text
Input:  s = 'hello'
Output: 'olleh'
```

### Think About

* Can you solve this using Python slicing `s[::-1]`?
* How would you solve this iteratively using a two-pointer approach or building a list?

**File:** `01.py`

---

## 2. Count Vowels and Consonants

Given a string `s`, count the total number of vowels ('a', 'e', 'i', 'o', 'u', case-insensitive) and consonants (alphabetic characters that are not vowels). Ignore digits, spaces, and special characters.

### Example

```text
Input:  s = 'takeuforward'
Output: {'vowels': 5, 'consonants': 7}
```

### Think About

* Use a set of vowels `{'a', 'e', 'i', 'o', 'u'}` for O(1) lookup.
* Use `ch.isalpha()` before categorizing characters.

**File:** `02.py`

---

## 3. Count Uppercase and Lowercase Characters

Given a string `s`, count the number of uppercase English letters and lowercase English letters.

### Example

```text
Input:  s = 'Hello World'
Output: {'uppercase': 2, 'lowercase': 8}
```

### Think About

* Use `ch.isupper()` and `ch.islower()` methods.
* Ignore characters that are not alphabetic.

**File:** `03.py`

---

## 4. Count Digits in a String

Given a string `s`, count how many characters are numeric digits ('0'-'9').

### Example

```text
Input:  s = 'user123abc45'
Output: 5  # Digits: 1, 2, 3, 4, 5
```

### Think About

* Use `ch.isdigit()` or check `'0' <= ch <= '9'`.
* Increment a counter whenever a digit is found.

**File:** `04.py`

---

## 5. Count Words in a String

Given a string `s`, count the total number of words separated by one or more spaces.

### Example

```text
Input:  s = 'The quick brown fox'
Output: 4
```

### Think About

* Use `s.split()` which automatically handles multiple consecutive spaces and leading/trailing spaces.
* The length of the resulting list gives the word count.

**File:** `05.py`

---

# 🟢 LEVEL 2 — Character Transformations & Checks

## 6. Toggle Case of Each Character

Given a string `s`, convert all lowercase letters to uppercase and all uppercase letters to lowercase. Non-alphabetic characters should remain unchanged.

### Example

```text
Input:  s = 'Hello World'
Output: 'hELLO wORLD'
```

### Think About

* Use `ch.swapcase()` or check `ch.islower()` / `ch.isupper()` manually.
* Construct the resulting string using `"".join(...)`.

**File:** `06.py`

---

## 7. Palindrome Check

Given a string `s`, return True if the string reads the same backward as forward, otherwise False (exact match, case-sensitive).

### Example

```text
Input:  s = 'racecar'
Output: True
```

### Think About

* Compare `s` with `s[::-1]`.
* Alternatively, use two pointers comparing characters from outside inward.

**File:** `07.py`

---

## 8. Remove All Spaces from a String

Given a string `s`, remove every space character from the string and return the result.

### Example

```text
Input:  s = 'take u forward'
Output: 'takeuforward'
```

### Think About

* Use `s.replace(' ', '')` or `"".join(s.split(' '))`.
* Or filter characters with a list comprehension: `[c for c in s if c != ' ']`.

**File:** `08.py`

---

## 9. Length of Last Word

Given a string `s` consisting of words and spaces, return the length of the last word in the string.

### Example

```text
Input:  s = 'Hello World'
Output: 5  # Last word is 'World'
```

### Think About

* Strip trailing whitespace with `s.rstrip()`.
* Scan backward from the end until reaching a space or the beginning of the string.

**File:** `09.py`

---

## 10. Count Occurrences of a Character in a String

Given a string `s` and a character `ch`, count how many times `ch` appears in `s`.

### Example

```text
Input:  s = 'programming', ch = 'm'
Output: 2
```

### Think About

* Traverse through `s` and increment a counter when character matches `ch`.
* Or use Python's built-in `s.count(ch)`.

**File:** `10.py`

---

# 🟡 LEVEL 3 — Word & Digit Manipulation

## 11. Swap First and Last Character

Given a string `s`, swap its first and last characters and return the modified string.

### Example

```text
Input:  s = 'hello'
Output: 'oellh'
```

### Think About

* If `len(s) <= 1`, the string remains unchanged.
* Otherwise, slice as `s[-1] + s[1:-1] + s[0]`.

**File:** `11.py`

---

## 12. Reverse Words in a String

Given an input string `s`, reverse the order of the words. Return a string of the words in reverse order joined by a single space, removing leading, trailing, and multiple spaces between words.

### Example

```text
Input:  s = 'the sky is blue'
Output: 'blue is sky the'
```

### Think About

* Use `s.split()` to extract words without redundant spaces.
* Reverse the list of words and join with `' '.join(...)`.

**File:** `12.py`

---

## 13. Largest Odd Number in a String

Given a string `num` representing a large integer, return the largest-valued odd integer (as a substring) that is a non-empty substring of `num`, or an empty string `""` if no odd integer exists.

### Example

```text
Input:  num = '52'
Output: '5'
```

### Think About

* Any prefix ending with an odd digit is an odd integer.
* Traverse from the end toward the start: the first odd digit you see gives the longest prefix `num[:i+1]`.

**File:** `13.py`

---

## 14. Remove Vowels from a String

Given a string `s`, remove all vowel characters ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U') and return the remaining string.

### Example

```text
Input:  s = 'takeuforward'
Output: 'tkfrwrd'
```

### Think About

* Use a set of vowels `set('aeiouAEIOU')`.
* Build a list of characters not in the vowels set and join.

**File:** `14.py`

---

## 15. Check if String Contains Only Digits

Given a string `s`, return True if the string contains only numeric digit characters ('0'-'9') and is non-empty, otherwise False.

### Example

```text
Input:  s = '12345'
Output: True
```

### Think About

* Check `s.isdigit()` and ensure `len(s) > 0`.
* Remember signs like '-' or decimal points '.' are not digits.

**File:** `15.py`

---

# 🟡 LEVEL 4 — Slicing, Patterns & Transformations

## 16. Reverse a String II

Given a string `s` and an integer `k`, reverse the first `k` characters for every `2k` characters counting from the start of the string.

### Example

```text
Input:  s = 'abcdefg', k = 2
Output: 'bacdfeg'
```

### Think About

* Convert the string to a list of characters.
* Iterate `i` in steps of `2k`: reverse the slice from `i` to `i + k`.

**File:** `16.py`

---

## 17. Valid Anagram

Given two strings `s` and `t`, return True if `t` is an anagram of `s` (contains the exact same characters with the same frequencies), and False otherwise.

### Example

```text
Input:  s = 'anagram', t = 'nagaram'
Output: True
```

### Think About

* If `len(s) != len(t)`, return False immediately.
* Compare frequency counters or sorted lists: `sorted(s) == sorted(t)`.

**File:** `17.py`

---

## 18. Longest Common Prefix

Find the longest common prefix string amongst an array of strings `strs`. If there is no common prefix, return an empty string `""`.

### Example

```text
Input:  strs = ['flower', 'flow', 'flight']
Output: 'fl'
```

### Think About

* Take the first string as the initial prefix.
* Compare with each subsequent string, trimming the prefix from the end until it matches.

**File:** `18.py`

---

## 19. Isomorphic Strings

Two strings `s` and `t` are isomorphic if characters in `s` can be replaced to get `t`, preserving character order and maintaining a one-to-one character mapping.

### Example

```text
Input:  s = 'egg', t = 'add'
Output: True  # 'e' -> 'a', 'g' -> 'd'
```

### Think About

* Use two hash maps `map_s_to_t` and `map_t_to_s` to enforce bijection.
* Check that mapping consistency holds at every index.

**File:** `19.py`

---

## 20. Rotate String

Given two strings `s` and `goal`, return True if and only if `s` can become `goal` after some number of cyclic shifts.

### Example

```text
Input:  s = 'abcde', goal = 'cdeab'
Output: True
```

### Think About

* If `len(s) != len(goal)`, return False.
* `goal` must be a substring of `s + s`.

**File:** `20.py`

---

# 🟠 LEVEL 5 — Frequency, Sets & Substrings

## 21. Sort Characters by Frequency

Given a string `s`, sort the characters in decreasing order based on the frequency of each character. Return the sorted string.

### Example

```text
Input:  s = 'tree'
Output: 'eert'  # ('eetr' is also valid)
```

### Think About

* Count frequencies using `Counter(s)` or a dictionary.
* Sort items by frequency descending, then construct each character repeated by its count: `char * count`.

**File:** `21.py`

---

## 22. Check if a String is a Pangram

A pangram is a sentence where every letter of the English alphabet appears at least once. Return True if the given string `s` is a pangram (case-insensitive), otherwise False.

### Example

```text
Input:  s = 'thequickbrownfoxjumpsoverthelazydog'
Output: True
```

### Think About

* Convert string to lowercase and collect unique alphabetic characters in a set.
* Check if the size of the set is 26.

**File:** `22.py`

---

## 23. First Unique Character in a String

Given a string `s`, find the first non-repeating character and return its index. If it does not exist, return -1.

### Example

```text
Input:  s = 'leetcode'
Output: 0  # 'l' is at index 0
```

### Think About

* Build character frequency map in first pass.
* In second pass, return the index of the first character with `freq[c] == 1`.

**File:** `23.py`

---

## 24. Print All Substrings of a String

Given a string `s`, generate and return all contiguous substrings of `s`.

### Example

```text
Input:  s = 'abc'
Output: ['a', 'ab', 'abc', 'b', 'bc', 'c']
```

### Think About

* Use two nested loops: outer loop for start index `i`, inner loop for end index `j`.
* Extract substring using slicing `s[i:j]`.

**File:** `24.py`

---

## 25. Remove Outermost Parentheses

A valid parentheses string is decomposed into primitive parts. Return the string after removing the outermost parentheses of every primitive part.

### Example

```text
Input:  s = '(()())(())'
Output: '()()()'
```

### Think About

* Track an open parentheses counter `opened`.
* When encountering '(', include it in output only if `opened > 0`, then increment `opened`.
* When encountering ')', decrement `opened`, and include it in output only if `opened > 0`.

**File:** `25.py`

---

# 🔴 LEVEL 6 — Advanced Palindromes & Parentheses

## 26. Longest Word in a Sentence

Given a sentence string `s`, find and return the word with the maximum length. If there is a tie, return the first occurring longest word.

### Example

```text
Input:  s = 'The quick brown fox jumped over the lazy dog'
Output: 'jumped'
```

### Think About

* Split `s` into words using `s.split()`.
* Use `max(words, key=len)` to find the longest word (Python's `max` preserves first occurrence on ties).

**File:** `26.py`

---

## 27. Find the Index of the First Occurrence in a String

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or -1 if `needle` is not part of `haystack`.

### Example

```text
Input:  haystack = 'sadbutsad', needle = 'sad'
Output: 0
```

### Think About

* Check slices of length `len(needle)` across `haystack` from index `0` to `len(haystack) - len(needle)`.
* Alternatively, use `haystack.find(needle)`.

**File:** `27.py`

---

## 28. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters to lowercase and removing all non-alphanumeric characters, it reads the same forward and backward. Return True if `s` is a valid palindrome, otherwise False.

### Example

```text
Input:  s = 'A man, a plan, a canal: Panama'
Output: True  # 'amanaplanacanalpanama'
```

### Think About

* Filter characters with `[c.lower() for c in s if c.isalnum()]`.
* Compare the filtered list with its reverse.

**File:** `28.py`

---

## 29. Maximum Nesting Depth of the Parentheses

Given a valid parentheses string `s`, return the maximum nesting depth of parentheses in `s`.

### Example

```text
Input:  s = '(1+(2*3)+((8)/4))+1'
Output: 3
```

### Think About

* Keep a running `current_depth` counter and `max_depth`.
* Increment on '(', update `max_depth = max(max_depth, current_depth)`, and decrement on ')'.

**File:** `29.py`

---

## 30. Reverse Vowels of a String

Given a string `s`, reverse only all the vowels in the string and return it. The vowels are 'a', 'e', 'i', 'o', and 'u' in both lower and upper cases.

### Example

```text
Input:  s = 'IceCreAm'
Output: 'AceCreIm'
```

### Think About

* Convert `s` to a list of characters.
* Use two pointers `left` and `right`. Move `left` forward until it points to a vowel, and move `right` backward until it points to a vowel, then swap.

**File:** `30.py`
