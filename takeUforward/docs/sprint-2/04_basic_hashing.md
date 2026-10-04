# 🟢 LEVEL 1 — Number Frequencies & Extremes

## 1. Counting Frequencies of Array Elements

Given an array `nums` of integers, count and return the frequency of each distinct element using a hash map or dictionary.

### Example

```text
Input:  nums = [1, 2, 2, 3, 3, 3]
Output: {1: 1, 2: 2, 3: 3}
```

### Think About

* How do you initialize a hash map (dictionary) in Python?
* For each element `x` in `nums`, update its count with `freq[x] = freq.get(x, 0) + 1`.

**File:** `01.py`

---

## 2. Highest Occurring Element in an Array

Given an array `nums` of integers, find and return the element that appears the most number of times (has the maximum frequency). If there is a tie, return the smaller element.

### Example

```text
Input:  nums = [1, 3, 2, 1, 4, 1]
Output: 1  # Frequency is 3
```

### Think About

* Count frequencies using a dictionary or Counter.
* Iterate through the frequency map to find the key with maximum count, breaking ties by choosing the minimum key.

**File:** `02.py`

---

## 3. Second Highest Occurring Element

Given an array `nums`, find and return the element with the second highest frequency. If multiple elements have the same second highest frequency, return the smaller element (or -1 if no second highest exists).

### Example

```text
Input:  nums = [1, 2, 2, 3, 3, 3]
Output: 2  # Frequencies: 3 -> 3, 2 -> 2, 1 -> 1
```

### Think About

* Find all distinct frequencies and identify the second highest frequency value.
* Find elements matching this second highest frequency and return the smallest one.

**File:** `03.py`

---

## 4. Sum of Highest and Lowest Frequency

Given an array `nums`, find the highest frequency and the lowest frequency among all distinct elements, and return their sum.

### Example

```text
Input:  nums = [1, 2, 2, 3, 3, 3]
Output: 4  # Highest freq = 3 (for 3), Lowest freq = 1 (for 1); Sum = 3 + 1 = 4
```

### Think About

* Build the frequency map of the array.
* Find `max(freq.values())` and `min(freq.values())`, then compute their sum.

**File:** `04.py`

---

## 5. Lowest Occurring Element in an Array

Given an array `nums`, find and return the element that appears the least number of times (lowest frequency). If multiple elements have the lowest frequency, return the smallest element.

### Example

```text
Input:  nums = [1, 2, 2, 3, 3, 3]
Output: 1  # Frequency is 1
```

### Think About

* Build a frequency dictionary.
* Find the minimum frequency and among all elements with that minimum frequency, return the minimum element.

**File:** `05.py`

---

# 🟢 LEVEL 2 — Uniqueness & Repetition in Arrays

## 6. Count Distinct Elements in Array

Given an array `nums`, count and return the total number of unique (distinct) elements using a hash set or hash map.

### Example

```text
Input:  nums = [1, 2, 2, 3, 4, 4, 5]
Output: 5  # Distinct: 1, 2, 3, 4, 5
```

### Think About

* How does a hash set handle duplicate insertions?
* What is the time complexity of converting a list to a set?

**File:** `06.py`

---

## 7. Count Elements That Appear Exactly Once

Given an array `nums`, count and return how many elements have a frequency of exactly 1.

### Example

```text
Input:  nums = [1, 2, 2, 3, 4, 4, 5]
Output: 3  # Elements appearing once: 1, 3, 5
```

### Think About

* Count frequencies of all elements using a hash map.
* Count how many keys have `count == 1`.

**File:** `07.py`

---

## 8. Count Elements That Appear More Than Once

Given an array `nums`, count and return how many distinct elements have a frequency greater than 1 (i.e. duplicates).

### Example

```text
Input:  nums = [1, 2, 2, 3, 4, 4, 4, 5]
Output: 2  # Elements appearing >1 time: 2, 4
```

### Think About

* Count occurrences of each element.
* Filter and count keys where `count > 1`.

**File:** `08.py`

---

## 9. Single Number

Given a non-empty array of integers `nums`, every element appears twice except for one. Find and return that single element.

### Example

```text
Input:  nums = [2, 2, 1]
Output: 1
```

### Think About

* How can you use a hash map to find the element with frequency 1?
* What mathematical or bitwise property (XOR) can also solve this in O(1) space?

**File:** `09.py`

---

## 10. Contains Duplicate

Given an integer array `nums`, return True if any value appears at least twice in the array, and return False if every element is distinct.

### Example

```text
Input:  nums = [1, 2, 3, 1]
Output: True
```

### Think About

* Use a hash set to track seen elements while traversing `nums`.
* If an element is already in the set, return True early.

