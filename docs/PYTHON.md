# Master Python from 0 → 100: Complete Python Learning, Internals, Advanced & Production Engineering
## Fundamentals · Internals · Concurrency · Backend · Production
### 0 → 100 | 36 Levels | 100 Topics | Beginner → Principal Engineer Edition

---

## What Is This File?

This is a complete **Python mastery learning roadmap** that takes you from absolute
beginner to principal-level Python engineer.

It covers:
- **Foundations** — How Python works, data types, control flow, functions, OOP
- **Internals** — CPython, bytecode, memory management, GIL, descriptors, metaclasses
- **Advanced** — Generators, decorators, async, concurrency, type system
- **Production** — FastAPI, databases, Redis, testing, security, observability, deployment

Every topic is a **copy-paste block** you drop into the Teaching Prompt below.
Claude then teaches that topic with a full lesson: analogy, internal behavior,
trade-offs, common mistakes, production considerations, and interview Q&As.

---

## The Teaching Prompt

Copy this once. Save it permanently (Notion, Claude Project, sticky note).
Every time you study a topic, paste the topic block into `{PASTE TOPIC HERE}`.

```
You are a Principal Python Engineer, Python Core Developer, Backend Architect,
and Senior Software Engineer with 20+ years of real-world industry experience
writing, scaling, and operating production Python systems.

Your task is to teach me Python — from fundamentals through internals, advanced
features, concurrency, backend engineering, and production-grade systems — in a
way that builds genuine engineering understanding, not just interview memorization.

I am a developer who wants to go from beginner to principal-level Python mastery.
I want to understand WHY Python behaves the way it does, not just how to write it.

I want:
- Clear understanding from fundamentals → production-grade Python
- Engineering judgment — when to use X, when NOT to use X, and why
- Real trade-off analysis (not "it depends" without explanation)
- Python internals — what happens underneath the syntax
- Production-readiness thinking
- Understanding of how concepts evolve and connect to each other

---

STRICT TEACHING RULES
1. Start from the problem — explain WHY the concept exists before the concept itself
2. Use a simple real-world analogy FIRST, then go technical
3. Never say "it depends" without explaining exactly what it depends on
4. Always explain WHY a feature/pattern exists (what problem it solves)
5. Always explain WHEN NOT to use it — this is as important as when to use it
6. Show trade-offs explicitly: performance, readability, maintainability, memory, complexity
7. Use code-based diagrams (arrows and boxes) for execution flow and memory
8. Compare alternatives in a table (e.g. list vs tuple, threading vs asyncio, ORM vs raw SQL)
9. Connect every concept to a real production scenario
10. Show the EVOLUTION — how a naive solution leads to the pattern you are teaching
11. Show FAILURE SCENARIOS — what goes wrong if you misuse this feature?
12. Include memory and time complexity where relevant
13. Show what a junior writes vs what a senior writes vs what a principal writes
14. Include interview questions from beginner → advanced
15. End with a hands-on exercise or debugging challenge
16. Do NOT suggest complex patterns when simple code solves the problem
17. Highlight common mistakes and anti-patterns beginners fall into
18. Always show internal implementation behavior where relevant

---

OUTPUT FORMAT — use this structure every time, no exceptions:

### 1. Simple Explanation (ELI5 + Real-World Analogy)
### 2. Technical Deep Dive
### 3. Why Does This Exist? (The Problem It Solves)
### 4. How It Works Internally (CPython / Memory / Execution Diagram)
### 5. When Should You Use It? (Concrete Situations)
### 6. When Should You NOT Use It? (Anti-patterns + Over-engineering)
### 7. Alternatives Comparison Table
### 8. Trade-offs (Performance / Memory / Readability / Maintainability / Complexity)
### 9. Evolution (How This Concept Builds From What Came Before)
### 10. Failure Scenarios (What breaks when you misuse this)
### 11. Production Considerations (What senior engineers worry about)
### 12. Junior vs Senior vs Principal (How thinking differs at each level)
### 13. Common Mistakes Beginners Make
### 14. Interview Questions & Answers (Beginner → Advanced)
### 15. Code Example (Clean, well-commented)
### 16. Production Example (Realistic, full context)
### 17. Exercise / Debugging Challenge
### 18. Quick Revision Summary (bullet points, max 10 lines)
### 19. Most Important Takeaway

---

Topic to teach:
👉 {PASTE TOPIC HERE}
```

