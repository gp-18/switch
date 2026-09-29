# Python Basics --- Interview Notes + Practice Bank Before DSA

Use this as a write-by-hand revision sheet and practice checklist. Try
each question without looking at a solution. The questions are grouped
by topic; each topic has **5 practice questions**.

------------------------------------------------------------------------

# Part 1 --- Interview Notes to Write by Hand

## 1. Python Fundamentals

-   **Python:** high-level, general-purpose programming language with
    readable syntax.
-   **Common uses:** automation, web development, data engineering,
    scripting, testing, AI/ML.
-   **CPython execution (simplified):** `.py` source code → bytecode →
    Python virtual machine executes bytecode.
-   **Interactive mode:** run statements one by one in the Python shell.
-   **Script mode:** save code in a `.py` file and run the file.
-   **Dynamic typing:** a variable name can refer to values of different
    types at different times.
-   **Indentation:** defines code blocks; use consistent indentation,
    commonly 4 spaces.

## 2. Variables, Types, Input and Output

-   **Variable:** a name that refers to an object/value; Python does not
    require a type declaration.
-   **Naming:** use letters, digits, and `_`; cannot start with a digit;
    names are case-sensitive; keywords cannot be variable names.
-   **Common types:** `int`, `float`, `str`, `bool`, `NoneType`.
-   `print(value)` displays output.
-   `input(prompt)` always returns a string; convert it when numeric
    input is needed.
-   Type conversion: `int("12")`, `float("3.5")`, `str(12)`.
-   `type(value)` checks an object's type.
-   `=` assigns a value; `==` compares values.

## 3. Strings --- Know These Methods

A **string (`str`)** is an immutable sequence of characters. Methods
that appear to change a string return a new string.

  --------------------------------------------------------------------------------
  Method / operation      What it does            Example
  ----------------------- ----------------------- --------------------------------
  `len(s)`                Number of characters    `len("cat")` → `3`

  `s.upper()`             Uppercase copy          `"cat".upper()` → `"CAT"`

  `s.lower()`             Lowercase copy          `"CAT".lower()` → `"cat"`

  `s.capitalize()`        Uppercase first         `"hELLO".capitalize()` →
                          character, lowercase    `"Hello"`
                          the rest                

  `s.title()`             Title-case words        `"hello world".title()` →
                                                  `"Hello World"`

  `s.strip()`             Removes whitespace at   `"  hi  ".strip()` → `"hi"`
                          both ends               

  `s.lstrip()` /          Removes whitespace at   `" hi ".lstrip()` → `"hi "`
  `s.rstrip()`            left / right end        

  `s.replace(old, new)`   Replaces occurrences    `"banana".replace("a", "o")` →
                                                  `"bonono"`

  `s.find(sub)`           First index, or `-1` if `"banana".find("na")` → `2`
                          absent                  

  `s.count(sub)`          Counts non-overlapping  `"banana".count("a")` → `3`
                          occurrences             

  `s.startswith(x)`       Tests prefix            `"python".startswith("py")` →
                                                  `True`

  `s.endswith(x)`         Tests suffix            `"notes.txt".endswith(".txt")` →
                                                  `True`

  `s.split(sep)`          Splits into a list      `"a,b".split(",")` →
                                                  `["a", "b"]`

  `sep.join(items)`       Joins strings using     `"-".join(["a", "b"])` → `"a-b"`
                          separator               

  `s.isdigit()`           Checks whether          `"123".isdigit()` → `True`
                          characters are digits   

  `s.isalpha()`           Checks whether          `"abc".isalpha()` → `True`
                          characters are letters  

  `s.isalnum()`           Checks letters/digits   `"abc123".isalnum()` → `True`
                          only                    

  `s.isspace()`           Checks whitespace-only  `"  ".isspace()` → `True`
                          string                  

  `s.islower()` /         Checks letter case      `"abc".islower()` → `True`
  `s.isupper()`                                   

  `s[index]`              Accesses one character; `"cat"[0]` → `"c"`
                          indexing starts at 0    

  `s[start:end]`          Slice; `end` is         `"python"[1:4]` → `"yth"`
                          excluded                
  --------------------------------------------------------------------------------

