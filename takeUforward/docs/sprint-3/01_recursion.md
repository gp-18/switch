# 🟢 LEVEL 1 — Head Recursion: Numbers & Printing

## 1. Print 1 to N using recursion

Given an integer `n`, print numbers from 1 to `n` in increasing order using recursion.

### Example

```text
Input:  n = 5
Output: 1 2 3 4 5
```

### Think About

* What is the base case when `n` drops below 1?
* In head recursion, call `solve(n - 1)` before printing `n` so smaller numbers are printed on the return journey.

**File:** `01.py`

---

## 2. Print first N even numbers in increasing order

Given an integer `n`, print the first `n` even natural numbers (2, 4, 6, ..., 2*n) in increasing order using recursion.

### Example

```text
Input:  n = 4
Output: 2 4 6 8
```

### Think About

* Base case: if `n == 0`, return immediately.
* Recursively call for `n - 1` first, then print `2 * n`.

**File:** `02.py`

---

## 3. Print digits of a number from left to right

Given a non-negative integer `n`, print its digits from left to right separated by spaces using recursion.

### Example

```text
Input:  n = 1234
Output: 1 2 3 4
```

### Think About

* How do you isolate the last digit (`n % 10`) and the remaining prefix (`n // 10`)?
* Recurse on `n // 10` first, then print `n % 10`. What is the base case when `n < 10`?

**File:** `03.py`

---

## 4. Convert decimal to binary using recursion

Given a decimal integer `n`, print or return its binary representation using recursion.

### Example

```text
Input:  n = 10
Output: 1010
```

### Think About

* Base case: if `n == 0`, how should zero be handled?
* For `n > 0`, recurse on `n // 2` first, then append or print `n % 2`.

**File:** `04.py`

---

## 5. Sum of first N natural numbers

Given an integer `n`, calculate and return the sum of the first `n` natural numbers (1 to n) using recursion.

### Example

```text
Input:  n = 5
Output: 15
```

### Think About

* Base case: `n == 1` returns 1 (or `n == 0` returns 0).
* Recursive relation: `sum(n) = n + sum(n - 1)`.

**File:** `05.py`

---

# 🟢 LEVEL 2 — Head Recursion: Math, Strings & Powers

## 6. Factorial of N

Given a non-negative integer `n`, compute and return `n!` using recursion.

### Example

```text
Input:  n = 5
Output: 120
```

### Think About

* Base cases: `0! = 1` and `1! = 1`.
* Recursive step: `factorial(n) = n * factorial(n - 1)`.

**File:** `06.py`

---

## 7. Print array elements in reverse order using recursion

Given an array of integers, print all elements from last to first using recursion.

### Example

```text
Input:  nums = [1, 2, 3, 4, 5]
Output: 5 4 3 2 1
```

### Think About

* Pass an index pointer starting from the end, or recurse from index 0 to `len - 1` and print after the call returns.
* Base case: when index goes out of bounds (`< 0` or `>= len(nums)`).

**File:** `07.py`

---

## 8. Print a string in reverse using recursion

Given a string `s`, print its characters in reverse order using recursion.

### Example

```text
Input:  s = 'hello'
Output: olleh
```

### Think About

* Either print the last character first and recurse on `s[:-1]`, or recurse on `s[1:]` and print `s[0]` on the return unwinding.
* Base case: empty string `len(s) == 0`.

**File:** `08.py`

---

## 9. Reverse a string using recursion

Given a string `s`, return a new string with its characters reversed using recursion.

### Example

```text
Input:  s = 'takeuforward'
Output: 'drawrofuwkat'
```

### Think About

* Base case: if `len(s) <= 1`, return `s`.
* Recursive step: return `reverse(s[1:]) + s[0]`.

**File:** `09.py`

---

## 10. Power of a number (x raised to n)

Given two integers `x` (base) and `n` (exponent), calculate and return x^n using recursion.

### Example

```text
Input:  x = 2, n = 5
Output: 32
```

### Think About

* Base case: any number raised to power 0 is 1 (`x^0 = 1`).
* Recursive step: `power(x, n) = x * power(x, n - 1)`.

**File:** `10.py`

---

# 🟡 LEVEL 3 — Head Recursion: Digits, Sequences & Reduction