**File:** `10.py`

---

# 🟡 LEVEL 3 — Advanced Number Hashing & Pairs

## 11. First Repeating Element in Array

Given an array `nums`, find and return the first element that repeats (the one whose first occurrence has the smallest index and appears again later). Return -1 if no element repeats.

### Example

```text
Input:  nums = [10, 5, 3, 4, 3, 5, 6]
Output: 5  # 5 repeats and appears before 3 repeats
```

### Think About

* Precompute the frequency of each element using a hash map.
* Iterate through the original array in order: the first element with `freq[x] > 1` is the answer.

**File:** `11.py`

---

## 12. First Non-Repeating Element in Array

Given an array `nums` of integers, find and return the first element that appears only once in the array. If no such element exists, return -1.

### Example

```text
Input:  nums = [4, 5, 1, 2, 0, 4]
Output: 5  # 5 is the first element with frequency 1
```

### Think About

* Count frequencies of all elements in the first pass.
* In a second pass through `nums`, return the first element where `freq[x] == 1`.

**File:** `12.py`

---

## 13. Count Occurrences of a Given Number (Multiple Queries)

Given an array `nums` and a list of query numbers `queries`, precompute the frequencies of all numbers in `nums` so that each query count can be answered in O(1) time.

### Example

```text
Input:  nums = [1, 3, 2, 1, 3, 1], queries = [1, 3, 4]
Output: [3, 2, 0]
```

### Think About

* Build a frequency hash map from `nums` in O(N) time.
* Answer each query in O(1) time using `freq.get(q, 0)`.

**File:** `13.py`

---

## 14. Count Pairs with Equal Elements

Given an array `nums`, count and return the number of pairs (i, j) such that i < j and nums[i] == nums[j].

### Example

```text
Input:  nums = [1, 2, 3, 1, 1, 3]
Output: 4  # Pairs: (0,3), (0,4), (3,4) for 1s; (2,5) for 3s -> 3 + 1 = 4
```

### Think About

* If an element appears `k` times, the number of pairs formed by this element is `k * (k - 1) // 2`.
* Alternatively, update the pair count while building the frequency map in a single pass.

**File:** `14.py`

---

## 15. Missing Number

Given an array `nums` containing `n` distinct numbers taken from the range `[0, n]`, use a hash set or boolean frequency array to find the single number missing from the range.

### Example

```text
Input:  nums = [3, 0, 1]
Output: 2  # n = 3, range [0, 3], missing is 2
```

### Think About

* Store all elements of `nums` in a hash set.
* Iterate `i` from `0` to `n`: the number not in the set is the missing number.

**File:** `15.py`

---

# 🟡 LEVEL 4 — Character Frequency Basics

## 16. Count Frequency of Characters in a String

Given a string `s`, count and return the frequency of each character using character hashing or a hash map.

### Example

```text
Input:  s = 'banana'
Output: {'b': 1, 'a': 3, 'n': 2}
```

### Think About

* Use a dictionary or an array of size 26 / 256 for character hashing.
* Convert each character to an index using `ord(c) - ord('a')` if characters are lowercase English letters.

**File:** `16.py`

---

## 17. Highest Occurring Character

Given a string `s`, find and return the character that appears the most times. If there is a tie, return the lexicographically smaller character.

### Example

```text
Input:  s = 'takeuforward'
Output: 'a'  # Frequency is 2 (ties with 'r', 'a' is lexicographically smaller)
```

### Think About

* Build a character frequency dictionary.
* Find the maximum frequency and break ties by choosing the character with the smallest ASCII value.

**File:** `17.py`

---

## 18. Lowest Occurring Character

Given a string `s`, find and return the character that appears the least number of times (lowest frequency). If multiple have the same lowest frequency, return the lexicographically smaller character.

### Example

```text
Input:  s = 'banana'
Output: 'b'  # 'b' has frequency 1
```

### Think About

* Count character frequencies.
* Find the minimum frequency and return the lexicographically smallest character having that frequency.

**File:** `18.py`

---

## 19. First Non-Repeating Character in a String

Given a string `s`, find and return the first non-repeating character (or its index). If all characters repeat, return -1.

### Example

```text
Input:  s = 'leetcode'
Output: 'l'  # Index 0 ('l' appears only once)
```

### Think About

* First pass: build frequency map of characters.
* Second pass: check characters of `s` in original order to find the first one with `count == 1`.

**File:** `19.py`

---

## 20. First Repeating Character in a String

Given a string `s`, find and return the first character that appears more than once (the one whose second occurrence comes earliest). If no character repeats, return -1.

### Example

```text
Input:  s = 'geeksforgeeks'
Output: 'e'  # 'e' repeats earliest at index 2
```