---

## Roadmap Structure — 36 Levels, 100 Topics

```
LEVEL 0   Python Orientation & Setup                 Topics 1–4
LEVEL 1   Variables, Objects & Memory                Topics 5–7
LEVEL 2   Python Data Types                          Topics 8–12
LEVEL 3   Data Structures                            Topics 13–17
LEVEL 4   Control Flow                               Topics 18–21
LEVEL 5   Functions — Fundamentals                   Topics 22–25
LEVEL 6   Functions — Advanced                       Topics 26–29
LEVEL 7   Strings & Text Processing                  Topics 30–32
LEVEL 8   Modules, Packages & Imports                Topics 33–35
LEVEL 9   Virtual Environments & Dependency Mgmt     Topics 36–37
LEVEL 10  Object-Oriented Programming — Basics       Topics 38–41
LEVEL 11  Object-Oriented Programming — Advanced     Topics 42–45
LEVEL 12  Magic / Dunder Methods                     Topics 46–47
LEVEL 13  Pythonic Programming                       Topics 48–50
LEVEL 14  Exceptions & Error Handling                Topics 51–53
LEVEL 15  Iterators & Generators                     Topics 54–56
LEVEL 16  Decorators                                 Topics 57–59
LEVEL 17  Context Managers                           Topics 60–61
LEVEL 18  Type Hints & Static Typing                 Topics 62–64
LEVEL 19  Dataclasses & Data Containers              Topics 65–66
LEVEL 20  Functional Programming                     Topics 67–68
LEVEL 21  Python Internals — CPython                 Topics 69–71
LEVEL 22  Memory Management & GC                     Topics 72–74
LEVEL 23  The GIL                                    Topics 75–76
LEVEL 24  Concurrency — Threading                    Topics 77–79
LEVEL 25  Concurrency — Multiprocessing              Topics 80–81
LEVEL 26  AsyncIO — Foundations                      Topics 82–84
LEVEL 27  AsyncIO — Advanced                         Topics 85–86
LEVEL 28  Performance Engineering                    Topics 87–88
LEVEL 29  Testing                                    Topics 89–91
LEVEL 30  Debugging & Profiling                      Topics 92–93
LEVEL 31  Code Quality & Clean Code                  Topics 94–95
LEVEL 32  Design Patterns in Python                  Topics 96–97
LEVEL 33  Architecture                               Topics 98–99
LEVEL 34  Backend Python — FastAPI                   Topics 100–102
LEVEL 35  Databases & SQLAlchemy                     Topics 103–105
LEVEL 36  Production Python                          Topics 106–110
```

---

## All 110 Topics at a Glance

### LEVEL 0 — Python Orientation & Setup
```
Topic 1   What is Python? CPython, PyPy, and the Python Ecosystem
Topic 2   The Python Execution Model — Source → Bytecode → PVM
Topic 3   Installing Python, PATH, REPL, and Running Your First Script
Topic 4   Python Versions — 3.8 vs 3.10 vs 3.12 and What Changed
```

### LEVEL 1 — Variables, Objects & Memory
```
Topic 5   Variables are References — Not Boxes
Topic 6   Object Identity, Equality, and Interning — id(), is, ==
Topic 7   Mutability vs Immutability — The Most Misunderstood Python Concept
```

### LEVEL 2 — Python Data Types
```
Topic 8   int, float, bool, None — The Primitive Types (and Why They're Not)
Topic 9   Strings — Unicode, Encoding, Immutability, and intern()
Topic 10  bytes and bytearray — When You Work Below Text
Topic 11  Type Conversion and Type Coercion — Explicit vs Implicit
Topic 12  Dynamic Typing at Runtime — type(), isinstance(), and duck typing
```

### LEVEL 3 — Data Structures
```
Topic 13  list — Dynamic Arrays, Memory, Complexity, and Gotchas
Topic 14  tuple — Immutability, Packing/Unpacking, and Named Tuples
Topic 15  dict — Hash Tables, Collision, O(1) Lookups, and Insertion Order
Topic 16  set and frozenset — Hashing, Uniqueness, and Set Operations
Topic 17  collections Module — deque, Counter, defaultdict, OrderedDict
```

