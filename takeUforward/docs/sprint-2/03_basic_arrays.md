# 🟢 LEVEL 1 — Basic Traversals & Aggregations

## 1. Sum of Array Elements

Given an array `nums` of integers, calculate and return the sum of all elements.

### Example

```text
Input:  nums = [1, 2, 3, 4, 5]
Output: 15
```

### Think About

* How can you initialize an accumulator variable?
* How do you iterate through every element in the array?

**File:** `01.py`

---

## 2. Count of Odd Numbers in Array

Given an array `nums` of integers, count and return how many numbers are odd.

### Example

```text
Input:  nums = [1, 2, 3, 4, 5, 6]
Output: 3  # Odd elements: 1, 3, 5
```

### Think About

* How do you test if an integer is odd using the modulo `%` operator?
* Keep a running count that increments whenever an odd element is encountered.

**File:** `02.py`

---

## 3. Count of Even Numbers in Array

Given an array `nums` of integers, count and return how many numbers are even.

### Example

```text
Input:  nums = [1, 2, 3, 4, 5, 6]
Output: 3  # Even elements: 2, 4, 6
```

### Think About

* An integer is even if `num % 2 == 0`.
* Consider how zero and negative numbers behave under `% 2` in Python.

**File:** `03.py`

---

## 4. Reverse an Array

Given an array `nums`, reverse the order of its elements.

### Example

```text
Input:  nums = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
```

### Think About

* Can you reverse the array in-place using two pointers (left and right)?
* What condition signals that the two pointers have met or crossed?

**File:** `04.py`

---

## 5. Largest Element

Given an array `nums` of integers, find and return the largest element.

### Example

```text
Input:  nums = [3, 7, 2, 9, 5]
Output: 9
```

### Think About

* What should you initialize your `max_val` to? (Hint: avoid initializing to 0 if negatives exist).
* Update `max_val` whenever you encounter an element greater than it.

**File:** `05.py`

---

## 6. Smallest Element

Given an array `nums` of integers, find and return the smallest element.

### Example

```text
Input:  nums = [4, 7, 1, 9, 3]
Output: 1
```

### Think About

* Initialize your `min_val` to the first element `nums[0]` or infinity.
* Compare every element against `min_val` and update when smaller.

**File:** `06.py`

---

## 7. Average of Array Elements

Given an array `nums` of integers, calculate and return the average (arithmetic mean) of its elements.

### Example

```text
Input:  nums = [1, 2, 3, 4, 5]
Output: 3.0
```

### Think About

* Average is defined as total sum divided by the number of elements: `sum(nums) / len(nums)`.
* Watch out for floating point division and division by zero if empty.

**File:** `07.py`

---

# 🟢 LEVEL 2 — Conditional Searches & Calculations

## 8. Linear Search

Given an array `nums` and a target value `target`, return the index of the first occurrence of `target`, or -1 if it is not present in `nums`.

### Example

```text
Input:  nums = [10, 25, 30, 45, 50], target = 30
Output: 2
```

### Think About

* Iterate through the array with index `i` from 0 to `len(nums) - 1`.
* As soon as `nums[i] == target`, return `i`. If loop finishes without match, return `-1`.

**File:** `08.py`

---

## 9. Count Positive, Negative and Zero Elements

Given an array `nums` of integers, count the number of positive elements, negative elements, and zero elements.

### Example

```text
Input:  nums = [1, -2, 0, 4, -5, 6, 0]
Output: {'positive': 3, 'negative': 2, 'zero': 2}
```

### Think About

* Use three separate counters for positive, negative, and zero.
* Check conditions: `num > 0`, `num < 0`, and `num == 0`.

**File:** `09.py`

---

## 10. Sum of Even Numbers in Array

Given an array `nums` of integers, calculate and return the sum of all even numbers.

### Example

```text
Input:  nums = [1, 2, 3, 4, 5, 6]
Output: 12  # 2 + 4 + 6 = 12
```

### Think About

* Filter or check each element with `num % 2 == 0`.
* Add only even numbers to the total sum.

**File:** `10.py`

---

## 11. Sum of Odd Numbers in Array

Given an array `nums` of integers, calculate and return the sum of all odd numbers.