**String traps** - Strings are immutable: `s.upper()` does not modify
`s`; use `s = s.upper()` to keep the result. - `strip()` removes
characters at the ends, not from the middle. - `find()` returns `-1` if
the substring is missing. - `split()` returns a list; `join()` is called
on the separator string. - `input()` returns a string, even when the
user types digits.

## 4. Escape Sequences and f-Strings

-   `\\n` creates a new line; `\\t` creates a tab; `\\\\` represents a
    backslash; `\\"` represents a double quote inside a double-quoted
    string.
-   **f-string:** puts expressions inside `{}`:
    `name = "Asha"; print(f"Hello, {name}")`.
-   Prefer f-strings for readable output containing variables or
    calculations.

## 5. Numbers and Operators

-   Numeric types used most often: `int` and `float`; `bool` is also
    numeric in some contexts.
-   Arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`.
-   `/` gives true division; `//` gives floor division; `%` gives
    remainder; `**` raises to a power.
-   Example: `7 / 2 == 3.5`, `7 // 2 == 3`, `7 % 2 == 1`, `2 ** 3 == 8`.
-   Use parentheses to make complex expressions clear.
-   Watch out: `//` rounds down toward negative infinity, so
    `-7 // 2 == -4`.

## 6. Comparisons and Logical Operators

-   Comparisons: `==`, `!=`, `<`, `<=`, `>`, `>=`; result is `True` or
    `False`.
-   Identity: `is` checks whether two references point to the same
    object; `==` checks value equality. Usually use `is None` for `None`
    checks.
-   Logical operators: `and`, `or`, `not`.
-   **Short-circuiting:** `and` stops when the left side is false; `or`
    stops when the left side is true.
-   Chained comparisons are supported: `0 <= score <= 100`.
-   Ternary expression: `result = "even" if n % 2 == 0 else "odd"`.

## 7. `if`, `elif`, `else`

-   `if` checks the first condition.
-   `elif` checks another condition only if earlier conditions were
    false.
-   `else` runs when no earlier condition is true.
-   Conditions are checked from top to bottom; order matters.
-   Use `==` for equality, not `=`.
-   Include boundary cases: zero, negative values, exact limits, and
    invalid input when relevant.

## 8. `for` Loops and `range()`

-   A `for` loop iterates over items in an iterable, such as a string,
    list, tuple, or `range`.
-   `range(stop)` generates numbers from `0` to `stop - 1`.
-   `range(start, stop, step)` excludes `stop`.
-   Use a `for` loop when iterating over a sequence or a known range.
-   `break` exits the nearest loop; `continue` skips to the next
    iteration.
-   A loop can have an `else` block, which runs if the loop ends without
    `break`.

## 9. `while` Loops

-   A `while` loop repeats while its condition is true.
-   Update the state used by the condition to avoid an accidental
    infinite loop.
-   Use `break` to exit early and `continue` to skip to the next
    iteration.
-   Test zero and boundary values carefully.
-   Use `for` for straightforward iteration; use `while` when repetition
    depends on a changing condition.

## 10. Nested Loops

-   A nested loop is a loop inside another loop.
-   For `n` outer iterations and `m` inner iterations, the body runs
    about `n × m` times: `O(nm)`; if both are `n`, this is `O(n²)`.
-   Common uses: grids, tables, pairs, and simple patterns.
-   Track each loop variable separately and dry-run small inputs.

## 11. Functions and `return`

-   A function is a reusable block defined with `def`.
-   Parameters are names in the function definition; arguments are
    values passed when calling it.
-   `return` sends a result back to the caller and ends that function
    call.
-   `print()` displays a value; it does not return that value to the
    caller.