### LEVEL 4 — Control Flow
```
Topic 18  if / elif / else and Truthiness in Python
Topic 19  for Loops, while Loops, break, continue, pass, else on Loops
Topic 20  match / case — Structural Pattern Matching (Python 3.10+)
Topic 21  Comprehensions — list, dict, set, generator expressions
```

### LEVEL 5 — Functions — Fundamentals
```
Topic 22  Defining Functions — Parameters, Arguments, Return Values
Topic 23  *args and **kwargs — Flexible Function Signatures
Topic 24  Default Arguments and the Mutable Default Argument Bug
Topic 25  Scope and LEGB — Local, Enclosing, Global, Built-in
```

### LEVEL 6 — Functions — Advanced
```
Topic 26  First-Class Functions, Higher-Order Functions, Lambda
Topic 27  Closures — Functions That Remember
Topic 28  Recursion — When to Use and When to Avoid
Topic 29  Keyword-Only and Positional-Only Arguments (Python 3.8+)
```

### LEVEL 7 — Strings & Text Processing
```
Topic 30  String Methods, f-strings, and Formatting
Topic 31  Regular Expressions with re — Patterns, Groups, and Common Uses
Topic 32  Encoding and Decoding — Unicode → bytes → Unicode
```

### LEVEL 8 — Modules, Packages & Imports
```
Topic 33  import, from...import, __name__, __main__ — The Import System
Topic 34  Packages, __init__.py, Relative vs Absolute Imports
Topic 35  Circular Imports — How They Happen and How to Fix Them
```

### LEVEL 9 — Virtual Environments & Dependency Management
```
Topic 36  venv, pip, requirements.txt — The Basics
Topic 37  pyproject.toml, Poetry, uv, pip-tools — Modern Dependency Management
```

### LEVEL 10 — Object-Oriented Programming — Basics
```
Topic 38  Classes, Objects, __init__, Instance vs Class Attributes
Topic 39  Methods — Instance, Class (@classmethod), Static (@staticmethod)
Topic 40  Encapsulation — Public, Protected, Private, Properties (@property)
Topic 41  Inheritance — Single, Multiple, super(), and Method Resolution
```

### LEVEL 11 — Object-Oriented Programming — Advanced
```
Topic 42  Composition vs Inheritance — The Most Important OOP Decision
Topic 43  Polymorphism and Duck Typing — Python's Version of Interfaces
Topic 44  Abstract Base Classes (ABC) — Contracts Without Strict Types
Topic 45  MRO — Method Resolution Order and C3 Linearization
```

### LEVEL 12 — Magic / Dunder Methods
```
Topic 46  Core Dunders — __str__, __repr__, __eq__, __hash__, __len__
Topic 47  Protocol Dunders — __iter__, __next__, __getitem__, __call__, __enter__, __exit__
```

### LEVEL 13 — Pythonic Programming
```
Topic 48  EAFP vs LBYL — Python's Exception-Based Philosophy
Topic 49  Pythonic Idioms — enumerate, zip, any, all, sorted, unpacking
Topic 50  functools and itertools — The Standard Library Power Tools
```

### LEVEL 14 — Exceptions & Error Handling
```
Topic 51  Exception Hierarchy, try/except/else/finally, raise
Topic 52  Custom Exceptions and Exception Chaining (raise from)
Topic 53  Error Handling Strategies — When to Catch, When to Propagate
```

### LEVEL 15 — Iterators & Generators
```
Topic 54  Iterables vs Iterators — iter(), next(), and the Protocol
Topic 55  Generators — yield, Generator Expressions, Lazy Evaluation
Topic 56  Generator Pipelines and Infinite Generators
```

### LEVEL 16 — Decorators
```
Topic 57  Decorators — Functions That Wrap Functions
Topic 58  Parameterized Decorators and functools.wraps
Topic 59  Class Decorators and Real-World Decorator Patterns
```

### LEVEL 17 — Context Managers
```
Topic 60  Context Managers — __enter__, __exit__, the with Statement
Topic 61  contextlib — @contextmanager, suppress, ExitStack
```

### LEVEL 18 — Type Hints & Static Typing
```
Topic 62  Type Hints Basics — str, int, list, Optional, Union, None
Topic 63  Generics, TypeVar, Protocol, TypedDict, Literal, Final
Topic 64  mypy and pyright — Static Type Checking in Practice
```