### Think About

* Use a hash set of seen characters while scanning `s` from left to right.
* As soon as `c in seen`, return `c` immediately.

**File:** `20.py`

---

# 🟠 LEVEL 5 — String Validation & Uniqueness

## 21. Check if Two Strings are Anagrams

Given two strings `s` and `t`, return True if `t` is an anagram of `s` (contains the exact same characters with the same frequencies), and False otherwise.

### Example

```text
Input:  s = 'anagram', t = 'nagaram'
Output: True
```

### Think About

* If `len(s) != len(t)`, they cannot be anagrams.
* Compare character count maps of both strings, or increment with `s` and decrement with `t`.

**File:** `21.py`

---

## 22. Check if a String is a Pangram

A pangram is a sentence where every letter of the English alphabet appears at least once. Return True if the given string `s` is a pangram, otherwise False (ignore case).

### Example

```text
Input:  s = 'thequickbrownfoxjumpsoverthelazydog'
Output: True
```

### Think About

* Convert string to lowercase and filter alphabetic characters into a hash set.
* Check if the size of the set is equal to 26.

**File:** `22.py`

---

## 23. Count Distinct Characters in a String

Given a string `s`, count and return the number of distinct (unique) characters present in it.

### Example

```text
Input:  s = 'hello'
Output: 4  # Distinct: 'h', 'e', 'l', 'o'
```

### Think About

* Add all characters of `s` to a hash set.
* The length of the set gives the count of distinct characters.

**File:** `23.py`

---

## 24. Check if All Characters are Unique

Given a string `s`, determine if all characters in the string are unique (no character appears more than once). Return True if all are unique, otherwise False.

### Example

```text
Input:  s = 'abcdef'
Output: True
```

### Think About

* Check if `len(s) == len(set(s))`.
* Alternatively, use a boolean visited array/set and return False as soon as a duplicate is found.

**File:** `24.py`

---

## 25. Sort Characters by Frequency

Given a string `s`, sort the characters in decreasing order based on the frequency of each character. Return the sorted string.

### Example

```text
Input:  s = 'tree'
Output: 'eert'  # 'e' appears twice, 'r' and 't' appear once ('eetr' is also valid)
```

### Think About

* Count frequencies of each character.
* Sort characters by their frequency in descending order, then reconstruct the string.

**File:** `25.py`

---

# 🔴 LEVEL 6 — Advanced String Hashing & Mappings

## 26. Check if String Can be Rearranged to a Palindrome

Given a string `s`, determine whether the characters can be rearranged to form a palindrome. Return True if possible, otherwise False.

### Example

```text
Input:  s = 'civic'
Output: True  # Already a palindrome
```

### Think About

* A string can be rearranged into a palindrome if and only if at most one character has an odd frequency.
* Count frequencies and check how many odd counts exist.

**File:** `26.py`

---

## 27. Remove Duplicate Characters from a String

Given a string `s`, remove all duplicate characters, keeping only the first occurrence of each character in its original relative order.

### Example

```text
Input:  s = 'programming'
Output: 'progami'
```

### Think About

* Maintain a hash set `seen` and a list for output characters.
* Append character to output only if it is not yet in `seen`.

**File:** `27.py`

---

## 28. Count Vowels and Consonants

Given a string `s`, count the number of vowels (a, e, i, o, u, case-insensitive) and consonants (alphabetic characters that are not vowels). Ignore spaces, digits, and punctuation.

### Example

```text
Input:  s = 'takeuforward'
Output: {'vowels': 5, 'consonants': 7}
```

### Think About

* Use a set of vowels `{'a', 'e', 'i', 'o', 'u'}` for O(1) lookup.
* Check `c.isalpha()` before classifying each character.

**File:** `28.py`

---

## 29. Isomorphic Strings

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`, preserving order and ensuring a one-to-one mapping with no two characters mapping to the same character.

### Example

```text
Input:  s = 'egg', t = 'add'
Output: True  # 'e' -> 'a', 'g' -> 'd'
```

### Think About

* Maintain two mapping dictionaries: `map_s_to_t` and `map_t_to_s`.
* Verify consistency of mappings at every index.

**File:** `29.py`

---

## 30. Ransom Note

Given two strings `ransomNote` and `magazine`, return True if `ransomNote` can be constructed using the letters from `magazine` (each letter in `magazine` can only be used once), otherwise False.

### Example

```text
Input:  ransomNote = 'a', magazine = 'b'
Output: False
```

### Think About

* Count frequencies of letters in `magazine` using a hash map or Counter.
* For each letter in `ransomNote`, decrement its available count. If count drops below zero, return False.

**File:** `30.py`