-   Local variables are generally available only inside the function
    where they are defined.
-   Break large tasks into small functions that have clear inputs and
    outputs.

## 12. Function Arguments

-   **Positional arguments:** matched by position.
-   **Keyword arguments:** matched by parameter name,
    e.g. `greet(name="Mira")`.
-   **Default arguments:** used when an argument is omitted.
-   `*args` collects extra positional arguments into a tuple.
-   `**kwargs` collects extra keyword arguments into a dictionary.
-   Avoid mutable default values such as `items=[]`; use `None` and
    create a new list inside the function.

## 13. Useful Built-ins and Problem-Solving Patterns

-   Useful built-ins: `print()`, `input()`, `len()`, `type()`, `int()`,
    `float()`, `str()`, `range()`, `sum()`, `min()`, `max()`, `abs()`,
    `sorted()`, `enumerate()`.
-   **Counter:** start at `0`, increment when an event occurs.
-   **Sum accumulator:** start at `0`, add each value.
-   **Product accumulator:** start at `1`, multiply each value.
-   **Search flag:** start as `False`, set to `True` when found.
-   Even/odd: `n % 2 == 0`.
-   Last digit of a non-negative integer: `n % 10`.
-   Remove last digit of a non-negative integer: `n // 10`.
-   Reverse digits and digit sum can be built using `% 10` and `// 10`.
-   Test empty inputs, one-item inputs, zeros, negatives, repeated
    values, and boundaries.

## 14. Complexity Basics Before DSA

-   A single basic operation is often described as `O(1)`.
-   Scanning `n` characters/items once is `O(n)`.
-   Two nested loops over `n` items each are commonly `O(n²)`.
-   Complexity depends on the amount of work as input size grows;
    analyze the loop body and number of iterations.
-   These are common patterns, not a guarantee for every operation or
    implementation.

------------------------------------------------------------------------

# Part 2 --- Practice Questions (5 per topic)

**Instructions:** Write and run your own solution. For every solution,
test a normal case and at least one edge case. Questions are
intentionally solution-free so you can practise problem-solving.

## Topic 1: Python Fundamentals, `print()` and Variables

1.  Print your name, age, and city on separate lines.
2.  Create variables for a product name, price, and quantity; print a
    readable bill line.
3.  Swap the values of two variables without creating a third variable.
4.  Create a variable, reassign it to a value of a different type, and
    print `type()` before and after.
5.  Fix the variable names in this snippet so they are valid Python
    names: `2name = "Raj"`, `first-name = "Raj"`, `class = 10`.

## Topic 2: Input, Output and Type Conversion

1.  Ask for a user's name and print a greeting.
2.  Read two integers and print their sum.
3.  Read a price as input and convert it to `float`; print the price
    plus 18% tax.
4.  Read two numbers and print their average.
5.  Ask for a birth year and calculate an approximate age using the
    current year supplied as another input.

## Topic 3: String Basics, Indexing and Slicing

1.  Read a full name and print its length.
2.  Given a word, print its first and last characters safely; handle an
    empty string.
3.  Print the first three characters and the last three characters of a
    string.
4.  Reverse a string using slicing.
5.  Check whether a string is a palindrome after converting it to
    lowercase (first ignore spaces, then try ignoring spaces and
    punctuation).

## Topic 4: String Methods

1.  Take a user-entered name with extra spaces and inconsistent case;
    clean it and display it in title case.
2.  Count how many times a chosen character appears in a string.
3.  Replace every space in a sentence with a hyphen.
4.  Split a comma-separated string of names into a list, remove extra
    spaces from each name, and print each name.
5.  Check whether an email-like string ends with `".com"` and whether a
    supplied code contains only letters and digits. State the
    limitations of these checks.

## Topic 5: Escape Sequences and f-Strings

1.  Print a three-line address using `\\n`.
2.  Print a table-like line with tab-separated name, age, and city using
    `\\t`.