### Example

```text
Input:  nums = [1, 2, 3, 4, 5, 6]
Output: 9  # 1 + 3 + 5 = 9
```

### Think About

* An element is odd if `num % 2 != 0`.
* Add each odd element to an accumulator.

**File:** `11.py`

---

## 12. Product of Array Elements

Given an array `nums` of integers, find and return the product of all elements.

### Example

```text
Input:  nums = [1, 2, 3, 4]
Output: 24  # 1 * 2 * 3 * 4 = 24
```

### Think About

* Initialize product accumulator to 1 (not 0).
* What happens immediately if any element in the array is 0?

**File:** `12.py`

---

# 🟡 LEVEL 3 — Index Manipulation & Verification

## 13. Sum of Elements at Even Indices

Given an array `nums`, calculate and return the sum of elements located at even indices (0, 2, 4, ...).

### Example

```text
Input:  nums = [10, 20, 30, 40, 50]
Output: 90  # nums[0] + nums[2] + nums[4] = 10 + 30 + 50 = 90
```

### Think About

* Iterate by step of 2: `range(0, len(nums), 2)`.
* Sum elements `nums[i]` for each even index `i`.

**File:** `13.py`

---

## 14. Sum of Elements at Odd Indices

Given an array `nums`, calculate and return the sum of elements located at odd indices (1, 3, 5, ...).

### Example

```text
Input:  nums = [10, 20, 30, 40, 50]
Output: 60  # nums[1] + nums[3] = 20 + 40 = 60
```

### Think About

* Iterate by step of 2 starting at index 1: `range(1, len(nums), 2)`.
* What should be returned if the array has only 1 element?

**File:** `14.py`

---

## 15. Count Elements Greater Than a Given Number

Given an array `nums` and a threshold integer `k`, count how many elements are strictly greater than `k`.

### Example

```text
Input:  nums = [1, 5, 8, 3, 10, 2], k = 4
Output: 3  # Elements greater than 4: 5, 8, 10
```

### Think About

* Iterate through `nums` and compare `x > k`.
* Count matches.

**File:** `15.py`

---

## 16. Check if the Array is Sorted

Given an array `nums`, return True if the array is sorted in non-decreasing order, otherwise False.

### Example

```text
Input:  nums = [1, 2, 3, 4, 5]
Output: True
```

### Think About

* Compare adjacent elements: check if `nums[i] <= nums[i+1]` for all `i`.
* If any `nums[i] > nums[i+1]` is found, return False immediately.

**File:** `16.py`

---

## 17. Check if the Array is a Palindrome

Given an array `nums`, return True if the array reads the same forward and backward, otherwise False.

### Example

```text
Input:  nums = [1, 2, 3, 2, 1]
Output: True
```

### Think About

* Compare `nums[i]` with `nums[len(nums) - 1 - i]` from both ends inward.
* Can you do this using two pointers until `left >= right`?

**File:** `17.py`

---

# 🟡 LEVEL 4 — Order Statistics & Tracking

## 18. Second Largest Element

Given an array `nums` of integers, find and return the second largest distinct element. If no second largest exists, return -1.

### Example

```text
Input:  nums = [12, 35, 1, 10, 34, 1]
Output: 34
```

### Think About

* Can you track both `largest` and `second_largest` in a single pass?
* Make sure duplicates of the largest element do not count as second largest.

**File:** `18.py`

---

## 19. Second Smallest Element

Given an array `nums` of integers, find and return the second smallest distinct element. If no second smallest exists, return -1.

### Example

```text
Input:  nums = [12, 35, 1, 10, 34, 1]
Output: 10
```

### Think About

* Maintain `smallest` and `second_smallest` initialized appropriately.
* Update when an element is between `smallest` and `second_smallest`.

**File:** `19.py`

---

## 20. Contains Duplicate

Given an array `nums`, return True if any value appears at least twice in the array, and False if every element is distinct.

### Example

```text
Input:  nums = [1, 2, 3, 1]
Output: True
```

### Think About

* Can you use a hash set to track seen elements in O(N) time?
* Compare `len(nums) != len(set(nums))`.

**File:** `20.py`

---