### LEVEL 19 — Dataclasses & Data Containers
```
Topic 65  @dataclass — Auto-generated Methods, Frozen, Slots, default_factory
Topic 66  dict vs dataclass vs NamedTuple vs TypedDict vs Pydantic — When to Use Which
```

### LEVEL 20 — Functional Programming
```
Topic 67  map, filter, reduce, and Why Python Prefers Comprehensions
Topic 68  functools — partial, lru_cache, cache, reduce, wraps
```

### LEVEL 21 — Python Internals — CPython
```
Topic 69  CPython Internals — Interpreter, Frames, Code Objects, Call Stack
Topic 70  Bytecode — dis.dis(), How Python Code Becomes Instructions
Topic 71  Python Execution Model — Source → AST → Bytecode → PVM → Result
```

### LEVEL 22 — Memory Management & GC
```
Topic 72  Reference Counting — How Python Tracks Object Lifetimes
Topic 73  Garbage Collection — Cyclic References and the gc Module
Topic 74  Memory Leaks, Weak References, Object Interning, and tracemalloc
```

### LEVEL 23 — The GIL
```
Topic 75  The GIL — What It Is, Why It Exists, and What It Actually Does
Topic 76  GIL Implications — CPU-bound vs I/O-bound, Free-Threaded Python 3.13+
```

### LEVEL 24 — Concurrency — Threading
```
Topic 77  threading — Thread Lifecycle, Locks, RLock, Semaphore, Event
Topic 78  Race Conditions and Deadlocks — How They Happen and How to Prevent Them
Topic 79  ThreadPoolExecutor — Managed Thread Pools in Practice
```

### LEVEL 25 — Concurrency — Multiprocessing
```
Topic 80  multiprocessing — Processes, Pools, IPC, and Shared Memory
Topic 81  ProcessPoolExecutor and When to Use Processes vs Threads
```

### LEVEL 26 — AsyncIO — Foundations
```
Topic 82  AsyncIO — Event Loop, Coroutines, async/await from First Principles
Topic 83  Tasks, Futures, gather, create_task, TaskGroup
Topic 84  Async Context Managers, Async Iterators, Async Generators
```

### LEVEL 27 — AsyncIO — Advanced
```
Topic 85  AsyncIO Internals — What Happens When You await a Coroutine
Topic 86  Sync vs Threading vs Multiprocessing vs AsyncIO — The Decision Framework
```

### LEVEL 28 — Performance Engineering
```
Topic 87  Profiling First — cProfile, py-spy, tracemalloc, timeit
Topic 88  Optimization Techniques — Algorithms, Data Structures, Caching, Vectorization
```

### LEVEL 29 — Testing
```
Topic 89  pytest — Fixtures, Parametrize, Markers, and Best Practices
Topic 90  Mocking — unittest.mock, MagicMock, patch, monkeypatch
Topic 91  Test Strategy — Unit vs Integration vs E2E, Property-Based Testing with Hypothesis
```

### LEVEL 30 — Debugging & Profiling
```
Topic 92  Debugging — pdb, IDE Debugger, Stack Traces, Root Cause Analysis
Topic 93  Logging — structlog, Structured Logging, Log Levels, Production Logging
```

### LEVEL 31 — Code Quality & Clean Code
```
Topic 94  PEP 8, Ruff, Black, isort, mypy, Bandit — The Modern Python Toolchain
Topic 95  SOLID, DRY, KISS, YAGNI — Principles and When They Go Wrong
```

### LEVEL 32 — Design Patterns in Python
```
Topic 96  Creational Patterns — Factory, Builder, Singleton in Python
Topic 97  Structural + Behavioral Patterns — Adapter, Strategy, Observer, Command
```

### LEVEL 33 — Architecture
```
Topic 98  Clean Architecture and Hexagonal Architecture in Python
Topic 99  Repository Pattern, Service Layer, Dependency Injection
```

### LEVEL 34 — Backend Python — FastAPI
```
Topic 100  FastAPI — Routing, Pydantic, Dependency Injection, Middleware
Topic 101  FastAPI — Authentication, Authorization, Background Tasks, WebSockets
Topic 102  FastAPI Request Lifecycle — ASGI → Middleware → DI → Handler → DB
```