3.  Use an f-string to print a person's name and age.
4.  Use an f-string to show two numbers and their sum in one sentence.
5.  Print a sentence containing both single and double quotation marks
    without causing a syntax error.

## Topic 6: Numbers and Arithmetic Operators

1.  Build a calculator that prints sum, difference, product, quotient,
    floor quotient, and remainder for two numbers; handle division by
    zero.
2.  Check whether an integer is even or odd.
3.  Given a non-negative integer, print its last digit and the number
    after removing its last digit.
4.  Calculate the area of a circle from a radius supplied by the user.
5.  Calculate the sum of the digits of a non-negative integer using a
    loop and `%` / `//`.

## Topic 7: Comparisons

1.  Read two numbers and print whether the first is greater, smaller, or
    equal.
2.  Check whether a number lies in the inclusive range 10 to 50.
3.  Given three numbers, print the largest without using `max()`.
4.  Check whether a string is empty.
5.  Explain and demonstrate the difference between `==` and `is` using
    two equal lists and a `None` check.

## Topic 8: `if`, `elif`, `else`

1.  Read an integer and print whether it is positive, negative, or zero.
2.  Convert a numeric score into grades using clearly stated grade
    boundaries; test exact boundary values.
3.  Read three numbers and print the largest; handle ties.
4.  Check whether a year is a leap year.
5.  Calculate a ticket price based on age bands, with a separate rule
    for children and senior citizens; test each boundary.

## Topic 9: Logical Operators, Chained Comparisons and Ternary

1.  Check whether a number is between 1 and 100 inclusive using a
    chained comparison.
2.  Check whether a person is eligible when both age and ID conditions
    must be met.
3.  Check whether a character is a vowel using `in` and a
    case-insensitive comparison.
4.  Use a ternary expression to label a number as even or odd.
5.  Demonstrate short-circuiting with `and` or `or`; explain why the
    second expression may not run.

## Topic 10: `for` Loops and `range()`

1.  Print numbers from 1 through 10.
2.  Print all even numbers from 2 through 50.
3.  Calculate the sum of numbers from 1 through `n`.
4.  Print a multiplication table for a number supplied by the user.
5.  Count the vowels in a string using a `for` loop.

## Topic 11: Iterating over Strings/Lists and Loop Control

1.  Print each character of a string on a separate line.
2.  Count how many numbers in a list are positive.
3.  Find the first occurrence of a target in a list using a loop and
    `break`.
4.  Print numbers from 1 to 20 but skip multiples of 3 using `continue`.
5.  Search a list using `for-else`; print "not found" only if no `break`
    occurs.

## Topic 12: Nested Loops

1.  Print a 5-by-5 rectangle of stars.
2.  Print a right-angled triangle of stars with `n` rows.
3.  Print a multiplication grid from 1 to 5.
4.  Print all ordered pairs `(i, j)` where both values range from 1 to
    3.
5.  For a list of numbers, print every pair of distinct positions and
    explain why the work grows quadratically.

## Topic 13: `while` Loops

1.  Print numbers from 1 through 10 using `while`.
2.  Keep asking for a password until the correct password is entered
    (use a practice-only password, not a real one).
3.  Repeatedly ask for numbers until the user enters 0, then print their
    sum.
4.  Reverse the digits of a non-negative integer using `%` and `//`.
5.  Create a menu that repeats until the user chooses "exit"; ensure
    every path either updates the condition or exits.

## Topic 14: Functions and `return`

1.  Write `greet(name)` that returns a greeting string; print the
    returned value in the caller.
2.  Write `is_even(n)` that returns `True` or `False`.
3.  Write `max_of_two(a, b)` without using `max()`, including equal
    values.
4.  Write `factorial(n)` for non-negative integers; decide how to handle
    negative input.
5.  Write a function that accepts a list of numbers and returns the sum
    without printing inside the function.

## Topic 15: Positional, Keyword and Default Arguments

1.  Write a `greet(name, greeting="Hello")` function and call it with
    and without the second argument.
