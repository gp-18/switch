# 🟢 LEVEL 1 — Digit Basics

## 1. Count Digits

Given an integer `n`, count how many digits it contains.

### Example

```text
Input:  12345
Output: 5
```

### Think About

* How can you remove the last digit?
* What happens when you repeatedly divide by 10?

**File:** `01_count_digits.py`

---

## 2. Count Odd Digits

Given an integer `n`, count how many digits are odd.

### Example

```text
Input:  123456
Output: 3
```

### Think About

* How do you extract the last digit?
* How do you check whether a digit is odd?

**File:** `02_count_odd_digits.py`

---

## 3. Reverse a Number

Reverse the digits of an integer.

### Example

```text
Input:  12345
Output: 54321
```

### Think About

How can you construct the reversed number one digit at a time?

**File:** `03_reverse_number.py`

---

## 4. Check Palindrome Number

Determine whether a number reads the same forward and backward.

### Example

```text
Input:  121
Output: True
```

```text
Input:  123
Output: False
```

**File:** `04_palindrome_number.py`

---

## 5. Find Largest Digit

Find the largest digit present in a number.

### Example

```text
Input:  58321
Output: 8
```

### Think About

Keep track of the largest digit seen so far.

**File:** `05_largest_digit.py`

---

# 🟢 LEVEL 2 — Basic Mathematical Logic

## 6. Factorial of a Number

Calculate:

```text
n! = n × (n-1) × ... × 1
```

### Example

```text
Input: 5
Output: 120
```

**File:** `06_factorial.py`

---

## 7. Armstrong Number

Check whether a number is an Armstrong number.

### Example

```text
153
```

Because:

```text
1³ + 5³ + 3³ = 153
```

**File:** `07_armstrong_number.py`

---

## 8. Perfect Number

Check whether a number is equal to the sum of its proper divisors.

### Example

```text
6
```

Divisors:

```text
1 + 2 + 3 = 6
```

Therefore:

```text
6 → Perfect Number
```

**File:** `08_perfect_number.py`

---

## 9. Prime Number

Check whether a number is prime.

### Example

```text
Input: 7
Output: True
```

A prime number has exactly two factors:

```text
1 and itself
```

**File:** `09_prime_number.py`

---

# 🟡 LEVEL 3 — Thinking About Optimization

## 10. Count Prime Numbers From 1 to N

Count how many prime numbers exist between `1` and `N`.

### Example

```text
Input: 10

Primes:
2, 3, 5, 7

Output: 4
```

### Think About

First try:

```text
Check every number → determine whether prime
```

Then think:

> Can I determine all primes together instead of repeatedly checking each number?

**File:** `10_count_primes.py`

---

## 11. GCD / HCF

Find the Greatest Common Divisor of two numbers.

### Example

```text
Input:
12, 18

Output:
6
```

**File:** `11_gcd.py`

---

## 12. LCM

Find the Least Common Multiple of two numbers.

### Example

```text
Input:
12, 18

Output:
36
```

### Think About

There is an important relationship between:

```text
GCD
LCM
```

**File:** `12_lcm.py`

---

## 13. Find All Divisors

Print or return all divisors of a number.

### Example

```text
Input: 12

Output:
1, 2, 3, 4, 6, 12
```

### Think About

Don't immediately check every number up to `n`.

Ask:

> If `i` divides `n`, what other divisor can I immediately find?

**File:** `13_divisors.py`

---

# 🟡 LEVEL 4 — More Digit Practice

## 14. Sum of Digits

Find the sum of all digits.

```text
Input: 12345
Output: 15
```

**File:** `14_sum_digits.py`

---

## 15. Product of Digits

Find the product of all digits.

```text
Input: 1234
Output: 24
```

**File:** `15_product_digits.py`

---

## 16. Count Even Digits

Count how many digits are even.

```text
Input: 123456
Output: 3
```

**File:** `16_count_even_digits.py`

---

## 17. Frequency of a Digit

Count how many times a particular digit occurs.

```text
Input: 122333
Digit: 3

Output: 3
```

**File:** `17_digit_frequency.py`

---

## 18. Remove a Digit

Remove all occurrences of a given digit from a number.

```text
Input: 12234
Remove: 2

Output: 134
```

**File:** `18_remove_digit.py`

---

## 19. Swap First and Last Digit

Swap the first and last digits of a number.

```text
Input: 12345
Output: 52341
```

**File:** `19_swap_first_last.py`

---

# 🟠 LEVEL 5 — Number Properties

## 20. Count Trailing Zeros

Count the number of zeros at the end of a number.

```text
Input: 12000
Output: 3
```

**File:** `20_trailing_zeros.py`

---

## 21. Calculate Power

Calculate:

```text
base^exponent
```

Example:

```text
2^5 = 32
```

First think about a simple repeated multiplication solution.

Then think about whether you can reduce the number of multiplications.

**File:** `21_power.py`

---

## 22. Check Power of Two

Determine whether a number is a power of 2.

Examples:

```text
1   → True
2   → True
4   → True
8   → True
16  → True
10  → False
```

**File:** `22_power_of_two.py`

---

## 23. Count Set Bits

Count the number of `1`s in the binary representation of a number.

Example:

```text
5 → 101

Number of set bits = 2
```

**File:** `23_count_set_bits.py`

---

# 🟠 LEVEL 6 — Mathematical Sequences

## 24. Fibonacci Number

Find the nth Fibonacci number.

Sequence:

```text
0, 1, 1, 2, 3, 5, 8, 13...
```

**File:** `24_fibonacci.py`

---

## 25. Sum of Numbers From 1 to N

Calculate:

```text
1 + 2 + 3 + ... + N
```

Example:

```text
N = 5

Output = 15
```

### Think About

First solve using a loop.

Then ask:

> Is there a mathematical formula?

**File:** `25_sum_1_to_n.py`

---

# 🔴 LEVEL 7 — Stronger Number Logic

## 26. Automorphic Number

Check whether the square of a number ends with the number itself.

Example:

```text
5² = 25
```

The square ends in `5`.

Therefore:

```text
5 → Automorphic
```

**File:** `26_automorphic.py`

---

## 27. Abundant Number

A number is abundant if the sum of its proper divisors is greater than the number.

Example:

```text
12

Proper divisors:
1 + 2 + 3 + 4 + 6 = 16

16 > 12
```

**File:** `27_abundant.py`

---

## 28. Check Coprime Numbers

Two numbers are coprime if:

```text
GCD(a, b) = 1
```

Example:

```text
8 and 15

GCD = 1

Therefore → Coprime
```

**File:** `28_coprime.py`

---

## 29. Prime Factorization

Find the prime factors of a number.

Example:

```text
60

60 = 2 × 2 × 3 × 5
```

Output:

```text
2, 2, 3, 5
```

### Think About

Instead of testing every possible factor repeatedly, use the fact that factors can be processed from the smallest upward.

**File:** `29_prime_factorization.py`

---

## 30. Generate All Prime Numbers Up To N

Generate every prime number from `2` to `N`.

Example:

```text
Input: 20

Output:
2, 3, 5, 7, 11, 13, 17, 19
```

### Think About

Compare:

```text
Approach 1:
Check every number individually.

Approach 2:
Use the Sieve of Eratosthenes.
```

This problem is important because it introduces a classic optimization pattern.