### LEVEL 35 — Databases & SQLAlchemy
```
Topic 103  SQLAlchemy — ORM, Core, Sessions, Transactions, Connection Pooling
Topic 104  Alembic — Database Migrations in Production
Topic 105  Redis in Python — Caching, Distributed Locks, Rate Limiting, Pub/Sub
```

### LEVEL 36 — Production Python
```
Topic 106  Configuration — Environment Variables, Secrets, pydantic-settings
Topic 107  Observability — Structured Logging, Prometheus Metrics, OpenTelemetry Tracing
Topic 108  Security — Input Validation, SQL Injection, Secrets, JWT, OAuth2
Topic 109  Docker, CI/CD, and Python Deployment — The Production Pipeline
Topic 110  Capstone Architecture — FastAPI + PostgreSQL + Redis + Kafka + AsyncIO
```

---

## Study Plans

### Quick Revision — Tonight (3 Hours)
```
Hour 1:
  Topic 5   — Variables are References (not boxes)
  Topic 15  — dict internals and hashing
  Topic 54  — Iterables vs Iterators
  Topic 55  — Generators and lazy evaluation

Hour 2:
  Topic 57  — Decorators from first principles
  Topic 75  — The GIL — what it actually does
  Topic 82  — AsyncIO from first principles
  Topic 72  — Reference counting and GC

Hour 3:
  Topic 51  — Exception handling strategies
  Topic 62  — Type hints in practice
  Topic 89  — pytest best practices
  Topic 95  — SOLID in Python
```

### Interview in 1 Week
```
Day 1:  Level 0–1  (Topics 1–7)    — Python model, variables, mutability
Day 2:  Level 2–3  (Topics 8–17)   — Data types and data structures
Day 3:  Level 5–6  (Topics 22–29)  — Functions (all of it)
Day 4:  Level 10–12 (Topics 38–47) — OOP and dunder methods
Day 5:  Level 15–17 (Topics 54–61) — Generators, decorators, context managers
Day 6:  Level 21–23 (Topics 69–76) — Internals, memory, GIL
Day 7:  Level 24–27 (Topics 77–86) — Concurrency, threading, asyncio
```

### Full Preparation (20 Weeks)
```
Week 1–2:    Level 0–4   (Fundamentals, Types, Data Structures, Control Flow)
Week 3–4:    Level 5–8   (Functions, Strings, Modules, Environments)
Week 5–6:    Level 10–13 (OOP Basic → Advanced, Dunders, Pythonic)
Week 7–8:    Level 14–17 (Exceptions, Iterators, Generators, Decorators)
Week 9–10:   Level 18–20 (Typing, Dataclasses, Functional Programming)
Week 11–12:  Level 21–23 (CPython Internals, Memory, GIL)
Week 13–14:  Level 24–27 (Threading, Multiprocessing, AsyncIO)
Week 15–16:  Level 28–31 (Performance, Testing, Debugging, Code Quality)
Week 17–18:  Level 32–33 (Design Patterns, Architecture)
Week 19–20:  Level 34–36 (FastAPI, Databases, Production Python)
```

---

## Topic Priority by Goal

### Python Interviews — FAANG / Product Company
```
★★★  Topic 5   — Variables are References
★★★  Topic 13  — list internals and complexity
★★★  Topic 15  — dict internals and hashing
★★★  Topic 54  — Iterables vs Iterators
★★★  Topic 55  — Generators and lazy evaluation
★★★  Topic 57  — Decorators from scratch
★★★  Topic 72  — Reference counting
★★★  Topic 75  — The GIL
★★★  Topic 82  — AsyncIO event loop
★★★  Topic 7   — Mutability and immutability
★★   Topic 27  — Closures
★★   Topic 46  — Dunder methods
★★   Topic 69  — CPython internals
```

### Backend / Django / FastAPI Developer
```
★★★  Topic 82  — AsyncIO foundations
★★★  Topic 100 — FastAPI in depth
★★★  Topic 103 — SQLAlchemy ORM
★★★  Topic 105 — Redis in Python
★★★  Topic 89  — pytest and testing strategy
★★★  Topic 107 — Structured logging and observability
★★★  Topic 62  — Type hints and Pydantic
★★★  Topic 98  — Clean architecture
★★   Topic 79  — ThreadPoolExecutor
★★   Topic 108 — Security in production
```