## 11. Nth Fibonacci number

Given an integer `n`, return the nth Fibonacci number using recursion (F(0)=0, F(1)=1).

### Example

```text
Input:  n = 4
Output: 3  # Sequence: 0, 1, 1, 2, 3
```

### Think About

* Base cases: `n == 0` returns 0, `n == 1` returns 1.
* Recursive step: `fib(n) = fib(n - 1) + fib(n - 2)`.

**File:** `11.py`

---

## 12. Sum of digits of a number using recursion

Given a non-negative integer `n`, return the sum of its digits using recursion.

### Example

```text
Input:  n = 1234
Output: 10  # 1 + 2 + 3 + 4 = 10
```

### Think About

* Base case: if `n < 10`, return `n`.
* Recursive step: `(n % 10) + sum_digits(n // 10)`.

**File:** `12.py`

---

## 13. Count digits of a number using recursion

Given a non-negative integer `n`, count and return the total number of digits using recursion.

### Example

```text
Input:  n = 12345
Output: 5
```

### Think About

* Base case: if `n < 10`, return 1.
* Recursive step: `1 + count_digits(n // 10)`.

**File:** `13.py`

---

## 14. Sum of array elements using recursion

Given an array `nums` of integers, calculate and return the sum of all elements using recursion.

### Example

```text
Input:  nums = [1, 2, 3, 4, 5]
Output: 15
```

### Think About

* Track current index `i`. Base case: if `i == len(nums)`, return 0.
* Recursive step: `nums[i] + sum_array(nums, i + 1)`.

**File:** `14.py`

---

## 15. Length of a string using recursion

Given a string `s`, find and return its length using recursion without using the built-in `len()` function.

### Example

```text
Input:  s = 'hello'
Output: 5
```

### Think About

* Base case: if `s == ""`, return 0.
* Recursive step: `1 + string_length(s[1:])`.

**File:** `15.py`

---

# 🟡 LEVEL 4 — Tail Recursion: Decrements & Forward Traversals

## 16. Print N to 1 using recursion

Given an integer `n`, print numbers from `n` down to `1` in decreasing order using tail recursion.

### Example

```text
Input:  n = 5
Output: 5 4 3 2 1
```

### Think About

* Base case: if `n == 0`, stop recursing.
* In tail recursion, do the work first: print `n`, then make the recursive call `print_n_to_1(n - 1)` as the final action.

**File:** `16.py`

---

## 17. Print name N times using recursion

Given a name string and an integer `n`, print the name `n` times using recursion.

### Example

```text
Input:  name = 'Parth', n = 3
Output: Parth
        Parth
        Parth
```

### Think About

* Base case: if `n <= 0`, return.
* Print `name`, then recurse with `n - 1`.

**File:** `17.py`

---

## 18. Print N to 0 using recursion

Given an integer `n`, print numbers from `n` down to `0` using tail recursion.

### Example

```text
Input:  n = 4
Output: 4 3 2 1 0
```

### Think About

* Base case: if `n < 0`, terminate.
* Print `n` first, then recursively call with `n - 1`.

**File:** `18.py`

---

## 19. Print even numbers from N to 1

Given an integer `n`, print all even numbers from `n` down to `1` in decreasing order using recursion.

### Example

```text
Input:  n = 7
Output: 6 4 2
```

### Think About

* Base case: if `n <= 1`, stop.
* If `n % 2 == 0`, print `n` and recurse for `n - 2`. If `n` is odd, recurse for `n - 1`.

**File:** `19.py`

---

## 20. Print array elements in order using recursion

Given an array of integers, print all elements from index `0` to `len(nums) - 1` in order using tail recursion.

### Example

```text
Input:  nums = [10, 20, 30, 40]
Output: 10 20 30 40
```

### Think About

* Maintain an index parameter `i = 0`. Base case: if `i == len(nums)`, return.
* Print `nums[i]`, then call `print_elements(nums, i + 1)`.

**File:** `20.py`

---

# 🟠 LEVEL 5 — Tail Recursion: Strings, Accumulators & Search

## 21. Print string characters in order using recursion

Given a string `s`, print each character from index `0` to end using recursion.

### Example