2.  Call a function using keyword arguments in a different order from
    its parameter list.
3.  Write `power(base, exponent=2)` and test both the default and custom
    exponent.
4.  Write a function with `*args` that returns the sum of any number of
    numeric arguments.
5.  Write a function with `**kwargs` that prints each key-value pair;
    explain what type `kwargs` is.

## Topic 16: Built-ins and Basic Problem-Solving Patterns

1.  Find the minimum, maximum, and sum of a list using built-ins.
2.  Count occurrences of a target in a list without using
    `list.count()`.
3.  Find the second-largest distinct number in a list; handle duplicates
    and lists with too few distinct values.
4.  Given a list of numbers, build a new list containing only even
    numbers.
5.  Find whether a target exists in a list and return a Boolean result
    rather than printing from the search function.

## Topic 17: Debugging and Edge Cases

1.  Fix a program that uses `=` instead of `==` in a condition.
2.  Fix a program that tries to add an integer directly to the string
    returned by `input()`.
3.  Fix a string-cleaning program that calls `.upper()` but discards the
    returned string.
4.  Find and fix an infinite `while` loop caused by a missing counter
    update.
5.  For a function that divides two numbers, list and test at least four
    edge cases, including a zero denominator.

## Topic 18: Introductory Time Complexity

1.  State the time complexity of printing each item in a list once.
2.  State the time complexity of two nested loops that each run `n`
    times.
3.  Compare a loop that stops at `n` with one that repeatedly halves
    `n`; describe the expected growth.
4.  Count how many times the inner statement executes in a loop with 4
    outer iterations and 3 inner iterations.
5.  Given a short loop, identify the input-size variable, number of
    iterations, and dominant operation.

------------------------------------------------------------------------

# Part 3 --- Roadmap: What to Learn Before Starting DSA

Follow this order. You do not need to master every advanced Python
feature before beginning DSA.

1.  **Syntax and data:** variables, types, `print()`, `input()`,
    conversion.
2.  **Strings:** indexing, slicing, immutability, common methods
    (`strip`, `split`, `join`, `replace`, `find`, `count`, case checks).
3.  **Operators and decisions:** arithmetic, comparisons, `if` / `elif`
    / `else`, logical operators.
4.  **Loops:** `for`, `range`, `while`, `break`, `continue`, nested
    loops, loop dry-runs.
5.  **Functions:** parameters, arguments, `return`, scope, default
    arguments, `*args`, `**kwargs`.
6.  **Core collections:** lists, tuples, sets, dictionaries; indexing,
    iteration, membership, common operations.
7.  **Useful Python patterns:** counters, accumulators, frequency
    counting, searching, min/max, reversing, two pointers after
    arrays/strings are learned.
8.  **Debugging and complexity:** trace variables, test edge cases,
    estimate `O(1)`, `O(n)`, `O(n²)`, and later `O(log n)`.
9.  **Then begin DSA:** arrays/lists and strings → hashing with
    dictionaries/sets → two pointers → sliding window → stack/queue →
    binary search → recursion → linked lists/trees/graphs → heaps and
    dynamic programming.

## Ready to Start DSA When You Can

-   [ ] Write `if` / `elif` / `else` from memory.
-   [ ] Use `for`, `while`, `range`, `break`, and `continue` without
    confusion.
-   [ ] Write a function that takes inputs and returns a result.
-   [ ] Work with strings and common string methods.
-   [ ] Use lists and dictionaries at a basic level.
-   [ ] Solve simple problems involving counting, sums, searching, and
    reversing.
-   [ ] Dry-run code on paper and test empty, single-item, zero,
    negative, and boundary inputs.
-   [ ] Explain the difference between a loop that visits `n` items once
    (`O(n)`) and nested loops (`O(n²)`).

**Practice rule:** attempt each question yourself first. If stuck, write
the input, expected output, and steps in plain English before writing
code. Do not move on based only on reading notes---write and run code.