### Senior / Staff Engineer Level
```
★★★  Topic 69  — CPython internals
★★★  Topic 70  — Bytecode and the dis module
★★★  Topic 72  — Reference counting
★★★  Topic 73  — Cyclic GC
★★★  Topic 75  — GIL deep dive
★★★  Topic 76  — Free-threaded Python 3.13+
★★★  Topic 85  — AsyncIO internals
★★★  Topic 87  — Profiling and optimization workflow
★★★  Topic 98  — Architecture — Clean and Hexagonal
★★★  Topic 110 — Production capstone
```

---

## Key Concepts Cheat Sheet

### The 10 Questions to Ask Before Writing Python Code
```
1.  Is this data mutable or immutable? What are the aliasing implications?
2.  Will this work on large data? What is the time and memory complexity?
3.  Is this I/O-bound or CPU-bound? Which concurrency model should I use?
4.  Is this function doing one thing? (Single Responsibility)
5.  Will this break if it receives None, empty list, or unexpected type?
6.  Am I catching exceptions at the right level — or swallowing them silently?
7.  Is this code testable? Can I inject dependencies?
8.  If this fails in production, will I be able to diagnose it from logs alone?
9.  Does this need to be async? Or am I adding complexity unnecessarily?
10. How will this perform at 10x or 100x the current data size?
```

### Python Memory Model in One Diagram
```
Source Code (.py)
       |
    Parser
       |
      AST (Abstract Syntax Tree)
       |
   Compiler
       |
   Bytecode (.pyc / __pycache__)
       |
  Code Object (stored on disk)
       |
    Frame (created at call time)
       |
  Python VM executes bytecode
       |
  Objects on the Heap
  (reference counted, GC-managed)
```

### The Concurrency Decision Framework
```
WORKLOAD TYPE          BEST MODEL
─────────────────────────────────────────────────────
I/O-bound (many tasks) → asyncio (single thread, max throughput)
I/O-bound (simple)     → threading (simpler code, still works)
CPU-bound              → multiprocessing (bypass the GIL)
Mixed I/O + CPU        → asyncio for I/O + ProcessPoolExecutor for CPU
Background jobs        → Celery / RQ / Dramatiq + queue
```

### Mutability Quick Reference
```
IMMUTABLE (safe to share, hashable)
  int, float, bool, str, bytes, tuple, frozenset, None

MUTABLE (aliasing can cause bugs)
  list, dict, set, bytearray, most objects

RULE: If you pass a mutable object into a function,
      the function can change the original.
      Use .copy() or copy.deepcopy() to prevent this.
```

### When to Use What — Data Container Decision Table
```
NEED                                    USE
──────────────────────────────────────────────────────────────
Ordered, mutable sequence               list
Ordered, immutable, hashable sequence   tuple
Unique unordered items                  set
Fast key → value lookup                 dict
Immutable record with field names       NamedTuple or dataclass(frozen=True)
Mutable record with auto-methods        @dataclass
Data over an API / validation needed    Pydantic BaseModel
Dictionary with type hints (no methods) TypedDict
```

### The Python Concurrency Trap
```
❌ WRONG ASSUMPTION:
   "I'll use threading to speed up my CPU-heavy code."
   → The GIL means only one thread runs Python bytecode at a time.
   → CPU-bound threading is often SLOWER than single-threaded.

✅ CORRECT:
   CPU-bound  → multiprocessing (separate processes, no shared GIL)
   I/O-bound  → asyncio or threading (GIL released during I/O waits)
```

### The Generator vs List Decision
```
USE A LIST when:
  - You need random access (list[3])
  - You need len()
  - You will iterate multiple times
  - The data fits in memory

USE A GENERATOR when:
  - Data is large or infinite
  - You iterate once and discard
  - You are building processing pipelines
  - Memory efficiency matters
```

### Common Python Pitfalls — Quick Reference
```
PITFALL                           EXPLANATION
──────────────────────────────────────────────────────────
Mutable default argument          def f(x=[]) → shared across calls
Late binding closure              lambda i=i: i  needed in loops
`is` vs `==`                      is checks identity, == checks equality
Bare except:                      Catches SystemExit, KeyboardInterrupt too
Swallowing exceptions             except Exception: pass hides real bugs
Aliasing mutation                 b = a; b.append(1) changes a too
Blocking in async                 time.sleep() in async blocks event loop
N+1 queries                       Lazy-loading in a loop hits DB N times
Missing __repr__                  Hard to debug objects in logs
Comparing None with ==            Use `is None`, not `== None`
```

