# 🐍 Python OOP Master — Fundamentals, Internals, Dunder Methods & Interview Prep

> **One file. One source of truth.** From "what is a class?" to "walk me through what `type.__call__` does when you instantiate a class" — with the code, the internals, the traps, and the interview answers.
>
> Version: **Python 3.12** (notes where behaviour differs across versions) · Target: **Product-based company backend interviews (Python)** · Foundation reference: **[takeUforward OOPS sheet](https://takeuforward.org/prep-hub/oops)** (Java-based — every concept here is re-explained the *Python* way)

---

## 📍 Table of Contents

**Part I — How to use this guide**
- [0.1 How to use this guide](#01-how-to-use-this-guide)
- [0.2 takeUforward syllabus → Python mapping](#02-takeuforward-syllabus--python-mapping)
- [0.3 Java vs Python OOP: the differences that matter](#03-java-vs-python-oop-the-differences-that-matter)
- [0.4 Dependency graph & learning sequence](#04-dependency-graph--learning-sequence)
- [0.5 Study plan](#05-study-plan)
- [0.6 Mentor modes (Learning / Practice / Interview / Revision)](#06-mentor-modes)

**Part II — Foundations**
- [M0. Python foundations for OOP](#m0-python-foundations-for-oop)

**Part III — Core OOP**
- [M1. OOP fundamentals: classes, objects, self, attributes](#m1-oop-fundamentals)
- [M2. Method types: instance, class, static](#m2-method-types)
- [M3. Object relationships: association, aggregation, composition](#m3-object-relationships)
- [M4. Encapsulation](#m4-encapsulation)
- [M5. Abstraction](#m5-abstraction)
- [M6. Inheritance](#m6-inheritance)
- [M7. Polymorphism](#m7-polymorphism)

**Part IV — Python internals (where interviews get deep)**
- [M8. Object creation & lifecycle (`__new__` vs `__init__`)](#m8-object-creation--lifecycle)
- [M9. `super()` and MRO](#m9-super-and-mro)
- [M10. Attribute lookup & descriptors](#m10-attribute-lookup--descriptors)
- [M11. Properties & decorators](#m11-properties--decorators)
- [M12. Dunder methods — the complete data model](#m12-dunder-methods--the-complete-data-model)
- [M13. `__str__` vs `__repr__` — master module](#m13-__str__-vs-__repr__--master-module)
- [M14. Identity, equality, hashing & copying](#m14-identity-equality-hashing--copying)
- [M15. Iterators, generators & context managers](#m15-iterators-generators--context-managers)
- [M16. Exceptions as classes](#m16-exceptions-as-classes)

**Part V — Advanced Python OOP**
- [M17. Advanced OOP: protocols, mixins, DI, metaclasses, dataclasses, slots, generics](#m17-advanced-python-oop)

**Part VI — Design**
- [M18. SOLID principles in Python](#m18-solid-principles-in-python)
- [M19. Design patterns in Python](#m19-design-patterns-in-python)
- [M20. Real-world backend examples](#m20-real-world-backend-examples)

**Part VII — Interview**
- [M21. Interview question bank](#m21-interview-question-bank)
- [M22. Output prediction (42 questions)](#m22-output-prediction)
- [M23. Coding exercises & mock interviews](#m23-coding-exercises--mock-interviews)
- [M24. Mastery tracker & final revision sheet](#m24-mastery-tracker--final-revision-sheet)

---

# PART I — HOW TO USE THIS GUIDE

## 0.1 How to use this guide

### The core belief
Most people learn OOP as **vocabulary** ("encapsulation means data hiding"). Interviewers at product companies test OOP as **mechanics** ("what exactly happens when you write `obj.x`?") and **design** ("model a payment system so new providers can be added without touching existing code"). This guide teaches all three layers:

```
Layer 1: CONCEPT      → what it is, why it exists               (every developer)
Layer 2: MECHANISM    → how Python actually implements it        (strong candidates)
Layer 3: DESIGN       → when to use it, trade-offs, real systems (senior/backend roles)
```

### The 15-part teaching format
Core modules follow this structure (smaller topics merge some parts):

| # | Part | # | Part |
|---|---|---|---|
| 1 | What is it? | 9 | Internal mechanism |
| 2 | Why does it exist? | 10 | Common mistakes |
| 3 | How it works internally | 11 | Comparison |
| 4 | Syntax | 12 | Real-world application |
| 5 | Simple example | 13 | Interview questions |
| 6 | Detailed example | 14 | 🎤 Interview-ready answer |
| 7 | Execution flow | 15 | 📝 Revision notes |
| 8 | Dry run | | |

### Rules for studying
1. **Type every example and run it.** Don't trust your eyes — trust the interpreter. Use `python -i file.py` to poke at objects afterwards.
2. **Predict before you run.** Write your predicted output in a comment, then run. Every wrong prediction is a lesson — log it in the [tracker](#m24-mastery-tracker--final-revision-sheet).
3. **Say the 🎤 interview answers out loud.** Being able to *speak* it in 60 seconds is the bar.
4. **Use the introspection tools constantly:** `type()`, `id()`, `vars()`, `dir()`, `Cls.__mro__`, `Cls.__dict__`, `help()`.

### Legend
| Symbol | Meaning |
|---|---|
| ⭐ | Essential — asked in most Python interviews |
| 🔶 | Important — asked in strong product-company interviews |
| 🔷 | Advanced — senior/internals rounds |
| ⚪ | Rare / specialised — know it exists |
| 🎤 | Interview-ready answer you can speak |
| ⚠️ | Trap / common mistake |

---

## 0.2 takeUforward syllabus → Python mapping

The [takeUforward OOPS sheet](https://takeuforward.org/prep-hub/oops) has **6 modules** taught in Java. Here's where each topic lives in this guide, and what changes in Python.

| TUF module | TUF topics | In this guide | What's different in Python |
|---|---|---|---|
| **1. Introduction to OOPS** | Java basics, What is OOPS, Classes & Objects, Attributes & Methods, Constructors | [M0](#m0-python-foundations-for-oop), [M1](#m1-oop-fundamentals), [M8](#m8-object-creation--lifecycle) | No `new` keyword; construction is split into `__new__` (create) + `__init__` (initialise); explicit `self`; attributes can be added at runtime |
| **2. Core Principles** | Encapsulation, Inheritance, Polymorphism, Abstraction | [M4](#m4-encapsulation)–[M7](#m7-polymorphism) | Encapsulation by convention + name mangling, not enforcement; multiple inheritance with MRO; duck typing; no signature overloading |
| **3. Advanced OOP features** | Access modifiers, Interfaces, `static` keyword, Inner classes | [M4](#m4-encapsulation), [M5](#m5-abstraction), [M2](#m2-method-types), [M3](#m3-object-relationships) | `_x` / `__x` conventions; ABCs & `Protocol` instead of `interface`; `@staticmethod` **and** `@classmethod`; nested classes rarely used |
| **4. Relationships & Object Behaviour** | Association, Aggregation, Composition | [M3](#m3-object-relationships), [M17](#m17-advanced-python-oop) | Same concepts; Python leans heavily on composition + dependency injection |
| **5. Advanced Programming** | Object cloning, Exception handling, Generics, File handling | [M14](#m14-identity-equality-hashing--copying), [M16](#m16-exceptions-as-classes), [M17](#m17-advanced-python-oop), [M15](#m15-iterators-generators--context-managers) | `copy`/`deepcopy` instead of `clone()`; exceptions are class hierarchies; generics are type hints only (no runtime enforcement); files via context managers |
| **6. Design & Lifecycle** | Design principles, Object lifecycle | [M18](#m18-solid-principles-in-python)–[M20](#m20-real-world-backend-examples), [M8](#m8-object-creation--lifecycle) | Reference counting + cyclic GC instead of JVM GC; `__del__` vs `finalize()` |

**Python-specific topics TUF doesn't cover (but Python interviews do):** names vs objects, `__new__`, metaclasses, the descriptor protocol, the complete dunder data model, `__str__`/`__repr__`, `__eq__`/`__hash__` contract, MRO & C3, cooperative `super()`, properties, `__slots__`, dataclasses, protocols, context managers, generators, `__getattr__` vs `__getattribute__`.

---

## 0.3 Java vs Python OOP: the differences that matter

| Concept | Java | Python | Interview one-liner |
|---|---|---|---|
| Creating objects | `new Car()` | `Car()` — calling the class | "A class is a callable; calling it runs `type.__call__`, which runs `__new__` then `__init__`." |
| Constructor | One special method, can be overloaded | `__new__` allocates, `__init__` initialises; no overloading → default args or `@classmethod` alternative constructors | |
| `this` | Implicit | `self` is an **explicit** first parameter (just a convention name) | "`obj.m()` is `type(obj).m(obj)`." |
| Access modifiers | `private`, `protected`, `public` enforced by compiler | Conventions: `_x` (internal), `__x` (name-mangled to `_Class__x`); nothing is truly private | "We're all consenting adults." |
| Interfaces | `interface` keyword | `abc.ABC` + `@abstractmethod` (nominal) or `typing.Protocol` (structural) or plain duck typing | |
| Static members | `static` fields & methods | Class attributes; `@staticmethod` (no implicit arg); `@classmethod` (receives class — Java has no equivalent) | |
| Overloading | Compile-time, by signature | Not supported — last definition wins. Use defaults, `*args/**kwargs`, `functools.singledispatch(method)` | |
| Overriding | `@Override`, `final` prevents | Redefine in subclass; `typing.final`/`@override` (3.12) are type-checker hints only | |
| Multiple inheritance | Classes: no (interfaces only) | Fully supported; resolved via **C3 MRO** | |
| `super` | Calls direct parent | Calls the **next class in the MRO of the instance's type** — may not be the parent! | |
| Abstract class | `abstract class` | Subclass of `ABC` with ≥1 `@abstractmethod`; instantiation raises `TypeError` | |
| Generics | Compile-time, erased at runtime | Type hints (`list[int]`, `TypeVar`, PEP 695 `class Box[T]`); only checked by tools like mypy | |
| Equality | `.equals()` + `hashCode()` | `__eq__` + `__hash__`; defining `__eq__` alone makes instances **unhashable** | |
| `toString()` | One method | `__str__` (users) and `__repr__` (developers) | |
| Destructor | `finalize()` (deprecated) | `__del__` (unreliable timing); use context managers | |
| Cloning | `clone()`, `Cloneable` | `copy.copy`, `copy.deepcopy`, `__copy__`, `__deepcopy__` | |
| Inner classes | Inner classes capture outer `this` | Nested classes do **not** capture the outer instance; mostly used for namespacing | |
| Everything is an object | Primitives aren't | Literally everything: ints, functions, classes, modules | |
| Classes at runtime | Fixed at compile time | Classes are objects created at runtime by a metaclass (`type`) and can be modified | |

---

## 0.4 Dependency graph & learning sequence

```text
M0 Python foundations (names, references, mutability, functions, closures, decorators)
 │
 ▼
M1 Classes, objects, self, attributes, namespaces  ──►  M2 Method types
 │                                                         │
 ├──► M3 Relationships (association/aggregation/composition)
 │                                                         │
 ▼                                                         ▼
M4 Encapsulation ──► M5 Abstraction ──► M6 Inheritance ──► M7 Polymorphism
 │                                          │
 │                    ┌─────────────────────┘
 ▼                    ▼
M8 Object lifecycle  M9 super() & MRO
 │                    │
 └────────┬───────────┘
          ▼
M10 Attribute lookup & descriptors ──► M11 Properties & decorators
          │
          ▼
M12 Dunder data model ──► M13 str vs repr ──► M14 Equality/hashing/copying ──► M15 Iterators/context managers
          │                                                                         │
          ▼                                                                         ▼
M16 Exceptions as classes ──────────────────────────────────────────────► M17 Advanced OOP (protocols, metaclasses, dataclasses, slots)
                                                                                    │
                                                                                    ▼
                                                     M18 SOLID ──► M19 Design patterns ──► M20 Real-world backend examples
                                                                                    │
                                                                                    ▼
                                                     M21–M23 Interview bank, output prediction, mocks
```

### Why this order is correct
- **M0 before everything:** 80% of "weird" OOP behaviour (shared class lists, `self.x` shadowing, mutable defaults, `is` vs `==`) is actually *names-and-references* behaviour. Learn it once, and OOP stops being surprising.
- **Encapsulation before abstraction:** properties (encapsulation) are needed for abstract properties.
- **Inheritance before polymorphism:** overriding is the most common form of polymorphism.
- **MRO before descriptors:** attribute lookup walks the MRO; you can't explain lookup without it.
- **Descriptors before properties/dunders:** `@property`, `@classmethod`, `@staticmethod`, and even bound methods *are* descriptors — learning descriptors makes all of them one idea.
- **Dunders before SOLID/patterns:** patterns in Python use `__call__`, `__getattr__` (proxies), `__iter__` (iterator), context managers.
- **Design last:** you can't judge "composition vs inheritance" until you know both mechanically.

---

## 0.5 Study plan

Designed to run **alongside** your DSA and system design prep (≈ 45–60 min/day for OOP).

| Week | Modules | Exit criteria |
|---|---|---|
| 1 | M0, M1, M2 | Explain names vs objects; class vs instance attribute shadowing; three method types with code |
| 2 | M3, M4, M5 | Write a class with validated properties; an ABC and a Protocol; explain name mangling |
| 3 | M6, M7, M9 | Predict any diamond-inheritance `super()` output; compute an MRO by hand with C3 |
| 4 | M8, M10, M11 | Explain `type.__call__` → `__new__` → `__init__`; full attribute lookup order; write a descriptor |
| 5 | M12, M13, M14 | Implement a Vector and a custom collection; explain the `__eq__`/`__hash__` contract |
| 6 | M15, M16, M17 | Write iterator, generator, context manager (sync + async); dataclasses, slots, metaclass basics |
| 7 | M18, M19 | Refactor bad code using each SOLID principle; implement 10 core patterns from memory |
| 8 | M20–M23 | Two LLD case studies end-to-end; 42/42 output predictions; 4 mock interviews |

> **Falling behind?** Never skip M0, M1, M6, M8, M9, M12, M13, M14 — they're the highest-yield interview modules. Patterns can be done at "core 10" depth (Singleton, Factory, Builder, Adapter, Decorator, Facade, Proxy, Strategy, Observer, Template Method).

---

## 0.6 Mentor modes

Paste these into any AI chat to use this README interactively.

**📘 Learning mode**
```text
I'm studying <TOPIC> from my Python OOP Master README.
Teach it in this order: concept → why it exists → how Python implements it internally →
smallest code example → dry run with execution order → 3 interview questions.
Stop after each step and ask me one check question before continuing.
```

**🛠 Practice mode**
```text
Give me one <easy|medium|hard> exercise on <TOPIC>: a coding task, an output-prediction
snippet, or a debugging task. Do NOT show the solution.
Give progressive hints only when I type "hint" (max 4).
When I submit, review correctness, Pythonic style, edge cases, and one follow-up.
```

**🎤 Interview mode**
```text
Act as a senior backend interviewer at a product company. Ask me Python OOP questions on
<TOPICS>, one at a time, starting medium and going deeper with follow-ups based on my answers.
After each answer score me 1-5 on: correctness, depth (internals), clarity, follow-up readiness.
Tell me exactly what a strong candidate would have added.
```

**🔁 Revision mode**
```text
Quiz me rapid-fire on <TOPICS>: 5 flash questions, 3 output predictions, 2 "compare X vs Y".
Track which I miss and re-ask those at the end in a different form.
```

---

# PART II — FOUNDATIONS

## M0. Python Foundations for OOP

> **Why this module matters:** almost every "surprising" OOP behaviour in Python — shared mutable class attributes, `self.count += 1` not updating the class, mutable default arguments, `is` vs `==`, shallow copies — is explained by **three facts**:
> 1. Variables are **names** bound to **objects**; they're not boxes holding values.
> 2. Some objects can change (**mutable**), some can't (**immutable**).
> 3. Assignment **never copies** — it binds another name to the same object.

### M0.1 Names, objects, references

**What is it?** In Python, every value is an **object** living in memory. Every object has:
- an **identity** (`id(obj)` — unique while it's alive; in CPython it's the memory address),
- a **type** (`type(obj)` — decides what it can do),
- a **value**.

A **variable** is just a **name** in a namespace (a dict-like table) that **refers** to an object.

```python
a = [1, 2, 3]     # create a list object, bind name 'a' to it
b = a             # bind name 'b' to the SAME object (no copy!)
b.append(4)
print(a)          # [1, 2, 3, 4]  ← one object, two names
print(a is b)     # True          ← same identity
```
```text
   namespace            heap
  ┌─────────┐      ┌──────────────┐
  │ a  ─────┼─────►│ [1, 2, 3, 4] │  id=0x7f...
  │ b  ─────┼─────►│              │
  └─────────┘      └──────────────┘
```

**Rebinding vs mutating** — the single most important distinction:
```python
x = [1, 2]
y = x
y = y + [3]      # REBINDING: builds a NEW list, binds y to it; x untouched
print(x, y)      # [1, 2] [1, 2, 3]

x = [1, 2]
y = x
y += [3]         # MUTATING: list.__iadd__ extends in place; x sees it
print(x, y)      # [1, 2, 3] [1, 2, 3]
```

### M0.2 Mutable vs immutable

| Immutable (value can't change) | Mutable (value can change in place) |
|---|---|
| `int`, `float`, `bool`, `complex`, `str`, `bytes`, `tuple`, `frozenset`, `None` | `list`, `dict`, `set`, `bytearray`, most user-defined objects |

"Changing" an immutable object really creates a new one:
```python
s = "hi"
print(id(s))
s += "!"         # new str object; name s rebound
print(id(s))     # different id
```
⚠️ A tuple is immutable, but if it **contains** a mutable object, that inner object can still change: `t = ([1],); t[0].append(2)` → `([1, 2],)`.

### M0.3 Identity vs equality: `is`, `==`, `id()`

| Operator | Asks | Implemented by |
|---|---|---|
| `a is b` | Same object? (`id(a) == id(b)`) | Cannot be overridden |
| `a == b` | Equal values? | `a.__eq__(b)` (see [M14](#m14-identity-equality-hashing--copying)) |

```python
a = [1, 2]; b = [1, 2]
print(a == b, a is b)   # True False
```
- Use `is` **only** for singletons: `x is None`, `x is True`, sentinels.
- ⚠️ `256 is 256`-style tricks depend on CPython's small-int cache and string interning — an implementation detail. Never rely on it.

### M0.4 Functions are objects (first-class functions)
```python
def greet(name): return f"Hello {name}"

say = greet                     # another name for the same function object
print(say("Parth"))             # Hello Parth
print(type(greet))              # <class 'function'>
print(greet.__name__)           # greet
handlers = {"greet": greet}     # stored in a dict
def apply(f, v): return f(v)    # passed as an argument
```
This matters for OOP because **methods are just functions stored in a class**, and decorators like `@property` are functions that take functions.

### M0.5 Parameters: positional, keyword, defaults, `*args`, `**kwargs`
```python
def f(a, b=2, *args, c, d=4, **kwargs):
    print(a, b, args, c, d, kwargs)

f(1, 5, 6, 7, c=3, e=9)    # 1 5 (6, 7) 3 4 {'e': 9}

def g(a, b, /, c, *, d):   # a, b positional-only; d keyword-only
    ...
```
`*args`/`**kwargs` are how Python replaces Java-style overloading and how cooperative `super().__init__(**kwargs)` works ([M9](#m9-super-and-mro)).

### M0.6 ⚠️ Mutable default arguments
Default values are evaluated **once**, when the `def` statement runs — not on each call.
```python
def add_item(item, bucket=[]):     # ONE list created at def time
    bucket.append(item)
    return bucket

print(add_item(1))   # [1]
print(add_item(2))   # [1, 2]   ← same list reused!

def add_item(item, bucket=None):   # ✅ fix
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
```
Same trap in `__init__(self, items=[])` — every instance would share the list.

### M0.7 Scope: LEGB, `global`, `nonlocal`
Name lookup order: **L**ocal → **E**nclosing function → **G**lobal (module) → **B**uilt-ins.
```python
x = "global"
def outer():
    x = "enclosing"
    def inner():
        nonlocal x          # rebind the enclosing x (without this, assignment makes a new local)
        x = "changed"
    inner()
    print(x)                # changed
outer()
print(x)                    # global
```
⚠️ **Class bodies are NOT an enclosing scope for methods.** Inside a method, a bare name `count` does not find the class attribute `count`; you must write `self.count` or `ClassName.count`.
```python
class C:
    count = 0
    def show(self):
        return count        # NameError! class scope is skipped by LEGB
```

### M0.8 Closures
A closure is a function that remembers variables from its enclosing scope even after that scope has finished.
```python
def make_counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

c = make_counter()
print(c(), c(), c())   # 1 2 3
```
Closures are "objects with one method" — a stateful callable. (Classes with `__call__` are the OOP version — [M12-D](#category-d-callable-objects--__call__).)

⚠️ **Late binding:** closures look up variables when **called**, not when defined.
```python
fns = [lambda: i for i in range(3)]
print([f() for f in fns])          # [2, 2, 2]
fns = [lambda i=i: i for i in range(3)]
print([f() for f in fns])          # [0, 1, 2]  ← default arg captures current value
```

### M0.9 Decorators (basics)
A decorator is a callable that takes a function and returns a replacement.
```python
import functools, time

def timer(func):
    @functools.wraps(func)                 # keep func's name/docstring
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.4f}s")
        return result
    return wrapper

@timer               # same as: slow = timer(slow)
def slow(): time.sleep(0.1)
```
Full treatment (decorators with arguments, class decorators, method decorators) in [M11](#m11-properties--decorators).

### M0.10 Type hints
Type hints document intent and enable static checkers (mypy, pyright). **Python ignores them at runtime.**
```python
from typing import Optional
def find_user(user_id: int) -> Optional[dict]:   # or: dict | None  (3.10+)
    ...
find_user("abc")   # runs fine at runtime! only a type checker would complain
```

### M0.11 Built-in collections recap (OOP-relevant facts)
| Type | Mutable | Hashable (usable as dict key / set item) | Ordered |
|---|---|---|---|
| `list` | ✅ | ❌ | ✅ |
| `tuple` | ❌ | ✅ if all items hashable | ✅ |
| `dict` | ✅ | ❌ | ✅ insertion order (3.7+) |
| `set` | ✅ | ❌ | ❌ |
| `frozenset` | ❌ | ✅ | ❌ |

### 🎤 Interview-ready answer: "Is Python pass-by-value or pass-by-reference?"
> "Neither, exactly — it's **pass-by-object-reference** (call by sharing). The function parameter becomes a new name bound to the same object the caller passed. If the object is mutable and the function mutates it, the caller sees the change. If the function *rebinds* the parameter to a new object, the caller's name is unaffected."

### 📝 Revision notes
```
names → objects; assignment binds, never copies
mutate (append, +=, setattr) vs rebind (=, x = x + y)
is = identity (use for None); == = __eq__
defaults evaluated ONCE → never use mutable defaults
LEGB; class body is NOT an enclosing scope for methods
closures late-bind; decorators = function in, function out (use functools.wraps)
type hints are not enforced at runtime
```

---

# PART III — CORE OOP

## M1. OOP Fundamentals

### 1. What is OOP?
**Object-Oriented Programming** organises code around **objects** — bundles of **state** (data/attributes) and **behaviour** (methods) — instead of around loose functions operating on loose data.

**Analogy:** a `BankAccount` object is like a physical passbook *plus* the bank clerk who's the only one allowed to update it. You don't edit the balance directly; you ask the account to `deposit()`, and it enforces the rules.

### 2. Why does it exist? Procedural vs OOP
```python
# PROCEDURAL: data and functions are separate; anyone can break the rules
account = {"owner": "Parth", "balance": 100}
def withdraw(acc, amount):
    acc["balance"] -= amount          # no validation; any code can also do acc["balance"] = -999

# OOP: data + the rules that protect it live together
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def withdraw(self, amount):
        if amount <= 0 or amount > self._balance:
            raise ValueError("Invalid amount")
        self._balance -= amount

    @property
    def balance(self):
        return self._balance
```
| Concern | Procedural | OOP |
|---|---|---|
| Where are rules enforced? | Everywhere data is used (duplicated) | In one class |
| Adding a new variant (SavingsAccount) | `if type == ...` everywhere | New subclass / strategy |
| Modelling real domains | Awkward at scale | Natural (User, Order, Payment) |
| Small scripts | Simpler ✅ | Overkill |

Python is **multi-paradigm**: use OOP where modelling state + behaviour helps; plain functions are fine elsewhere.

### 3. Classes and objects
- A **class** is a blueprint/factory. In Python, **a class is itself an object** (an instance of `type`).
- An **object (instance)** is a concrete thing built from the class.

```python
class Dog:
    species = "Canis familiaris"          # class attribute: shared by all dogs

    def __init__(self, name, age):        # initialiser: sets up a new instance
        self.name = name                  # instance attributes: per-dog
        self.age = age

    def bark(self):                       # instance method: behaviour
        return f"{self.name} says woof"

d1 = Dog("Bruno", 3)
d2 = Dog("Tiger", 5)
print(d1.bark())              # Bruno says woof
print(d1.species, d2.species) # Canis familiaris Canis familiaris
print(type(d1))               # <class '__main__.Dog'>
print(type(Dog))              # <class 'type'>   ← the class is an object too
```

### 4. `self` — what it really is
`self` is **not a keyword**. It's the conventional name for the first parameter of an instance method, which receives the instance.

```python
d1.bark()          # what you write
Dog.bark(d1)       # what effectively happens
```
**Internal mechanism:** `d1.bark` looks up `bark` on the class, finds a **function**, and because functions are **descriptors** ([M10](#m10-attribute-lookup--descriptors)), accessing it through an instance produces a **bound method** that remembers `d1`. Calling the bound method inserts `d1` as the first argument.
```python
m = d1.bark
print(m)                     # <bound method Dog.bark of <__main__.Dog object at 0x...>>
print(m.__self__ is d1)      # True
print(m.__func__ is Dog.bark)# True
```
Why explicit `self`? "Explicit is better than implicit" — it makes instance access (`self.x`) visually distinct from local variables, and it lets methods be called as plain functions (`Dog.bark(d1)`).

### 5. Instance attributes vs class attributes
| | Instance attribute | Class attribute |
|---|---|---|
| Defined | `self.x = ...` (usually in `__init__`) | In the class body |
| Stored in | `obj.__dict__` | `Class.__dict__` |
| Shared? | No — one per object | Yes — one for the class |
| Use for | Per-object state | Constants, defaults, counters, config |

**Lookup rule (simplified):** `obj.x` checks `obj.__dict__` first, then the class, then base classes (full rules in [M10](#m10-attribute-lookup--descriptors)).

**Shadowing:** assigning `obj.x = ...` **always** writes to the instance dict; it never modifies the class attribute.
```python
class Config:
    timeout = 30

a, b = Config(), Config()
a.timeout = 5                 # creates an INSTANCE attribute on a; shadows the class one
print(a.timeout, b.timeout, Config.timeout)   # 5 30 30
Config.timeout = 60
print(a.timeout, b.timeout)   # 5 60   ← b still reads the class attribute
del a.timeout
print(a.timeout)              # 60     ← shadow removed, class attribute visible again
```

⚠️ **Trap 1 — mutable class attribute is shared:**
```python
class Team:
    members = []                    # ONE list for the whole class
    def add(self, name):
        self.members.append(name)   # mutation, not assignment → modifies the shared list

t1, t2 = Team(), Team()
t1.add("A")
print(t2.members)                   # ['A']  😱
# Fix: create per-instance state in __init__:  self.members = []
```

⚠️ **Trap 2 — `self.count += 1` creates an instance attribute:**
```python
class Counter:
    count = 0
    def __init__(self):
        self.count += 1             # reads class 0, writes INSTANCE attr = 1
c1, c2 = Counter(), Counter()
print(Counter.count, c1.count)      # 0 1
# Fix: Counter.count += 1   (or type(self).count += 1 to respect subclasses)
```

### 6. Namespaces, `__dict__`, `vars()`, `dir()`
```python
class P:
    kind = "point"
    def __init__(self, x): self.x = x
    def norm(self): return abs(self.x)

p = P(3)
print(p.__dict__)          # {'x': 3}                      ← instance namespace
print(vars(p))             # {'x': 3}                      ← same thing
print('kind' in P.__dict__, 'norm' in P.__dict__)   # True True
print(type(P.__dict__))    # <class 'mappingproxy'>        ← read-only view of class namespace
print('x' in dir(p), 'kind' in dir(p), 'norm' in dir(p))  # True True True  ← dir() includes inherited names
```
- `obj.__dict__` / `vars(obj)`: only attributes stored **on that object**.
- `dir(obj)`: everything reachable — instance, class, bases (sorted list; customisable via `__dir__`).
- Objects using `__slots__` have no `__dict__` ([M17](#m17-advanced-python-oop)).

**Dynamic attributes:** Python lets you add attributes at runtime (`p.y = 10`). Powerful, but adding attributes outside `__init__` makes classes hard to reason about — avoid in production code (linters flag it).

### 7. `type()`, `isinstance()`, `issubclass()`
```python
class Animal: pass
class Cat(Animal): pass
c = Cat()
print(type(c) is Cat, type(c) is Animal)   # True False   ← exact type only
print(isinstance(c, Animal))               # True         ← respects inheritance
print(isinstance(c, (int, Animal)))        # True         ← tuple of types
print(issubclass(Cat, Animal))             # True
print(issubclass(Cat, object))             # True         ← everything inherits object
```
✅ Prefer `isinstance` over `type(x) == C` (it respects subclasses/Liskov). Better still: don't check types at all — rely on duck typing or polymorphism ([M7](#m7-polymorphism)).

### 8. Object identity, state, behaviour
- **Identity:** `id(obj)` / `is` — which object.
- **State:** the values in its attributes at a moment in time.
- **Behaviour:** the methods it responds to.
Two objects can have equal state but different identity (`a == b` but `a is not b`).

### Common mistakes
- Forgetting `self` in a method definition → `TypeError: ... takes 0 positional arguments but 1 was given`.
- Forgetting `self.` when reading an attribute inside a method → `NameError`.
- Mutable class attributes used as per-instance state.
- Creating attributes outside `__init__`.

### 🎤 Interview-ready answer: "What is `self`?"
> "`self` is the conventional name for the first parameter of an instance method. When I call `obj.method(arg)`, Python looks up `method` on the class; since functions are descriptors, accessing it through the instance creates a bound method with `obj` attached, and calling it passes `obj` as the first argument — so it's equivalent to `Class.method(obj, arg)`. It's explicit by design, which is why instance attributes are always written as `self.x`."

### 🎤 "Class attribute vs instance attribute?"
> "Class attributes live in the class's `__dict__` and are shared; instance attributes live in each object's `__dict__`. Reads look in the instance first, then the class and its MRO. Writes through an instance always create or update an instance attribute, so `self.count += 1` shadows the class attribute instead of updating it. The classic bug is a mutable class attribute like a list, which all instances end up sharing."

### 📝 Revision notes
```
class = object (instance of type) ; instance = object built by calling the class
obj.m(a) == type(obj).m(obj, a) via bound method (functions are descriptors)
reads: instance __dict__ → class → bases ; writes via instance → instance __dict__
mutable class attr = shared ; self.x += 1 shadows class attr
vars/__dict__ = own attrs ; dir = everything reachable
isinstance > type() == ; prefer duck typing
```

---

## M2. Method Types

### Overview
| Method type | Decorator | First argument (automatic) | Can access instance state | Can access class state | Typical use |
|---|---|---|---|---|---|
| Instance method | none | `self` (the instance) | ✅ | ✅ via `self.__class__` / `type(self)` | Behaviour that uses or changes object state |
| Class method | `@classmethod` | `cls` (the class it was called on) | ❌ (no instance) | ✅ | Alternative constructors, class-level config, factories that respect subclasses |
| Static method | `@staticmethod` | nothing | ❌ | ❌ (unless you hard-code the class name) | Utility logically related to the class |

### Instance methods
```python
class Order:
    tax_rate = 0.18
    def __init__(self, amount): self.amount = amount
    def total(self):                         # needs instance state
        return self.amount * (1 + self.tax_rate)
```
`Order(100).total()` → bound method → `Order.total(order_instance)`.

### Class methods — alternative constructors & inheritance-aware factories
```python
from datetime import date

class User:
    def __init__(self, name, birth_year):
        self.name, self.birth_year = name, birth_year

    @classmethod
    def from_csv(cls, line):                  # alternative constructor
        name, year = line.split(",")
        return cls(name, int(year))           # cls, NOT User → works for subclasses

    @classmethod
    def from_age(cls, name, age):
        return cls(name, date.today().year - age)

class Admin(User): pass

a = Admin.from_csv("Parth,2003")
print(type(a).__name__)                       # Admin   ← cls was Admin
```
**Why `cls` matters:** if `from_csv` hard-coded `User(...)`, `Admin.from_csv` would return a `User` — a subtle Liskov violation. This is the Python answer to Java's overloaded constructors (e.g., `dict.fromkeys`, `datetime.fromtimestamp`, `int.from_bytes` are all classmethods).

### Static methods
```python
class Password:
    @staticmethod
    def is_strong(pw: str) -> bool:           # no self/cls needed
        return len(pw) >= 8 and any(c.isdigit() for c in pw)

print(Password.is_strong("abc12345"))         # True  (callable on class...)
print(Password().is_strong("abc"))            # False (...or instance)
```
**When to use:** the function conceptually belongs to the class's namespace (validation, parsing helpers) and doesn't need class or instance.
**When not:** if it doesn't relate to the class at all, a module-level function is more Pythonic. If you find yourself writing `ClassName.something` inside it, it should be a `@classmethod`.

### Internal mechanism (preview of [M10](#m10-attribute-lookup--descriptors))
All three are **descriptors** stored in the class `__dict__`:
| Stored object | `obj.m` returns | `Cls.m` returns |
|---|---|---|
| plain function | bound method (bound to `obj`) | the plain function |
| `classmethod(f)` | method bound to `type(obj)` | method bound to `Cls` |
| `staticmethod(f)` | `f` unchanged | `f` unchanged |

```python
class Demo:
    def inst(self): ...
    @classmethod
    def cm(cls): ...
    @staticmethod
    def sm(): ...

d = Demo()
print(type(Demo.__dict__['cm']).__name__, type(Demo.__dict__['sm']).__name__)  # classmethod staticmethod
print(d.cm.__self__ is Demo)    # True — bound to the class even when called on an instance
print(Demo.sm is d.sm)          # True — plain function, nothing bound
```

### Inheritance behaviour
```python
class Base:
    registry_name = "base"
    @classmethod
    def describe(cls): return f"{cls.__name__}:{cls.registry_name}"
    @staticmethod
    def helper(): return "static"

class Child(Base):
    registry_name = "child"

print(Base.describe(), Child.describe())   # Base:base Child:child  ← cls follows the caller
print(Child.helper())                      # static                 ← inherited, no binding
```
All three can be overridden in subclasses. Overriding a classmethod with a regular method (or vice versa) works but is confusing — keep kinds consistent.

### Common mistakes
- Forgetting `@classmethod` and wondering why `cls` is an instance.
- Using `@staticmethod` then hard-coding the class name (breaks subclasses → use `@classmethod`).
- Thinking `@staticmethod` is "faster" or "more efficient" — the difference is negligible; choose by meaning.

### 🎤 Interview-ready answer: "Instance vs class vs static method?"
> "An instance method receives the instance as `self` and works with per-object state. A classmethod receives the class as `cls` — whichever class it was called on, so it's subclass-aware — and is the idiomatic way to write alternative constructors like `from_json`. A staticmethod receives nothing automatically; it's just a function namespaced inside the class. Internally all three are descriptors: functions bind to the instance, classmethod binds to the class, and staticmethod returns the raw function."

### 📝 Revision notes
```
instance: self ; classmethod: cls (caller's class → subclass-aware) ; staticmethod: nothing
alternative constructors → @classmethod returning cls(...)
static = namespaced utility; if it references the class name → make it classmethod
all three are descriptors in Class.__dict__
```

---

## M3. Object Relationships

### What & why
Objects collaborate. How strongly they're tied determines coupling, lifecycle, and testability.

| Relationship | Meaning | Lifecycle | Strength | UML | Example |
|---|---|---|---|---|---|
| **Association** | "uses / knows about" | Independent | Weak | `A ——> B` | `Teacher` teaches `Student`s |
| **Aggregation** | "has-a", parts can exist alone | Part outlives whole | Medium | `A ◇——> B` | `Department` has `Employee`s |
| **Composition** | "owns", part can't exist without the whole | Part created/destroyed with whole | Strong | `A ◆——> B` | `Order` owns its `OrderLine`s |
| **Inheritance** | "is-a" | — | Strongest coupling | `B ——▷ A` | `SavingsAccount` is an `Account` |
| **Dependency** | Uses temporarily (parameter/local) | — | Weakest | `A - - -> B` | `ReportService.generate(db)` |

```python
class Employee:
    def __init__(self, name): self.name = name

class Department:                        # AGGREGATION: employees passed in, live independently
    def __init__(self, name, employees: list[Employee]):
        self.name = name
        self.employees = employees

class OrderLine:
    def __init__(self, sku, qty, price): self.sku, self.qty, self.price = sku, qty, price

class Order:                             # COMPOSITION: Order creates and owns its lines
    def __init__(self):
        self._lines: list[OrderLine] = []
    def add_line(self, sku, qty, price):
        self._lines.append(OrderLine(sku, qty, price))   # created inside, never shared
    def total(self):
        return sum(l.qty * l.price for l in self._lines)

class Teacher:                           # ASSOCIATION: interacts, no ownership
    def grade(self, student, marks): student.marks = marks
```
**Python note:** Python can't enforce lifecycles; the distinction is **design intent** — who creates the object, who holds the only reference, and what happens when the container goes away.

### Nested (inner) classes
```python
class LinkedList:
    class _Node:                         # namespacing: only meaningful inside LinkedList
        __slots__ = ("val", "next")
        def __init__(self, val, nxt=None): self.val, self.next = val, nxt
    def __init__(self): self.head = None
    def push(self, v): self.head = self._Node(v, self.head)
```
⚠️ Unlike Java inner classes, a Python nested class **does not** have access to an outer instance. It's just a class stored as a class attribute. Use it for namespacing; prefer module-level classes otherwise.

### 🎤 "Aggregation vs composition?"
> "Both are has-a relationships. In composition the whole owns the part's lifecycle — an `Order` creates its `OrderLine`s and they're meaningless without it. In aggregation the parts exist independently and are just referenced — a `Department` holds `Employee`s that existed before and survive after it. In Python this is design intent rather than something the language enforces: I show it by who constructs the object and whether references are shared."

---

## M4. Encapsulation

### 1. What is it?
**Encapsulation** = bundling data with the methods that operate on it, **and** controlling how that data is accessed and changed so the object's **invariants** (rules that must always be true, e.g. `balance >= 0`) can't be broken from outside.

### 2. Why does it exist?
- Protect invariants (no negative balance, valid email).
- Hide implementation details so they can change without breaking callers.
- Give one place for validation, logging, caching.

### 3. How Python does it (very different from Java)
Python has **no enforced access modifiers**. It uses **conventions** plus one mechanism (name mangling):

| Style | Example | Meaning | Enforced? |
|---|---|---|---|
| Public | `self.name` | Part of the API | — |
| "Protected" (internal) | `self._name` | "Internal; don't touch from outside unless you know what you're doing." Not imported by `from module import *` (module-level names) | ❌ convention only |
| "Private" (name-mangled) | `self.__name` | Renamed to `self._ClassName__name` to avoid **accidental clashes in subclasses** | ⚠️ only renaming |
| Dunder | `__init__` | Reserved for Python's special methods — never invent your own | — |

### Name mangling — internal mechanism
Inside a class body, any identifier of the form `__name` (at least two leading underscores, **at most one trailing underscore**) is textually rewritten at compile time to `_ClassName__name`.
```python
class Account:
    def __init__(self):
        self.__pin = 1234          # stored as _Account__pin

a = Account()
print(a.__dict__)                  # {'_Account__pin': 1234}
try:
    print(a.__pin)                 # outside the class: no rewriting → attribute doesn't exist
except AttributeError as e:
    print("AttributeError")
print(a._Account__pin)             # 1234  ← still reachable: NOT real privacy
```
**Its real purpose — avoiding subclass collisions:**
```python
class Base:
    def __init__(self): self.__id = "base"          # _Base__id
    def base_id(self): return self.__id             # reads _Base__id

class Child(Base):
    def __init__(self):
        super().__init__()
        self.__id = "child"                          # _Child__id — doesn't overwrite Base's

c = Child()
print(c.base_id())          # base   ← Base's internal state is safe from Child
print(sorted(vars(c)))      # ['_Base__id', '_Child__id']
```
Dunder names (`__init__`, `__len__`) are **not** mangled because they end with two underscores.

### 4. Getters/setters → the Pythonic way: `@property`
**Bad (Java-style):**
```python
class Temperature:
    def __init__(self, c): self._c = c
    def get_celsius(self): return self._c
    def set_celsius(self, v):
        if v < -273.15: raise ValueError("below absolute zero")
        self._c = v
# callers: t.set_celsius(t.get_celsius() + 1)   ← noisy
```
**Improved (Pythonic):** start with a plain public attribute; when you need validation, switch to a property — **callers don't change**.
```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius            # goes through the setter → validated even at construction

    @property
    def celsius(self):                    # getter: t.celsius
        return self._celsius

    @celsius.setter
    def celsius(self, value):             # setter: t.celsius = 30
        if value < -273.15:
            raise ValueError("below absolute zero")
        self._celsius = value

    @celsius.deleter
    def celsius(self):                    # deleter: del t.celsius
        del self._celsius

    @property
    def fahrenheit(self):                 # computed, read-only attribute
        return self._celsius * 9 / 5 + 32

t = Temperature(25)
t.celsius += 5
print(t.celsius, t.fahrenheit)            # 30 86.0
try:
    t.fahrenheit = 100
except AttributeError:
    print("read-only")                    # read-only
```
Why this is a big deal: in Java you write getters "just in case" because changing a field to a method breaks callers. In Python, **property lets you upgrade an attribute to managed access without breaking the API** — so start simple.

### 5. Common misconceptions
- ❌ "`__x` makes it private." → It only renames to prevent clashes.
- ❌ "Encapsulation = getters and setters." → It's about protecting invariants; properties are just one tool.
- ❌ "Use `__x` everywhere." → Use `_x` by default; `__x` only when designing for inheritance and clashes are a real risk.

### 6. Encapsulation vs abstraction
| | Encapsulation | Abstraction |
|---|---|---|
| Focus | **Protecting** internal state | **Hiding complexity** behind a simple interface |
| Question | "How do I stop misuse of my data?" | "What does the caller need to know?" |
| Tools | `_x`, `__x`, properties, validation | ABCs, Protocols, clean public methods |
| Example | `balance` can only change via `deposit()` | `PaymentGateway.charge()` hides HTTP, retries, signing |

### 7. Real-world backend applications
- Domain models validating invariants (`Order.status` transitions only via `order.ship()`).
- Config objects exposing read-only properties.
- SDK clients hiding `_session`, `_retry_policy`.
- Django model properties for computed fields (`full_name`).

### 13. Interview questions
| Question | Follow-up |
|---|---|
| How do you make an attribute private in Python? | Can it still be accessed? How? |
| What is name mangling and why does it exist? | Does it apply to `__init__`? |
| Why prefer `@property` over getters/setters? | How would you make an attribute read-only? |
| Is `_x` enforced anywhere? | `from module import *` behaviour |

### 🎤 Interview-ready answer
> "Encapsulation means keeping state and the behaviour that guards it together, so invariants can't be violated from outside. Python doesn't enforce access modifiers: a single underscore signals 'internal', and a double underscore triggers name mangling to `_ClassName__attr`, which exists mainly to prevent accidental clashes in subclasses, not for security. For controlled access I use `@property` with setters for validation and computed or read-only attributes — and because properties keep the attribute syntax, I can start with a plain attribute and add validation later without changing callers."

### 📝 Revision notes
```
_x = internal by convention ; __x → _Class__x (anti-clash, not security) ; __x__ not mangled
@property / .setter / .deleter → validation, computed, read-only
start with public attrs; upgrade to property later without breaking callers
encapsulation protects state; abstraction hides complexity
```

---

## M5. Abstraction

### 1. What is it?
**Abstraction** = exposing **what** an object does while hiding **how**. Callers depend on a small, stable interface (`storage.save(key, data)`) instead of implementation details (S3 SDK calls, local filesystem paths).

### 2. Why does it exist?
- Swap implementations (S3 ↔ local disk ↔ in-memory fake for tests).
- Reduce cognitive load: callers learn one interface.
- Enforce that every implementation provides required behaviour.

### 3. Three ways to express an interface in Python
| Mechanism | Typing style | Checked when | Requires inheritance? | Best for |
|---|---|---|---|---|
| **Duck typing** | Implicit | At call time (AttributeError) | No | Small scripts, flexible APIs |
| **ABC** (`abc.ABC` + `@abstractmethod`) | **Nominal** (by declared parent) | **At instantiation** | Yes (or `register`) | Frameworks, shared base behaviour, enforcing implementations |
| **`typing.Protocol`** | **Structural** (by shape) | By type checker (static); optionally `isinstance` with `@runtime_checkable` | No | Decoupled interfaces, third-party classes you can't modify |

### 4. Abstract Base Classes (ABC)
```python
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def charge(self, amount: int, token: str) -> str:
        """Charge and return a transaction id."""

    @property
    @abstractmethod                       # abstract property: @property on the OUTSIDE
    def name(self) -> str: ...

    def pay(self, amount, token):         # concrete method shared by all gateways (template)
        if amount <= 0:
            raise ValueError("amount must be positive")
        return f"{self.name}:{self.charge(amount, token)}"

class StripeGateway(PaymentGateway):
    name = "stripe"                       # a plain class attribute satisfies the abstract property
    def charge(self, amount, token):
        return "txn_123"

class BrokenGateway(PaymentGateway):
    name = "broken"                       # forgot charge()

print(StripeGateway().pay(500, "tok"))    # stripe:txn_123
for cls in (PaymentGateway, BrokenGateway):
    try:
        cls()
    except TypeError:
        print(f"TypeError: can't instantiate {cls.__name__}")
```
**Internal mechanism:**
- `ABC` is just a class whose metaclass is `ABCMeta` (`class X(metaclass=ABCMeta)` is equivalent).
- `@abstractmethod` sets `func.__isabstractmethod__ = True`.
- When the class is created, `ABCMeta` computes `cls.__abstractmethods__` — the set of names still abstract after considering all bases.
- `object.__new__` refuses to instantiate a class whose `__abstractmethods__` is non-empty → `TypeError` **at instantiation** (not at class definition).
- Abstract methods **can have bodies**; subclasses can call them via `super()`.
- `PaymentGateway.register(SomeClass)` declares a **virtual subclass**: `isinstance` passes, but nothing is enforced or inherited.

### 5. Protocols (structural typing, PEP 544)
```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Notifier(Protocol):
    def send(self, to: str, msg: str) -> None: ...

class SMSClient:                         # does NOT inherit Notifier
    def send(self, to, msg): print(f"SMS to {to}: {msg}")

def alert(n: Notifier):                  # type checker accepts any object with send(to, msg)
    n.send("+91...", "server down")

alert(SMSClient())                       # SMS to +91...: server down
print(isinstance(SMSClient(), Notifier)) # True — runtime check only verifies the method EXISTS
```
⚠️ `@runtime_checkable` `isinstance` checks only that attribute names exist — not signatures or return types.

### 6. Duck typing
"If it walks like a duck and quacks like a duck, it's a duck." Python doesn't check types before calling a method; it just tries.
```python
class File:
    def read(self): return "file data"
class Socket:
    def read(self): return "socket data"
for src in (File(), Socket()):
    print(src.read())          # both work; no common base class needed
```
**EAFP** ("easier to ask forgiveness than permission") is the duck-typing style: `try: x.read() except AttributeError:` rather than `if hasattr(...)`.

### 7. Comparison: ABC vs Protocol vs Java interface
| | Java interface | ABC | Protocol |
|---|---|---|---|
| Must implementer declare it? | Yes (`implements`) | Yes (inherit) | No |
| Can contain shared code | Default methods | ✅ Concrete methods | Possible but unusual |
| Enforced at runtime | Compile time | At instantiation | No (static only) |
| Works with classes you don't own | No | Via `register()` | ✅ Yes |

### 8. Common mistakes
- Putting `@abstractmethod` **above** `@property` (wrong order → not treated as property correctly). Correct: `@property` then `@abstractmethod` underneath.
- Expecting `TypeError` when the subclass is *defined* — it happens when it's *instantiated*.
- Using ABCs for everything — often a Protocol or plain duck typing is lighter.

### 9. Real-world backend applications
- `StorageBackend` ABC with `S3Storage`, `LocalStorage`, `InMemoryStorage` (tests).
- `Repository` interfaces in clean architecture.
- Django's `BaseCommand`, DRF's `BasePermission` (abstract-ish base classes).
- `collections.abc.Mapping`, `Iterable`, etc. — inherit to get mixin methods for free.

### 🎤 Interview-ready answer
> "Abstraction is exposing what something does while hiding how. In Python I can express an interface three ways: duck typing, where any object with the right methods works; ABCs, where I subclass `ABC` and mark methods `@abstractmethod` — `ABCMeta` collects them into `__abstractmethods__` and instantiation fails with `TypeError` until all are implemented; and `typing.Protocol`, which is structural — any class with matching methods satisfies it without inheriting, checked by type checkers. I use ABCs when I want enforcement or shared base behaviour, and Protocols when I want loose coupling or to describe classes I don't own."

### 📝 Revision notes
```
ABC = metaclass ABCMeta ; @abstractmethod → __abstractmethods__ ; TypeError on instantiation
abstract property: @property above @abstractmethod
Protocol = structural, static check; @runtime_checkable isinstance checks names only
duck typing + EAFP ; register() = virtual subclass, no enforcement
```

---

## M6. Inheritance

### 1. What & why
**Inheritance** creates a new class (child/derived/subclass) from an existing one (parent/base/superclass), **reusing** its attributes and methods and **specialising** behaviour. It models an **"is-a"** relationship: a `SavingsAccount` *is an* `Account`.

### 2. Types of inheritance
```text
Single        Multilevel      Hierarchical        Multiple         Hybrid (diamond)
  A             A                 A              A     B                A
  │             │               / | \             \   /               /   \
  B             B              B  C  D              C                B     C
                │                                                     \   /
                C                                                       D
```
```python
class A: pass
class B(A): pass            # single
class C(B): pass            # multilevel  A → B → C
class D(A): pass            # hierarchical: B and D both from A
class E(B, D): pass         # multiple
# B(A), D(A), E(B, D) → hybrid/diamond — resolved by MRO (M9)
```

### 3. Overriding and extending
```python
class Notifier:
    def __init__(self, sender):
        self.sender = sender
    def send(self, to, msg):
        return f"[{self.sender}] {msg} → {to}"

class EmailNotifier(Notifier):
    def __init__(self, sender, smtp_host):
        super().__init__(sender)               # EXTEND: let the parent set up its part
        self.smtp_host = smtp_host
    def send(self, to, msg):                   # OVERRIDE + extend parent behaviour
        base = super().send(to, msg)
        return f"EMAIL via {self.smtp_host}: {base}"

print(EmailNotifier("noreply", "smtp.x.com").send("a@b.com", "Hi"))
# EMAIL via smtp.x.com: [noreply] Hi → a@b.com
```

### 4. Constructor inheritance rules
| Child defines `__init__`? | What happens |
|---|---|
| No | Parent's `__init__` is inherited and used (found via MRO) |
| Yes, calls `super().__init__(...)` | Both run — ✅ the normal case |
| Yes, **doesn't** call `super().__init__` | Parent's `__init__` **never runs** → parent attributes missing → `AttributeError` later ⚠️ |

```python
class Base:
    def __init__(self): self.created = True
class Bad(Base):
    def __init__(self): self.name = "x"          # forgot super().__init__()
try:
    Bad().created
except AttributeError:
    print("AttributeError: 'created' never set")
```

### 5. How attribute/method lookup works with inheritance
`obj.method` searches `type(obj).__mro__` left to right — the child first, then parents. The **first** match wins. That's why overriding works: the child's definition is found before the parent's.
```python
print(EmailNotifier.__mro__)
# (<class 'EmailNotifier'>, <class 'Notifier'>, <class 'object'>)
```

### 6. Inheritance limitations (why "composition over inheritance")
- **Tight coupling:** children depend on parent internals; parent changes can break children (*fragile base class problem*).
- **Rigid hierarchies:** behaviour is fixed at class-definition time; can't swap at runtime.
- **Class explosion:** `EmailNotifier`, `SMSNotifier`, `RetryingEmailNotifier`, `RetryingSMSNotifier`, `LoggingRetryingEmailNotifier`… combinations multiply.
- **Liskov violations:** inheriting for code reuse when "is-a" isn't true (`Square(Rectangle)` problem — [M18](#m18-solid-principles-in-python)).

### 7. Composition vs inheritance
```python
# Inheritance: behaviour baked into the class hierarchy
class RetryingEmailNotifier(EmailNotifier): ...

# Composition: behaviour assembled from parts, swappable at runtime
class NotificationService:
    def __init__(self, channel, retry_policy, logger):
        self.channel, self.retry, self.log = channel, retry_policy, logger
    def notify(self, to, msg):
        return self.retry.run(lambda: self.channel.send(to, msg))
```
| Use inheritance when | Use composition when |
|---|---|
| True "is-a", stable hierarchy | "has-a" / "uses-a" |
| Framework requires it (Django models, `Exception`) | Behaviour should vary independently or at runtime |
| Subclass is substitutable everywhere (Liskov) | You want easy testing with fakes |
| Sharing a template algorithm (Template Method) | Combinations would explode |

### 🎤 Interview-ready answer
> "Inheritance lets a subclass reuse and specialise a base class — an is-a relationship. Python supports single, multilevel, hierarchical, and multiple inheritance; method lookup follows the class's MRO, so a subclass's override is found first, and `super()` lets it extend rather than replace the parent's behaviour. If a subclass defines `__init__`, it must call `super().__init__()` or the parent's setup never runs. I use inheritance for genuine is-a hierarchies and framework extension points, but default to composition for combining behaviours, since inheritance couples children to parent internals and doesn't allow runtime swapping."

### 📝 Revision notes
```
child reuses + overrides ; lookup = MRO, first match wins
child __init__ must call super().__init__() ; no child __init__ → parent's used
types: single, multilevel, hierarchical, multiple, hybrid(diamond → MRO)
limits: tight coupling, fragile base, class explosion → prefer composition
```

---

## M7. Polymorphism

### 1. What is it?
**Polymorphism** ("many forms") = the **same operation** works on **different types**, each responding in its own way. The caller writes one piece of code; behaviour depends on the object.

### 2. Why does it exist?
It removes type-checking conditionals:
```python
# ❌ Without polymorphism
def area(shape):
    if shape["type"] == "circle": return 3.14159 * shape["r"] ** 2
    elif shape["type"] == "square": return shape["s"] ** 2
    # every new shape → edit this function (violates Open/Closed)

# ✅ With polymorphism
class Circle:
    def __init__(self, r): self.r = r
    def area(self): return 3.14159 * self.r ** 2
class Square:
    def __init__(self, s): self.s = s
    def area(self): return self.s ** 2

print([round(s.area(), 2) for s in (Circle(1), Square(2))])   # [3.14, 4]
```

### 3. Forms of polymorphism in Python
| Form | How | Example |
|---|---|---|
| **Subtype (runtime) via overriding** | Subclasses override a base method | `EmailNotifier.send` vs `SMSNotifier.send` |
| **Duck typing** | Any object with the method works — no shared base | `len()` works on str, list, your class with `__len__` |
| **Operator polymorphism** | Dunder methods | `+` means add for ints, concat for lists, your `Vector.__add__` |
| **Protocol-based** | Structural typing for static checks | `Notifier` Protocol |
| **Single dispatch** | Choose implementation by argument type | `functools.singledispatch` |
| **Parametric** | Generics in type hints | `list[T]`, `class Box[T]` |

### 4. Internal mechanism: dynamic dispatch
`obj.area()` is resolved **at runtime**: Python looks up `area` on `type(obj)` via its MRO at the moment of the call. There's no compile-time binding, no vtable you declare — every method call is "virtual".

### 5. Method overloading — why Python doesn't have it
A class body is executed top to bottom like a script; `def` binds a name in the class namespace. A second `def` with the same name **rebinds** it:
```python
class Calc:
    def add(self, a, b): return a + b
    def add(self, a, b, c): return a + b + c     # replaces the first one

try:
    Calc().add(1, 2)
except TypeError:
    print("TypeError: first add() no longer exists")
```
Also, with dynamic typing there are no declared parameter types to dispatch on at compile time.

**Pythonic alternatives:**
```python
# 1. Default arguments
def connect(host, port=5432, *, timeout=10): ...

# 2. *args / **kwargs
def total(*nums): return sum(nums)

# 3. Alternative constructors (classmethods) instead of overloaded constructors
#    User.from_csv(...), User.from_dict(...)

# 4. functools.singledispatch — dispatch on the FIRST argument's type
from functools import singledispatch, singledispatchmethod

@singledispatch
def serialize(obj): raise TypeError(f"can't serialize {type(obj).__name__}")
@serialize.register
def _(obj: int): return f"int:{obj}"
@serialize.register
def _(obj: list): return "[" + ",".join(serialize(x) for x in obj) + "]"
print(serialize([1, 2]))          # [int:1,int:2]

# 5. singledispatchmethod — for methods (dispatches on the first arg AFTER self)
class Formatter:
    @singledispatchmethod
    def fmt(self, v): return str(v)
    @fmt.register
    def _(self, v: float): return f"{v:.2f}"
print(Formatter().fmt(3.14159), Formatter().fmt("x"))   # 3.14 x

# 6. typing.overload — ONLY for type checkers; you still write one real implementation
```

### 6. Real-world backend applications
- Payment providers sharing `charge()`; notification channels sharing `send()`.
- Serializers: DRF serializers, `json.JSONEncoder.default` override.
- File-like objects: anything with `read()` works with `json.load`, `csv.reader`.
- Middleware chains: every middleware implements `__call__(request)`.

### Common misconceptions
- ❌ "Python supports overloading." → Last definition wins.
- ❌ "Polymorphism needs inheritance." → Duck typing gives polymorphism without any shared base.
- ❌ "Operator overloading is overloading." → It's operator **polymorphism** via dunder methods.

### 🎤 Interview-ready answer
> "Polymorphism means one interface, many implementations — the caller invokes `obj.send()` and the object's type decides what happens. In Python every method call is dynamically dispatched by looking up the name on the object's type at runtime, so overriding gives runtime polymorphism, and duck typing gives polymorphism even without a common base class. Operators are polymorphic through dunder methods. Python has no signature-based overloading — a second `def` just rebinds the name — so I use default arguments, `*args/**kwargs`, classmethod alternative constructors, or `functools.singledispatch` when I really need type-based dispatch."

### 📝 Revision notes
```
same call, behaviour by type ; replaces if/elif type checks (Open/Closed)
overriding (subtype) | duck typing | operators via dunders | Protocol | singledispatch
every call is dynamic dispatch via type(obj).__mro__
no overloading: later def rebinds name → defaults, *args, classmethods, singledispatch(method)
```

---

# PART IV — PYTHON INTERNALS

## M8. Object Creation & Lifecycle

> ⭐ **One of the most important modules.** "What happens when you write `obj = MyClass(...)`?" separates candidates who *use* Python from those who *understand* it.

### 1. What is it?
An object's lifecycle: **creation** (allocation) → **initialisation** → **use** → **unreachable** → **finalisation** → **memory freed**.

### 2. The big picture: `obj = MyClass(1, 2)`
```text
obj = MyClass(1, 2)
 │
 ├─ 1. Evaluate the name MyClass  → the class object
 ├─ 2. Evaluate arguments          → (1, 2)
 ├─ 3. CALL the class. A class is called like any object: Python uses type(MyClass).__call__
 │       type(MyClass) is the METACLASS — normally `type`
 │
 ▼
type.__call__(MyClass, 1, 2)
 │
 ├─ 4. instance = MyClass.__new__(MyClass, 1, 2)        ← ALLOCATE (usually object.__new__)
 │
 ├─ 5. if isinstance(instance, MyClass):                  ← only then is __init__ called
 │         type(instance).__init__(instance, 1, 2)        ← INITIALISE (must return None)
 │
 └─ 6. return instance
 │
 ▼
7. bind the name `obj` to the returned object (refcount +1)
```

### 3. `type.__call__` written in Python (simplified but faithful)
```python
class MyType(type):
    def __call__(cls, *args, **kwargs):
        instance = cls.__new__(cls, *args, **kwargs)        # step 4
        if isinstance(instance, cls):                       # step 5 guard
            result = type(instance).__init__(instance, *args, **kwargs)
            if result is not None:
                raise TypeError(f"__init__() should return None, not '{type(result).__name__}'")
        return instance                                     # step 6
```
Real CPython implements this in C (`type_call`), but the behaviour matches.

### 4. Watch it happen — execution order
```python
class Meta(type):
    def __call__(cls, *args, **kwargs):
        print(f"1. Meta.__call__({cls.__name__}, {args})")
        obj = super().__call__(*args, **kwargs)
        print("4. Meta.__call__ returns")
        return obj

class MyClass(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print(f"2. __new__(cls={cls.__name__}, args={args})")
        return super().__new__(cls)            # object.__new__ takes ONLY cls
    def __init__(self, x, y):
        print(f"3. __init__(self, x={x}, y={y})")
        self.x, self.y = x, y

obj = MyClass(1, 2)
print("5. got", obj.x, obj.y)
```
```text
1. Meta.__call__(MyClass, (1, 2))
2. __new__(cls=MyClass, args=(1, 2))
3. __init__(self, x=1, y=2)
4. Meta.__call__ returns
5. got 1 2
```

### 5. `__new__` vs `__init__` — the deep dive

| | `__new__(cls, ...)` | `__init__(self, ...)` |
|---|---|---|
| Job | **Create** and return the instance | **Initialise** an already-created instance |
| First argument | `cls` — the class (instance doesn't exist yet) | `self` — the new instance |
| Kind | Static method (implicitly — no decorator needed) | Instance method |
| Must return | The instance (any object, actually) | `None` (anything else → `TypeError`) |
| Called by | `type.__call__` | `type.__call__`, **only if** `__new__` returned an instance of `cls` |
| Default | `object.__new__(cls)` allocates a blank instance | `object.__init__` does nothing |
| Override when | Immutable subclasses, singletons/caching, returning subclasses, metaclasses | Almost always — normal setup |

**Why `__new__` receives `cls`:** the instance doesn't exist yet; `__new__` is what makes it. It needs to know *which class* to instantiate (could be a subclass calling up via `super()`).

**Why `__new__` is implicitly static:** it's called as `cls.__new__(cls, ...)` with the class passed explicitly. Python special-cases the name `__new__` and wraps it in `staticmethod` automatically when the class is created (you'll see `staticmethod` in `MyClass.__dict__['__new__']`).

**Why `__init__` returns `None`:** the caller already has the instance from `__new__`; `__init__` only mutates it. Returning anything else is almost certainly a bug, so Python raises.
```python
class Bad:
    def __init__(self): return 5
try:
    Bad()
except TypeError as e:
    print(e)                    # __init__() should return None, not 'int'
```

### 6. Exceptions to the normal flow (interview favourites)

**(a) `__new__` returns a different type → `__init__` is SKIPPED**
```python
class Weird:
    def __new__(cls):
        return 42                   # not an instance of Weird
    def __init__(self):
        print("init")               # never runs
w = Weird()
print(w, type(w).__name__)          # 42 int
```

**(b) `__new__` returns an EXISTING instance → `__init__` RUNS AGAIN** (the singleton trap)
```python
class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self, value):
        print(f"init {value}")
        self.value = value          # re-runs → overwrites state!

a = Singleton(1)
b = Singleton(2)
print(a is b, a.value)
```
```text
init 1
init 2
True 2
```
Fix: guard initialisation (`if getattr(self, "_ready", False): return` … `self._ready = True`), or do all setup in `__new__`, or use a different singleton approach ([M19](#m19-design-patterns-in-python)).

**(c) `__new__` returns an instance of a SUBCLASS → the subclass's `__init__` runs**
```python
class Shape:
    def __new__(cls, kind):
        if cls is Shape:                                  # factory behaviour only on the base
            cls = {"circle": Circle, "square": Square}[kind]
        return super().__new__(cls)
    def __init__(self, kind):
        print("Shape.__init__")

class Circle(Shape):
    def __init__(self, kind):
        print("Circle.__init__")

class Square(Shape): pass

s = Shape("circle")
print(type(s).__name__)
```
```text
Circle.__init__
Circle
```
Because `isinstance(obj, Shape)` is True, `type.__call__` runs `type(obj).__init__` — that's `Circle.__init__`. (This is clever but surprising; a `@classmethod` factory is usually clearer.)

**(d) A metaclass overrides `__call__`** → it can skip `__new__`/`__init__` entirely (e.g., return a cached instance).

**(e) Unpickling and `copy.copy`** create instances via `cls.__new__(cls)` (or `__reduce_ex__`) **without calling `__init__`** — so invariants set only in `__init__` won't be re-run.

### 7. `object.__new__` argument rules (a confusing error explained)
```python
class P:
    def __new__(cls, *args):
        return super().__new__(cls, *args)   # ❌ passing args to object.__new__
    def __init__(self, x): self.x = x
```
`object.__new__` raises `TypeError: object.__new__() takes exactly one argument` if you pass extra args **and** you've overridden `__new__`. Always call `super().__new__(cls)` (just `cls`) unless the parent is a type whose `__new__` needs the value (like `int`, `str`, `tuple`).

### 8. Immutable types need `__new__`
For immutable built-ins, the value is fixed **at allocation**. By the time `__init__` runs, it's too late to change it.
```python
class UpperStr(str):
    def __new__(cls, value):
        return super().__new__(cls, value.upper())   # set the value at creation

class PositiveInt(int):
    def __new__(cls, value):
        if value <= 0:
            raise ValueError("must be positive")
        return super().__new__(cls, value)

class Point(tuple):
    def __new__(cls, x, y):
        return super().__new__(cls, (x, y))
    @property
    def x(self): return self[0]
    @property
    def y(self): return self[1]

print(UpperStr("hello"), PositiveInt(5) + 1, Point(3, 4).x)   # HELLO 6 3
```
Trying it in `__init__` fails: `str.__init__` can't change an already-built string.

### 9. Alternative constructors
Prefer `@classmethod` factories over clever `__new__` logic:
```python
class Money:
    def __init__(self, paise: int): self.paise = paise
    @classmethod
    def from_rupees(cls, rupees: float): return cls(round(rupees * 100))
```

### 10. `__new__` in metaclasses (preview — full detail in [M17](#m17-advanced-python-oop))
When Python executes a `class` statement, it calls the metaclass: `Meta(name, bases, namespace)` → `Meta.__new__(Meta, name, bases, ns)` creates the **class object**, then `Meta.__init__` initialises it. Same `__new__`/`__init__` split, one level up.

### 11. Object lifetime & garbage collection (CPython)

**References and reference counting**
- Every object has a reference count: how many references point to it (names, list slots, attributes…).
- When it drops to **0**, CPython frees the object **immediately** (and calls `__del__` first if defined).
- `del name` removes a **name**, decrementing the count — it doesn't directly destroy the object.
```python
class Res:
    def __init__(self, n): self.n = n
    def __del__(self): print(f"__del__ {self.n}")

a = Res(1)
b = a            # refcount 2
del a            # refcount 1 → nothing printed
print("after del a")
del b            # refcount 0 → finalised now (in CPython)
print("after del b")
```
```text
after del a
__del__ 1
after del b
```

**Cyclic garbage collection**
Reference counting can't free cycles (`a.other = b; b.other = a` — each keeps the other at count ≥ 1). CPython's **generational cyclic GC** (`gc` module) periodically finds groups of objects reachable only from each other and frees them. Objects start in generation 0; survivors get promoted to 1, then 2 (checked less often). `gc.collect()` forces a collection.

**`__del__` — the finaliser**
- Called when the object is about to be destroyed — **not** when `del` is written.
- Since Python 3.4 (PEP 442), objects with `__del__` in cycles **are** collected (previously they leaked into `gc.garbage`).

**Why `__del__` is unreliable for cleanup:**
1. **Timing is not guaranteed** — on PyPy/Jython (no refcounting) or in cycles, it runs whenever the GC decides.
2. **May not run at all** at interpreter shutdown.
3. **Exceptions inside it are ignored** (printed as "Exception ignored in…").
4. Globals it references may already be torn down at shutdown.
5. Any lingering reference (traceback, cache, closure) keeps the object alive.

✅ **Use context managers (`with`) for deterministic cleanup** ([M15](#m15-iterators-generators--context-managers)); use `weakref.finalize` for a safety net.

**Weak references**
A weak reference refers to an object **without** increasing its refcount — the object can still be collected.
```python
import weakref

class Session: pass
s = Session()
r = weakref.ref(s)
print(r() is s)           # True — dereference by calling
del s
print(r())                # None — object was collected

cache = weakref.WeakValueDictionary()   # entries vanish when values are no longer used elsewhere
```
Use cases: caches, observer lists that shouldn't keep observers alive, parent back-references in trees.
```python
class Conn:
    def __init__(self):
        self._finalizer = weakref.finalize(self, print, "closing connection")  # safer than __del__
    def close(self): self._finalizer()         # idempotent: runs at most once
```

**Object resurrection**
`__del__` can store `self` somewhere reachable, bringing the object back to life. Since PEP 442, `__del__` is called **at most once** per object — a resurrected object won't have its finaliser run again.
```python
graveyard = []
class Phoenix:
    def __del__(self):
        print("__del__ called")
        graveyard.append(self)       # resurrect!
p = Phoenix()
del p                                # __del__ called
print(len(graveyard))                # 1 — still alive
graveyard.clear()                    # destroyed for real; __del__ NOT called again
print("done")
```
```text
__del__ called
1
done
```

### 12. Common mistakes
- Passing extra args to `object.__new__`.
- Doing validation for immutable subclasses in `__init__`.
- Singleton via `__new__` without guarding `__init__`.
- Relying on `__del__` to close files/connections.
- Thinking `del obj` destroys the object.

### 13. Interview questions
| # | Question | Follow-up |
|---|---|---|
| 1 | What happens when you call `MyClass()`? | Who calls `__new__`? What's a metaclass's role? |
| 2 | `__new__` vs `__init__`? | Why is `__new__` static? Why does `__init__` return None? |
| 3 | When is `__init__` not called? | What if `__new__` returns a cached instance? |
| 4 | How do you subclass `int`/`str` with custom values? | Why doesn't `__init__` work? |
| 5 | How does Python free memory? | What about cycles? Generations? |
| 6 | Should you use `__del__`? | Alternatives? What is resurrection? |
| 7 | What are weak references for? | `WeakValueDictionary` use case |

### 🎤 Interview-ready answer: "What happens when you instantiate a class?"
> "A class is a callable object, so `MyClass(args)` invokes `type(MyClass).__call__` — normally `type.__call__`, since `type` is the default metaclass. That calls `MyClass.__new__(cls, *args)`, which allocates and returns the new instance — by default via `object.__new__`. If the returned object is an instance of `MyClass`, `type.__call__` then calls `__init__` on it with the same arguments to initialise state; `__init__` must return `None`. Finally the instance is returned and bound to the name. The interesting edge cases are: if `__new__` returns something that isn't an instance, `__init__` is skipped; if it returns a cached instance, `__init__` runs again — which is the classic singleton bug; and immutable types like `int` or `str` must be customised in `__new__` because their value is fixed at allocation."

### 🎤 "How does garbage collection work in Python?"
> "CPython primarily uses reference counting: each object tracks how many references point to it, and when the count hits zero it's deallocated immediately, calling `__del__` first if defined. Reference counting can't reclaim cycles, so there's also a generational cyclic garbage collector that periodically finds groups of objects only reachable from each other. Because finalisation timing isn't guaranteed across implementations or at shutdown, I don't rely on `__del__` for cleanup — I use context managers, or `weakref.finalize` as a safety net."

### 📝 Revision notes
```
MyClass(a) → type(MyClass).__call__ → cls.__new__(cls, a) → if isinstance: type(obj).__init__(obj, a) → return obj
__new__: implicit staticmethod, gets cls, RETURNS instance ; __init__: gets self, returns None
__new__ returns non-instance → __init__ skipped ; returns existing → __init__ re-runs
returns subclass instance → subclass __init__ runs ; copy/pickle skip __init__
immutables (int/str/tuple) → customise in __new__ ; super().__new__(cls) only cls
refcount → immediate free ; cyclic GC (generations 0/1/2) for cycles
__del__ unreliable → with / weakref.finalize ; __del__ runs at most once (PEP 442)
```

---

## M9. `super()` and MRO

### 1. What is the MRO?
The **Method Resolution Order** is the ordered list of classes Python searches when looking up an attribute on a class or its instances. Every class has it: `Cls.__mro__` (tuple) or `Cls.mro()` (list).

```python
class A: pass
class B(A): pass
print(B.__mro__)     # (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
```

### 2. Why does it exist? The diamond problem
```text
        A          show()
       / \
      B   C        both override show()
       \ /
        D          D(B, C) — which show()? should A run once or twice?
```
Python needs one **consistent, predictable** order that (1) checks a child before its parents, (2) respects the left-to-right order of bases, and (3) visits each class **exactly once**. That order is computed by **C3 linearization**.

### 3. C3 linearization — the algorithm
For `class C(B1, B2, ..., Bn)`:
```text
L[C] = C + merge(L[B1], L[B2], ..., L[Bn], [B1, B2, ..., Bn])
L[object] = [object]
```
**merge:** repeatedly take the **first head** (first element of a list) that does **not** appear in the **tail** (any position except first) of any list. Append it to the result and remove it from all lists. If no head qualifies → `TypeError: Cannot create a consistent method resolution order (MRO)`.

**Worked example 1 — the diamond**
```text
L[A] = A O               (O = object)
L[B] = B A O
L[C] = C A O
L[D] = D + merge(BAO, CAO, BC)
     B: not in any tail (tails: AO, AO, C) → take B      → D B   ; lists: AO, CAO, C
     A: in tail of CAO                    → skip; try C  → D B C ; lists: AO, AO, —
     A: not in any tail                   → take A       → D B C A
     O                                                   → D B C A O
```

**Worked example 2 — a harder one**
```python
class O: pass
class A(O): pass
class B(O): pass
class C(A, B): pass
class D(B): pass
class E(C, D): pass
```
```text
L[C] = C + merge(AO, BO, AB) = C A B O
L[D] = D B O
L[E] = E + merge(CABO, DBO, CD)
  C (not in tails ABO, BO, D)             → E C        lists: ABO, DBO, D
  A (not in tails BO, BO, —)              → E C A      lists: BO, DBO, D
  B is in tail of DBO → skip; D ok        → E C A D    lists: BO, BO, —
  B                                       → E C A D B
  O                                       → E C A D B O
```
```python
print([k.__name__ for k in E.__mro__])   # ['E', 'C', 'A', 'D', 'B', 'O', 'object']
```

**Worked example 3 — an impossible hierarchy**
```python
class X: pass
class Y(X): pass
try:
    class Z(X, Y): pass      # asks for X before Y, but Y is a subclass of X (Y must come first)
except TypeError as e:
    print("TypeError: Cannot create a consistent MRO")
```

### 4. What `super()` really does
⚠️ **`super()` does NOT mean "my parent".** It means **"the next class after the current one in the MRO of `type(self)`"**.

```text
super()            (inside a method of class K, with first arg self)
  ≡ super(K, self)
  → a proxy that looks up attributes in type(self).__mro__, starting AFTER K
```
- Zero-argument `super()` works because the compiler gives methods defined in a class a hidden `__class__` cell (= K) and uses the method's first argument.
- Because the MRO is determined by the **instance's actual type**, the same `super()` call in class `B` can reach different classes depending on whether `self` is a `B` or a `D`.

### 5. The diamond with cooperative `super()`
```python
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

class D(B, C):
    def show(self):
        print("D")
        super().show()

D().show()
print([k.__name__ for k in D.__mro__])
```
```text
D
B
C
A
['D', 'B', 'C', 'A', 'object']
```
**Dry run — what `super()` resolves to in each frame (`self` is a `D` throughout):**
| Executing | `type(self).__mro__` | `super()` = next after… | Resolves to |
|---|---|---|---|
| `D.show` | D, B, C, A, object | after D | `B.show` |
| `B.show` | (same) | after B | **`C.show`** ← not A! |
| `C.show` | (same) | after C | `A.show` |
| `A.show` | (same) | — (doesn't call super) | stops |

And `B().show()` alone prints `B`, `A` — because then the MRO is `B, A, object`. **Same code, different next class.** That's why every class must call `super()` — it's a chain, and each link doesn't know who's next.

**Why the diamond problem is solved:** C3 puts `A` after both `B` and `C`, and each class appears once, so `A.show` runs exactly once, after all its subclasses.

### 6. What goes wrong without cooperation
**(a) A class in the chain doesn't call `super()` → the chain breaks:**
```python
class A:
    def show(self): print("A")
class B(A):
    def show(self): print("B")              # no super() call
class C(A):
    def show(self): print("C"); super().show()
class D(B, C):
    def show(self): print("D"); super().show()
D().show()      # D, B  ← C and A never run
```
**(b) Calling parents by name → base initialised twice:**
```python
class A:
    def __init__(self): print("A init")
class B(A):
    def __init__(self): print("B init"); A.__init__(self)
class C(A):
    def __init__(self): print("C init"); A.__init__(self)
class D(B, C):
    def __init__(self):
        print("D init"); B.__init__(self); C.__init__(self)
D()
```
```text
D init
B init
A init
C init
A init      ← A initialised twice (double connections, double counters...)
```

### 7. Cooperative `__init__` with different signatures — the `**kwargs` pattern
Each class takes the arguments it needs and forwards the rest:
```python
class Base:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)          # object.__init__() must receive NO extra args

class Named(Base):
    def __init__(self, name, **kwargs):
        self.name = name
        super().__init__(**kwargs)

class Aged(Base):
    def __init__(self, age, **kwargs):
        self.age = age
        super().__init__(**kwargs)

class Person(Named, Aged):
    pass

p = Person(name="Parth", age=23)
print(p.name, p.age)                        # Parth 23
print([k.__name__ for k in Person.__mro__]) # ['Person', 'Named', 'Aged', 'Base', 'object']
```
Rules of cooperative multiple inheritance (Raymond Hettinger's "super considered super"):
1. Every method in the chain calls `super()` with the same method name.
2. Use keyword arguments; each class strips its own and passes `**kwargs` on.
3. Have a **root** class that ends the chain without passing unexpected args to `object`.
4. Signatures of the shared method must be compatible.

### 8. Mixins
A **mixin** is a small class providing one extra capability, designed to be combined via multiple inheritance — not instantiated alone.
```python
import json

class JsonMixin:
    def to_json(self):
        return json.dumps(self.__dict__)

class ReprMixin:
    def __repr__(self):
        fields = ", ".join(f"{k}={v!r}" for k, v in vars(self).items())
        return f"{type(self).__name__}({fields})"

class User(ReprMixin, JsonMixin):
    def __init__(self, name, email): self.name, self.email = name, email

u = User("Parth", "p@x.com")
print(u)            # User(name='Parth', email='p@x.com')
print(u.to_json())  # {"name": "Parth", "email": "p@x.com"}
```
Convention: mixins go **left** of the main base class (`class MyView(LoginRequiredMixin, View)` in Django) so their methods come first in the MRO and can `super()` into the base.

### 9. `super()` in other contexts
```python
class Base:
    @classmethod
    def create(cls): return cls()

class Child(Base):
    @classmethod
    def create(cls):
        obj = super().create()        # works in classmethods: super(Child, cls)
        obj.extra = True
        return obj

print(type(Child.create()).__name__, Child.create().extra)   # Child True
```

### 10. Common MRO mistakes
- Assuming `super()` calls the direct parent.
- Mixing `Parent.method(self)` calls with `super()` calls in one hierarchy.
- Forgetting `super().__init__()` in one class → breaks the chain for everyone after it.
- Passing positional args through a cooperative chain (signatures don't line up).
- Ordering bases inconsistently → MRO `TypeError`.

### 🎤 Interview-ready answer: "How does `super()` work with multiple inheritance?"
> "Every class has an MRO computed by C3 linearization: the class first, then a merge of its bases' MROs that preserves local base order and puts every class before its own parents, with each class appearing once. `super()` isn't 'call my parent' — it returns a proxy that looks up the method in `type(self).__mro__` starting after the class where the call is written. So in a diamond `D(B, C)`, `B`'s `super()` call goes to `C`, not `A`, when `self` is a `D`. For this to work every class must cooperate: call `super()`, accept `**kwargs`, and pass along what it doesn't use. That guarantees each method in the hierarchy runs exactly once, which is how Python handles the diamond problem."

### 📝 Revision notes
```
MRO = C3: L[C] = C + merge(L[bases]..., [bases]) ; take first head not in any tail
child before parents, left-to-right bases, each class once ; inconsistent → TypeError
super() = next class AFTER current class in type(self).__mro__ (not "parent")
diamond D(B,C): D B C A object ; B's super → C when self is D
cooperate: every class calls super(), uses **kwargs, root class ends chain
Parent.__init__(self) in diamonds → double init ; mixins go left
```

---

## M10. Attribute Lookup & Descriptors

> 🔷 This module unifies **properties, methods, classmethods, staticmethods, `__slots__`, and ORMs** into one mechanism. Master it and half of Python's "magic" disappears.

### 1. What is a descriptor?
Any object that defines at least one of these methods, **stored as a class attribute** of another class:
| Method | Called on | Signature |
|---|---|---|
| `__get__` | `obj.attr` (read) | `__get__(self, instance, owner)` → value |
| `__set__` | `obj.attr = v` | `__set__(self, instance, value)` → None |
| `__delete__` | `del obj.attr` | `__delete__(self, instance)` → None |
| `__set_name__` | when the owner class is created | `__set_name__(self, owner, name)` |

- **Data descriptor:** defines `__set__` or `__delete__` (e.g. `property`, `__slots__` members).
- **Non-data descriptor:** only `__get__` (e.g. functions, `classmethod`, `staticmethod`, `functools.cached_property`).

The difference determines **priority** against the instance `__dict__`.

### 2. The full attribute lookup algorithm — `obj.name`
`obj.name` calls `type(obj).__getattribute__(obj, "name")` — normally `object.__getattribute__`, which does:
```text
1. cls_attr = search for "name" in type(obj).__mro__ (each class's __dict__, in order)

2. if cls_attr is a DATA descriptor:
       return cls_attr.__get__(obj, type(obj))            ← beats the instance dict

3. if "name" in obj.__dict__:
       return obj.__dict__["name"]                         ← instance attribute

4. if cls_attr is a NON-DATA descriptor:
       return cls_attr.__get__(obj, type(obj))             ← e.g. function → bound method

5. if cls_attr was found (plain class attribute):
       return cls_attr

6. raise AttributeError
       → if the class defines __getattr__, Python calls type(obj).__getattr__(obj, "name") instead
```
**Mnemonic:** **Data descriptor > instance dict > non-data descriptor > class attribute > `__getattr__`.**

### Setting — `obj.name = value` (`object.__setattr__`)
```text
1. cls_attr = search "name" in type(obj).__mro__
2. if cls_attr has __set__        → cls_attr.__set__(obj, value)
   (if it's a data descriptor with only __delete__ / property without setter → AttributeError)
3. else                           → obj.__dict__["name"] = value
```
Note there's no "non-data descriptor" step: assignment always goes to the instance dict unless a data descriptor intercepts it. That's why instance attributes can **shadow methods**.

### Class-level lookup — `Cls.name`
Handled by `type.__getattribute__`: it checks the metaclass for data descriptors, then searches `Cls.__mro__` and calls `__get__(None, Cls)` on descriptors found there. That's why `Cls.method` gives you the plain function and `Cls.prop` gives you the property object itself (property's `__get__` returns itself when `instance is None`).

### 3. Proof: data vs non-data priority
```python
class DataDesc:
    def __get__(self, inst, owner): return "from data descriptor"
    def __set__(self, inst, value): print("DataDesc.__set__ intercepted")

class NonDataDesc:
    def __get__(self, inst, owner): return "from non-data descriptor"

class C:
    d = DataDesc()
    n = NonDataDesc()

c = C()
c.__dict__["d"] = "instance value"        # bypass __set__ by writing the dict directly
c.__dict__["n"] = "instance value"
print(c.d)    # from data descriptor      ← data descriptor beats instance dict
print(c.n)    # instance value            ← instance dict beats non-data descriptor
c.d = 5       # DataDesc.__set__ intercepted
```

### 4. Functions are descriptors → that's how methods bind
```python
class Greeter:
    def hello(self): return f"hello from {id(self)}"

g = Greeter()
f = Greeter.__dict__["hello"]           # the raw function in the class namespace
print(type(f).__name__)                 # function
bound = f.__get__(g, Greeter)           # what g.hello does under the hood
print(bound() == g.hello())             # True
print(f.__get__(None, Greeter) is f)    # True ← Greeter.hello returns the plain function
```
Because functions are **non-data** descriptors, an instance attribute shadows a method:
```python
g.hello = lambda: "shadowed"
print(g.hello())      # shadowed
```

### 5. Re-implementing `property`, `staticmethod`, `classmethod` in pure Python
```python
class MyProperty:                                   # DATA descriptor
    def __init__(self, fget=None, fset=None):
        self.fget, self.fset = fget, fset
    def __get__(self, inst, owner):
        if inst is None: return self                # accessed on the class
        return self.fget(inst)
    def __set__(self, inst, value):
        if self.fset is None: raise AttributeError("can't set attribute")
        self.fset(inst, value)
    def setter(self, fset):
        return type(self)(self.fget, fset)          # returns a NEW property (that's why names must match)

class MyStaticMethod:                               # NON-data
    def __init__(self, f): self.f = f
    def __get__(self, inst, owner): return self.f   # no binding at all

class MyClassMethod:                                # NON-data
    def __init__(self, f): self.f = f
    def __get__(self, inst, owner):
        return self.f.__get__(owner, type(owner))   # bind to the CLASS (owner), not the instance

class Demo:
    def __init__(self): self._x = 1
    @MyProperty
    def x(self): return self._x
    @x.setter
    def x(self, v): self._x = v
    @MyStaticMethod
    def s(): return "static"
    @MyClassMethod
    def c(cls): return cls.__name__

d = Demo(); d.x = 42
print(d.x, d.s(), d.c(), Demo.c())     # 42 static Demo Demo
```

### 6. Writing a real descriptor: reusable validated fields (+ `__set_name__`)
```python
class Positive:
    def __set_name__(self, owner, name):        # called at class creation; learns its attribute name
        self.private = "_" + name
    def __get__(self, inst, owner):
        if inst is None: return self
        return getattr(inst, self.private)
    def __set__(self, inst, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f"{self.private[1:]} must be a positive number")
        setattr(inst, self.private, value)

class Product:
    price = Positive()           # one descriptor instance per FIELD, shared by all products
    quantity = Positive()
    def __init__(self, price, quantity):
        self.price = price       # → Positive.__set__
        self.quantity = quantity

p = Product(99.5, 3)
print(p.price, vars(p))          # 99.5 {'_price': 99.5, '_quantity': 3}
try:
    p.quantity = -1
except ValueError as e:
    print(e)                     # quantity must be a positive number
```
⚠️ Store per-instance data **on the instance** (or in a `WeakKeyDictionary`), never on `self` of the descriptor — the descriptor is shared by all instances.

This is exactly how Django model fields, SQLAlchemy columns, and Pydantic-like libraries work.

### 7. `functools.cached_property` — a non-data descriptor trick
It computes once, then **writes the result into the instance `__dict__`**. Since it's non-data, the instance dict wins on later lookups → the method is never called again.
```python
from functools import cached_property
class Report:
    @cached_property
    def data(self):
        print("computing...")
        return [1, 2, 3]
r = Report()
r.data; r.data         # "computing..." printed once
print("data" in vars(r))   # True
```

### 8. `__getattribute__` vs `__getattr__`
| | `__getattribute__(self, name)` | `__getattr__(self, name)` |
|---|---|---|
| Called | On **every** attribute access | **Only** when normal lookup raises `AttributeError` |
| Default | `object.__getattribute__` (the algorithm above) | Not defined |
| Risk | Infinite recursion if you access `self.x` inside | Low |
| Use | Rare: logging every access, access control | Common: delegation, proxies, lazy/dynamic attrs, defaults |

```python
class Lazy:
    def __init__(self): self.real = 1
    def __getattr__(self, name):               # only for MISSING attributes
        return f"<dynamic {name}>"

class Logged:
    def __getattribute__(self, name):
        print(f"access {name}")
        return object.__getattribute__(self, name)   # ✅ delegate; self.name here → infinite recursion

l = Lazy()
print(l.real, l.missing)    # 1 <dynamic missing>
```
**Delegation (Proxy/wrapper) with `__getattr__`:**
```python
class LoggingClient:
    def __init__(self, client): self._client = client
    def __getattr__(self, name):
        attr = getattr(self._client, name)       # forward anything we don't define
        if callable(attr):
            def wrapper(*a, **kw):
                print(f"calling {name}")
                return attr(*a, **kw)
            return wrapper
        return attr
```
⚠️ **`__setattr__` recursion trap:** inside `__setattr__`, `self.x = v` calls `__setattr__` again → infinite recursion. Use `super().__setattr__(name, value)` or `object.__setattr__(self, name, value)`.

### 9. Special method lookup bypasses the instance (and `__getattribute__`)
Implicit invocations (`len(obj)`, `obj + x`, `with obj`) look up the dunder **on the type**, not the instance, and skip `__getattribute__`/`__getattr__`:
```python
class Box: pass
b = Box()
b.__len__ = lambda: 5
print(b.__len__())          # 5  ← explicit attribute access finds the instance attr
try:
    len(b)                  # implicit: looks at type(b).__len__ → not there
except TypeError:
    print("TypeError: object of type 'Box' has no len()")
```
This is why proxies using `__getattr__` must explicitly define dunders like `__len__` and `__iter__`.

### 10. `__dir__`
`dir(obj)` calls `type(obj).__dir__(obj)`. Override to advertise dynamic attributes (useful with `__getattr__` for IDE/REPL autocompletion).

### 🎤 Interview-ready answer: "Explain attribute lookup / the descriptor protocol."
> "A descriptor is an object with `__get__`, `__set__`, or `__delete__` stored as a class attribute; it customises what happens when that attribute is accessed on instances. `object.__getattribute__` resolves `obj.x` in a fixed order: first it searches the type's MRO; if it finds a data descriptor — one with `__set__` or `__delete__`, like a property — that wins. Otherwise the instance `__dict__` wins. Then non-data descriptors — like plain functions, which is how bound methods are created — and then plain class attributes. If all that fails it raises `AttributeError`, and `__getattr__` is called as a fallback if defined. Properties, methods, classmethods, staticmethods, `cached_property`, and `__slots__` are all built on this."

### 📝 Revision notes
```
descriptor = class attr with __get__/__set__/__delete__ ; __set_name__(owner, name)
DATA (has __set__/__delete__) > instance __dict__ > NON-DATA (__get__ only) > class attr > __getattr__
set: data descriptor __set__ else instance __dict__
function = non-data descriptor → bound method ; property = data ; cached_property = non-data writing __dict__
__getattribute__ every access (recursion risk → object.__getattribute__) ; __getattr__ only on miss
implicit dunder lookup uses type(obj), bypasses instance & __getattr__
```

---

## M11. Properties & Decorators

### Properties in depth
`property` is a built-in **data descriptor** class: `property(fget=None, fset=None, fdel=None, doc=None)`.
```python
class Circle:
    def __init__(self, r): self.radius = r

    def _get_radius(self): return self._r
    def _set_radius(self, v):
        if v < 0: raise ValueError("negative radius")
        self._r = v
    radius = property(_get_radius, _set_radius, doc="Radius (validated)")   # classic form

    @property                    # decorator form: area = property(area)
    def area(self): return 3.14159 * self._r ** 2

print(type(Circle.__dict__["radius"]).__name__)   # property
print(Circle.radius.__doc__)                      # Radius (validated)
```
- `@x.setter` returns a **copy** of the property with `fset` added — which is why the setter function **must have the same name** (`x`), otherwise you end up with two different properties.
- A property without a setter raises `AttributeError` on assignment (3.11+: "property 'area' of 'Circle' object has no setter").
- Properties are **class-level**: you can't add a property to a single instance.

### Property vs method vs plain attribute
| Use | When |
|---|---|
| Plain attribute | Simple data, no rules (start here) |
| Property | Looks like data; cheap to compute; needs validation/derivation/read-only |
| Method | Does work, has side effects, takes arguments, or is expensive (`user.fetch_orders()`) |
| `cached_property` | Expensive, computed once per instance, doesn't change |

⚠️ Don't hide slow I/O behind a property — `order.total` should not make a network call.

### Decorators in depth

**1. Function decorator (recap)** — `@deco` above `def f` means `f = deco(f)`.

**2. Decorator with arguments** — three levels: factory → decorator → wrapper.
```python
import functools, time

def retry(times=3, exceptions=(Exception,), delay=0.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    if attempt == times:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

calls = {"n": 0}
@retry(times=3, exceptions=(ConnectionError,))
def flaky():
    calls["n"] += 1
    if calls["n"] < 3: raise ConnectionError
    return "ok"
print(flaky(), calls["n"])   # ok 3
```
`@retry(times=3)` → `flaky = retry(times=3)(flaky)`.

**3. Why `functools.wraps`?** Without it, the wrapper replaces the function's `__name__`, `__doc__`, `__module__`, `__qualname__`, and `__wrapped__` isn't set — breaking debugging, logging, docs, and framework introspection (e.g., FastAPI/Flask route names).

**4. Stacking order** — applied bottom-up, executed top-down:
```python
@a
@b
def f(): ...      # f = a(b(f)) → calling f runs a's wrapper first, then b's
```

**5. Decorators on methods** — the wrapper receives `self` as the first positional arg automatically, because the decorated result is still a function (a descriptor) stored in the class:
```python
def log_call(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        print(f"{type(self).__name__}.{func.__name__}{args}")
        return func(self, *args, **kwargs)
    return wrapper

class Service:
    @log_call
    def process(self, x): return x * 2
print(Service().process(5))    # Service.process(5,)  then 10
```

**6. Class-based decorators (stateful)** — and the method-binding trap:
```python
class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func, self.count = func, 0
    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)
    def __get__(self, inst, owner):             # needed to work on METHODS
        if inst is None: return self
        return functools.partial(self.__call__, inst)   # bind the instance like a function would

@CountCalls
def ping(): return "pong"
ping(); ping()
print(ping.count)        # 2
```
Without `__get__`, decorating a method with a class instance breaks: an instance of `CountCalls` isn't a descriptor, so `obj.method()` wouldn't pass `self`.

**7. Class decorators** — take a class, return a (usually the same, modified) class:
```python
REGISTRY = {}
def register(cls):
    REGISTRY[cls.__name__.lower()] = cls
    return cls

@register
class StripeGateway: ...
print(REGISTRY)          # {'stripegateway': <class '__main__.StripeGateway'>}
```
`@dataclass`, `@functools.total_ordering`, and `@runtime_checkable` are class decorators.

### 🎤 Interview-ready answer: "How does `@property` work?"
> "`property` is a built-in data descriptor class. `@property` replaces the method with a property object holding it as `fget`; `@x.setter` returns a copy with `fset` added, which is why the setter must reuse the name. When I access `obj.x`, attribute lookup finds the property in the class, and since it's a data descriptor it takes priority over the instance `__dict__` and calls `fget(obj)`. Assignment calls `fset`, or raises `AttributeError` if there's none — that's how read-only attributes work. I use properties for validation and cheap computed values while keeping attribute syntax, so a plain attribute can become managed later without changing callers."

### 📝 Revision notes
```
property(fget, fset, fdel, doc) = data descriptor ; setter returns copy → same name
property: cheap data-like ; method: work/side effects/args ; cached_property: expensive once
decorator: f = deco(f) ; with args: factory→decorator→wrapper ; always functools.wraps
stack: @a @b f → a(b(f)) ; class-based decorator on methods needs __get__
class decorators: registries, @dataclass, @total_ordering
```

---

## M12. Dunder Methods — The Complete Data Model

### What are they?
**Dunder** ("double underscore") / **magic** / **special** methods are hooks that let your objects plug into Python's syntax and built-ins. You **implement** them; Python **calls** them. You almost never call them directly (`len(x)`, not `x.__len__()`).

### Three rules that apply to every dunder
1. **Looked up on the type, not the instance** (`type(obj).__len__`) — and implicit calls bypass `__getattribute__`/`__getattr__` ([M10 §9](#m10-attribute-lookup--descriptors)).
2. **Return `NotImplemented`** (a singleton, not an exception) from binary operators/comparisons when you don't support the other operand — Python then tries the other side. Don't confuse with `raise NotImplementedError` (for abstract methods).
3. **Never invent your own `__names__`** — the namespace is reserved for Python.

### Importance legend
⭐ Essential · 🔶 Important · 🔷 Advanced · ⚪ Rare/specialised

---

### Category A: Object creation & destruction
| Method | Triggered by | Receives | Returns | Level |
|---|---|---|---|---|
| `__new__(cls, *a, **kw)` | `Cls(...)` via `type.__call__` | the class + call args | the new instance | 🔶 |
| `__init__(self, *a, **kw)` | after `__new__` returns an instance of `cls` | instance + call args | `None` | ⭐ |
| `__del__(self)` | refcount → 0 / GC collects | instance | ignored | 🔷 |

Full treatment: [M8](#m8-object-creation--lifecycle).

---

### Category B: Representation
| Method | Triggered by | Must return | If missing | Level |
|---|---|---|---|---|
| `__repr__` | `repr(obj)`, REPL echo, inside containers, `!r`, debuggers | `str` | `<module.Cls object at 0x...>` | ⭐ |
| `__str__` | `str(obj)`, `print(obj)`, `f"{obj}"` (via `__format__`), `%s` | `str` | falls back to `__repr__` | ⭐ |
| `__format__(self, spec)` | `format(obj, spec)`, `f"{obj:spec}"` | `str` | `object.__format__`: `str(self)` if spec is empty, else `TypeError` | 🔶 |
| `__bytes__` | `bytes(obj)` | `bytes` | `TypeError` | ⚪ |
| (`ascii(obj)`) | uses `repr()` and escapes non-ASCII | — | — | ⚪ |

```python
class Money:
    def __init__(self, amount): self.amount = amount
    def __repr__(self): return f"Money({self.amount!r})"
    def __str__(self): return f"₹{self.amount:,.2f}"
    def __format__(self, spec):
        if spec == "short":
            return f"₹{self.amount / 1000:.1f}k"
        return format(str(self), spec)          # delegate width/alignment specs to str
    def __bytes__(self): return str(self.amount).encode()

m = Money(125000)
print(m)                 # ₹125,000.00
print(repr(m))           # Money(125000)
print(f"{m:short}")      # ₹125.0k
print(f"[{m:>15}]")      # [    ₹125,000.00]
print(bytes(m))          # b'125000'
```
Deep dive: [M13](#m13-__str__-vs-__repr__--master-module).

---

### Category C: Attribute access
| Method | Triggered by | Returns | Level |
|---|---|---|---|
| `__getattribute__(self, name)` | **every** `obj.name` | value or raise `AttributeError` | 🔷 |
| `__getattr__(self, name)` | only when normal lookup raises `AttributeError` | value or raise `AttributeError` | 🔶 |
| `__setattr__(self, name, value)` | `obj.name = value`, `setattr()` | `None` | 🔶 |
| `__delattr__(self, name)` | `del obj.name`, `delattr()` | `None` | 🔷 |
| `__dir__(self)` | `dir(obj)` | iterable of names | ⚪ |

```python
class ReadOnlyAfterInit:
    def __init__(self, **fields):
        for k, v in fields.items():
            object.__setattr__(self, k, v)          # bypass our own guard
        object.__setattr__(self, "_frozen", True)
    def __setattr__(self, name, value):
        if getattr(self, "_frozen", False):
            raise AttributeError(f"cannot modify {name!r}: object is frozen")
        super().__setattr__(name, value)            # ✅ never self.name = value here (recursion)
    def __delattr__(self, name):
        raise AttributeError("cannot delete attributes")

cfg = ReadOnlyAfterInit(db="postgres", pool=10)
try:
    cfg.pool = 20
except AttributeError as e:
    print(e)                # cannot modify 'pool': object is frozen
```
Lookup order and recursion traps: [M10](#m10-attribute-lookup--descriptors).

---

### Category D: Callable objects — `__call__`
| Method | Triggered by | Level |
|---|---|---|
| `__call__(self, *a, **kw)` | `obj(...)` | ⭐ |

A class with `__call__` makes **instances** callable — a function with state and configuration.
```python
import time

class RateLimiter:
    """Allow at most `limit` calls per `window` seconds."""
    def __init__(self, limit, window):
        self.limit, self.window, self.calls = limit, window, []
    def __call__(self) -> bool:
        now = time.monotonic()
        self.calls = [t for t in self.calls if now - t < self.window]
        if len(self.calls) < self.limit:
            self.calls.append(now)
            return True
        return False

allow = RateLimiter(limit=2, window=1.0)
print(allow(), allow(), allow())    # True True False
print(callable(allow))              # True
```
- `callable(obj)` is `True` if `type(obj)` defines `__call__` (functions, classes, bound methods, instances with `__call__`).
- **Classes are callable** because their metaclass (`type`) defines `__call__` — that's the instantiation mechanism from [M8](#m8-object-creation--lifecycle).
- Connection to decorators: any callable can be a decorator, so class-based decorators use `__call__` ([M11](#m11-properties--decorators)).
- Backend uses: middleware objects (`__call__(request)`), strategy objects, configured validators, ASGI apps (`async def __call__(self, scope, receive, send)`).

---

### Category E: Comparison (rich comparisons)
| Expression | Method called | Reflected fallback | Level |
|---|---|---|---|
| `a == b` | `a.__eq__(b)` | `b.__eq__(a)`, then identity (`a is b`) | ⭐ |
| `a != b` | `a.__ne__(b)` | `b.__ne__(a)`; default `__ne__` inverts `__eq__` | ⭐ |
| `a < b` | `a.__lt__(b)` | `b.__gt__(a)`, else `TypeError` | ⭐ |
| `a <= b` | `a.__le__(b)` | `b.__ge__(a)` | ⭐ |
| `a > b` | `a.__gt__(b)` | `b.__lt__(a)` | ⭐ |
| `a >= b` | `a.__ge__(b)` | `b.__le__(a)` | ⭐ |

Rules:
- Return `NotImplemented` for unsupported types → Python tries the reflected method → `==` finally falls back to identity, ordering raises `TypeError`.
- If the right operand's type is a **subclass** of the left's and overrides the reflected method, the **right side is tried first**.
- No automatic derivation of `<=` from `<` and `==` — use `functools.total_ordering`.
- Chaining: `a < b < c` means `a < b and b < c` (b evaluated once).
- Sorting (`sorted`, `list.sort`, `min`, `max`, `heapq`) only needs `__lt__`.

```python
from functools import total_ordering

@total_ordering                          # supply __eq__ + ONE of lt/le/gt/ge; it derives the rest
class Version:
    def __init__(self, s): self.parts = tuple(int(p) for p in s.split("."))
    def __eq__(self, other):
        if not isinstance(other, Version): return NotImplemented
        return self.parts == other.parts
    def __lt__(self, other):
        if not isinstance(other, Version): return NotImplemented
        return self.parts < other.parts
    def __hash__(self): return hash(self.parts)
    def __repr__(self): return f"Version('{'.'.join(map(str, self.parts))}')"

vs = [Version("1.10.0"), Version("1.2.0"), Version("1.9.3")]
print(sorted(vs))                         # [Version('1.2.0'), Version('1.9.3'), Version('1.10.0')]
print(Version("2.0") >= Version("1.9"))   # True (derived)
print(Version("1.0") == "1.0")            # False (both sides NotImplemented → identity)
```
`total_ordering` derived methods are slightly slower; for hot paths, define all four. Dataclasses can generate them with `@dataclass(order=True)`.

---

### Category F: Hashing — `__hash__`
| Method | Triggered by | Returns | Level |
|---|---|---|---|
| `__hash__(self)` | `hash(obj)`, dict keys, set members | `int` | ⭐ |

**The contract:** if `a == b` then `hash(a) == hash(b)` (the reverse need not hold). A hash must **not change** while the object is in a dict/set.
**The trap:** defining `__eq__` without `__hash__` sets `__hash__ = None` → instances become **unhashable**. Full treatment: [M14](#m14-identity-equality-hashing--copying).

---

### Categories G, H, I: Arithmetic, reflected, and in-place operators
| Operator | Normal | Reflected | In-place | Level |
|---|---|---|---|---|
| `+` | `__add__` | `__radd__` | `__iadd__` (`+=`) | ⭐ |
| `-` | `__sub__` | `__rsub__` | `__isub__` | ⭐ |
| `*` | `__mul__` | `__rmul__` | `__imul__` | ⭐ |
| `/` | `__truediv__` | `__rtruediv__` | `__itruediv__` | 🔶 |
| `//` | `__floordiv__` | `__rfloordiv__` | `__ifloordiv__` | 🔶 |
| `%` | `__mod__` | `__rmod__` | `__imod__` | 🔶 |
| `**` | `__pow__` | `__rpow__` | `__ipow__` | 🔶 |
| `@` | `__matmul__` | `__rmatmul__` | `__imatmul__` | 🔷 |
| `divmod()` | `__divmod__` | `__rdivmod__` | — | ⚪ |
| `&` `\|` `^` | `__and__` `__or__` `__xor__` | `__rand__` … | `__iand__` … | 🔷 |
| `<<` `>>` | `__lshift__` `__rshift__` | `__rlshift__` … | `__ilshift__` … | ⚪ |
| unary `-x` `+x` `~x` | `__neg__` `__pos__` `__invert__` | — | — | 🔶 |

**How `a + b` is evaluated:**
```text
1. If type(b) is a proper subclass of type(a) AND overrides __radd__ → try b.__radd__(a) first
2. r = a.__add__(b)          → if not NotImplemented, done
3. r = b.__radd__(a)         → only if types differ; if not NotImplemented, done
4. TypeError: unsupported operand type(s)
```
**How `a += b` is evaluated:**
```text
1. if type(a) has __iadd__: a = a.__iadd__(b)   (should mutate self and RETURN self)
2. else: a = a + b                               (falls back to __add__/__radd__ → new object, rebinding)
```

```python
import math

class Vector:
    def __init__(self, x, y): self.x, self.y = x, y
    def __repr__(self): return f"Vector({self.x}, {self.y})"
    def __eq__(self, o):
        return isinstance(o, Vector) and (self.x, self.y) == (o.x, o.y)
    def __hash__(self): return hash((self.x, self.y))

    def __add__(self, o):
        if not isinstance(o, Vector): return NotImplemented
        return Vector(self.x + o.x, self.y + o.y)
    def __radd__(self, o):
        if o == 0: return self                  # lets sum() start from 0
        return NotImplemented
    def __sub__(self, o):
        if not isinstance(o, Vector): return NotImplemented
        return Vector(self.x - o.x, self.y - o.y)
    def __mul__(self, k):                       # scalar multiplication
        if not isinstance(k, (int, float)): return NotImplemented
        return Vector(self.x * k, self.y * k)
    __rmul__ = __mul__                          # k * v → v.__rmul__(k)
    def __matmul__(self, o): return self.x * o.x + self.y * o.y   # dot product
    def __neg__(self): return Vector(-self.x, -self.y)
    def __abs__(self): return math.hypot(self.x, self.y)
    def __bool__(self): return bool(self.x or self.y)

a, b = Vector(1, 2), Vector(3, 4)
print(a + b, b - a, a * 3, 3 * a)        # Vector(4, 6) Vector(2, 2) Vector(3, 6) Vector(3, 6)
print(a @ b, abs(b), -a, bool(Vector(0, 0)))   # 11 5.0 Vector(-1, -2) False
print(sum([a, b, Vector(1, 1)]))         # Vector(5, 7)   ← 0 + a uses a.__radd__(0)
try:
    a + 5
except TypeError as e:
    print("TypeError")                   # both sides returned NotImplemented
```

**In-place: mutate vs rebind**
```python
v = Vector(1, 2); alias = v
v += Vector(1, 1)                 # no __iadd__ → v = v + ... → NEW object
print(v, alias, v is alias)       # Vector(2, 3) Vector(1, 2) False

class Cart:
    def __init__(self): self.items = []
    def __iadd__(self, item):
        self.items.append(item)   # mutate in place
        return self               # ⚠️ MUST return self, or the name becomes None
c = Cart(); alias = c
c += "book"
print(alias.items, c is alias)    # ['book'] True
```
This is exactly the `list` vs `tuple` difference: `lst += [x]` mutates (`list.__iadd__`), `tup += (x,)` rebinds.

---

### Category J: Collection emulation (containers, iteration)
| Method | Triggered by | Returns | Fallback if missing | Level |
|---|---|---|---|---|
| `__len__` | `len(obj)`, truthiness fallback | `int ≥ 0` | `TypeError` | ⭐ |
| `__getitem__(self, key)` | `obj[key]`, slicing (`key` is a `slice`) | item | `TypeError` | ⭐ |
| `__setitem__(self, key, v)` | `obj[key] = v` | `None` | `TypeError` | ⭐ |
| `__delitem__(self, key)` | `del obj[key]` | `None` | `TypeError` | 🔶 |
| `__contains__(self, item)` | `item in obj` | `bool` | iterate via `__iter__`, else `__getitem__` | ⭐ |
| `__iter__` | `iter(obj)`, `for`, unpacking, `list(obj)` | an **iterator** | old protocol: `__getitem__(0, 1, …)` until `IndexError` | ⭐ |
| `__next__` | `next(it)` | next item / raise `StopIteration` | — | ⭐ |
| `__reversed__` | `reversed(obj)` | iterator | uses `__len__` + `__getitem__` | 🔶 |
| `__missing__(self, key)` | `dict` subclass `__getitem__` on missing key | value | `KeyError` | 🔶 |
| `__length_hint__` | `operator.length_hint` (pre-sizing) | `int` | — | ⚪ |

Invalid index → raise `IndexError`; invalid key → `KeyError`; wrong type → `TypeError`.

```python
class Playlist:
    def __init__(self, songs=()): self._songs = list(songs)
    def __len__(self): return len(self._songs)
    def __getitem__(self, idx):
        if isinstance(idx, slice):
            return Playlist(self._songs[idx])     # slicing returns same type
        return self._songs[idx]                   # raises IndexError naturally
    def __setitem__(self, idx, song): self._songs[idx] = song
    def __delitem__(self, idx): del self._songs[idx]
    def __contains__(self, song): return song in self._songs
    def __iter__(self): return iter(self._songs)
    def __reversed__(self): return reversed(self._songs)
    def __repr__(self): return f"Playlist({self._songs})"

p = Playlist(["a", "b", "c", "d"])
print(len(p), p[0], p[-1], p[1:3])       # 4 a d Playlist(['b', 'c'])
p[0] = "A"; del p[3]
print("A" in p, list(reversed(p)))       # True ['c', 'b', 'A']
for song in p: print(song, end=" ")      # A b c
print()
```
**The old sequence protocol** — only `__getitem__` is enough for iteration and `in`:
```python
class Squares:
    def __getitem__(self, i):
        if i >= 5: raise IndexError
        return i * i
print(list(Squares()), 9 in Squares())   # [0, 1, 4, 9, 16] True
```
**`__missing__`:**
```python
class DefaultZero(dict):
    def __missing__(self, key): return 0
d = DefaultZero(a=1)
print(d["a"], d["zzz"])                  # 1 0
```
✅ **Shortcut:** inherit from `collections.abc.Sequence` / `MutableMapping` etc. — implement the abstract core (`__getitem__`, `__len__`) and get `__contains__`, `__iter__`, `__reversed__`, `index`, `count` for free. Iterators/generators in depth: [M15](#m15-iterators-generators--context-managers).

---

### Category K: Boolean & numeric conversion
| Method | Triggered by | Must return | Fallback | Level |
|---|---|---|---|---|
| `__bool__` | `bool(obj)`, `if obj`, `while obj`, `and/or/not` | `bool` | `__len__() != 0`, else **True** | ⭐ |
| `__int__` | `int(obj)` | `int` | `__index__` (the old `__trunc__` fallback is deprecated since 3.11), else `TypeError` | 🔶 |
| `__float__` | `float(obj)` | `float` | `__index__` | 🔶 |
| `__complex__` | `complex(obj)` | `complex` | `__float__` / `__index__` | ⚪ |
| `__index__` | slicing/indexing, `bin()`, `hex()`, `oct()`, `operator.index()`, `range()` | `int` (lossless!) | `TypeError` | 🔷 |
| `__abs__` | `abs(obj)` | number | `TypeError` | 🔶 |
| `__round__(self, n=None)` | `round(obj[, n])` | number | `TypeError` | ⚪ |
| `__trunc__` / `__floor__` / `__ceil__` | `math.trunc/floor/ceil(obj)` | number | `TypeError` (floor/ceil fall back to `__float__`) | ⚪ |

```python
import math
class Basket:
    def __init__(self, items): self.items = items
    def __len__(self): return len(self.items)          # no __bool__ → truthiness uses __len__
print(bool(Basket([])), bool(Basket([1])))             # False True
class Plain: pass
print(bool(Plain()))                                   # True  ← default for any object

class Slot:
    def __init__(self, n): self.n = n
    def __index__(self): return self.n                 # "I am an integer" — lossless conversion
print([10, 20, 30][Slot(2)], bin(Slot(5)), list(range(Slot(3))))   # 30 0b101 [0, 1, 2]

class Price:
    def __init__(self, v): self.v = v
    def __float__(self): return float(self.v)
    def __round__(self, n=None): return Price(round(self.v, n))
    def __floor__(self): return math.floor(self.v)
    def __repr__(self): return f"Price({self.v})"
print(float(Price(9.99)), round(Price(9.987), 2), math.floor(Price(9.99)))  # 9.99 Price(9.99) 9
```
`__int__` vs `__index__`: `__int__` may lose information (`int(3.9) → 3`); `__index__` promises the object *is* an integer — that's why floats can't be list indices.

---

### Category L: Context managers
| Method | Triggered by | Returns | Level |
|---|---|---|---|
| `__enter__(self)` | entering `with obj as x:` | value bound to `x` (often `self`) | ⭐ |
| `__exit__(self, exc_type, exc, tb)` | leaving the block (normally or via exception) | truthy → **suppress** the exception | ⭐ |
| `__aenter__` / `__aexit__` | `async with` | awaitables (async def) | 🔶 |

Full treatment with execution order: [M15](#m15-iterators-generators--context-managers).

---

### Category M: Async special methods
| Method | Triggered by | Returns | Level |
|---|---|---|---|
| `__await__` | `await obj` | an **iterator** (usually via `yield from` another awaitable's `__await__()`) | 🔷 |
| `__aiter__` | `async for x in obj` | an async iterator (regular `def`, returns object with `__anext__`) | 🔶 |
| `__anext__` | each `async for` step | awaitable; raise `StopAsyncIteration` to stop | 🔶 |
| `__aenter__` / `__aexit__` | `async with obj` | awaitables | 🔶 |

```python
import asyncio

class Countdown:                                   # async iterator
    def __init__(self, n): self.n = n
    def __aiter__(self): return self
    async def __anext__(self):
        if self.n <= 0: raise StopAsyncIteration
        await asyncio.sleep(0)                      # pretend I/O
        self.n -= 1
        return self.n + 1

class DBConnection:                                # async context manager
    async def __aenter__(self):
        print("connect"); return self
    async def __aexit__(self, exc_type, exc, tb):
        print("disconnect"); return False

class Answer:                                      # custom awaitable
    def __await__(self):
        yield from asyncio.sleep(0).__await__()
        return 42

async def main():
    async with DBConnection() as db:
        async for i in Countdown(3):
            print(i, end=" ")
        print()
    print(await Answer())

asyncio.run(main())
```
```text
connect
3 2 1
disconnect
42
```
In practice, `async def` coroutines and async generators (`async def` + `yield`) replace most hand-written `__await__`/`__anext__`; `contextlib.asynccontextmanager` replaces hand-written `__aenter__`/`__aexit__`.

---

### Category N: Descriptors & class creation hooks
| Method | Defined on | Triggered by | Level |
|---|---|---|---|
| `__get__`, `__set__`, `__delete__` | descriptor class | attribute access on owner's instances | 🔷 |
| `__set_name__(self, owner, name)` | descriptor class | owner class creation | 🔷 |
| `__init_subclass__(cls, **kw)` | base class (implicit classmethod) | a subclass being created | 🔶 |
| `__class_getitem__(cls, item)` | class (implicit classmethod) | `Cls[int]` (generic aliases) | ⚪ |
| `__prepare__(name, bases, **kw)` | **metaclass** (classmethod) | before class body executes → returns namespace mapping | ⚪ |
| `__instancecheck__` / `__subclasscheck__` | **metaclass** | `isinstance` / `issubclass` | ⚪ |
| `__subclasshook__` | ABC (classmethod) | `issubclass` against an ABC | ⚪ |
| `__mro_entries__` | non-class base object | used in a `class` statement's bases | ⚪ |

```python
class Plugin:
    registry = {}
    def __init_subclass__(cls, name=None, **kwargs):     # runs for every SUBCLASS definition
        super().__init_subclass__(**kwargs)
        Plugin.registry[name or cls.__name__.lower()] = cls

class CSVExporter(Plugin, name="csv"): pass
class JSONExporter(Plugin): pass
print(Plugin.registry)   # {'csv': <class '__main__.CSVExporter'>, 'jsonexporter': <class '__main__.JSONExporter'>}
```
`__init_subclass__` replaces most metaclass use cases (registries, validation of subclasses). Descriptors: [M10](#m10-attribute-lookup--descriptors). Metaclasses & `__prepare__`: [M17](#m17-advanced-python-oop).

---

### Category O: Other important special methods & attributes
| Name | Purpose | Level |
|---|---|---|
| `__copy__`, `__deepcopy__(memo)` | Customise `copy.copy` / `copy.deepcopy` ([M14](#m14-identity-equality-hashing--copying)) | 🔶 |
| `__getstate__`, `__setstate__` | Customise pickling/copying state (e.g., drop a DB connection) | 🔷 |
| `__reduce__`, `__reduce_ex__` | Low-level pickling protocol | ⚪ |
| `__sizeof__` | `sys.getsizeof` | ⚪ |
| `__fspath__` | `os.fspath`, makes object accepted where paths are (`open(obj)`) | ⚪ |
| `__match_args__` | Positional patterns in `match` statements | ⚪ |
| `__buffer__` / `__release_buffer__` | Buffer protocol (3.12+) | ⚪ |
| `__post_init__` | **Not data model** — dataclass hook after generated `__init__` | 🔶 |
| `__slots__` | Class attribute: fixed attribute set, no `__dict__` ([M17](#m17-advanced-python-oop)) | 🔶 |
| `__dict__`, `__class__`, `__module__`, `__name__`, `__qualname__`, `__doc__`, `__mro__`, `__bases__`, `__annotations__` | Introspection attributes | 🔶 |

---

### 📊 Complete dunder revision table
| Category | ⭐ Essential | 🔶 Important | 🔷 Advanced | ⚪ Rare |
|---|---|---|---|---|
| Creation | `__init__` | `__new__` | `__del__` | — |
| Representation | `__repr__`, `__str__` | `__format__` | — | `__bytes__` |
| Attributes | — | `__getattr__`, `__setattr__` | `__getattribute__`, `__delattr__` | `__dir__` |
| Callable | `__call__` | — | — | — |
| Comparison | `__eq__`, `__lt__` (+ others) | `__ne__` behaviour | — | — |
| Hashing | `__hash__` | — | — | — |
| Arithmetic | `__add__`, `__sub__`, `__mul__` | `__truediv__`, `__floordiv__`, `__mod__`, `__pow__`, `__r*__`, `__i*__`, `__neg__` | `__matmul__`, bitwise | `__divmod__`, shifts |
| Containers | `__len__`, `__getitem__`, `__setitem__`, `__contains__`, `__iter__`, `__next__` | `__delitem__`, `__reversed__`, `__missing__` | — | `__length_hint__` |
| Conversion | `__bool__` | `__int__`, `__float__`, `__abs__` | `__index__` | `__complex__`, `__round__`, `__trunc__`, `__floor__`, `__ceil__` |
| Context | `__enter__`, `__exit__` | `__aenter__`, `__aexit__` | — | — |
| Async | — | `__aiter__`, `__anext__` | `__await__` | — |
| Class machinery | — | `__init_subclass__` | `__get__`, `__set__`, `__delete__`, `__set_name__` | `__prepare__`, `__class_getitem__`, `__instancecheck__`, `__subclasscheck__`, `__subclasshook__`, `__mro_entries__` |
| Copy/pickle | — | `__copy__`, `__deepcopy__` | `__getstate__`, `__setstate__` | `__reduce__`, `__reduce_ex__` |

### Common mistakes with dunders
- Raising `NotImplementedError` (or `TypeError`) instead of **returning** `NotImplemented` in operators.
- `__iadd__` that forgets `return self`.
- `__eq__` without `__hash__` (unhashable) or hashing mutable fields.
- `__repr__`/`__str__` returning non-strings.
- Setting dunders on instances (`obj.__len__ = ...`) — implicit calls ignore them.
- `__bool__` returning a non-bool (e.g., `0` → `TypeError`).
- Overloading operators with surprising semantics (`+` that mutates).

### 🎤 Interview-ready answer: "What are dunder methods?"
> "They're Python's data-model hooks — methods with double-underscore names that the interpreter calls to implement syntax and built-ins: `len(x)` calls `type(x).__len__`, `a + b` calls `__add__` and falls back to `b.__radd__` if the first returns `NotImplemented`, `with` calls `__enter__`/`__exit__`, `for` calls `__iter__`/`__next__`. They're looked up on the type, not the instance, which is why you can't monkey-patch them on a single object. Implementing them is how you make custom objects behave like built-ins — like a `Money` type with arithmetic and formatting, or a collection that supports indexing, slicing, and iteration."

---

## M13. `__str__` vs `__repr__` — Master Module

### 1. What are they?
| | `__repr__` | `__str__` |
|---|---|---|
| Audience | **Developers** (debugging, logs, REPL) | **End users** (UI, messages) |
| Goal | **Unambiguous** — ideally `eval(repr(obj)) == obj` | **Readable** |
| Called by | `repr()`, REPL echo, containers' str/repr, `!r`, `f"{x=}"`, debuggers, `%r` | `str()`, `print()`, `f"{x}"`, `format(x)` (empty spec), `%s`, `logging` `%s` args |
| Default (`object`) | `<module.ClassName object at 0x7f...>` | **falls back to `__repr__`** |

**Rule of thumb:** *always* write `__repr__`. Add `__str__` only if users need a different, friendlier form.

### 2. Why two methods?
`str(datetime)` → `2026-11-13 10:00:00` (for humans) vs `repr(datetime)` → `datetime.datetime(2026, 11, 13, 10, 0)` (tells a developer *exactly* what it is). For strings: `str("42")` → `42`, `repr("42")` → `'42'` — the quotes tell you it's a string, not an int. That ambiguity is precisely what `repr` resolves.

### 3. Internal mechanism — who calls what
```text
print(obj)            → str(obj)        → type(obj).__str__(obj)    → (object.__str__ calls repr)
str(obj)              → type(obj).__str__(obj)
repr(obj)             → type(obj).__repr__(obj)
f"{obj}"              → format(obj, "") → type(obj).__format__(obj, "") → object.__format__ → str(obj)
f"{obj!r}"            → repr(obj)
f"{obj!s}"            → str(obj)
f"{obj!a}"            → ascii(obj)      → repr(obj) with non-ASCII escaped
f"{obj=}"             → "obj=" + repr(obj)     (3.8+)
str([obj])            → list.__repr__   → repr(obj) for each element   ← containers ALWAYS use repr
logging.info("%s", obj) → str(obj)  (lazily, only if the record is emitted)
REPL: >>> obj         → repr(obj)
```

### 4. The four cases (memorise these)
```python
class Neither:
    def __init__(self): self.x = 1

class OnlyStr:
    def __str__(self): return "OnlyStr-str"

class OnlyRepr:
    def __repr__(self): return "OnlyRepr()"

class Both:
    def __str__(self): return "Both-str"
    def __repr__(self): return "Both()"
```
| Expression | `Neither` | `OnlyStr` | `OnlyRepr` | `Both` |
|---|---|---|---|---|
| `print(obj)` / `str(obj)` | `<__main__.Neither object at 0x…>` | `OnlyStr-str` | `OnlyRepr()` ← fallback | `Both-str` |
| `repr(obj)` | `<__main__.Neither object at 0x…>` | `<__main__.OnlyStr object at 0x…>` ⚠️ | `OnlyRepr()` | `Both()` |
| `f"{obj}"` | `<… object at 0x…>` | `OnlyStr-str` | `OnlyRepr()` | `Both-str` |
| `print([obj])` | `[<… object at 0x…>]` | `[<__main__.OnlyStr object at 0x…>]` ⚠️ | `[OnlyRepr()]` | `[Both()]` |

**Key takeaways:**
- `__str__` falls back to `__repr__`, but **never the other way round**.
- Containers show `repr` of their elements → defining only `__str__` gives ugly lists/dicts/logs. That's why `__repr__` is the one to always define.

### 5. Detailed example: a good `__repr__`
```python
class Order:
    def __init__(self, order_id, customer, amount):
        self.order_id, self.customer, self.amount = order_id, customer, amount

    def __repr__(self):
        # !r → strings get quotes; type(self).__name__ → correct name for subclasses
        return (f"{type(self).__name__}(order_id={self.order_id!r}, "
                f"customer={self.customer!r}, amount={self.amount!r})")

    def __str__(self):
        return f"Order #{self.order_id} for {self.customer}: ₹{self.amount:,}"

o = Order(101, "Parth", 2500)
print(o)          # Order #101 for Parth: ₹2,500
print(repr(o))    # Order(order_id=101, customer='Parth', amount=2500)
print([o])        # [Order(order_id=101, customer='Parth', amount=2500)]
print(f"{o=}")    # o=Order(order_id=101, customer='Parth', amount=2500)
class PriorityOrder(Order): pass
print(repr(PriorityOrder(1, "A", 9)))   # PriorityOrder(order_id=1, customer='A', amount=9)
```

### 6. Conventions
1. If possible, make `repr` look like a valid constructor call: `Point(x=1, y=2)`.
2. If not possible (connections, files), use angle brackets with key info: `<DBConnection host='db1' open=True>`.
3. Use `!r` for fields so `'1'` and `1` are distinguishable.
4. Never put secrets in `repr` (passwords, tokens) — reprs end up in logs and error trackers.
5. Keep `repr` cheap and side-effect free — debuggers call it constantly.
6. For recursive structures, use `reprlib.recursive_repr()` to avoid infinite recursion.
7. `@dataclass` generates a good `__repr__` for you.

### 7. Common mistakes
- Defining only `__str__` (containers and logs show `<object at 0x…>`).
- Returning non-`str` (→ `TypeError: __str__ returned non-string`).
- Hard-coding the class name in `repr` (wrong for subclasses).
- Printing inside `__repr__` instead of returning.

### 8. Interview questions
| Question | Expected answer |
|---|---|
| What does `print` call? | `str()` → `__str__`, which falls back to `__repr__` |
| What do containers use for their elements? | `repr` |
| Only `__str__` defined — what does `repr(obj)` show? | Default `<… object at 0x…>` |
| What should a good `repr` look like? | Unambiguous, ideally a constructor call; `eval(repr(x)) == x` |
| What do f-strings use? | `format(obj, spec)` → `__format__` → `str` for empty spec; `!r` for repr |

### 🎤 Interview-ready answer
> "`__repr__` is the developer-facing, unambiguous representation — used by `repr()`, the REPL, debuggers, and for elements inside containers — ideally something like a constructor call. `__str__` is the user-facing, readable form used by `print`, `str()`, and f-strings. If `__str__` isn't defined, Python falls back to `__repr__`, but not vice versa — so I always define `__repr__`, and add `__str__` only when users need a friendlier form. I use `!r` for fields and `type(self).__name__` so it stays correct for subclasses, and I keep secrets out of it since reprs end up in logs."

### 📝 Revision notes
```
repr = developers, unambiguous, eval-able ; str = users, readable
str falls back to repr, NEVER reverse ; containers use repr of elements
print/str/f"{x}"/%s → str ; repr/REPL/!r/f"{x=}"/containers → repr
ALWAYS define __repr__ ; use !r and type(self).__name__ ; no secrets
```

---

## M14. Identity, Equality, Hashing & Copying

### 1. How these connect
```text
identity  (is, id)      → "same object?"         → cannot be customised
equality  (==, __eq__)  → "same value?"          → you define it
hashing   (__hash__)    → "which bucket?"        → MUST agree with equality
copying   (copy module) → "new object with same value" → shallow vs deep
```

### 2. Default behaviour
```python
class P:
    def __init__(self, x): self.x = x
a, b = P(1), P(1)
print(a == b, a is b)            # False False  ← default __eq__ is identity
print(hash(a) == hash(a))        # True         ← default hash derived from id()
```

### 3. Defining equality
```python
class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented            # let the other side try / fall back to identity
        return (self.x, self.y) == (other.x, other.y)

print(Point(1, 2) == Point(1, 2))        # True
print(Point(1, 2) != Point(1, 3))        # True  ← default __ne__ inverts __eq__
try:
    {Point(1, 2)}
except TypeError as e:
    print(e)                             # unhashable type: 'Point'
```
⚠️ **Defining `__eq__` without `__hash__` sets `Point.__hash__ = None`.** Python does this deliberately: the default identity-based hash would violate "equal objects have equal hashes".

### 4. The hash contract
1. `a == b` ⇒ `hash(a) == hash(b)` (unequal objects *may* collide).
2. The hash must **not change** during the object's lifetime in a dict/set → hash only **immutable** state.
3. Implementation: hash a tuple of the same fields used in `__eq__`:
```python
class Point:
    __slots__ = ("_x", "_y")
    def __init__(self, x, y):
        self._x, self._y = x, y
    @property
    def x(self): return self._x            # read-only → effectively immutable
    @property
    def y(self): return self._y
    def __eq__(self, o):
        return NotImplemented if not isinstance(o, Point) else (self.x, self.y) == (o.x, o.y)
    def __hash__(self):
        return hash((self.x, self.y))
print(len({Point(1, 2), Point(1, 2), Point(3, 4)}))   # 2
```

### 5. How dicts and sets actually find keys
```text
d[key]:
  1. h = hash(key) → choose slot
  2. for each candidate entry in that slot chain:
        if entry_key is key        → found (identity shortcut!)
        if entry_hash == h and entry_key == key → found
  3. not found → KeyError (or __missing__)
```
**Trap 1 — mutating a key after insertion makes it unfindable:**
```python
class Key:
    def __init__(self, v): self.v = v
    def __eq__(self, o): return isinstance(o, Key) and self.v == o.v
    def __hash__(self): return hash(self.v)        # hashes MUTABLE state ⚠️

k = Key(1)
d = {k: "value"}
k.v = 2                       # hash changes, but the entry is still in the slot for hash(1)
print(k in d, Key(1) in d)    # False False   ← entry is lost
```
**Trap 2 — the identity shortcut:**
```python
nan = float("nan")
print(nan == nan)             # False
print(nan in [nan], {nan: 1}[nan])   # True 1  ← containers check `is` before `==`
```

### 6. Inheritance & hashing
If a subclass overrides `__eq__` without `__hash__`, **its** `__hash__` becomes `None` even if the parent was hashable. To keep the parent's hash explicitly: `__hash__ = Parent.__hash__`.

### 7. Dataclass equality & hashing rules
| `@dataclass(...)` | `__eq__` | `__hash__` |
|---|---|---|
| default (`eq=True, frozen=False`) | generated | **`None`** (unhashable) |
| `frozen=True` | generated | generated from fields ✅ |
| `unsafe_hash=True` | generated | generated (you promise not to mutate) |
| `eq=False` | identity (inherited) | identity-based (inherited) |

### 8. Copying
| Operation | Creates new outer object? | Inner objects | Example |
|---|---|---|---|
| `b = a` | ❌ (alias) | shared | — |
| Shallow copy | ✅ | **shared** | `copy.copy(a)`, `a[:]`, `list(a)`, `a.copy()`, `dict(a)` |
| Deep copy | ✅ | recursively copied | `copy.deepcopy(a)` |

```python
import copy
team = {"name": "core", "members": ["a", "b"]}
alias = team
shallow = copy.copy(team)
deep = copy.deepcopy(team)

team["members"].append("c")
team["name"] = "platform"
print(alias["name"], alias["members"])       # platform ['a', 'b', 'c']
print(shallow["name"], shallow["members"])   # core ['a', 'b', 'c']   ← new dict, SAME inner list
print(deep["name"], deep["members"])         # core ['a', 'b']        ← fully independent
```
**Circular references:** `deepcopy` keeps a `memo` dict (`id(original) → copy`) so cycles and shared sub-objects are copied once and reconnected correctly.

**Custom copying:**
```python
class Client:
    def __init__(self, url, cache):
        self.url, self.cache, self.session = url, cache, object()   # pretend session is a live socket
    def __copy__(self):
        new = type(self).__new__(type(self))       # create without calling __init__
        new.__dict__.update(self.__dict__)
        new.session = object()                     # never share a live connection
        return new
    def __deepcopy__(self, memo):
        new = type(self).__new__(type(self))
        memo[id(self)] = new                       # register BEFORE recursing (handles cycles)
        new.url = self.url
        new.cache = copy.deepcopy(self.cache, memo)
        new.session = object()
        return new

c1 = Client("https://api", {"k": [1]})
c2 = copy.deepcopy(c1)
print(c2.cache == c1.cache, c2.cache is c1.cache, c2.session is c1.session)   # True False False
```
⚠️ Classic trap: `grid = [[0] * 3] * 3` → three references to the **same** row (`grid[0][0] = 1` changes all rows). Use `[[0] * 3 for _ in range(3)]`.

### 🎤 Interview-ready answer: "`__eq__` and `__hash__` relationship?"
> "`is` checks identity and can't be overridden; `==` calls `__eq__`, which defaults to identity. Hash-based containers find keys by hash first, then confirm with an identity check or `==`, so the contract is that equal objects must have equal hashes, and a hash must not change while the object is in a set or dict. That's why defining `__eq__` alone sets `__hash__` to `None` — the inherited identity hash would break the contract. If I need value objects as keys, I make them immutable — frozen dataclass or read-only properties — and hash a tuple of the same fields I compare in `__eq__`. Hashing mutable state causes keys to silently disappear after mutation."

### 📝 Revision notes
```
is = identity (id) ; == = __eq__ (default identity) ; return NotImplemented for foreign types
__eq__ without __hash__ → __hash__ = None (unhashable) ; subclass overriding __eq__ loses hash too
contract: a == b ⇒ hash(a) == hash(b) ; hash only immutable fields: hash((f1, f2))
dict lookup: hash → slot → `is` shortcut → == ; mutating key = lost entry
dataclass: eq → unhashable unless frozen=True / unsafe_hash
alias vs shallow (shares inner) vs deep (memo handles cycles) ; __copy__/__deepcopy__ for resources
```

---

## M15. Iterators, Generators & Context Managers

### Part A — Iteration protocol
| Term | Definition | Must implement |
|---|---|---|
| **Iterable** | Something you can loop over; `iter(x)` works | `__iter__` returning an iterator (or old-style `__getitem__`) |
| **Iterator** | Produces values one at a time and remembers position | `__next__` (raise `StopIteration` at end) **and** `__iter__` returning `self` |

**What `for x in obj:` really does:**
```python
it = iter(obj)              # type(obj).__iter__(obj)
while True:
    try:
        x = next(it)        # type(it).__next__(it)
    except StopIteration:
        break
    ...                     # loop body
```

**Custom iterator + re-iterable container (the correct design):**
```python
class CountdownIterator:
    def __init__(self, start): self.current = start
    def __iter__(self): return self                   # iterators are iterable (of themselves)
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

class Countdown:                                      # ITERABLE: makes a FRESH iterator each time
    def __init__(self, start): self.start = start
    def __iter__(self): return CountdownIterator(self.start)

c = Countdown(3)
print(list(c), list(c))       # [3, 2, 1] [3, 2, 1]   ← re-iterable

it = CountdownIterator(3)
print(list(it), list(it))     # [3, 2, 1] []          ← iterators are exhausted after one pass
```
⚠️ **Exhaustion trap:** if a class's `__iter__` returns `self` (it's its own iterator), it can only be looped once. Same with `map`, `filter`, `zip`, file objects, and generators.

### Part B — Generators
A **generator function** contains `yield`. Calling it doesn't run the body — it returns a **generator object** (an iterator). Each `next()` runs until the next `yield`, then pauses with all local state preserved.
```python
def countdown(n):
    print("start")
    while n > 0:
        yield n               # pause here, hand n to the caller
        n -= 1
    print("end")              # reaching the end raises StopIteration automatically

g = countdown(2)              # nothing printed yet — lazy
print(next(g))                # start / 2
print(next(g))                # 1
print(list(g))                # end / []
```
**Generators make `__iter__` trivial** (and re-iterable, since each call creates a new generator):
```python
class Countdown:
    def __init__(self, start): self.start = start
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1
```
- **Generator expressions:** `(x * x for x in range(10**9))` — O(1) memory, lazy.
- **`yield from it`** delegates to a sub-iterator (flattening, composing pipelines).
- **Backend uses:** streaming large files/DB result sets in chunks, paginated API clients, lazy ETL pipelines, `StreamingResponse` bodies.
```python
def read_in_batches(rows, size):
    batch = []
    for row in rows:
        batch.append(row)
        if len(batch) == size:
            yield batch
            batch = []
    if batch:
        yield batch
print(list(read_in_batches(range(7), 3)))    # [[0, 1, 2], [3, 4, 5], [6]]
```

### Part C — Context managers
**What & why:** guarantee **setup and teardown** around a block — even if an exception occurs. The reliable replacement for `__del__` and for manual `try/finally`.

**What `with EXPR as VAR: BODY` really does:**
```python
mgr = EXPR
enter, exit_ = type(mgr).__enter__, type(mgr).__exit__   # looked up on the TYPE
VAR = enter(mgr)                                         # value returned by __enter__ (not mgr itself!)
try:
    BODY
except BaseException as e:
    if not exit_(mgr, type(e), e, e.__traceback__):      # truthy return → exception SUPPRESSED
        raise
else:
    exit_(mgr, None, None, None)
```
**Execution order demo:**
```python
class Managed:
    def __init__(self, name, suppress=False): self.name, self.suppress = name, suppress
    def __enter__(self):
        print(f"enter {self.name}")
        return self
    def __exit__(self, exc_type, exc, tb):
        print(f"exit {self.name}, exception={exc_type.__name__ if exc_type else None}")
        return self.suppress

with Managed("A"):
    print("body A")

with Managed("B", suppress=True):
    print("body B")
    raise ValueError("boom")
    print("never runs")
print("after B")

try:
    with Managed("C"):
        raise KeyError("k")
except KeyError:
    print("KeyError propagated")
```
```text
enter A
body A
exit A, exception=None
enter B
body B
exit B, exception=ValueError
after B
enter C
exit C, exception=KeyError
KeyError propagated
```

**Real-world: database transaction**
```python
class Transaction:
    def __init__(self, conn): self.conn = conn
    def __enter__(self):
        self.conn.begin()
        return self.conn
    def __exit__(self, exc_type, exc, tb):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
        return False                 # never swallow errors silently in a transaction
```
**`contextlib` shortcuts:**
```python
from contextlib import contextmanager, suppress, ExitStack, closing
import time

@contextmanager
def timed(label):
    start = time.perf_counter()          # ← __enter__ part
    try:
        yield                            # ← value bound by `as` (here None); body runs now
    finally:
        print(f"{label}: {time.perf_counter() - start:.3f}s")   # ← __exit__ part, always runs

with timed("query"):
    sum(range(10_000))

with suppress(FileNotFoundError):        # ignore one specific exception
    open("/no/such/file")

with ExitStack() as stack:               # dynamic number of context managers
    files = [stack.enter_context(open(__file__)) for _ in range(2)]
```
Async: `async with` uses `__aenter__`/`__aexit__`; `contextlib.asynccontextmanager` is the generator-based shortcut (e.g., acquiring an async DB pool connection, FastAPI `lifespan`).

### 🎤 Interview-ready answer: "Iterable vs iterator?" / "How does `with` work?"
> "An iterable has `__iter__` that returns an iterator; an iterator has `__next__`, raising `StopIteration` when done, and its `__iter__` returns itself. A `for` loop calls `iter()` once and `next()` repeatedly. Containers should return a fresh iterator each time so they're re-iterable — generators make that easy because each call creates new state. For `with`, Python calls `__enter__` on the manager and binds its return value to the `as` target; when the block exits, `__exit__` gets the exception type, value, and traceback — or `None`s — and if it returns a truthy value the exception is suppressed. It's the deterministic way to manage resources like connections, locks, and transactions."

### 📝 Revision notes
```
iterable: __iter__ → iterator ; iterator: __next__ + __iter__ returns self ; StopIteration
iterators exhaust ; containers return fresh iterators ; generator __iter__ = easy & re-iterable
generator: yield pauses & keeps state ; lazy ; yield from delegates
with: v = __enter__() ; body ; __exit__(type, exc, tb) → truthy suppresses
@contextmanager: code before yield = enter, finally after yield = exit
```

---

## M16. Exceptions as Classes

### What & why
Exceptions are **objects** — instances of classes in an inheritance hierarchy. That means `except` clauses are `isinstance` checks, and you design exception hierarchies with the same OOP principles as any other classes.
```text
BaseException
 ├── SystemExit, KeyboardInterrupt, GeneratorExit   ← don't catch these casually
 └── Exception                                      ← catch this (or narrower)
      ├── ValueError, TypeError, KeyError, IndexError, AttributeError ...
      ├── OSError → FileNotFoundError, ConnectionError ...
      └── YourAppError  ← your hierarchy goes here
```

### Designing a domain exception hierarchy
```python
class AppError(Exception):
    """Base for all application errors."""
    status_code = 500
    def __init__(self, message, *, code=None):
        super().__init__(message)
        self.message, self.code = message, code or type(self).__name__

class NotFoundError(AppError):
    status_code = 404

class ValidationError(AppError):
    status_code = 422
    def __init__(self, message, *, field):
        super().__init__(message)
        self.field = field

class PaymentDeclinedError(AppError):
    status_code = 402

def handle(exc: AppError):                 # one handler for the whole hierarchy (polymorphism!)
    return {"status": exc.status_code, "error": exc.code, "message": exc.message}

try:
    raise ValidationError("email is invalid", field="email")
except AppError as e:
    print(handle(e), e.field)
# {'status': 422, 'error': 'ValidationError', 'message': 'email is invalid'} email
```

### Key mechanics
```python
try:
    risky()
except (KeyError, IndexError) as e:   # isinstance check against a tuple; order matters (specific first)
    ...
else:
    ...                               # runs only if NO exception happened
finally:
    ...                               # always runs (cleanup)

raise ServiceError("upstream failed") from err   # explicit chaining → err stored in __cause__
# an exception raised inside an except block is implicitly chained via __context__
# `raise X from None` hides the original context
```
- `except Exception:` — never bare `except:` (it catches `KeyboardInterrupt`/`SystemExit`).
- Python 3.11+: `ExceptionGroup` and `except*` for multiple concurrent errors (e.g., from `asyncio.TaskGroup`).
- Exceptions should carry **data** (fields), not just strings, so handlers can act on them.
- Backend pattern: raise domain exceptions in the service layer; translate them to HTTP responses in **one** place (a FastAPI exception handler / Django middleware).

### 🎤 Interview-ready answer
> "Exceptions are classes, so I design them as a hierarchy: one base application exception carrying shared data like an error code and HTTP status, and specific subclasses for not-found, validation, conflicts. Because `except` does an `isinstance` check, a single handler for the base class can translate any domain error into a response polymorphically. I chain with `raise ... from err` to preserve the root cause, catch `Exception` rather than using a bare `except`, and keep cleanup in `finally` or context managers."

---

# PART V — ADVANCED PYTHON OOP

## M17. Advanced Python OOP

### When are these features worth it?
| Feature | Use when | Unnecessary when |
|---|---|---|
| Protocols | Decoupled interfaces, typing third-party classes | Single implementation, no type checking |
| ABCs | Enforcing implementations, shared template code | Duck typing suffices |
| Mixins | Small orthogonal capabilities reused across classes | Only one class needs it (just write the method) |
| Composition / DI | Swappable dependencies, testability | Trivial scripts |
| Metaclasses | Frameworks (ORMs, plugin systems) that must control class creation | Almost always — use `__init_subclass__` or class decorators |
| `__init_subclass__` | Registries, validating subclasses | No subclass hooks needed |
| Dataclasses | Data-holding classes with little behaviour | Classes with complex invariants or custom `__init__` logic |
| `NamedTuple` | Immutable, tuple-compatible records | Need mutability or methods-heavy classes |
| `Enum` | Fixed set of named constants (status, role) | Open-ended values |
| `__slots__` | Millions of instances, memory-sensitive | Need dynamic attributes; few instances |
| Generics | Reusable typed containers/repositories | Untyped code |

### 1. Duck typing → Protocols → ABCs (recap)
See [M5](#m5-abstraction). Decision rule: **duck typing** for flexibility, **Protocol** to document & type-check that flexibility, **ABC** when you need enforcement at instantiation or shared implementation.

### 2. Composition, delegation & dependency injection
```python
from typing import Protocol

class Cache(Protocol):
    def get(self, key: str): ...
    def set(self, key: str, value, ttl: int) -> None: ...

class Repo(Protocol):
    def find_user(self, user_id: int) -> dict | None: ...

class UserService:
    # DEPENDENCY INJECTION: dependencies are passed in, not constructed inside
    def __init__(self, repo: Repo, cache: Cache):
        self._repo, self._cache = repo, cache

    def get_user(self, user_id: int):
        key = f"user:{user_id}"
        if (hit := self._cache.get(key)) is not None:
            return hit
        user = self._repo.find_user(user_id)
        if user:
            self._cache.set(key, user, ttl=300)
        return user

class InMemoryCache:
    def __init__(self): self._d = {}
    def get(self, key): return self._d.get(key)
    def set(self, key, value, ttl): self._d[key] = value

class FakeRepo:
    def find_user(self, user_id): return {"id": user_id, "name": "Parth"}

svc = UserService(FakeRepo(), InMemoryCache())     # tests inject fakes; prod injects Postgres + Redis
print(svc.get_user(1))                             # {'id': 1, 'name': 'Parth'}
```
- **Composition:** `UserService` *has* a repo and a cache.
- **Delegation:** it forwards work to them (`__getattr__` can automate delegation — [M10](#m10-attribute-lookup--descriptors)).
- **Dependency injection:** the *caller* decides which implementations to use → loose coupling, easy testing. Frameworks: FastAPI `Depends`, `dependency-injector`; often plain constructor injection is enough.

### 3. Classes are objects → dynamic class creation
```python
def make_model(name, fields):                        # class factory
    def __init__(self, **kw):
        for f in fields: setattr(self, f, kw.get(f))
    def __repr__(self):
        return f"{name}(" + ", ".join(f"{f}={getattr(self, f)!r}" for f in fields) + ")"
    return type(name, (object,), {"__init__": __init__, "__repr__": __repr__, "fields": fields})

User = make_model("User", ["id", "email"])           # type(name, bases, namespace) creates a class
print(User(id=1, email="a@b.com"))                   # User(id=1, email='a@b.com')
print(type(User), type(type))                        # <class 'type'> <class 'type'>
```
The object model's two key relationships:
```text
instance-of:  obj ──► MyClass ──► type ──► type   (type is an instance of itself)
subclass-of:  MyClass ──► object ;  type ──► object
```

### 4. Metaclasses
**What:** a metaclass is **the class of a class** — it controls how classes are created and behave. The default metaclass is `type`.

**What happens when Python executes a `class` statement:**
```text
class Order(Base, metaclass=Meta, flag=True):  BODY
 1. determine the metaclass (explicit, or most-derived metaclass of the bases)
 2. ns = Meta.__prepare__("Order", (Base,), flag=True)        → namespace mapping (default: dict)
 3. execute BODY inside ns                                     → methods, attributes collected
 4. cls = Meta("Order", (Base,), ns, flag=True)
       → Meta.__new__(Meta, ...)  → type.__new__ builds the class object, which:
            a. calls __set_name__ on every attribute that defines it (descriptors)
            b. calls parent's __init_subclass__(flag=True)
       → Meta.__init__(cls, ...)
 5. apply class decorators (bottom-up)
 6. bind the name Order
```
```python
class Meta(type):
    @classmethod
    def __prepare__(mcls, name, bases, **kw):
        print(f"1 __prepare__ {name}")
        return {}
    def __new__(mcls, name, bases, ns, **kw):
        print(f"3 Meta.__new__ {name}")
        return super().__new__(mcls, name, bases, ns)
    def __init__(cls, name, bases, ns, **kw):
        print(f"6 Meta.__init__ {name}")
        super().__init__(name, bases, ns)

class Field:
    def __set_name__(self, owner, name): print(f"4 __set_name__ {name}")

class Base(metaclass=Meta):
    def __init_subclass__(cls, **kw): print(f"5 __init_subclass__ {cls.__name__}")

def deco(cls):
    print(f"7 decorator {cls.__name__}")
    return cls

print("--- defining Order ---")
@deco
class Order(Base):
    print("2 executing class body")
    total = Field()
```
```text
1 __prepare__ Base
3 Meta.__new__ Base
6 Meta.__init__ Base
--- defining Order ---
1 __prepare__ Order
2 executing class body
3 Meta.__new__ Order
4 __set_name__ total
5 __init_subclass__ Order
6 Meta.__init__ Order
7 decorator Order
```
**Practical metaclass: enforce an interface at class-definition time**
```python
class RequireHandle(type):
    def __new__(mcls, name, bases, ns):
        cls = super().__new__(mcls, name, bases, ns)
        if bases and "handle" not in ns:
            raise TypeError(f"{name} must define handle()")
        return cls

class Handler(metaclass=RequireHandle): pass
try:
    class BadHandler(Handler): pass
except TypeError as e:
    print(e)                # BadHandler must define handle()
```
**Metaclass `__call__`** controls *instantiation* (see [M8](#m8-object-creation--lifecycle)) — e.g., a singleton metaclass that caches one instance per class.

**When NOT to use metaclasses:** almost always. Prefer, in order: plain code → class decorators → `__init_subclass__` → `__set_name__` descriptors → metaclass. Metaclasses also conflict when combining classes from different frameworks (metaclass conflict errors). Real users: Django ORM (`ModelBase`), SQLAlchemy declarative base, `ABCMeta`, `EnumMeta`.

### 5. Dataclasses
```python
from dataclasses import dataclass, field, asdict, replace

@dataclass(order=True, slots=True)               # slots=True (3.10+)
class Employee:
    sort_index: float = field(init=False, repr=False)
    name: str
    salary: float = 0.0
    skills: list[str] = field(default_factory=list)   # ✅ never a bare [] default

    def __post_init__(self):                     # runs after the generated __init__
        if self.salary < 0:
            raise ValueError("salary must be >= 0")
        self.sort_index = self.salary            # order=True compares fields in order → by salary first

a = Employee("Parth", 90000, ["python"])
b = Employee("Asha", 120000)
print(a)                     # Employee(name='Parth', salary=90000, skills=['python'])
print(a < b, a == Employee("Parth", 90000, ["python"]))   # True True
print(asdict(b))             # {'sort_index': 120000, 'name': 'Asha', 'salary': 120000, 'skills': []}
print(replace(a, salary=95000).salary)   # 95000  ← copy with changes

@dataclass(frozen=True)
class Money:
    amount: int
    currency: str = "INR"
m = Money(100)
print(hash(m) == hash(Money(100)))       # True  ← frozen → hashable
try:
    m.amount = 5
except Exception as e:
    print(type(e).__name__)              # FrozenInstanceError
```
Generated: `__init__`, `__repr__`, `__eq__`; optionally ordering (`order=True`), hashing (`frozen`/`unsafe_hash`), `__slots__` (`slots=True`), `__match_args__`. Options: `kw_only=True`, `field(compare=False)`, `InitVar`. A bare mutable default (`skills: list = []`) raises `ValueError` at class definition.

### 6. `NamedTuple` and `Enum`
```python
from typing import NamedTuple
from enum import Enum, auto

class Point(NamedTuple):           # immutable, tuple-compatible, lightweight
    x: int
    y: int = 0
    def dist(self): return (self.x ** 2 + self.y ** 2) ** 0.5
p = Point(3, 4)
x, y = p                           # unpacks like a tuple
print(p, p.dist(), p._replace(y=0))   # Point(x=3, y=4) 5.0 Point(x=3, y=0)

class OrderStatus(Enum):
    PENDING = auto()
    PAID = auto()
    SHIPPED = auto()
    def can_cancel(self): return self in (OrderStatus.PENDING, OrderStatus.PAID)

s = OrderStatus.PAID
print(s, s.name, s.value, s.can_cancel())       # OrderStatus.PAID PAID 2 True
print(OrderStatus["SHIPPED"] is OrderStatus(3)) # True  ← members are singletons; compare with `is`
print([m.name for m in OrderStatus])            # ['PENDING', 'PAID', 'SHIPPED']
```
`StrEnum` (3.11) members are also `str` — handy for JSON/DB values. `IntEnum`, `Flag` for bitflags.

### 7. `__slots__`
```python
class PointSlots:
    __slots__ = ("x", "y")          # fixed attribute set; no per-instance __dict__
    def __init__(self, x, y): self.x, self.y = x, y

p = PointSlots(1, 2)
try:
    p.z = 3
except AttributeError:
    print("AttributeError: no __dict__, can't add z")
print(hasattr(p, "__dict__"))      # False
print(type(PointSlots.__dict__["x"]).__name__)   # member_descriptor  ← slots are DATA descriptors
```
- **Benefits:** less memory per instance (no dict — often 40–60% smaller), slightly faster attribute access, prevents typos creating new attributes.
- **Costs/caveats:** no dynamic attributes; no `__weakref__` unless listed; a slot can't have a class-level default of the same name (`ValueError: 'x' in __slots__ conflicts with class variable`); subclasses without `__slots__` get a `__dict__` again; multiple inheritance with non-empty slots in several bases fails.
- Use for: high-volume objects (events, rows, graph nodes). `@dataclass(slots=True)` is the easy way.

### 8. Generics, `Self`, and typing
```python
from typing import Generic, TypeVar, Self

T = TypeVar("T")

class Repository(Generic[T]):                   # classic syntax
    def __init__(self): self._items: dict[int, T] = {}
    def add(self, id: int, item: T) -> None: self._items[id] = item
    def get(self, id: int) -> T | None: return self._items.get(id)

class Stack[T]:                                 # PEP 695 syntax (Python 3.12+)
    def __init__(self) -> None: self._data: list[T] = []
    def push(self, item: T) -> None: self._data.append(item)
    def pop(self) -> T: return self._data.pop()

class QueryBuilder:
    def __init__(self): self.parts: list[str] = []
    def where(self, cond: str) -> Self:          # Self (3.11): subclasses keep their own type in chains
        self.parts.append(cond)
        return self

users: Repository[dict] = Repository()
users.add(1, {"name": "Parth"})
print(users.get(1), QueryBuilder().where("a=1").where("b=2").parts)
```
**Runtime vs static typing:** Python never enforces these hints at runtime — `Repository[int]().add(1, "str")` runs fine. Type checkers (mypy/pyright) catch it before deployment. Runtime validation needs explicit code or libraries (Pydantic, attrs validators).

### 🎤 Interview-ready answer: "What is a metaclass? When would you use one?"
> "Classes are objects, and a metaclass is the class that creates them — `type` by default. When Python executes a `class` statement it calls the metaclass's `__prepare__` to get a namespace, runs the class body in it, then calls the metaclass with the name, bases, and namespace; `type.__new__` builds the class, calling `__set_name__` on descriptors and the parent's `__init_subclass__`, then decorators run. Metaclasses let frameworks like Django's ORM or `ABCMeta` customise class creation. In application code I almost never need one: `__init_subclass__` covers registration and validation of subclasses, class decorators cover post-processing, and descriptors cover per-attribute behaviour."

### 📝 Revision notes
```
DI = pass dependencies in (constructor) → swap fakes in tests ; composition + delegation
type(name, bases, ns) creates classes ; type is its own metaclass
class stmt: metaclass → __prepare__ → body → Meta.__new__ (type.__new__: __set_name__, __init_subclass__) → Meta.__init__ → decorators
prefer decorators/__init_subclass__ over metaclasses
dataclass: field(default_factory=list), __post_init__, frozen → hashable, order, slots
NamedTuple immutable tuple ; Enum singletons (compare with is)
__slots__: no __dict__, less memory, no dynamic attrs, slots are data descriptors
generics & Self are static-only hints
```

---

# PART VI — DESIGN

## M18. SOLID Principles in Python

> SOLID principles exist to keep code **easy to change**. Each one targets a specific kind of pain: classes that change for too many reasons, features that require editing old code, subclasses that break callers, fat interfaces, and high-level code glued to low-level details.

### S — Single Responsibility Principle
**Definition:** A class should have **one reason to change** (one actor/stakeholder it serves).

**Why:** When one class handles business rules, persistence, formatting, and email, a change to the email template risks breaking billing.

```python
# ❌ BAD: four reasons to change (pricing rules, DB schema, PDF format, email provider)
class InvoiceService:
    def calculate_total(self, items): ...
    def save_to_db(self, invoice): ...
    def render_pdf(self, invoice): ...
    def email_customer(self, invoice): ...

# ✅ GOOD: each class has one job; a coordinator composes them
class InvoiceCalculator:
    def total(self, items): return sum(i["qty"] * i["price"] for i in items)
class InvoiceRepository:
    def save(self, invoice): ...
class InvoicePdfRenderer:
    def render(self, invoice) -> bytes: ...
class InvoiceMailer:
    def send(self, invoice, pdf: bytes): ...

class InvoiceService:                      # orchestration only
    def __init__(self, calc, repo, renderer, mailer):
        self.calc, self.repo, self.renderer, self.mailer = calc, repo, renderer, mailer
    def issue(self, invoice):
        invoice["total"] = self.calc.total(invoice["items"])
        self.repo.save(invoice)
        self.mailer.send(invoice, self.renderer.render(invoice))
```
**Backend example:** Django "fat models" vs services; FastAPI route handlers that contain SQL + validation + email → split into router / service / repository.
**Common violations:** "Manager"/"Utils" god classes; route handlers with business logic.
**Trade-off:** too much splitting → many tiny classes and indirection. Split along **reasons to change**, not lines of code.

### O — Open/Closed Principle
**Definition:** Software entities should be **open for extension, closed for modification** — add new behaviour by adding code, not editing tested code.

```python
# ❌ BAD: every new provider means editing this function
def pay(provider, amount):
    if provider == "stripe": ...
    elif provider == "razorpay": ...
    elif provider == "paypal": ...      # edit, retest, redeploy

# ✅ GOOD: polymorphism + registry — new provider = new class only
from abc import ABC, abstractmethod

class PaymentProvider(ABC):
    registry: dict[str, type["PaymentProvider"]] = {}
    def __init_subclass__(cls, key, **kw):
        super().__init_subclass__(**kw)
        PaymentProvider.registry[key] = cls
    @abstractmethod
    def charge(self, amount: int) -> str: ...

class Stripe(PaymentProvider, key="stripe"):
    def charge(self, amount): return f"stripe charged {amount}"
class Razorpay(PaymentProvider, key="razorpay"):
    def charge(self, amount): return f"razorpay charged {amount}"

def pay(provider: str, amount: int):
    return PaymentProvider.registry[provider]().charge(amount)
print(pay("razorpay", 500))      # razorpay charged 500
```
**Trade-off:** don't build extension points speculatively (YAGNI) — apply OCP where variation actually happens.

### L — Liskov Substitution Principle
**Definition:** Objects of a subclass must be usable **anywhere** the base class is expected, without breaking correctness. Subclasses must not **strengthen preconditions**, **weaken postconditions**, or break **invariants**.

```python
# ❌ BAD: classic Rectangle/Square
class Rectangle:
    def __init__(self, w, h): self.w, self.h = w, h
    def set_width(self, w): self.w = w
    def area(self): return self.w * self.h

class Square(Rectangle):
    def __init__(self, s): super().__init__(s, s)
    def set_width(self, w): self.w = self.h = w      # changes height too!

def stretch(r: Rectangle):
    r.set_width(5)
    assert r.area() == 5 * r.h                     # holds for Rectangle...
    return r.area()

print(stretch(Rectangle(2, 3)))   # 15
print(stretch(Square(3)))         # 25 — "works", but a caller expecting width-only change is surprised
```
Other violations: a `ReadOnlyRepository(Repository)` whose `save()` raises `NotImplementedError`; a subclass that accepts fewer input types or returns `None` where the base returns a value.

```python
# ✅ GOOD: model what's actually common; don't force an is-a that isn't true
class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...
class Rect(Shape):
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h
class Sq(Shape):
    def __init__(self, s): self.s = s
    def area(self): return self.s ** 2
```
**Backend example:** a `CachedUserRepo` that returns stale data where callers need fresh reads; a payment provider subclass that silently doesn't support refunds.

### I — Interface Segregation Principle
**Definition:** Clients shouldn't be forced to depend on methods they don't use. Prefer **small, focused interfaces**.
```python
from typing import Protocol

# ❌ BAD: fat interface — a read-only report service must "implement" delete
class Storage(ABC):
    @abstractmethod
    def read(self, key): ...
    @abstractmethod
    def write(self, key, data): ...
    @abstractmethod
    def delete(self, key): ...
    @abstractmethod
    def list_versions(self, key): ...

# ✅ GOOD: role interfaces; each client asks only for what it needs
class Reader(Protocol):
    def read(self, key: str) -> bytes: ...
class Writer(Protocol):
    def write(self, key: str, data: bytes) -> None: ...

class S3Storage:                          # implements both structurally
    def read(self, key): return b"..."
    def write(self, key, data): ...

def build_report(src: Reader): return src.read("report.csv")   # depends on Reader only
```
In Python, Protocols make ISP cheap: the *client* defines the narrow interface it needs.

### D — Dependency Inversion Principle
**Definition:** High-level modules shouldn't depend on low-level modules; **both depend on abstractions**. Abstractions shouldn't depend on details.
```python
# ❌ BAD: business logic hard-wired to a concrete SMTP client (untestable, unswappable)
class SignupService:
    def __init__(self):
        self.mailer = SmtpMailer("smtp.gmail.com")      # concrete dependency created inside
    def signup(self, email): ...; self.mailer.send(email, "Welcome!")

# ✅ GOOD: depend on an abstraction; inject the concrete implementation
class Mailer(Protocol):
    def send(self, to: str, body: str) -> None: ...

class SignupService:
    def __init__(self, mailer: Mailer):
        self.mailer = mailer
    def signup(self, email):
        self.mailer.send(email, "Welcome!")

class FakeMailer:
    def __init__(self): self.sent = []
    def send(self, to, body): self.sent.append((to, body))

fake = FakeMailer()
SignupService(fake).signup("p@x.com")
print(fake.sent)        # [('p@x.com', 'Welcome!')]   ← unit test without network
```
**DIP vs DI:** DIP is the *principle* (depend on abstractions); Dependency Injection is a *technique* to achieve it (pass dependencies in).

### Related principles
| Principle | Meaning | Python practice |
|---|---|---|
| **Composition over inheritance** | Build behaviour by combining objects | Inject strategies/collaborators instead of subclassing |
| **High cohesion** | A class's members belong together | Methods use most of the class's state |
| **Loose coupling** | Classes know little about each other | Depend on Protocols; communicate via small interfaces/events |
| **Separation of concerns** | Different concerns in different layers | Router → Service → Repository → DB |
| **DRY / KISS / YAGNI** | Don't repeat; keep simple; don't build what you don't need | Avoid speculative abstractions |
| **Law of Demeter** | Talk to friends, not strangers | Avoid `order.customer.address.city.name` chains |
| **Testability** | Code can be tested in isolation | DI + fakes; pure functions for logic |

### 🎤 Interview-ready answer: "Explain SOLID with examples."
> "SRP: a class should have one reason to change — I separate a pricing calculator from the repository and the mailer instead of one invoice god-class. OCP: add behaviour by adding code — new payment providers are new subclasses registered via `__init_subclass__`, not new `elif` branches. LSP: subclasses must be substitutable — `Square` extending a mutable `Rectangle` breaks callers, so I model them as siblings under `Shape`. ISP: keep interfaces small — in Python I define narrow Protocols like `Reader` and `Writer` from the client's perspective. DIP: high-level business logic depends on abstractions, and concrete implementations are injected — which is what makes services unit-testable with fakes."

### 📝 Revision notes
```
S: one reason to change (split by actor) ; O: extend via new classes/registry, not if/elif
L: subclass usable wherever base is (no stronger preconditions, weaker results, broken invariants)
I: small role interfaces (Protocols defined by clients) ; D: depend on abstractions, inject concretes
composition > inheritance ; high cohesion, loose coupling ; don't over-engineer (YAGNI)
```

---

## M19. Design Patterns in Python

> Patterns are **named solutions to recurring design problems**. In Python, several classic (Java/C++) patterns shrink dramatically because functions are first-class, classes are objects, and modules are singletons. Interviewers love asking: *"How would this pattern look in Python specifically?"*

### Quick map
| Category | Pattern | One-line purpose | Python shortcut |
|---|---|---|---|
| Creational | Singleton | One shared instance | A module-level instance |
| | Factory Method | Let subclasses/registry decide which class to create | Dict of classes / `@classmethod` |
| | Abstract Factory | Create families of related objects | A class or dict of factories |
| | Builder | Construct complex objects step by step | kwargs/dataclass for simple cases; fluent builder for complex |
| | Prototype | Create by cloning | `copy.deepcopy` |
| Structural | Adapter | Make an incompatible interface fit | Wrapper class / `__getattr__` |
| | Decorator | Add behaviour by wrapping, same interface | Wrapper objects; `@decorators` for functions |
| | Facade | Simple front for a complex subsystem | A service class/module |
| | Proxy | Control access to an object | `__getattr__` delegation |
| | Composite | Treat trees and leaves uniformly | Recursive classes with a shared method |
| | Bridge | Vary abstraction and implementation independently | Composition + injection |
| | Flyweight | Share common state across many objects | `functools.cache` factory, `__slots__` |
| Behavioral | Strategy | Swap algorithms at runtime | Pass a function |
| | Observer | Notify subscribers of events | List of callables / signals |
| | State | Behaviour changes with internal state | State classes or a transition table |
| | Command | Request as an object (queue, undo) | Callables / `functools.partial` |
| | Template Method | Fixed algorithm skeleton, customisable steps | ABC with hook methods |
| | Chain of Responsibility | Pass a request along handlers | Middleware lists |
| | Iterator | Sequential access without exposing internals | `__iter__` + generators |
| | Mediator | Centralise communication between objects | Event bus / coordinator |
| | Memento | Snapshot and restore state | `copy.deepcopy` / dataclass snapshots |
| | Visitor | Add operations to a class hierarchy without changing it | `functools.singledispatch` |

---

### Creational patterns

#### 1. Singleton
**Problem:** exactly one instance should exist (config, connection pool, logger registry).
```text
┌────────────────────────┐
│ Singleton              │
│ - _instance (class)    │
│ + get_instance()/()    │──► always returns the same object
└────────────────────────┘
```
```python
import threading

# ✅ Most Pythonic: modules are imported once → a module-level instance IS a singleton
# settings.py:   settings = Settings()      everywhere:  from settings import settings

# Metaclass version (thread-safe, no __init__ re-run problem)
class SingletonMeta(type):
    _instances: dict = {}
    _lock = threading.Lock()
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:                              # double-checked locking
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class ConnectionPool(metaclass=SingletonMeta):
    def __init__(self, size=10):
        print("pool created")
        self.size = size

p1, p2 = ConnectionPool(5), ConnectionPool(20)
print(p1 is p2, p1.size)        # pool created / True 5   ← __init__ ran once
```
**Bad implementation:** the `__new__`-only singleton that re-runs `__init__` ([M8](#m8-object-creation--lifecycle)).
**When not to use:** most of the time — singletons are global state, hide dependencies, and make tests interfere with each other. Prefer creating one instance at startup and **injecting** it.
**Interview Q:** "Make it thread-safe" → lock + double check. "Why is it considered an anti-pattern?" → hidden global state, testability.

#### 2. Factory Method
**Problem:** client code shouldn't know which concrete class to instantiate.
```text
Client ──► NotifierFactory.create(kind) ──► EmailNotifier | SMSNotifier | PushNotifier
```
```python
class EmailNotifier:
    def send(self, to, msg): return f"email→{to}: {msg}"
class SMSNotifier:
    def send(self, to, msg): return f"sms→{to}: {msg}"

class NotifierFactory:
    _creators = {"email": EmailNotifier, "sms": SMSNotifier}
    @classmethod
    def register(cls, kind, creator): cls._creators[kind] = creator    # open for extension
    @classmethod
    def create(cls, kind):
        try:
            return cls._creators[kind]()
        except KeyError:
            raise ValueError(f"unknown notifier {kind!r}") from None

print(NotifierFactory.create("sms").send("+91", "OTP 1234"))   # sms→+91: OTP 1234
```
**Classic GoF form:** an abstract `Creator` with `create_product()` overridden by subclasses — use when the creator also has shared logic around creation.
**Bad:** `if kind == "email": ... elif ...` scattered across the codebase.
**Backend:** creating payment/storage/notification clients from config.

#### 3. Abstract Factory
**Problem:** create **families** of related objects that must be used together (all-AWS or all-GCP).
```text
CloudFactory (abstract) ── create_storage(), create_queue()
   ├── AWSFactory  ──► S3Storage,  SQSQueue
   └── GCPFactory  ──► GCSStorage, PubSubQueue
```
```python
class AWSFactory:
    def create_storage(self): return "S3Storage"
    def create_queue(self): return "SQSQueue"
class GCPFactory:
    def create_storage(self): return "GCSStorage"
    def create_queue(self): return "PubSubQueue"

def build_infra(factory):            # client never mixes families accidentally
    return factory.create_storage(), factory.create_queue()
print(build_infra(GCPFactory()))     # ('GCSStorage', 'PubSubQueue')
```
**When not:** only one product type → a simple factory is enough.

#### 4. Builder
**Problem:** constructing an object needs many optional parts/steps; a constructor with 12 parameters is unreadable.
```python
class SQLQuery:
    def __init__(self, table, fields, conditions, order, limit):
        self.table, self.fields, self.conditions, self.order, self.limit = table, fields, conditions, order, limit
    def __str__(self):
        sql = f"SELECT {', '.join(self.fields)} FROM {self.table}"
        if self.conditions: sql += " WHERE " + " AND ".join(self.conditions)
        if self.order: sql += f" ORDER BY {self.order}"
        if self.limit is not None: sql += f" LIMIT {self.limit}"
        return sql

class QueryBuilder:
    def __init__(self, table):
        self._table, self._fields, self._conds, self._order, self._limit = table, ["*"], [], None, None
    def select(self, *fields): self._fields = list(fields); return self      # fluent: return self
    def where(self, cond): self._conds.append(cond); return self
    def order_by(self, col): self._order = col; return self
    def limit(self, n): self._limit = n; return self
    def build(self):
        if self._limit is not None and self._limit <= 0:
            raise ValueError("limit must be positive")                      # validate before building
        return SQLQuery(self._table, self._fields, self._conds, self._order, self._limit)

q = QueryBuilder("users").select("id", "email").where("active = true").order_by("id").limit(10).build()
print(q)   # SELECT id, email FROM users WHERE active = true ORDER BY id LIMIT 10
```
**Python note:** for simple cases, keyword arguments with defaults or a dataclass replace Builder. Use Builder when construction is **multi-step, validated, or produces different representations** (SQLAlchemy queries, HTTP request builders).

#### 5. Prototype
**Problem:** creating an object from scratch is expensive or complex; cloning a configured template is easier.
```python
import copy
class ReportTemplate:
    def __init__(self, title, sections, styles):
        self.title, self.sections, self.styles = title, sections, styles
    def clone(self, **changes):
        new = copy.deepcopy(self)          # deep: don't share the sections list
        new.__dict__.update(changes)
        return new

base = ReportTemplate("Monthly", ["summary", "charts"], {"font": "Inter"})
q3 = base.clone(title="Q3 Report")
q3.sections.append("appendix")
print(base.sections, q3.title)     # ['summary', 'charts'] Q3 Report
```

---

### Structural patterns

#### 6. Adapter
**Problem:** you have code expecting interface `A`, and a class (often third-party/legacy) providing interface `B`.
```text
Client ──► PaymentProvider.charge(amount_paise)
                    ▲
            LegacyGatewayAdapter ──wraps──► LegacyGateway.make_payment(rupees, currency)
```
```python
class LegacyGateway:                                    # can't modify (third-party)
    def make_payment(self, rupees: float, currency: str): return f"paid {rupees} {currency}"

class LegacyGatewayAdapter:                             # exposes OUR interface
    def __init__(self, legacy: LegacyGateway): self._legacy = legacy
    def charge(self, amount_paise: int) -> str:
        return self._legacy.make_payment(amount_paise / 100, "INR")   # translate call + units

print(LegacyGatewayAdapter(LegacyGateway()).charge(49900))   # paid 499.0 INR
```
**Backend:** wrapping vendor SDKs (SMS, payments, storage) behind your own interface — so switching vendors touches one adapter.

#### 7. Decorator (the GoF pattern)
**Problem:** add responsibilities to an object dynamically, without subclass explosion. The wrapper has the **same interface** as the wrapped object.
```text
Notifier ◄── EmailNotifier
   ▲
   └── NotifierDecorator(wrapped: Notifier) ◄── RetryDecorator, LoggingDecorator
```
```python
class Email:
    def send(self, to, msg): return f"email {to}: {msg}"

class LoggingNotifier:
    def __init__(self, inner): self.inner = inner
    def send(self, to, msg):
        print(f"[log] sending to {to}")
        return self.inner.send(to, msg)

class RetryNotifier:
    def __init__(self, inner, attempts=3): self.inner, self.attempts = inner, attempts
    def send(self, to, msg):
        for i in range(self.attempts):
            try:
                return self.inner.send(to, msg)
            except ConnectionError:
                if i == self.attempts - 1: raise

notifier = LoggingNotifier(RetryNotifier(Email()))     # compose behaviours at runtime
print(notifier.send("a@b.com", "hi"))
```
**Pattern vs Python `@decorator`:** Python's `@` syntax wraps **functions/classes at definition time**; the GoF pattern wraps **objects at runtime**. Same idea — wrapping — different targets.

#### 8. Facade
**Problem:** clients need a simple entry point to a complex subsystem.
```python
class Inventory:
    def reserve(self, sku, qty): return True
class Payments:
    def charge(self, user, amount): return "txn_1"
class Shipping:
    def schedule(self, order_id): return "ship_9"

class CheckoutFacade:                       # one simple method hides three subsystems
    def __init__(self, inv, pay, ship): self.inv, self.pay, self.ship = inv, pay, ship
    def place_order(self, user, sku, qty, amount):
        if not self.inv.reserve(sku, qty):
            raise RuntimeError("out of stock")
        txn = self.pay.charge(user, amount)
        return {"txn": txn, "shipment": self.ship.schedule(txn)}

print(CheckoutFacade(Inventory(), Payments(), Shipping()).place_order("u1", "SKU1", 1, 999))
```
**Backend:** service-layer classes; SDK clients (`boto3.client("s3")` is a facade over HTTP signing, retries, serialization).

#### 9. Proxy
**Problem:** control access to an object — lazy creation, caching, access control, rate limiting, remote access — with the **same interface**.
```python
class ExpensiveReportService:
    def generate(self, month):
        print(f"generating {month}...")
        return f"report-{month}"

class CachingProxy:
    def __init__(self, target): self._target, self._cache = target, {}
    def generate(self, month):
        if month not in self._cache:
            self._cache[month] = self._target.generate(month)
        return self._cache[month]
    def __getattr__(self, name):            # forward everything else untouched
        return getattr(self._target, name)

svc = CachingProxy(ExpensiveReportService())
svc.generate("2026-10"); svc.generate("2026-10")   # "generating..." printed once
```
**Proxy vs Decorator:** same structure; **intent** differs — Proxy *controls access* to the subject (often managing its lifecycle), Decorator *adds behaviour*. **Backend:** ORM lazy-loaded relations, auth-checking wrappers, cached clients.

#### 10. Composite
**Problem:** treat individual objects and groups of objects **uniformly** (trees).
```python
class File:
    def __init__(self, name, size): self.name, self.size_bytes = name, size
    def size(self): return self.size_bytes

class Folder:
    def __init__(self, name): self.name, self.children = name, []
    def add(self, node): self.children.append(node); return self
    def size(self): return sum(child.size() for child in self.children)   # recursion, uniform call

root = Folder("root").add(File("a.txt", 100)).add(Folder("img").add(File("b.png", 400)))
print(root.size())     # 500
```
**Backend:** permission groups containing users and groups; nested menu/category trees; org charts.

#### 11. Bridge
**Problem:** two dimensions vary independently (message *type* × delivery *channel*) — inheritance would need every combination (`UrgentEmail`, `UrgentSMS`, `DigestEmail`, …).
```python
class EmailChannel:
    def deliver(self, text): return f"EMAIL: {text}"
class SMSChannel:
    def deliver(self, text): return f"SMS: {text}"

class Message:                                   # abstraction holds a reference to an implementation
    def __init__(self, channel): self.channel = channel
class UrgentAlert(Message):
    def send(self, text): return self.channel.deliver(f"🚨 URGENT: {text}")
class Digest(Message):
    def send(self, items): return self.channel.deliver("Digest: " + ", ".join(items))

print(UrgentAlert(SMSChannel()).send("DB down"))           # SMS: 🚨 URGENT: DB down
print(Digest(EmailChannel()).send(["a", "b"]))             # EMAIL: Digest: a, b
```
2 abstractions + 2 channels = 4 classes instead of 4 combination classes (and it scales as m + n, not m × n).

#### 12. Flyweight
**Problem:** millions of objects share most of their data; store the shared (**intrinsic**) part once.
```python
from functools import cache

class CurrencyInfo:                       # intrinsic, shared, immutable
    __slots__ = ("code", "symbol", "decimals")
    def __init__(self, code, symbol, decimals): self.code, self.symbol, self.decimals = code, symbol, decimals

@cache
def currency(code):                       # flyweight factory
    table = {"INR": ("₹", 2), "JPY": ("¥", 0)}
    return CurrencyInfo(code, *table[code])

class Txn:                                # extrinsic state (amount) per object
    __slots__ = ("amount", "cur")
    def __init__(self, amount, code): self.amount, self.cur = amount, currency(code)

t1, t2 = Txn(100, "INR"), Txn(200, "INR")
print(t1.cur is t2.cur)                   # True — one shared CurrencyInfo
```
Python itself uses flyweights: small-int caching, string interning.

---

### Behavioral patterns

#### 13. Strategy
**Problem:** choose an algorithm at runtime without `if/elif` chains.
```python
# ❌ BAD
def price(amount, customer_type):
    if customer_type == "regular": return amount
    elif customer_type == "premium": return amount * 0.9
    elif customer_type == "festival": return amount * 0.8 if amount > 1000 else amount

# ✅ GOOD (class-based strategies)
from typing import Protocol
class PricingStrategy(Protocol):
    def apply(self, amount: float) -> float: ...

class Regular:
    def apply(self, amount): return amount
class Premium:
    def __init__(self, pct=10): self.pct = pct
    def apply(self, amount): return amount * (1 - self.pct / 100)
class Festival:
    def apply(self, amount): return amount * 0.8 if amount > 1000 else amount

class Checkout:
    def __init__(self, strategy: PricingStrategy): self.strategy = strategy
    def total(self, amount): return round(self.strategy.apply(amount), 2)

print(Checkout(Premium(15)).total(2000), Checkout(Festival()).total(2000))   # 1700.0 1600.0

# ✅ Pythonic: strategies can just be functions
def bulk_discount(amount): return amount - 100 if amount > 5000 else amount
class CheckoutFn:
    def __init__(self, strategy=lambda a: a): self.strategy = strategy
    def total(self, amount): return self.strategy(amount)
print(CheckoutFn(bulk_discount).total(6000))     # 5900
```
**SOLID:** OCP (new strategy = new class), SRP, DIP. **Backend:** pricing, retry/backoff policies, auth methods, serialisation formats, sorting/ranking.

#### 14. Observer (Pub/Sub)
**Problem:** when something happens, many independent parts must react — without the publisher knowing them.
```text
EventBus ── subscribe(event, handler) ; publish(event, payload) ──► handler1, handler2, ...
```
```python
from collections import defaultdict

class EventBus:
    def __init__(self): self._subs = defaultdict(list)
    def subscribe(self, event, handler): self._subs[event].append(handler)
    def unsubscribe(self, event, handler): self._subs[event].remove(handler)
    def publish(self, event, **payload):
        for handler in list(self._subs[event]):        # copy: handlers may unsubscribe during iteration
            handler(**payload)

bus = EventBus()
bus.subscribe("order_placed", lambda order_id, **_: print(f"email receipt for {order_id}"))
bus.subscribe("order_placed", lambda order_id, amount, **_: print(f"analytics: {order_id} ₹{amount}"))
bus.publish("order_placed", order_id=42, amount=999)
```
⚠️ Observers held by strong references stay alive forever → memory leaks; use `weakref.WeakMethod`/`WeakSet` for object observers. Handlers that raise can block others — wrap each in try/except in production.
**Backend:** Django signals, domain events, webhooks, Kafka/RabbitMQ (distributed observer).

#### 15. State
**Problem:** an object's behaviour depends on its state, and transitions have rules — avoid giant `if self.status == ...` blocks.
```python
class OrderState:
    def pay(self, order): raise ValueError(f"cannot pay in {type(self).__name__}")
    def ship(self, order): raise ValueError(f"cannot ship in {type(self).__name__}")
    def cancel(self, order): raise ValueError(f"cannot cancel in {type(self).__name__}")

class Pending(OrderState):
    def pay(self, order): order.state = Paid()
    def cancel(self, order): order.state = Cancelled()
class Paid(OrderState):
    def ship(self, order): order.state = Shipped()
    def cancel(self, order): order.state = Cancelled()   # + refund
class Shipped(OrderState): pass
class Cancelled(OrderState): pass

class Order:
    def __init__(self): self.state = Pending()
    def pay(self): self.state.pay(self)
    def ship(self): self.state.ship(self)
    def cancel(self): self.state.cancel(self)

o = Order(); o.pay(); o.ship()
print(type(o.state).__name__)       # Shipped
try:
    o.cancel()
except ValueError as e:
    print(e)                        # cannot cancel in Shipped
```
**Simpler alternative:** an `Enum` + transition table `{(PENDING, "pay"): PAID, ...}` when states don't carry different behaviour.

#### 16. Command
**Problem:** encapsulate a request as an object so it can be queued, logged, retried, or undone.
```python
class AddItem:
    def __init__(self, cart, item): self.cart, self.item = cart, item
    def execute(self): self.cart.append(self.item)
    def undo(self): self.cart.remove(self.item)

class History:
    def __init__(self): self._done = []
    def run(self, cmd): cmd.execute(); self._done.append(cmd)
    def undo(self):
        if self._done: self._done.pop().undo()

cart, h = [], History()
h.run(AddItem(cart, "book")); h.run(AddItem(cart, "pen"))
h.undo()
print(cart)              # ['book']
```
**Backend:** task queues (Celery tasks are serialised commands), job scheduling, audit logs, CQRS commands, migration steps with rollback.

#### 17. Template Method
**Problem:** several workflows share the same **skeleton**, differing in a few steps.
```python
from abc import ABC, abstractmethod

class DataExporter(ABC):
    def export(self):                       # the TEMPLATE — fixed order, not meant to be overridden
        rows = self.fetch()
        rows = [self.transform(r) for r in rows]
        return self.write(rows)
    @abstractmethod
    def fetch(self): ...
    def transform(self, row): return row    # HOOK with default behaviour
    @abstractmethod
    def write(self, rows): ...

class CSVUserExporter(DataExporter):
    def fetch(self): return [{"id": 1, "name": "parth"}]
    def transform(self, row): return {**row, "name": row["name"].title()}
    def write(self, rows): return "\n".join(f"{r['id']},{r['name']}" for r in rows)

print(CSVUserExporter().export())           # 1,Parth
```
**Template Method (inheritance) vs Strategy (composition):** Template fixes the skeleton in a base class; Strategy injects a whole interchangeable algorithm. **Backend:** Django class-based views (`get_queryset`, `get_context_data` hooks), ETL jobs, test fixtures (`setUp`/`tearDown`).

#### 18. Chain of Responsibility
**Problem:** a request passes through a sequence of handlers; each may handle it, modify it, or stop the chain.
```python
class Handler:
    def __init__(self, nxt=None): self.next = nxt
    def handle(self, req):
        return self.next.handle(req) if self.next else {"status": 200, "body": "OK"}

class Auth(Handler):
    def handle(self, req):
        if not req.get("token"): return {"status": 401}
        return super().handle(req)
class RateLimit(Handler):
    def handle(self, req):
        if req.get("calls", 0) > 100: return {"status": 429}
        return super().handle(req)
class Validate(Handler):
    def handle(self, req):
        if "body" not in req: return {"status": 422}
        return super().handle(req)

pipeline = Auth(RateLimit(Validate()))
print(pipeline.handle({"token": "t", "body": {}}), pipeline.handle({"body": {}}))
# {'status': 200, 'body': 'OK'} {'status': 401}
```
**Backend:** web framework middleware (Django/Starlette), logging handler chains, approval workflows.

#### 19. Iterator
**Problem:** traverse a collection without exposing its internals. In Python this is the **iteration protocol** ([M15](#m15-iterators-generators--context-managers)).
```python
class PaginatedAPI:
    def __init__(self, pages): self._pages = pages          # pretend each page is an HTTP call
    def __iter__(self):
        for page in self._pages:                           # fetch lazily, page by page
            yield from page

print(list(PaginatedAPI([[1, 2], [3], [4, 5]])))           # [1, 2, 3, 4, 5]
```

#### 20. Mediator
**Problem:** many objects talk to each other directly → a web of dependencies. Route communication through one mediator.
```python
class ChatRoom:                                 # mediator
    def __init__(self): self.users = {}
    def join(self, user): self.users[user.name] = user; user.room = self
    def send(self, sender, to, msg):
        if to in self.users: self.users[to].receive(sender, msg)

class User:
    def __init__(self, name): self.name, self.room, self.inbox = name, None, []
    def send(self, to, msg): self.room.send(self.name, to, msg)   # knows only the mediator
    def receive(self, sender, msg): self.inbox.append(f"{sender}: {msg}")

room = ChatRoom(); a, b = User("a"), User("b")
room.join(a); room.join(b)
a.send("b", "hi")
print(b.inbox)          # ['a: hi']
```
**Mediator vs Observer:** Observer broadcasts to whoever subscribed; Mediator contains coordination **logic** between known participants. **Backend:** workflow orchestrators (saga coordinators), message brokers.

#### 21. Memento
**Problem:** save and restore an object's state (undo, checkpoints) without exposing its internals.
```python
import copy

class Editor:
    def __init__(self): self.text, self.cursor = "", 0
    def type(self, s): self.text += s; self.cursor = len(self.text)
    def save(self): return copy.deepcopy(vars(self))          # memento (opaque snapshot)
    def restore(self, memento): self.__dict__.update(copy.deepcopy(memento))

ed = Editor(); ed.type("Hello")
snap = ed.save()
ed.type(" world")
ed.restore(snap)
print(ed.text, ed.cursor)       # Hello 5
```
**Backend:** draft versions, config rollback, game/workflow checkpoints, optimistic UI undo.

#### 22. Visitor
**Problem:** add new operations over a stable class hierarchy (e.g., AST nodes, shapes) without editing every class.
```python
from functools import singledispatch

class Num:
    def __init__(self, v): self.v = v
class Add:
    def __init__(self, l, r): self.l, self.r = l, r
class Mul:
    def __init__(self, l, r): self.l, self.r = l, r

@singledispatch                                # Pythonic visitor: dispatch on node type
def evaluate(node): raise TypeError(type(node))
@evaluate.register
def _(node: Num): return node.v
@evaluate.register
def _(node: Add): return evaluate(node.l) + evaluate(node.r)
@evaluate.register
def _(node: Mul): return evaluate(node.l) * evaluate(node.r)

@singledispatch
def show(node): raise TypeError(type(node))    # a NEW operation — no node class edited
@show.register
def _(node: Num): return str(node.v)
@show.register
def _(node: Add): return f"({show(node.l)} + {show(node.r)})"
@show.register
def _(node: Mul): return f"{show(node.l)} * {show(node.r)}"

expr = Mul(Add(Num(2), Num(3)), Num(4))
print(show(expr), "=", evaluate(expr))         # (2 + 3) * 4 = 20
```
Classic GoF uses `node.accept(visitor)` → `visitor.visit_Add(node)` (double dispatch); Python's `ast.NodeVisitor` uses `visit_<ClassName>` methods. **Trade-off:** easy to add operations, hard to add new node types (every visitor must handle them).

---

### Pattern interview questions
| Question | Strong answer points |
|---|---|
| Strategy vs State? | Strategy: client picks an algorithm; State: object changes its own behaviour as its state transitions |
| Decorator vs Proxy vs Adapter? | Same wrapping structure; Decorator adds behaviour (same interface), Proxy controls access (same interface), Adapter **changes** the interface |
| Factory vs Builder? | Factory chooses **which** class; Builder controls **how** a complex object is assembled step by step |
| Template Method vs Strategy? | Inheritance + fixed skeleton vs composition + swappable algorithm |
| Why is Singleton controversial? | Global mutable state, hidden dependencies, test coupling; prefer DI of one instance |
| Which patterns are "built into" Python? | Iterator (protocol), Decorator (`@`), Strategy/Command (first-class functions), Singleton (modules), Prototype (`copy`), Flyweight (interning), Observer (signals libraries) |

### 📝 Revision notes
```
Creational: Singleton(module/metaclass) Factory(registry) AbstractFactory(families) Builder(fluent, validate) Prototype(deepcopy)
Structural: Adapter(change iface) Decorator(add behaviour) Facade(simplify) Proxy(control access) Composite(tree uniform) Bridge(m+n not m×n) Flyweight(share intrinsic)
Behavioral: Strategy(swap algo) Observer(pub/sub) State(behaviour by state) Command(request object, undo/queue) Template(skeleton+hooks) Chain(middleware) Iterator(__iter__) Mediator(central coordinator) Memento(snapshot) Visitor(singledispatch)
```

---

## M20. Real-World Backend Examples

> Each example: **Requirements → Design (diagram + responsibilities) → Implementation → Principles & patterns → Testing → Interview follow-ups.** All code runs as-is (standard library only).

### Example 1: Employee Management
**Requirements:** different employee types compute pay differently; payroll must handle all types uniformly; adding a type shouldn't change payroll.
```text
        Employee (ABC)  ── name, emp_id ; monthly_pay() [abstract] ; __repr__
         ▲        ▲          ▲
   FullTime   Contractor   Intern
Payroll ──uses──► list[Employee]
```
```python
from abc import ABC, abstractmethod
from itertools import count

class Employee(ABC):
    _ids = count(1)                                     # class-level id generator
    def __init__(self, name):
        self.name, self.emp_id = name, next(Employee._ids)
    @abstractmethod
    def monthly_pay(self) -> float: ...
    def __repr__(self): return f"{type(self).__name__}(id={self.emp_id}, name={self.name!r})"

class FullTime(Employee):
    def __init__(self, name, annual_salary):
        super().__init__(name); self.annual_salary = annual_salary
    def monthly_pay(self): return round(self.annual_salary / 12, 2)

class Contractor(Employee):
    def __init__(self, name, hourly_rate, hours):
        super().__init__(name); self.hourly_rate, self.hours = hourly_rate, hours
    def monthly_pay(self): return self.hourly_rate * self.hours

class Intern(Employee):
    def __init__(self, name, stipend):
        super().__init__(name); self.stipend = stipend
    def monthly_pay(self): return self.stipend

class Payroll:
    def __init__(self, employees: list[Employee]): self.employees = employees
    def run(self):
        return {e.emp_id: e.monthly_pay() for e in self.employees}    # polymorphic call
    def total(self): return sum(self.run().values())

staff = [FullTime("Parth", 1_200_000), Contractor("Ravi", 800, 120), Intern("Neha", 25_000)]
print(Payroll(staff).run(), Payroll(staff).total())
# {1: 100000.0, 2: 96000, 3: 25000} 221000.0
```
**Principles:** abstraction (ABC), inheritance, polymorphism, OCP (new type = new subclass).
**Testing:** each `monthly_pay` in isolation; Payroll with a `FakeEmployee`.
**Follow-ups:** "Pay rules change per country?" → inject a `PayPolicy` strategy instead of more subclasses. "Employee can be both mentor and full-time?" → composition of roles, not multiple inheritance.

### Example 2 & 18: Payment System with Multiple Payment Providers
**Requirements:** support Stripe/Razorpay/UPI; choose provider by config or user; handle failures uniformly; add providers without touching checkout.
```text
CheckoutService ──► PaymentGateway (Protocol: charge, refund)
                        ▲          ▲            ▲
                  StripeGateway  RazorpayGateway  UPIAdapter ──wraps──► LegacyUPISDK
PaymentGatewayFactory.create(name) → PaymentGateway
```
```python
from dataclasses import dataclass
from typing import Protocol
import uuid

class PaymentError(Exception): pass

@dataclass(frozen=True)
class PaymentResult:
    provider: str
    txn_id: str
    amount_paise: int

class PaymentGateway(Protocol):
    name: str
    def charge(self, amount_paise: int, token: str) -> PaymentResult: ...
    def refund(self, txn_id: str) -> bool: ...

class StripeGateway:
    name = "stripe"
    def charge(self, amount_paise, token):
        if token == "declined": raise PaymentError("card declined")
        return PaymentResult(self.name, f"st_{uuid.uuid4().hex[:8]}", amount_paise)
    def refund(self, txn_id): return True

class RazorpayGateway:
    name = "razorpay"
    def charge(self, amount_paise, token):
        return PaymentResult(self.name, f"rzp_{uuid.uuid4().hex[:8]}", amount_paise)
    def refund(self, txn_id): return True

class LegacyUPISDK:                                       # third-party, different interface
    def pay(self, vpa, rupees): return {"ref": "upi_123", "ok": True}

class UPIAdapter:                                         # Adapter → our PaymentGateway interface
    name = "upi"
    def __init__(self, sdk: LegacyUPISDK): self._sdk = sdk
    def charge(self, amount_paise, token):
        resp = self._sdk.pay(token, amount_paise / 100)
        if not resp["ok"]: raise PaymentError("UPI failed")
        return PaymentResult(self.name, resp["ref"], amount_paise)
    def refund(self, txn_id): return False                # documented: refunds manual for UPI

class PaymentGatewayFactory:
    _registry = {"stripe": StripeGateway, "razorpay": RazorpayGateway,
                 "upi": lambda: UPIAdapter(LegacyUPISDK())}
    @classmethod
    def create(cls, name: str) -> PaymentGateway:
        if name not in cls._registry: raise ValueError(f"unsupported provider {name}")
        return cls._registry[name]()

class CheckoutService:
    def __init__(self, gateway: PaymentGateway): self.gateway = gateway   # DI
    def pay(self, amount_paise, token):
        if amount_paise <= 0: raise ValueError("invalid amount")
        try:
            return self.gateway.charge(amount_paise, token)
        except PaymentError as e:
            return f"payment failed via {self.gateway.name}: {e}"

print(CheckoutService(PaymentGatewayFactory.create("upi")).pay(49900, "parth@upi"))
print(CheckoutService(PaymentGatewayFactory.create("stripe")).pay(49900, "declined"))
```
**Patterns:** Strategy (gateway), Factory, Adapter, DI. **Principles:** OCP, DIP, LSP (note the UPI refund limitation — an LSP smell worth calling out in interviews; better: split `Refundable` into its own Protocol → ISP).
**Testing:** inject a `FakeGateway` that records calls / raises `PaymentError`.
**Follow-ups:** idempotency keys for retries; webhooks for async confirmation; storing amounts as integer paise (never floats); fallback provider on failure (chain of gateways).

### Example 3 & 17: Notification System with Multiple Providers
**Requirements:** notify via email/SMS/push; user preferences decide channels; failures retried; adding a channel is easy.
```text
NotificationService ── channels: dict[str, Channel] ── retry: RetryPolicy
Channel (Protocol: send(to, msg)) ◄── EmailChannel, SMSChannel, PushChannel
```
```python
from typing import Protocol

class Channel(Protocol):
    def send(self, to: str, msg: str) -> None: ...

class EmailChannel:
    def __init__(self): self.outbox = []
    def send(self, to, msg): self.outbox.append(("email", to, msg))

class SMSChannel:
    def __init__(self, fail_times=0): self.outbox, self._fail = [], fail_times
    def send(self, to, msg):
        if self._fail:                                  # simulate a flaky provider
            self._fail -= 1
            raise ConnectionError("sms gateway timeout")
        self.outbox.append(("sms", to, msg))

class RetryPolicy:
    def __init__(self, attempts=3): self.attempts = attempts
    def run(self, fn):
        for i in range(1, self.attempts + 1):
            try:
                return fn()
            except ConnectionError:
                if i == self.attempts: raise

class NotificationService:
    def __init__(self, channels: dict[str, Channel], retry: RetryPolicy):
        self.channels, self.retry = channels, retry
    def notify(self, user: dict, msg: str):
        results = {}
        for ch_name in user["prefs"]:
            ch = self.channels[ch_name]
            try:
                self.retry.run(lambda: ch.send(user[ch_name], msg))
                results[ch_name] = "sent"
            except ConnectionError:
                results[ch_name] = "failed"          # one channel failing doesn't stop others
        return results

sms = SMSChannel(fail_times=2)
svc = NotificationService({"email": EmailChannel(), "sms": sms}, RetryPolicy(3))
user = {"email": "p@x.com", "sms": "+9199", "prefs": ["email", "sms"]}
print(svc.notify(user, "Your order shipped"), sms.outbox)
# {'email': 'sent', 'sms': 'sent'} [('sms', '+9199', 'Your order shipped')]
```
**Patterns:** Strategy (channels), Bridge (message × channel), Observer (trigger from domain events), retry as composable policy.
**Follow-ups:** move sending to a queue (Celery/SQS) for latency; templates per channel; rate limits per provider; dead-letter queue for permanent failures.

### Example 4: Logger
**Requirements:** structured logs, multiple outputs, one configuration shared app-wide.
```python
import json, sys, time

class Handler:
    def emit(self, record: dict): raise NotImplementedError
class StdoutJSONHandler(Handler):
    def emit(self, record): print(json.dumps(record), file=sys.stdout)
class MemoryHandler(Handler):
    def __init__(self): self.records = []
    def emit(self, record): self.records.append(record)

class Logger:
    LEVELS = {"DEBUG": 10, "INFO": 20, "ERROR": 40}
    def __init__(self, name, level="INFO", handlers=None):
        self.name, self.level, self.handlers = name, self.LEVELS[level], handlers or []
    def log(self, level, msg, **ctx):
        if self.LEVELS[level] < self.level: return
        record = {"ts": round(time.time()), "logger": self.name, "level": level, "msg": msg, **ctx}
        for h in self.handlers: h.emit(record)                # chain of outputs
    def info(self, msg, **ctx): self.log("INFO", msg, **ctx)
    def error(self, msg, **ctx): self.log("ERROR", msg, **ctx)

mem = MemoryHandler()
log = Logger("orders", handlers=[mem])                        # module-level instance = app-wide "singleton"
log.info("order placed", order_id=42); log.log("DEBUG", "ignored")
print([r["msg"] for r in mem.records])                        # ['order placed']
```
**Real life:** use the standard `logging` module — it *is* this design (Logger hierarchy, Handlers, Formatters, Filters; `logging.getLogger(name)` returns a per-name singleton).
**Follow-ups:** why log with `%s` args instead of f-strings (lazy formatting); correlation/request IDs via `contextvars`.

### Example 5: Database Connection (context manager + pool)
```python
import sqlite3
from contextlib import contextmanager

class ConnectionPool:
    def __init__(self, dsn, size=2):
        self._dsn, self._free = dsn, [sqlite3.connect(dsn) for _ in range(size)]
    @contextmanager
    def connection(self):
        if not self._free: raise RuntimeError("pool exhausted")
        conn = self._free.pop()
        try:
            yield conn
            conn.commit()                       # success → commit
        except Exception:
            conn.rollback()                     # failure → rollback, then re-raise
            raise
        finally:
            self._free.append(conn)             # ALWAYS return to pool

pool = ConnectionPool(":memory:", size=1)
with pool.connection() as c:
    c.execute("CREATE TABLE t (x INT)"); c.execute("INSERT INTO t VALUES (1)")
with pool.connection() as c:
    print(c.execute("SELECT count(*) FROM t").fetchone())   # (1,)
```
**Principles:** encapsulation of connection lifecycle; deterministic cleanup via `with` (not `__del__`).
**Follow-ups:** thread safety (`queue.Queue` for the free list), max wait/timeout, health checks, async pools (`async with pool.acquire()`).

### Example 6: Repository Pattern
**Requirements:** business logic shouldn't know whether data lives in Postgres, SQLite, or memory.
```python
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class User:
    id: int | None
    email: str
    active: bool = True

class UserRepository(ABC):
    @abstractmethod
    def add(self, user: User) -> User: ...
    @abstractmethod
    def get(self, user_id: int) -> User | None: ...
    @abstractmethod
    def find_by_email(self, email: str) -> User | None: ...

class InMemoryUserRepository(UserRepository):          # for tests
    def __init__(self): self._rows, self._next = {}, 1
    def add(self, user):
        user.id, self._next = self._next, self._next + 1
        self._rows[user.id] = user
        return user
    def get(self, user_id): return self._rows.get(user_id)
    def find_by_email(self, email):
        return next((u for u in self._rows.values() if u.email == email), None)

class SQLiteUserRepository(UserRepository):            # for production-like runs
    def __init__(self, conn):
        self.conn = conn
        conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, email TEXT UNIQUE, active INT)")
    def add(self, user):
        cur = self.conn.execute("INSERT INTO users (email, active) VALUES (?, ?)", (user.email, int(user.active)))
        user.id = cur.lastrowid
        return user
    def _row(self, row): return User(row[0], row[1], bool(row[2])) if row else None
    def get(self, user_id):
        return self._row(self.conn.execute("SELECT id, email, active FROM users WHERE id = ?", (user_id,)).fetchone())
    def find_by_email(self, email):
        return self._row(self.conn.execute("SELECT id, email, active FROM users WHERE email = ?", (email,)).fetchone())
```
**Principles:** DIP, LSP (both repos must behave identically — test them with the **same** test suite), SRP (persistence only).

### Example 7: Service Layer
```python
class EmailAlreadyRegistered(Exception): pass

class UserService:
    def __init__(self, repo: UserRepository, mailer):
        self.repo, self.mailer = repo, mailer
    def register(self, email: str) -> User:
        email = email.strip().lower()
        if "@" not in email: raise ValueError("invalid email")
        if self.repo.find_by_email(email):
            raise EmailAlreadyRegistered(email)
        user = self.repo.add(User(None, email))
        self.mailer.send(email, "Welcome!")
        return user

class FakeMailer:
    def __init__(self): self.sent = []
    def send(self, to, body): self.sent.append(to)

import sqlite3
svc = UserService(SQLiteUserRepository(sqlite3.connect(":memory:")), FakeMailer())
print(svc.register(" Parth@X.com "))        # User(id=1, email='parth@x.com', active=True)
try:
    svc.register("parth@x.com")
except EmailAlreadyRegistered as e:
    print("duplicate:", e)                   # duplicate: parth@x.com
```
Layering: **router/controller** (HTTP, parsing) → **service** (business rules, transactions) → **repository** (persistence). Routers stay thin; services are framework-agnostic and unit-testable.

### Example 8: Authentication System
```python
import hashlib, hmac, os, secrets, time

class PasswordHasher:
    ITER = 200_000
    def hash(self, password: str) -> str:
        salt = os.urandom(16)
        dk = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, self.ITER)
        return f"{salt.hex()}${dk.hex()}"
    def verify(self, password: str, stored: str) -> bool:
        salt_hex, dk_hex = stored.split("$")
        dk = hashlib.pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(salt_hex), self.ITER)
        return hmac.compare_digest(dk.hex(), dk_hex)     # constant-time comparison

class TokenStore:
    def __init__(self, ttl=3600): self._tokens, self.ttl = {}, ttl
    def issue(self, user_id):
        token = secrets.token_urlsafe(32)
        self._tokens[token] = (user_id, time.time() + self.ttl)
        return token
    def resolve(self, token):
        user_id, exp = self._tokens.get(token, (None, 0))
        return user_id if time.time() < exp else None

class AuthService:
    def __init__(self, hasher, tokens, users: dict):
        self.hasher, self.tokens, self.users = hasher, tokens, users   # users: email → (id, hash)
    def login(self, email, password):
        record = self.users.get(email)
        if not record or not self.hasher.verify(password, record[1]):
            raise PermissionError("invalid credentials")      # same message: don't leak which part failed
        return self.tokens.issue(record[0])

h = PasswordHasher()
auth = AuthService(h, TokenStore(), {"p@x.com": (1, h.hash("s3cret!"))})
token = auth.login("p@x.com", "s3cret!")
print(auth.tokens.resolve(token))     # 1
```
**Patterns:** Strategy (swap hasher: bcrypt/argon2; swap token store: Redis/JWT), Facade (`AuthService`). **Follow-ups:** rate limiting login attempts, JWT vs opaque tokens, refresh tokens, never logging passwords (`__repr__`!).

### Example 9 & 16: File Storage with an Abstract Storage Interface
```python
from abc import ABC, abstractmethod
from pathlib import Path
import tempfile

class Storage(ABC):
    @abstractmethod
    def save(self, key: str, data: bytes) -> str: ...
    @abstractmethod
    def load(self, key: str) -> bytes: ...
    @abstractmethod
    def exists(self, key: str) -> bool: ...

class LocalStorage(Storage):
    def __init__(self, root): self.root = Path(root)
    def _path(self, key):
        p = (self.root / key).resolve()
        if self.root.resolve() not in p.parents: raise ValueError("path traversal blocked")
        return p
    def save(self, key, data):
        p = self._path(key); p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(data)
        return f"file://{p}"
    def load(self, key): return self._path(key).read_bytes()
    def exists(self, key): return self._path(key).exists()

class InMemoryStorage(Storage):
    def __init__(self): self._d = {}
    def save(self, key, data): self._d[key] = data; return f"mem://{key}"
    def load(self, key): return self._d[key]
    def exists(self, key): return key in self._d

# class S3Storage(Storage): wraps boto3 put_object/get_object — same interface

class AvatarService:
    def __init__(self, storage: Storage): self.storage = storage
    def upload(self, user_id, data: bytes):
        if len(data) > 1_000_000: raise ValueError("too large")
        return self.storage.save(f"avatars/{user_id}.png", data)

for backend in (InMemoryStorage(), LocalStorage(tempfile.mkdtemp())):
    svc = AvatarService(backend)
    svc.upload(7, b"\x89PNG...")
    print(type(backend).__name__, backend.exists("avatars/7.png"))
```
**Follow-ups:** streaming large files (iterators/chunks), presigned URLs, content-type detection, storage selection per environment via factory.

### Example 10: API Client
```python
import json
from urllib import request, error

class APIError(Exception):
    def __init__(self, status, body): super().__init__(f"HTTP {status}"); self.status, self.body = status, body

class GitHubClient:                                     # Facade over HTTP details
    BASE = "https://api.github.com"
    def __init__(self, token: str | None = None, timeout=10, transport=None):
        self._token, self._timeout = token, timeout
        self._transport = transport or self._urllib_transport     # injectable for tests
    def __repr__(self): return f"GitHubClient(token={'***' if self._token else None})"   # never leak secrets
    def _urllib_transport(self, method, url, headers):
        req = request.Request(url, method=method, headers=headers)
        try:
            with request.urlopen(req, timeout=self._timeout) as resp:
                return resp.status, json.loads(resp.read())
        except error.HTTPError as e:
            return e.code, e.read().decode()
    def _get(self, path):
        headers = {"Accept": "application/vnd.github+json"}
        if self._token: headers["Authorization"] = f"Bearer {self._token}"
        status, body = self._transport("GET", f"{self.BASE}{path}", headers)
        if status >= 400: raise APIError(status, body)
        return body
    def user(self, username): return self._get(f"/users/{username}")

fake = lambda method, url, headers: (200, {"login": url.rsplit("/", 1)[-1]})
print(GitHubClient("tok", transport=fake).user("octocat"), GitHubClient("tok"))
# {'login': 'octocat'} GitHubClient(token=***)
```
**Follow-ups:** retries with backoff (Example 12), connection reuse (`requests.Session`/`httpx.Client` as context manager), pagination via generators, rate-limit headers.

### Example 11: Cache (LRU + TTL)
```python
import time
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int, ttl: float | None = None):
        self.capacity, self.ttl, self._data = capacity, ttl, OrderedDict()   # key → (value, expires_at)
    def get(self, key, default=None):
        item = self._data.get(key)
        if item is None: return default
        value, exp = item
        if exp is not None and time.monotonic() > exp:
            del self._data[key]; return default
        self._data.move_to_end(key)                  # mark as most recently used
        return value
    def set(self, key, value):
        exp = time.monotonic() + self.ttl if self.ttl else None
        self._data[key] = (value, exp)
        self._data.move_to_end(key)
        if len(self._data) > self.capacity:
            self._data.popitem(last=False)           # evict least recently used
    def __len__(self): return len(self._data)
    def __contains__(self, key): return self.get(key) is not None

c = LRUCache(2)
c.set("a", 1); c.set("b", 2); c.get("a"); c.set("c", 3)
print("a" in c, "b" in c, len(c))     # True False 2
```
For functions: `functools.lru_cache(maxsize=...)` / `functools.cache`. In production: Redis with TTL; Cache-aside pattern in services ([M17 DI example](#m17-advanced-python-oop)).

### Example 12: Retry Mechanism
```python
import functools, random, time

class RetryPolicy:
    def __init__(self, attempts=3, base_delay=0.1, max_delay=2.0, retry_on=(ConnectionError, TimeoutError)):
        self.attempts, self.base, self.max, self.retry_on = attempts, base_delay, max_delay, retry_on
    def delay(self, attempt):                         # exponential backoff + full jitter
        return random.uniform(0, min(self.max, self.base * 2 ** (attempt - 1)))
    def __call__(self, func):                         # usable as a decorator
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, self.attempts + 1):
                try:
                    return func(*args, **kwargs)
                except self.retry_on:
                    if attempt == self.attempts: raise
                    time.sleep(self.delay(attempt))
        return wrapper

attempts = {"n": 0}
@RetryPolicy(attempts=4, base_delay=0.001)
def fetch():
    attempts["n"] += 1
    if attempts["n"] < 3: raise TimeoutError
    return "data"
print(fetch(), attempts["n"])         # data 3
```
**Follow-ups:** only retry **idempotent** operations (or use idempotency keys); jitter avoids thundering herds; circuit breaker after repeated failures; libraries: `tenacity`.

### Example 13: Strategy-Based Pricing
```python
from typing import Protocol

class PricingRule(Protocol):
    def apply(self, subtotal: float, ctx: dict) -> float: ...

class CouponRule:
    def __init__(self, coupons): self.coupons = coupons
    def apply(self, subtotal, ctx):
        return subtotal * (1 - self.coupons.get(ctx.get("coupon"), 0))
class MemberRule:
    def apply(self, subtotal, ctx): return subtotal * 0.95 if ctx.get("member") else subtotal
class MinimumPriceRule:
    def __init__(self, floor): self.floor = floor
    def apply(self, subtotal, ctx): return max(subtotal, self.floor)

class PricingEngine:                                  # rules run in order (a pipeline of strategies)
    def __init__(self, rules: list[PricingRule]): self.rules = rules
    def price(self, subtotal, **ctx):
        for rule in self.rules:
            subtotal = rule.apply(subtotal, ctx)
        return round(subtotal, 2)

engine = PricingEngine([CouponRule({"DIWALI10": 0.10}), MemberRule(), MinimumPriceRule(99)])
print(engine.price(1000, coupon="DIWALI10", member=True), engine.price(80))   # 855.0 99
```
**Principles:** OCP (new rule = new class), SRP per rule; rules can be loaded from config/DB.

### Example 14: Factory-Based Service Creation
```python
class Settings:
    def __init__(self, env="test", storage="memory", payment="razorpay"):
        self.env, self.storage, self.payment = env, storage, payment

class ServiceFactory:
    """Builds fully-wired services from configuration (one place knows concrete classes)."""
    def __init__(self, settings: Settings): self.s = settings
    def storage(self) -> Storage:
        return {"memory": InMemoryStorage, "local": lambda: LocalStorage("/tmp/app")}[self.s.storage]()
    def payment_gateway(self):
        return PaymentGatewayFactory.create(self.s.payment)
    def avatar_service(self): return AvatarService(self.storage())
    def checkout_service(self): return CheckoutService(self.payment_gateway())

f = ServiceFactory(Settings(storage="memory", payment="stripe"))
print(type(f.avatar_service().storage).__name__, f.checkout_service().gateway.name)   # InMemoryStorage stripe
```

### Example 15: Dependency Injection (Composition Root)
**Idea:** construct the object graph **once**, at the application's entry point (the *composition root*); everything else just receives dependencies.
```python
class Container:
    """A tiny DI container: registers providers, caches singletons."""
    def __init__(self): self._providers, self._singletons = {}, {}
    def register(self, name, provider, singleton=False):
        self._providers[name] = (provider, singleton)
    def resolve(self, name):
        provider, singleton = self._providers[name]
        if singleton:
            if name not in self._singletons:
                self._singletons[name] = provider(self)
            return self._singletons[name]
        return provider(self)

c = Container()
c.register("repo", lambda c: InMemoryUserRepository(), singleton=True)
c.register("mailer", lambda c: FakeMailer(), singleton=True)
c.register("user_service", lambda c: UserService(c.resolve("repo"), c.resolve("mailer")))

svc = c.resolve("user_service")
svc.register("asha@x.com")
print(c.resolve("repo").find_by_email("asha@x.com").id, c.resolve("mailer").sent)   # 1 ['asha@x.com']
```
In FastAPI, the same idea is `Depends(get_user_service)`; in tests you override providers with fakes (`app.dependency_overrides`).
**Interview follow-ups:** "Constructor vs setter vs framework injection?" — prefer constructor injection (explicit, immutable). "Isn't a container overkill?" — for small apps, a hand-written composition root (a `main()` that wires objects) is enough.

---

# PART VII — INTERVIEW

## M21. Interview Question Bank

> Format: **Question** · level · concept → expected answer (with the key detail interviewers listen for) → follow-up → 🎤 a spoken answer for the most-asked ones. Detailed explanations live in the linked modules.

### 🟢 Beginner

**B1. What is OOP? What are its benefits?** · *M1*
- **Answer:** Organising code around objects that bundle state and behaviour. Benefits: modelling domains naturally, encapsulating invariants, reuse via composition/inheritance, extensibility via polymorphism.
- **Follow-up:** "When would you *not* use OOP?" → small scripts, pure data transformations, where functions are simpler.

**B2. What's a class vs an object?** · *M1*
- **Answer:** A class is a blueprint (and in Python, itself an object of type `type`); an object is an instance created by calling the class.
- **Follow-up:** "What's `type(MyClass)`?" → `type` (the metaclass).

**B3. What is `self`?** · *M1* — 🎤 see [M1](#m1-oop-fundamentals). Key detail: `obj.m(x)` ≡ `type(obj).m(obj, x)` via bound methods; `self` is a convention, not a keyword.

**B4. What is `__init__`? Is it a constructor?** · *M8*
- **Answer:** It's the **initialiser** — it sets up an instance that `__new__` already created. The constructor role in Python is split: `__new__` creates, `__init__` initialises. `__init__` must return `None`.

**B5. Class attributes vs instance attributes?** · *M1* — Key detail: reads check instance then class; writes via an instance always create instance attributes; mutable class attributes are shared.

**B6. What are the four pillars of OOP?** · *M4–M7*
- **Answer:** Encapsulation (protect state/invariants), Abstraction (hide complexity behind interfaces), Inheritance (is-a reuse/specialisation), Polymorphism (one interface, many implementations).
- 🎤 "Encapsulation keeps state and the rules guarding it together — in Python via conventions, name mangling, and properties. Abstraction exposes what an object does but not how — ABCs or Protocols. Inheritance lets a subclass reuse and specialise a base, with lookup following the MRO. Polymorphism lets the same call behave differently per type — through overriding, duck typing, or operator dunders."

**B7. Does Python support private variables?** · *M4* — No enforced privacy. `_x` convention; `__x` name-mangled to `_Class__x` to avoid subclass clashes.

**B8. What's the difference between a method and a function?** · *M1/M10* — A method is a function stored on a class; accessed via an instance it becomes a bound method with `self` pre-filled.

### 🟡 Intermediate

**I1. `__new__` vs `__init__`?** · *M8* — 🎤 see [M8](#m8-object-creation--lifecycle). Must mention: `__new__` gets `cls`, returns the instance, implicitly static; `__init__` gets `self`, returns `None`, called only if `__new__` returns an instance of `cls`; immutable subclasses need `__new__`.
- **Follow-up:** "Implement a singleton; what's the bug with `__new__`-only?" → `__init__` re-runs.

**I2. `__str__` vs `__repr__`?** · *M13* — Must mention fallback direction (str → repr only) and containers using repr.

**I3. Instance vs class vs static methods?** · *M2* — Must mention: classmethods are subclass-aware (`cls`), used for alternative constructors; all three are descriptors.

**I4. Method overriding vs overloading in Python?** · *M7*
- **Answer:** Overriding = subclass redefines a base method (supported, dynamic dispatch). Overloading by signature isn't supported — later `def` rebinds the name. Alternatives: defaults, `*args/**kwargs`, `singledispatch`, classmethod constructors.

**I5. What does `super()` do?** · *M9* — "Next class after the current one in `type(self).__mro__`" — not "the parent".
- **Follow-up:** "What's printed in this diamond?" → see [M22](#m22-output-prediction).

**I6. What is MRO? How is it computed?** · *M9* — C3 linearization: child first, local base order preserved, each class once, parents after all children; `Cls.__mro__`.

**I7. How does Python handle the diamond problem?** · *M9* — C3 gives a single linear order where the shared base comes after both branches; cooperative `super()` calls run each class once.

**I8. Encapsulation in Python — how, given no private keyword?** · *M4* — Conventions, name mangling, properties for controlled access, `__slots__`/frozen dataclasses for immutability.

**I9. Abstraction — ABC vs Protocol vs duck typing?** · *M5* — Nominal & enforced at instantiation vs structural & static vs implicit at call time.

**I10. Composition vs inheritance — which and why?** · *M6* — Default to composition for flexibility/testability; inheritance for true is-a, stable hierarchies, framework hooks.
- 🎤 "Inheritance couples a subclass to its parent's implementation and fixes behaviour at class-definition time; composition assembles behaviour from injected collaborators that I can swap at runtime and fake in tests. I use inheritance for genuine is-a relationships and framework extension points like Django models, and composition for everything that varies — strategies, storage backends, notification channels — which also avoids combinatorial subclass explosions."

**I11. What is duck typing?** · *M5/M7* — Behaviour over type: any object with the needed methods works; EAFP style.

**I12. How does `@property` work?** · *M11* — Data descriptor; `fget`/`fset`/`fdel`; setter returns a new property (same name); beats instance dict.

**I13. What is an abstract class? Can it have concrete methods / a constructor?** · *M5* — Yes to both; instantiation fails while any `@abstractmethod` remains unimplemented (`__abstractmethods__`).

**I14. What are dataclasses? What do they generate?** · *M17* — `__init__`, `__repr__`, `__eq__` (+ order, hash, slots options); `default_factory`; `__post_init__`; plain `@dataclass` instances are unhashable.

**I15. What's a mixin?** · *M9* — Small class adding one capability via multiple inheritance, not meant to stand alone; placed left of the main base; uses cooperative `super()`.

**I16. `is` vs `==`?** · *M14* — Identity vs `__eq__`; use `is` only for singletons like `None`.

**I17. Why can't a list be a dict key? Can a tuple?** · *M14* — Lists are mutable → unhashable; tuples are hashable only if all elements are hashable.

**I18. What happens if you define `__eq__` but not `__hash__`?** · *M14* — `__hash__` becomes `None` → unhashable; keeps the hash contract.

**I19. Shallow vs deep copy?** · *M14* — Shallow copies the container, shares the elements; deep copies recursively with a memo for cycles.

**I20. What's the difference between an iterable and an iterator?** · *M15* — `__iter__` → iterator vs `__next__` + `__iter__` returning self; iterators are single-use.

### 🔴 Advanced

**A1. Walk through what happens when a class is instantiated.** · *M8* — `type(Cls).__call__` → `Cls.__new__(Cls, ...)` → if `isinstance(obj, Cls)`: `type(obj).__init__(obj, ...)` → return. Edge cases: non-instance skips init; cached instance re-inits; metaclass `__call__` can override everything.

**A2. What happens when Python executes a `class` statement?** · *M17* — Metaclass resolution → `__prepare__` → body executed into namespace → `Meta(name, bases, ns)` → `type.__new__` (→ `__set_name__`, `__init_subclass__`) → `Meta.__init__` → decorators → name bound.

**A3. Explain the attribute lookup order.** · *M10* — Data descriptor (from type MRO) > instance `__dict__` > non-data descriptor > class attribute > `__getattr__`.
- **Follow-up:** "Why can an instance attribute shadow a method but not a property?" → functions are non-data descriptors; property is a data descriptor.

**A4. `__getattribute__` vs `__getattr__`?** · *M10* — Every access vs only on `AttributeError`; recursion risk; delegation use case; dunders bypass both.

**A5. What is the descriptor protocol? Data vs non-data?** · *M10* — `__get__/__set__/__delete__`; `__set__` or `__delete__` ⇒ data descriptor ⇒ priority over instance dict.
- 🎤 see [M10](#m10-attribute-lookup--descriptors).

**A6. How are bound methods created?** · *M10* — Functions implement `__get__`; `func.__get__(obj, type(obj))` returns a bound method object with `__self__` and `__func__`.

**A7. What's a metaclass? When have you needed one?** · *M17* — 🎤 see [M17](#m17-advanced-python-oop). Strong answer: "rarely — `__init_subclass__` and class decorators cover most needs".

**A8. `__init_subclass__` and `__set_name__` — what are they for?** · *M12-N/M10* — Subclass registration/validation without metaclasses; descriptors learning their attribute names at class creation.

**A9. What does `__slots__` do and what are its trade-offs?** · *M17* — No per-instance `__dict__`; slot descriptors; memory/speed win; no dynamic attrs, no class-level defaults of the same name, inheritance caveats.

**A10. How does garbage collection work? Should you use `__del__`?** · *M8* — Refcounting + generational cyclic GC; `__del__` timing unreliable, exceptions ignored; prefer context managers / `weakref.finalize`.

**A11. What is object resurrection?** · *M8* — `__del__` storing `self` somewhere reachable; since PEP 442 the finaliser runs at most once.

**A12. How does cooperative multiple inheritance work with different `__init__` signatures?** · *M9* — Keyword args; each class consumes its own and forwards `**kwargs`; root class stops before `object`.

**A13. Explain how `a + b` is resolved.** · *M12-G* — Subclass-reflected priority → `a.__add__(b)` → `NotImplemented` → `b.__radd__(a)` → `TypeError`. `+=` tries `__iadd__` then falls back to `__add__` + rebinding.

**A14. Why does `t = ([1],); t[0] += [2]` raise but still modify the list?** · *M12-I* — `+=` = `t[0] = t[0].__iadd__([2])`: the list mutates in place, then the item assignment on the tuple fails.

**A15. How would you build a custom container that works with `len`, indexing, slicing, `in`, `for`, and `reversed`?** · *M12-J* — Implement the dunders, or inherit `collections.abc.Sequence` and implement `__getitem__` + `__len__`.

**A16. How does a `with` statement work? When is the exception suppressed?** · *M15* — `__enter__` result bound to `as`; `__exit__(type, value, tb)`; truthy return suppresses.

**A17. How do you make a class usable as a dict key safely?** · *M14* — Immutable fields (frozen dataclass/read-only properties), `__eq__` + `__hash__` over the same tuple of fields.

**A18. How do `property`, `classmethod`, and `staticmethod` differ as descriptors?** · *M10* — Data descriptor calling fget/fset; non-data binding to the owner class; non-data returning the raw function.

**A19. Why does `len(obj)` fail after `obj.__len__ = lambda: 3`?** · *M10 §9* — Implicit special-method lookup goes to `type(obj)`, bypassing the instance.

**A20. Explain SOLID with Python examples; which do you violate most often and why?** · *M18* — Honest answer + trade-offs (YAGNI, avoid premature abstraction).

### 🏗 Design-oriented (LLD-style) questions
| Question | What they're testing | Hint |
|---|---|---|
| Design a parking lot | Entities, relationships, polymorphism (vehicle/spot types), Strategy for fees | `ParkingLot` → `Level` → `Spot`; `FeeStrategy` |
| Design an LRU cache | Encapsulation, data structures | `OrderedDict` or dict + doubly linked list ([M20 Ex 11](#m20-real-world-backend-examples)) |
| Design a rate limiter | `__call__`, strategy (fixed/sliding window/token bucket) | Strategy per algorithm; per-key state |
| Design a notification system | OCP, Strategy/Bridge, retries | [M20 Ex 3](#m20-real-world-backend-examples) |
| Design a payment system | Adapter, Factory, idempotency | [M20 Ex 2](#m20-real-world-backend-examples) |
| Design an elevator / vending machine | State pattern | State classes with allowed transitions |
| Design a logging framework | Chain of handlers, levels, singleton per name | [M20 Ex 4](#m20-real-world-backend-examples) |

---

## M22. Output Prediction

> **Rules:** read the code, write your prediction, *then* open the answer. Every snippet was run on CPython 3.12.

#### Q1. Class vs instance attributes · 🟢 · *shadowing*
```python
class A:
    x = 1
a, b = A(), A()
a.x = 2
A.x = 3
print(a.x, b.x, A.x)
```
<details><summary>Answer</summary>

```text
2 3 3
```
`a.x = 2` creates an instance attribute on `a`; `b` still reads the (changed) class attribute.
</details>

#### Q2. Mutable class attribute · 🟢 · *shared state*
```python
class Cart:
    items = []
    def add(self, i): self.items.append(i)
c1, c2 = Cart(), Cart()
c1.add("x"); c2.add("y")
print(c1.items, Cart.items is c2.items)
```
<details><summary>Answer</summary>

```text
['x', 'y'] True
```
`append` mutates the one class-level list; no instance attribute is ever created.
</details>

#### Q3. `self.count += 1` · 🟡 · *read class, write instance*
```python
class C:
    count = 0
    def __init__(self): self.count += 1
c1 = C(); c2 = C()
print(C.count, c1.count, c2.count)
```
<details><summary>Answer</summary>

```text
0 1 1
```
`self.count += 1` → `self.count = self.count + 1`: reads class `0`, writes an instance attribute `1`.
</details>

#### Q4. Mutable default in `__init__` · 🟡 · *defaults evaluated once*
```python
class Bag:
    def __init__(self, items=[]):
        self.items = items
b1 = Bag(); b2 = Bag()
b1.items.append(1)
print(b2.items, b1.items is b2.items)
```
<details><summary>Answer</summary>

```text
[1] True
```
The default list is created once when `def` runs; both instances share it. Fix: `items=None`.
</details>

#### Q5. `__new__` / `__init__` order · 🟡 · *object creation*
```python
class P:
    def __new__(cls, *args):
        print("new", args)
        return super().__new__(cls)
    def __init__(self, x):
        print("init", x)
p = P(5)
```
<details><summary>Answer</summary>

```text
new (5,)
init 5
```
Both receive the same arguments from `type.__call__`; `__new__` first.
</details>

#### Q6. `__new__` returns another type · 🟡 · *`__init__` skipped*
```python
class Q:
    def __new__(cls):
        print("new")
        return [1, 2]
    def __init__(self):
        print("init")
obj = Q()
print(type(obj).__name__)
```
<details><summary>Answer</summary>

```text
new
list
```
The result isn't an instance of `Q`, so `type.__call__` doesn't call `__init__`.
</details>

#### Q7. Singleton re-initialisation · 🔴 · *`__init__` re-runs*
```python
class S:
    _inst = None
    def __new__(cls, v):
        if cls._inst is None:
            cls._inst = super().__new__(cls)
        return cls._inst
    def __init__(self, v):
        self.v = v
a = S(1); b = S(2)
print(a.v, b.v, a is b)
```
<details><summary>Answer</summary>

```text
2 2 True
```
`__new__` returns the cached instance (an instance of `S`), so `__init__` runs again and overwrites `v`.
</details>

#### Q8. Only `__str__` defined · 🟡 · *containers use repr*
```python
class T:
    def __str__(self): return "T!"
t = T()
print(t, str([t]) == f"[{t!r}]", "T!" in repr([t]))
```
<details><summary>Answer</summary>

```text
T! True False
```
`print(t)` uses `__str__`; the list's representation uses `repr(t)` — the default `<__main__.T object at …>`.
</details>

#### Q9. Only `__repr__` defined · 🟢 · *str falls back to repr*
```python
class R:
    def __repr__(self): return "R()"
print(R(), [R()], f"{R()}", str(R()))
```
<details><summary>Answer</summary>

```text
R() [R()] R() R()
```
</details>

#### Q10. `__eq__` without `__hash__` · 🟡 · *unhashable*
```python
class E:
    def __init__(self, v): self.v = v
    def __eq__(self, o): return self.v == o.v
print(E(1) == E(1), E.__hash__)
try:
    s = {E(1)}
except TypeError as e:
    print("TypeError:", e)
```
<details><summary>Answer</summary>

```text
True None
TypeError: unhashable type: 'E'
```
</details>

#### Q11. Diamond `__init__` with `super()` · 🔴 · *MRO*
```python
class A:
    def __init__(self): print("A"); super().__init__()
class B(A):
    def __init__(self): print("B"); super().__init__()
class C(A):
    def __init__(self): print("C"); super().__init__()
class D(C, B):
    def __init__(self): print("D"); super().__init__()
D()
print([k.__name__ for k in D.__mro__])
```
<details><summary>Answer</summary>

```text
D
C
B
A
['D', 'C', 'B', 'A', 'object']
```
Base order `(C, B)` puts C first; C's `super()` goes to **B** (next in D's MRO), not A.
</details>

#### Q12. Same `super()` call, different targets · 🔴 · *super is MRO-relative*
```python
class A:
    def hi(self): return "A"
class B(A):
    def hi(self): return "B" + super().hi()
class C(A):
    def hi(self): return "C" + super().hi()
class D(B, C):
    pass
print(B().hi(), D().hi())
```
<details><summary>Answer</summary>

```text
BA BCA
```
For a `B` instance, MRO is B→A. For a `D` instance, MRO is D→B→C→A, so B's `super()` reaches C.
</details>

#### Q13. Broken cooperation · 🔴 · *chain stops*
```python
class A:
    def go(self): print("A")
class B(A):
    def go(self): print("B")
class C(A):
    def go(self): print("C"); super().go()
class D(C, B):
    def go(self): print("D"); super().go()
D().go()
```
<details><summary>Answer</summary>

```text
D
C
B
```
MRO D→C→B→A. C's `super()` reaches B, which doesn't call `super()`, so A never runs.
</details>

#### Q14. Inconsistent MRO · 🔴 · *C3 failure*
```python
class X: pass
class Y(X): pass
try:
    class Z(X, Y): pass
except TypeError:
    print("TypeError")
class W(Y, X): pass
print([k.__name__ for k in W.__mro__])
```
<details><summary>Answer</summary>

```text
TypeError
['W', 'Y', 'X', 'object']
```
`(X, Y)` demands X before Y, but Y is a subclass of X and must precede it.
</details>

#### Q15. classmethod/staticmethod inheritance · 🟡 · *cls binding*
```python
class Base:
    @classmethod
    def make(cls): return cls()
    @staticmethod
    def kind(): return "base"
class Child(Base):
    @staticmethod
    def kind(): return "child"
obj = Child.make()
print(type(obj).__name__, obj.kind(), Base.kind())
```
<details><summary>Answer</summary>

```text
Child child base
```
</details>

#### Q16. Name mangling · 🟡 · *_Class__attr*
```python
class A:
    def __init__(self): self.__x = 1; self._y = 2
a = A()
print(a._y, a._A__x, hasattr(a, "__x"))
```
<details><summary>Answer</summary>

```text
2 1 False
```
</details>

#### Q17. Property vs instance dict · 🔴 · *data descriptor priority*
```python
class P:
    @property
    def x(self): return 10
p = P()
try:
    p.x = 5
except AttributeError:
    print("AttributeError")
p.__dict__["x"] = 99
print(p.x)
```
<details><summary>Answer</summary>

```text
AttributeError
10
```
No setter → assignment fails. Even after sneaking a value into `__dict__`, the property (data descriptor) wins on lookup.
</details>

#### Q18. Instance attribute shadows a method · 🟡 · *non-data descriptor*
```python
class M:
    def f(self): return "method"
m = M()
m.f = lambda: "instance"
print(m.f(), M().f())
```
<details><summary>Answer</summary>

```text
instance method
```
Functions are non-data descriptors, so the instance `__dict__` entry wins for `m` only.
</details>

#### Q19. `__getattr__` fallback · 🟡 · *only on miss*
```python
class G:
    x = 1
    def __getattr__(self, name): return f"missing:{name}"
g = G()
print(g.x, g.y)
g.y = 5
print(g.y)
```
<details><summary>Answer</summary>

```text
1 missing:y
5
```
</details>

#### Q20. `__getattribute__` intercepts everything · 🔴 · *lookup hooks*
```python
class L:
    def __init__(self): self.a = 1
    def __getattribute__(self, name):
        if name == "a": return 100
        return super().__getattribute__(name)
    def __getattr__(self, name): return "fallback"
l = L()
print(l.a, l.b, l.__dict__)
```
<details><summary>Answer</summary>

```text
100 fallback {'a': 1}
```
`l.b` raises `AttributeError` inside `__getattribute__`, which triggers `__getattr__`.
</details>

#### Q21. `sum()` and `__radd__` · 🔴 · *reflected operators*
```python
class N:
    def __init__(self, v): self.v = v
    def __add__(self, o): return N(self.v + (o.v if isinstance(o, N) else o))
    def __radd__(self, o): print("radd", o); return self + o
total = sum([N(1), N(2)])
print(total.v)
```
<details><summary>Answer</summary>

```text
radd 0
3
```
`sum` starts with `0`: `0 + N(1)` → `int.__add__` returns `NotImplemented` → `N(1).__radd__(0)`. Then `N(1) + N(2)` uses `__add__`.
</details>

#### Q22. `+=` vs `+` on lists · 🟡 · *mutate vs rebind*
```python
a = [1]; b = a
a += [2]
c = [1]; d = c
c = c + [2]
print(b, d)
```
<details><summary>Answer</summary>

```text
[1, 2] [1]
```
</details>

#### Q23. The tuple `+=` puzzle · 🔴 · *`__iadd__` + item assignment*
```python
t = ([1],)
try:
    t[0] += [2]
except TypeError:
    print("TypeError")
print(t)
```
<details><summary>Answer</summary>

```text
TypeError
([1, 2],)
```
The list's `__iadd__` mutates it first; then `t[0] = …` fails because tuples don't support item assignment.
</details>

#### Q24. Truthiness fallbacks · 🟡 · *`__bool__` → `__len__` → True*
```python
class B1:
    def __len__(self): return 0
class B2:
    def __bool__(self): return True
    def __len__(self): return 0
class B3: pass
print(bool(B1()), bool(B2()), bool(B3()))
```
<details><summary>Answer</summary>

```text
False True True
```
</details>

#### Q25. `in` without `__contains__` · 🟡 · *falls back to iteration*
```python
class It:
    def __iter__(self):
        print("iter"); yield 1; yield 2; yield 3
print(2 in It())
```
<details><summary>Answer</summary>

```text
iter
True
```
</details>

#### Q26. Iterator exhaustion · 🟢 · *single-use iterators*
```python
nums = map(lambda x: x * 2, [1, 2, 3])
print(list(nums), list(nums))
```
<details><summary>Answer</summary>

```text
[2, 4, 6] []
```
</details>

#### Q27. Generator laziness · 🟡 · *execution order*
```python
def gen():
    print("start")
    yield 1
    print("middle")
    yield 2
g = gen()
print("created")
print(next(g))
print(list(g))
```
<details><summary>Answer</summary>

```text
created
start
1
middle
[2]
```
Calling `gen()` runs nothing; each `next` runs to the following `yield`.
</details>

#### Q28. Context manager suppression · 🟡 · *`__exit__` returns True*
```python
class CM:
    def __enter__(self): print("enter"); return "value"
    def __exit__(self, *exc):
        print("exit", exc[0].__name__ if exc[0] else None)
        return True
with CM() as v:
    print(v)
    1 / 0
print("after")
```
<details><summary>Answer</summary>

```text
enter
value
exit ZeroDivisionError
after
```
`v` is what `__enter__` returned (not the CM). Returning `True` swallows the exception.
</details>

#### Q29. `NotImplemented` from both sides · 🔴 · *`==` fallback to identity*
```python
class A:
    def __eq__(self, o):
        print("A.eq"); return NotImplemented
class B:
    def __eq__(self, o):
        print("B.eq"); return NotImplemented
a = A()
print(a == B())
```
<details><summary>Answer</summary>

```text
A.eq
B.eq
False
```
Left tries, then the reflected `B.__eq__`, then `==` falls back to `a is b` → `False`. (For `<`, this would raise `TypeError`.)
</details>

#### Q30. Identity vs equality · 🟢 · *`is` vs `==`*
```python
a = [1, 2]; b = a; c = list(a)
print(a == c, a is c, a is b)
```
<details><summary>Answer</summary>

```text
True False True
```
</details>

#### Q31. Shallow vs deep copy · 🟡 · *shared inner objects*
```python
import copy
x = [[1], [2]]
s = copy.copy(x); d = copy.deepcopy(x)
x[0].append(9); x.append([3])
print(s, d)
```
<details><summary>Answer</summary>

```text
[[1, 9], [2]] [[1], [2]]
```
</details>

#### Q32. List multiplication aliasing · 🟡 · *references*
```python
g = [[0] * 2] * 2
g[0][0] = 1
print(g)
```
<details><summary>Answer</summary>

```text
[[1, 0], [1, 0]]
```
</details>

#### Q33. Late-binding lambdas in a class · 🟡 · *closures*
```python
class Btn:
    def __init__(self): self.handlers = [lambda: i for i in range(3)]
print([h() for h in Btn().handlers])
```
<details><summary>Answer</summary>

```text
[2, 2, 2]
```
All lambdas see the comprehension's final `i`. Fix: `lambda i=i: i`.
</details>

#### Q34. `__init_subclass__` · 🟡 · *class creation hook*
```python
class Base:
    subs = []
    def __init_subclass__(cls, **kw):
        super().__init_subclass__(**kw)
        Base.subs.append(cls.__name__)
class A(Base): pass
class B(A): pass
print(Base.subs)
```
<details><summary>Answer</summary>

```text
['A', 'B']
```
It fires for every descendant, including grandchildren (B inherits the hook via A).
</details>

#### Q35. Custom data descriptor · 🔴 · *`__get__` wins*
```python
class D:
    def __get__(self, i, o): return "desc"
    def __set__(self, i, v): i.__dict__["val"] = v
class C:
    val = D()
c = C()
c.val = 5
print(c.val, c.__dict__)
```
<details><summary>Answer</summary>

```text
desc {'val': 5}
```
</details>

#### Q36. Dataclass equality & hashing · 🟡 · *frozen*
```python
from dataclasses import dataclass
@dataclass
class P:
    x: int
print(P(1) == P(1), P.__hash__)
@dataclass(frozen=True)
class F:
    x: int
print(len({F(1), F(1)}))
```
<details><summary>Answer</summary>

```text
True None
1
```
</details>

#### Q37. `__slots__` · 🟡 · *no dynamic attributes*
```python
class S:
    __slots__ = ("a",)
s = S(); s.a = 1
try:
    s.b = 2
except AttributeError:
    print("AttributeError")
print(hasattr(s, "__dict__"))
```
<details><summary>Answer</summary>

```text
AttributeError
False
```
</details>

#### Q38. Abstract base classes · 🟡 · *instantiation check*
```python
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): ...
    def describe(self): return f"area={self.area()}"
class Sq(Shape):
    def __init__(self, s): self.s = s
    def area(self): return self.s ** 2
try:
    Shape()
except TypeError:
    print("TypeError")
print(Sq(3).describe(), Shape.__abstractmethods__)
```
<details><summary>Answer</summary>

```text
TypeError
area=9 frozenset({'area'})
```
</details>

#### Q39. "Overloading" · 🟢 · *last definition wins*
```python
class Calc:
    def add(self, a, b): return a + b
    def add(self, a, b, c=0): return a + b + c
print(Calc().add(1, 2), Calc().add(1, 2, 3))
```
<details><summary>Answer</summary>

```text
3 6
```
Only the second `add` exists; the default parameter makes both calls work.
</details>

#### Q40. Inherited class attributes · 🟡 · *lookup through the MRO*
```python
class Parent:
    x = 1
class Child(Parent): pass
Child.x = 2
print(Parent.x, Child.x)
del Child.x
print(Child.x)
Parent.x = 3
print(Child.x)
```
<details><summary>Answer</summary>

```text
1 2
1
3
```
</details>

#### Q41. `__del__` and reference counting (CPython) · 🔴 · *lifecycle*
```python
class R:
    def __init__(self, n): self.n = n
    def __del__(self): print("del", self.n)
def f():
    r = R(1)
    print("in f")
f()
print("after f")
x = R(2)
x = R(3)
del x
print("end")
```
<details><summary>Answer</summary>

```text
in f
del 1
after f
del 2
del 3
end
```
Local `r` dies when `f` returns; `R(2)` dies when `x` is rebound (after `R(3)` is created); `del x` drops the last reference to `R(3)`. Deterministic only in CPython.
</details>

#### Q42. Callable instances · 🟢 · *`__call__`*
```python
class Counter:
    def __init__(self): self.n = 0
    def __call__(self, step=1):
        self.n += step
        return self.n
c = Counter()
c(); c(5)
print(c.n, callable(c), callable(Counter))
```
<details><summary>Answer</summary>

```text
6 True True
```
Instances are callable because `Counter` defines `__call__`; the class is callable because `type` does.
</details>

---

## M23. Coding Exercises & Mock Interviews

> Attempt each exercise **before** opening the hints. Use hints one at a time. Solutions are collapsed at the end of each exercise.

### Coding exercises

#### E1. Bank account (encapsulation, properties, representation) · 🟢
Build `BankAccount(owner, balance=0)` with: `deposit(amount)`, `withdraw(amount)` (no overdraft, positive amounts only), read-only `balance`, transaction history, a good `__repr__`, a friendly `__str__`.
<details><summary>Hints</summary>

1. Store the balance as `_balance`; expose it with a `@property` and no setter.
2. Validate in one private helper `_check(amount)`.
3. History = list of `(kind, amount)` tuples created in `__init__` (not a class attribute!).
</details>
<details><summary>Solution</summary>

```python
class InsufficientFunds(Exception): pass

class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self._balance = 0
        self._history: list[tuple[str, float]] = []
        if balance: self.deposit(balance)

    @property
    def balance(self): return self._balance

    @property
    def history(self): return tuple(self._history)      # read-only view

    @staticmethod
    def _check(amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("amount must be a positive number")

    def deposit(self, amount):
        self._check(amount)
        self._balance += amount
        self._history.append(("deposit", amount))

    def withdraw(self, amount):
        self._check(amount)
        if amount > self._balance:
            raise InsufficientFunds(f"balance {self._balance} < {amount}")
        self._balance -= amount
        self._history.append(("withdraw", amount))

    def __repr__(self): return f"{type(self).__name__}(owner={self.owner!r}, balance={self._balance!r})"
    def __str__(self): return f"{self.owner}'s account: ₹{self._balance:,.2f}"

acc = BankAccount("Parth", 1000)
acc.withdraw(250)
print(acc, repr(acc), acc.history)
```
</details>

#### E2. `Money` value object (dunders, equality, hashing, immutability) · 🟡
`Money(amount_paise, currency)`: immutable; `+`/`-` only with same currency (else `ValueError`); `* int`; comparable and sortable; hashable; `sum()` works; prints as `INR 12.50`.
<details><summary>Hints</summary>

1. `@dataclass(frozen=True, order=True)` gives immutability, hashing, ordering — but ordering would compare currency too; decide if that's OK or implement `__lt__` yourself.
2. Return `NotImplemented` for foreign types.
3. `__radd__` must handle `0` for `sum()`.
</details>
<details><summary>Solution</summary>

```python
from dataclasses import dataclass
from functools import total_ordering

@total_ordering
@dataclass(frozen=True)
class Money:
    paise: int
    currency: str = "INR"

    def _same(self, other):
        if not isinstance(other, Money): return False
        if other.currency != self.currency:
            raise ValueError(f"currency mismatch: {self.currency} vs {other.currency}")
        return True

    def __add__(self, other):
        if not self._same(other): return NotImplemented
        return Money(self.paise + other.paise, self.currency)
    def __radd__(self, other):
        return self if other == 0 else NotImplemented
    def __sub__(self, other):
        if not self._same(other): return NotImplemented
        return Money(self.paise - other.paise, self.currency)
    def __mul__(self, k):
        if not isinstance(k, int): return NotImplemented
        return Money(self.paise * k, self.currency)
    __rmul__ = __mul__
    def __lt__(self, other):
        if not self._same(other): return NotImplemented
        return self.paise < other.paise
    def __str__(self): return f"{self.currency} {self.paise / 100:.2f}"

items = [Money(1250), Money(500), Money(99)]
print(sum(items), sorted(items)[0], Money(500) * 3, len({Money(500), Money(500)}))
# INR 18.49 INR 0.99 INR 15.00 1
```
</details>

#### E3. `SortedList` container (collection protocol) · 🟡
Always-sorted list: `add(x)`, `len`, indexing & slicing, fast `in` (binary search), iteration, `reversed`, `__repr__`.
<details><summary>Solution</summary>

```python
import bisect

class SortedList:
    def __init__(self, items=()): self._d = sorted(items)
    def add(self, x): bisect.insort(self._d, x)
    def __len__(self): return len(self._d)
    def __getitem__(self, i):
        return SortedList(self._d[i]) if isinstance(i, slice) else self._d[i]
    def __contains__(self, x):                       # O(log n) instead of O(n) default
        i = bisect.bisect_left(self._d, x)
        return i < len(self._d) and self._d[i] == x
    def __iter__(self): return iter(self._d)
    def __reversed__(self): return reversed(self._d)
    def __repr__(self): return f"SortedList({self._d})"

s = SortedList([5, 1, 4]); s.add(3)
print(s, s[1:3], 4 in s, list(reversed(s)))    # SortedList([1, 3, 4, 5]) SortedList([3, 4]) True [5, 4, 3, 1]
```
</details>

#### E4. Mini ORM fields (descriptors + `__set_name__` + `__init_subclass__`) · 🔴
Create `Field` descriptors with type checking (`IntField`, `StrField(max_len)`), and a `Model` base that collects declared fields into `cls._fields` and generates a keyword `__init__` and `__repr__`.
<details><summary>Hints</summary>

1. `__set_name__` gives each field its name; store values in `instance.__dict__[name]`.
2. `__init_subclass__` can scan `cls.__dict__` for `Field` instances.
3. `Model.__init__(self, **kwargs)` loops over `type(self)._fields`.
</details>
<details><summary>Solution</summary>

```python
class Field:
    expected = object
    def __set_name__(self, owner, name): self.name = name
    def __get__(self, inst, owner):
        if inst is None: return self
        return inst.__dict__.get(self.name)
    def __set__(self, inst, value):
        if not isinstance(value, self.expected):
            raise TypeError(f"{self.name} must be {self.expected.__name__}")
        self.validate(value)
        inst.__dict__[self.name] = value
    def validate(self, value): pass

class IntField(Field): expected = int
class StrField(Field):
    expected = str
    def __init__(self, max_len=255): self.max_len = max_len
    def validate(self, value):
        if len(value) > self.max_len: raise ValueError(f"{self.name} too long")

class Model:
    _fields: tuple = ()
    def __init_subclass__(cls, **kw):
        super().__init_subclass__(**kw)
        cls._fields = tuple(n for n, v in vars(cls).items() if isinstance(v, Field))
    def __init__(self, **kwargs):
        for name in self._fields:
            setattr(self, name, kwargs[name])
    def __repr__(self):
        args = ", ".join(f"{n}={getattr(self, n)!r}" for n in self._fields)
        return f"{type(self).__name__}({args})"

class User(Model):
    id = IntField()
    name = StrField(max_len=5)

print(User(id=1, name="Parth"))          # User(id=1, name='Parth')
try:
    User(id="1", name="x")
except TypeError as e:
    print(e)                             # id must be int
```
</details>

#### E5. Timer context manager (class and generator versions) · 🟢
`with Timer("db") as t:` records `t.elapsed` and prints it on exit; must not swallow exceptions.
<details><summary>Solution</summary>

```python
import time
from contextlib import contextmanager

class Timer:
    def __init__(self, label): self.label, self.elapsed = label, None
    def __enter__(self):
        self._start = time.perf_counter(); return self
    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self._start
        print(f"{self.label}: {self.elapsed:.4f}s")
        return False                               # propagate exceptions

@contextmanager
def timer(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        print(f"{label}: {time.perf_counter() - start:.4f}s")

with Timer("loop") as t:
    sum(range(100_000))
print(t.elapsed is not None)     # True
```
</details>

#### E6. Token-bucket rate limiter (`__call__`, encapsulated state) · 🟡
`limiter = TokenBucket(capacity=5, refill_per_sec=1)`; `limiter()` returns True/False. Make the clock injectable for tests.
<details><summary>Solution</summary>

```python
import time

class TokenBucket:
    def __init__(self, capacity, refill_per_sec, clock=time.monotonic):
        self.capacity, self.rate, self._clock = capacity, refill_per_sec, clock
        self._tokens, self._last = float(capacity), clock()
    def __call__(self, cost=1) -> bool:
        now = self._clock()
        self._tokens = min(self.capacity, self._tokens + (now - self._last) * self.rate)
        self._last = now
        if self._tokens >= cost:
            self._tokens -= cost
            return True
        return False

fake_time = [0.0]
tb = TokenBucket(2, 1, clock=lambda: fake_time[0])
print(tb(), tb(), tb())        # True True False
fake_time[0] = 1.0
print(tb())                    # True  (one token refilled)
```
</details>

#### E7. Refactor to Strategy · 🟢
Refactor this into classes/functions so a new carrier needs no edits to `shipping_cost`:
```python
def shipping_cost(carrier, weight_kg):
    if carrier == "bluedart": return 50 + 20 * weight_kg
    elif carrier == "delhivery": return 40 + 25 * weight_kg
    elif carrier == "indiapost": return 30 if weight_kg < 1 else 30 + 10 * weight_kg
```
<details><summary>Solution</summary>

```python
CARRIERS = {}
def carrier(name):
    def register(fn):
        CARRIERS[name] = fn
        return fn
    return register

@carrier("bluedart")
def _bluedart(w): return 50 + 20 * w
@carrier("delhivery")
def _delhivery(w): return 40 + 25 * w
@carrier("indiapost")
def _indiapost(w): return 30 if w < 1 else 30 + 10 * w

def shipping_cost(name, weight_kg):
    try:
        return CARRIERS[name](weight_kg)
    except KeyError:
        raise ValueError(f"unknown carrier {name}") from None

print(shipping_cost("delhivery", 2))     # 90
```
</details>

#### E8. Re-iterable `DateRange` (iteration protocol) · 🟡
`DateRange(start, end, step_days=1)` — iterable multiple times, supports `len`, `in`, and `reversed`.
<details><summary>Solution</summary>

```python
from datetime import date, timedelta

class DateRange:
    def __init__(self, start: date, end: date, step_days=1):
        self.start, self.end, self.step = start, end, timedelta(days=step_days)
    def __iter__(self):                                 # generator → fresh iterator each time
        d = self.start
        while d < self.end:
            yield d
            d += self.step
    def __len__(self):
        return max(0, -(-(self.end - self.start).days // self.step.days))
    def __contains__(self, d):
        return self.start <= d < self.end and (d - self.start).days % self.step.days == 0
    def __reversed__(self):
        return reversed(list(self))

r = DateRange(date(2026, 11, 1), date(2026, 11, 8), 2)
print([d.day for d in r], [d.day for d in r], len(r), date(2026, 11, 5) in r)
# [1, 3, 5, 7] [1, 3, 5, 7] 4 True
```
</details>

### 🐞 Debugging tasks
Find the bug, explain the mechanism, fix it.

| # | Buggy code | Bug & fix |
|---|---|---|
| D1 | `class Team: members = []` then `self.members.append(x)` | Shared class-level list. Create `self.members = []` in `__init__`. |
| D2 | `def __init__(self, tags=[]): self.tags = tags` | Mutable default shared across instances. Use `tags=None`. |
| D3 | `def __setattr__(self, k, v): self.__dict__[k] = v; self.k = v` | `self.k = v` recurses into `__setattr__` forever. Use `super().__setattr__(k, v)` only. |
| D4 | `class Child(Base): def __init__(self, x): self.x = x` → later `AttributeError` on a base attribute | Missing `super().__init__()`. |
| D5 | `@dataclass class P: x: int` used as dict key → `TypeError` | Plain dataclasses are unhashable; use `frozen=True`. |
| D6 | `def __iadd__(self, o): self.items.append(o)` → object becomes `None` | `__iadd__` must `return self`. |
| D7 | `def __eq__(self, o): return self.id == o.id` → `AttributeError` when comparing with `None` | Return `NotImplemented` for foreign types: `if not isinstance(o, User): return NotImplemented`. |
| D8 | Singleton via `__new__` loses state on every `Config()` call | `__init__` re-runs; guard it or use a module-level instance. |
| D9 | `class A: def __init__(self): self.__secret = 1` ; `class B(A): def reveal(self): return self.__secret` | Name mangling: B looks for `_B__secret`. Use `_secret` (single underscore) for subclass-visible internals. |
| D10 | `@property def x(self): ...` then `@x.setter def set_x(self, v): ...` | Setter must reuse the name `x`; otherwise `x` remains read-only and `set_x` becomes a separate property. |

### 🏗 Class design exercises (LLD practice)
For each: list entities, relationships (is-a / has-a), key methods, which patterns apply, and how you'd test it.
1. **Parking lot** — vehicle types, spot sizes, multiple levels, fee strategies, entry/exit tickets.
2. **Library management** — books vs copies (aggregation), members, loans, fines (strategy), reservations (observer).
3. **Food delivery order lifecycle** — State pattern for order status, notifications on transitions, payment via adapter.
4. **Splitwise** — users, groups, expenses, split strategies (equal/exact/percent), balance simplification.
5. **Rate limiter service** — algorithms as strategies, per-user buckets, Redis-backed store behind a Protocol.
6. **Feature flag system** — rules (percentage rollout, user list, region) as composable strategies; cache layer; audit log.

### 🎤 Mock interviews (45 minutes each)
Run these with the [Interview mode prompt](#06-mentor-modes) or a friend. Speak your answers.

**Mock 1 — Fundamentals → internals (Python developer screen)**
1. What's `self`? → follow-up: what object does `obj.method` return?
2. Class vs instance attributes → predict Q3 from [M22](#m22-output-prediction).
3. `__str__` vs `__repr__` → which one does a list use for its elements?
4. `__new__` vs `__init__` → write a class that rejects negative values when subclassing `int`.
5. What happens when you call `MyClass()`?
*Strong signals:* mentions bound methods, fallback directions, `type.__call__`, the `isinstance` check.

**Mock 2 — Inheritance deep dive**
1. Types of inheritance in Python. 2. Compute the MRO of a given hierarchy by hand (C3). 3. Predict a diamond `super()` output (Q11–Q13). 4. Why does `super()` in B reach C? 5. Cooperative `__init__` with different arguments — write it. 6. Composition vs inheritance — refactor a 6-subclass notifier hierarchy.
*Strong signals:* "super is MRO-relative to type(self)", `**kwargs` forwarding, class-explosion argument.

**Mock 3 — Data model & descriptors**
1. Make `Vector` support `+`, `*` (both sides), `abs`, `==`, use as dict key, `sum()`. 2. What's returned when an operator doesn't support the operand? 3. Attribute lookup order. 4. Why can an instance shadow a method but not a property? 5. Write a validated descriptor with `__set_name__`. 6. `__getattr__` vs `__getattribute__`.
*Strong signals:* `NotImplemented`, `__radd__` for `sum`, eq/hash contract, data vs non-data descriptor priority.

**Mock 4 — Design (LLD) round**
"Design a notification service that supports email, SMS, push, and WhatsApp; users choose channels; providers fail sometimes; we'll add more channels." Expect: requirements clarification → entities → interfaces (Protocol/ABC) → Strategy + Factory + retry policy + DI → class diagram → code for core parts → testing with fakes → extensions (queues, idempotency, rate limits, templates).
*Strong signals:* OCP/DIP named and justified, failure isolation per channel, testability, not over-engineering.

---

## M24. Mastery Tracker & Final Revision Sheet

### Status definitions
| Status | Meaning |
|---|---|
| ⬜ Not Started | — |
| 🟨 Learning | Read the module, ran the examples |
| 🟦 Practiced | Wrote own code + completed related output predictions |
| 🟪 Revised | Re-explained from memory after ≥ 3 days |
| 🟩 Interview Ready | All 6 criteria below ✅ |

**Interview-ready criteria (all must be true):** (1) I can explain the concept in 60 s · (2) I can implement it from scratch · (3) I can predict outputs of tricky snippets · (4) I can explain the internal mechanism · (5) I can state trade-offs / when not to use it · (6) I can handle two levels of follow-up.

### Tracker
| Module | Prerequisites | Theory | Code | Output pred. | Interview Qs | Last revised | Confidence (1–5) | Status |
|---|---|---|---|---|---|---|---|---|
| M0 Foundations | — | ☐ | ☐ | Q4, Q22, Q32, Q33 | ☐ | | | ⬜ |
| M1 Fundamentals | M0 | ☐ | ☐ | Q1–Q3, Q40 | B1–B5 | | | ⬜ |
| M2 Method types | M1 | ☐ | ☐ | Q15 | I3 | | | ⬜ |
| M3 Relationships | M1 | ☐ | ☐ | — | — | | | ⬜ |
| M4 Encapsulation | M1 | ☐ | ☐ | Q16, Q17 | B7, I8 | | | ⬜ |
| M5 Abstraction | M4 | ☐ | ☐ | Q38 | I9, I13 | | | ⬜ |
| M6 Inheritance | M5 | ☐ | ☐ | Q40 | I10 | | | ⬜ |
| M7 Polymorphism | M6 | ☐ | ☐ | Q39 | I4, I11 | | | ⬜ |
| M8 Lifecycle | M1, M6 | ☐ | ☐ | Q5–Q7, Q41 | I1, A1, A10, A11 | | | ⬜ |
| M9 super & MRO | M6 | ☐ | ☐ | Q11–Q14 | I5–I7, A12 | | | ⬜ |
| M10 Descriptors | M9 | ☐ | ☐ | Q17–Q20, Q35 | A3–A6, A18, A19 | | | ⬜ |
| M11 Properties & decorators | M10 | ☐ | ☐ | Q17 | I12 | | | ⬜ |
| M12 Dunders | M10 | ☐ | ☐ | Q21–Q25, Q29, Q42 | A13–A15 | | | ⬜ |
| M13 str vs repr | M12 | ☐ | ☐ | Q8, Q9 | I2 | | | ⬜ |
| M14 Equality/hash/copy | M12 | ☐ | ☐ | Q10, Q30, Q31, Q36 | I16–I19, A17 | | | ⬜ |
| M15 Iterators & context mgrs | M12 | ☐ | ☐ | Q25–Q28 | I20, A16 | | | ⬜ |
| M16 Exceptions | M6 | ☐ | ☐ | — | — | | | ⬜ |
| M17 Advanced | M10–M15 | ☐ | ☐ | Q34, Q36, Q37 | I14, I15, A2, A7–A9 | | | ⬜ |
| M18 SOLID | M4–M7 | ☐ | ☐ | — | A20 | | | ⬜ |
| M19 Patterns | M18 | ☐ | ☐ | — | Pattern table | | | ⬜ |
| M20 Real-world | M18, M19 | ☐ | ☐ | — | LLD table | | | ⬜ |

### Revision schedule (spaced repetition)
Revisit each module on **day 1, 3, 7, 21** after first study. Each revision: (1) re-read only the 📝 revision notes, (2) answer its interview questions aloud, (3) redo its output predictions without looking, (4) write one example from memory.

### 🧾 Final one-page revision sheet
```text
OBJECTS      names → objects; assignment never copies; mutate vs rebind; is (identity) vs == (__eq__)
CLASSES      class is an object (type); obj.m(a) == type(obj).m(obj, a) via bound method
ATTRIBUTES   read: inst dict → class → MRO ; write via instance → inst dict ; mutable class attrs shared
METHODS      instance(self) | @classmethod(cls, subclass-aware, alt constructors) | @staticmethod(nothing)
CREATION     Cls() → type.__call__ → __new__(cls) returns obj → if isinstance: __init__(self) returns None
             non-instance → init skipped ; cached → init re-runs ; immutables customise in __new__
LIFECYCLE    refcount + cyclic GC ; __del__ unreliable → with / weakref.finalize ; finaliser once (PEP 442)
ENCAPSULATE  _x convention ; __x → _Class__x (anti-clash) ; @property for validation/computed/read-only
ABSTRACT     ABC + @abstractmethod → TypeError at instantiation ; Protocol = structural, static ; duck typing
INHERIT      MRO = C3 (child first, base order kept, each once) ; super() = next in type(self).__mro__
             cooperative: everyone calls super(), **kwargs ; mixins left ; composition > inheritance
POLYMORPH    dynamic dispatch ; duck typing ; operators via dunders ; no overloading → defaults/singledispatch
LOOKUP       data descriptor > instance __dict__ > non-data descriptor > class attr > __getattr__
             functions = non-data (bound methods) ; property = data ; implicit dunders use type(obj)
DUNDERS      return NotImplemented ; a+b → __add__ → __radd__ ; += → __iadd__ (return self) or rebinding
             __bool__ → __len__ → True ; __contains__ → __iter__ → __getitem__ ; looked up on the type
REPR         always __repr__ (unambiguous, !r, type(self).__name__) ; __str__ falls back to repr ; containers use repr
HASH         a == b ⇒ hash equal ; __eq__ alone → __hash__ None ; hash immutable fields ; frozen dataclass
COPY         alias vs shallow (shared inner) vs deep (memo) ; __copy__/__deepcopy__
ITER/CTX     iterable(__iter__) vs iterator(__next__, single-use) ; generators lazy ; with → __enter__/__exit__(truthy suppresses)
ADVANCED     class stmt: __prepare__ → body → metaclass → __set_name__ → __init_subclass__ → decorators
             prefer __init_subclass__/decorators over metaclasses ; dataclass(frozen, slots, default_factory)
             __slots__: no __dict__, less memory ; generics/Self = static only
SOLID        S one reason to change | O extend not modify | L substitutable | I small interfaces | D depend on abstractions + DI
PATTERNS     Strategy, Factory, Adapter, Decorator, Facade, Proxy, Observer, State, Command, Template, Chain, Builder, Singleton(module)
```

---

> **Final word:** Python OOP interviews reward people who can explain *mechanisms*, not just definitions. When you answer, follow this shape: **definition → how Python implements it → a tiny example → a trap or trade-off → a real backend use.** If you can do that for every module in this file, you're ready. 🚀