```text
Input:  s = 'code'
Output: c o d e
```

### Think About

* Base case: if index `i == len(s)`, return.
* Print character at `i`, then recurse for `i + 1`.

**File:** `21.py`

---

## 22. Sum of first N numbers using an accumulator

Given an integer `n`, compute the sum of the first `n` numbers using tail recursion with an accumulator parameter.

### Example

```text
Input:  n = 5
Output: 15
```

### Think About

* Define helper `solve(n, acc=0)`.
* Base case: if `n == 0`, return `acc`.
* Recursive step: pass `acc + n` into `solve(n - 1, acc + n)`. Notice that no addition is postponed on unwinding!

**File:** `22.py`

---

## 23. Factorial of N using an accumulator

Given an integer `n`, compute n! using tail recursion with an accumulator parameter.

### Example

```text
Input:  n = 5
Output: 120
```

### Think About

* Define helper `solve(n, acc=1)`.
* Base case: if `n <= 1`, return `acc`.
* Tail call: `solve(n - 1, acc * n)`.

**File:** `23.py`

---

## 24. Maximum element in an array using recursion

Given an array `nums` of integers, find and return the maximum element using recursion.

### Example

```text
Input:  nums = [1, 5, 3, 9, 2]
Output: 9
```

### Think About

* Base case: if single element remains (`i == len(nums) - 1`), return `nums[i]`.
* Tail recursion option: pass running `current_max` through an accumulator `solve(nums, i + 1, max(current_max, nums[i]))`.

**File:** `24.py`

---

## 25. Linear search using recursion

Given an array `nums` and a `target` element, return the index of the first occurrence of `target` using recursion, or -1 if not found.

### Example

```text
Input:  nums = [10, 20, 30, 40], target = 30
Output: 2
```

### Think About

* Base cases: if index `i == len(nums)`, target was not found, return -1. If `nums[i] == target`, return `i`.
* Recursive step: return `linear_search(nums, target, i + 1)`.

**File:** `25.py`

---

# 🔴 LEVEL 6 — Tail Recursion: Two Pointers, Palindromes & Euclid

## 26. Check if the array is sorted using recursion

Given an array `nums`, return True if the array is sorted in non-decreasing order, otherwise False, using recursion.

### Example

```text
Input:  nums = [1, 2, 3, 4, 5]
Output: True
```

### Think About

* Base case: if `i >= len(nums) - 1`, array is sorted, return `True`.
* If `nums[i] > nums[i + 1]`, return `False` immediately. Otherwise recurse for `i + 1`.

**File:** `26.py`

---

## 27. Check palindrome using recursion

Given a string `s`, check if it is a palindrome using recursion by comparing characters from both ends. Return True or False.

### Example

```text
Input:  s = 'racecar'
Output: True
```

### Think About

* Use pointers `left` and `right`. Base case: if `left >= right`, return `True`.
* If `s[left] != s[right]`, return `False`. Otherwise recurse with `left + 1, right - 1`.

**File:** `27.py`

---

## 28. GCD of two numbers using recursion

Given two integers `a` and `b`, compute their Greatest Common Divisor (GCD) using the Euclidean algorithm with recursion.

### Example

```text
Input:  a = 48, b = 18
Output: 6
```

### Think About

* Base case: if `b == 0`, GCD is `a`.
* Euclidean relation: `gcd(a, b) = gcd(b, a % b)`.

**File:** `28.py`

---

## 29. Reverse an array using recursion (two pointers)

Given an array `nums`, reverse it in-place using two-pointer recursion.

### Example

```text
Input:  nums = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
```

### Think About

* Maintain `left` and `right` indices. Base case: if `left >= right`, return.
* Swap `nums[left]` and `nums[right]`, then recurse on `left + 1, right - 1`.

**File:** `29.py`

---

## 30. Count occurrences of a number in an array using recursion

Given an array `nums` and a `target` integer, count how many times `target` appears in the array using recursion.

### Example

```text
Input:  nums = [1, 2, 3, 2, 4, 2], target = 2
Output: 3
```

### Think About

* Base case: if index `i == len(nums)`, return 0.
* Recursive step: `(1 if nums[i] == target else 0) + count(nums, target, i + 1)`.

**File:** `30.py`