---

## Anti-Patterns to Mention in Every Interview

These show senior-level thinking. Mention what you are AVOIDING and why.

```
1.  Mutable default arguments
    → def func(items=[]) shares the list across all calls
    → Fix: def func(items=None): items = items or []

2.  Bare except: or except Exception: pass
    → Silently swallows bugs including KeyboardInterrupt
    → Always catch specific exceptions, always log

3.  Blocking code inside async functions
    → requests.get() or time.sleep() inside async def blocks the event loop
    → Use aiohttp / httpx for async HTTP, await asyncio.sleep() for delays

4.  Using is to compare values
    → `x is 256` may work due to interning; `x is 257` will not
    → Use == for value equality, is only for None/True/False/singletons

5.  Overusing classes
    → A class with one method and no state is just a function
    → Don't reach for OOP when a function solves the problem

6.  Using threads for CPU-bound work
    → The GIL prevents true parallelism for CPU tasks
    → Use multiprocessing or ProcessPoolExecutor instead

7.  No type hints in production code
    → Type hints enable mypy/pyright to catch bugs before runtime
    → They also serve as living documentation for your team

8.  Catching and re-raising without context
    → `raise SomeError()` loses the original traceback
    → Use `raise SomeError() from original_error` to preserve context

9.  Deep inheritance hierarchies
    → Hard to follow, hard to test, breaks easily
    → Prefer composition — build objects from smaller objects

10. Over-using global state
    → Shared global variables create hidden coupling and test nightmares
    → Pass dependencies explicitly or use dependency injection
```

---

## Interview Q&A — Most Asked Python Questions

### Conceptual (Verbal)
```
Q: What is the difference between is and ==?
A: == checks value equality — whether two objects have the same value.
   is checks identity — whether two variables point to the exact same
   object in memory (same id()). Use is only for None, True, False.
   Avoid `x is "hello"` — string interning is CPython implementation detail.

Q: What is the GIL and what problem does it solve?
A: The GIL (Global Interpreter Lock) is a mutex in CPython that ensures
   only one thread executes Python bytecode at a time. It exists to protect
   CPython's reference counting from race conditions in multithreaded code.
   It makes single-threaded Python simpler and C extension integration safer.
   The downside: CPU-bound threads cannot run in parallel. I/O-bound threads
   are mostly fine because the GIL is released during I/O waits.

Q: What is the difference between a generator and a list?
A: A list stores all values in memory at once. A generator computes values
   one at a time on demand (lazy evaluation) using yield. Generators use
   O(1) memory regardless of sequence length. You cannot index a generator
   or iterate it twice. Use generators for large or infinite sequences,
   lists when you need random access or multiple passes.

Q: How does Python's garbage collection work?
A: Primary mechanism: reference counting. Every object tracks how many
   references point to it. When count hits 0, memory is freed immediately.
   Problem: cyclic references (A → B → A) never reach 0. Solution: a
   cyclic garbage collector that periodically finds and breaks reference
   cycles. The gc module controls this. Use weakref for back-references
   that should not prevent collection.

Q: What are decorators and how do they work?
A: A decorator is a callable that takes a function and returns a new function.
   The @ syntax is shorthand: @timer above def f() is equivalent to f = timer(f).
   Decorators work because functions are first-class objects in Python — they
   can be passed as arguments and returned from other functions. Common uses:
   logging, caching (lru_cache), auth checks, retry logic, timing.
```

### Practical (Code)
```
Q: What does this code print?
   x = [1, 2, 3]
   y = x
   y.append(4)
   print(x)

A: [1, 2, 3, 4]. y = x does not copy the list — both variables point to
   the same object. Mutating y mutates the same object x refers to.
   To get independent copies: y = x.copy() (shallow) or copy.deepcopy(x).

Q: What is wrong with this function?
   def append_to(item, to=[]):
       to.append(item)
       return to

A: The default argument [] is evaluated ONCE at function definition time,
   not on each call. The same list is reused across all calls. So
   append_to(1) → [1], then append_to(2) → [1, 2]. Fix:
   def append_to(item, to=None):
       if to is None:
           to = []
       to.append(item)
       return to

Q: Design a rate limiter using Python + Redis
A: Key: rate:{user_id}, use Redis INCR + EXPIRE or sliding window with
   sorted sets. For token bucket: store (tokens, last_refill) in Redis hash.
   Use Lua script for atomicity — INCR + check in two separate commands
   has a race condition. Return 429 with Retry-After header on limit breach.
```