## 21. Counting Frequencies of Array Elements

Given an array `nums`, count and return the frequency of each distinct element (e.g. as a dictionary or map).

### Example

```text
Input:  nums = [1, 2, 2, 3, 3, 3]
Output: {1: 1, 2: 2, 3: 3}
```

### Think About

* Use a dictionary or Counter to store element -> count.
* Iterate through the array and increment counts.

**File:** `21.py`

---

## 22. Maximum Consecutive Ones

Given a binary array `nums` containing only 0s and 1s, return the maximum number of consecutive 1s in the array.

### Example

```text
Input:  nums = [1, 1, 0, 1, 1, 1]
Output: 3
```

### Think About

* Maintain a current streak counter and a maximum streak counter.
* When encountering 1, increment current streak. When 0, reset current streak to 0.

**File:** `22.py`

---

# 🟠 LEVEL 5 — Array Analysis & Comparisons

## 23. Missing Number

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

### Example

```text
Input:  nums = [3, 0, 1]
Output: 2  # n = 3, range [0, 3], missing is 2
```

### Think About

* The expected sum of numbers from 0 to n is `n * (n + 1) // 2`.
* Subtract the actual array sum from the expected sum to find the missing number.

**File:** `23.py`

---

## 24. Check if Array Contains Only Positive Numbers

Given an array `nums` of integers, return True if all elements are strictly positive (> 0), otherwise False.

### Example

```text
Input:  nums = [1, 2, 3, 4, 5]
Output: True
```

### Think About

* Iterate through the array and check if any element is `<= 0`.
* Remember that 0 is neither positive nor negative.

**File:** `24.py`

---

## 25. Difference Between Largest and Smallest Element

Given an array `nums` of integers, calculate and return the difference between the maximum and minimum elements (max - min).

### Example

```text
Input:  nums = [2, 10, 5, 1, 8]
Output: 9  # 10 - 1 = 9
```

### Think About

* Find the maximum element and minimum element in the array.
* Return `max_val - min_val`.

**File:** `25.py`

---

## 26. Count Occurrences of a Given Number

Given an array `nums` and a target integer `target`, count how many times `target` appears in `nums`.

### Example

```text
Input:  nums = [1, 2, 2, 3, 2, 4, 2], target = 2
Output: 4
```

### Think About

* Iterate through each element and increment a counter whenever `x == target`.
* Can also be solved with built-in list count, but implement the traversal logic.

**File:** `26.py`

---

# 🔴 LEVEL 6 — Multi-Array & Distinct Elements

## 27. Check if Two Arrays are Equal

Given two arrays `a` and `b`, determine if they contain the exact same elements with the same frequencies (irrespective of order).

### Example

```text
Input:  a = [1, 2, 5, 4, 0], b = [2, 4, 5, 0, 1]
Output: True
```

### Think About

* First check if lengths are equal (`len(a) == len(b)`).
* Compare frequency maps of both arrays or compare sorted versions.

**File:** `27.py`

---

## 28. Third Largest Element

Given an array `nums` of integers, find and return the third largest distinct element. If it does not exist, return -1.

### Example

```text
Input:  nums = [2, 4, 1, 3, 5]
Output: 3
```

### Think About

* Track `first`, `second`, and `third` largest distinct values in a single traversal.
* Ignore duplicates of already seen largest values.

**File:** `28.py`

---

## 29. Count Distinct Elements in Array

Given an array `nums` of integers, count and return the number of distinct (unique) elements present.

### Example

```text
Input:  nums = [1, 2, 2, 3, 4, 4, 5]
Output: 5  # Distinct: 1, 2, 3, 4, 5
```

### Think About

* Can you use a set to collect distinct elements?
* The size of the set gives the count of distinct elements.

**File:** `29.py`

---

## 30. Sum of Largest and Smallest Element

Given an array `nums` of integers, find the sum of the maximum and minimum elements in the array.

### Example

```text
Input:  nums = [1, 2, 3, 4, 5]
Output: 6  # min = 1, max = 5 -> 1 + 5 = 6
```

### Think About

* Find the maximum element and the minimum element.
* Return `max_element + min_element`.

**File:** `30.py`