---

## Python Version Quick Reference

```
FEATURE                            INTRODUCED IN
──────────────────────────────────────────────────────────
f-strings                          Python 3.6
dict preserves insertion order     Python 3.7 (guaranteed)
walrus operator :=                 Python 3.8
positional-only params (/)         Python 3.8
match / case (pattern matching)    Python 3.10
Union type as X | Y                Python 3.10
tomllib (read TOML)                Python 3.11
Exception groups + except*         Python 3.11
@override decorator                Python 3.12
Free-threaded mode (no GIL opt-in) Python 3.13
```

---

## Mastery Levels — How to Self-Assess

```
0–20   Python Tourist
       Can write simple scripts. Doesn't know why things work.

21–40  Junior Python Developer
       Understands syntax, basic OOP, can write working programs.
       Struggles with closures, generators, debugging internals.

41–60  Intermediate Python Developer
       Comfortable with decorators, generators, basic async.
       Writes clean code, understands mutability and scope.
       Beginning to reason about performance and testing.

61–75  Strong Backend Python Developer
       Writes production-quality Python. Understands the GIL.
       Comfortable with FastAPI, SQLAlchemy, async patterns.
       Writes tests, understands architecture basics.

76–85  Senior Python Engineer
       Understands CPython internals, memory model, concurrency.
       Makes informed trade-off decisions. Reviews code with authority.
       Builds maintainable, testable, observable systems.

86–95  Staff-Level Python Engineer
       Thinks in systems, not just code. Designs architecture.
       Understands Python performance limits. Knows when NOT to use Python.
       Mentors others. Evaluates technical decisions at org level.

96–100 Principal Python Engineer / Python Expert
       Deep CPython understanding. Can contribute to Python itself.
       Designs production platforms. Thinks in trade-offs, failure modes,
       and long-term maintainability at scale.
```

**Note:** A high score is not awarded for writing syntactically correct Python.
Assessment covers:
```
Understanding + Internals + Problem Solving + Code Quality
+ Architecture + Performance + Production Judgment
```

---

## The Python Execution Model — Full Diagram
```
.py Source File
       |
    Lexer (tokenizes source)
       |
    Parser (builds parse tree)
       |
    AST — Abstract Syntax Tree
       |
    Compiler (ast → bytecode)
       |
    Code Object (.pyc / __pycache__)
       |
  Frame Object (created per function call)
  ├── f_code      → the Code Object
  ├── f_locals    → local variable namespace
  ├── f_globals   → module global namespace
  ├── f_builtins  → built-in names
  └── f_back      → previous frame (call stack)
       |
  CPython PVM (evaluates bytecode)
  (ceval.c — the heart of CPython)
       |
  Objects on the Heap
  (PyObject — every value is an object)
  ├── ob_refcnt  → reference count
  └── ob_type    → pointer to type object
```

---

## The AsyncIO Execution Model
```
async def handler():
    result = await database_call()
    return result

                    EVENT LOOP
                    ──────────
  coroutine starts executing
         |
  hits `await database_call()`
         |
  suspends coroutine (yields control to event loop)
         |
  event loop registers I/O wait with OS (epoll/kqueue)
         |
  event loop picks up another ready coroutine and runs it
         |
  OS signals I/O is ready
         |
  event loop resumes the suspended coroutine
         |
  result is available, execution continues
```

---

## The Testing Pyramid for Python
```
         /\
        /  \
       / E2E \        ← Few, slow, test full system behavior
      /────────\
     /          \
    / Integration \   ← Some, test component interactions
   /──────────────\   (DB, Redis, real HTTP)
  /                \
 /   Unit Tests     \ ← Many, fast, test functions/classes in isolation
/────────────────────\
```

---

*110 topics · 36 levels · Complete Python 0 → 100 path*
*Built for developers targeting beginner → principal-level Python mastery*
