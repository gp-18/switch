# 🟢 LEVEL 1 — Constructor Basics & Initialization

## 1. Default Constructor vs Custom `__init__`

Create a class `Employee` with no `__init__` (`pass`), make an object `e`, and try to read `e.salary` — observe the `AttributeError`. Then write a custom `__init__` that takes no extra arguments and sets `id = 0`, `salary = 0.0`, and `name = None` as default instance attributes.

### Example

```text
Input:  e = Employee()
Output: e.id == 0, e.salary == 0.0, e.name == None
```

### Think About

* What does Python provide when you write no `__init__` at all?
* Instance attributes only exist after you explicitly assign them with `self.attribute = value` inside `__init__`.
* A default constructor ensures every object starts in a known, valid state.

**File:** `01.py`

---

## 2. Parameterized Constructor with Validation

Write a class `Employee` whose `__init__(self, name, salary)` stores both attributes. Inside the constructor, validate the inputs: raise a `ValueError` if `name` is empty, and raise a `ValueError` if `salary` is negative. The constructor should guarantee a valid object from the very first line.

### Example

```text
Input:  e = Employee("Raj", 10000)
Output: e.name == "Raj", e.salary == 10000

Input:  Employee("", 100)
Output: ValueError

Input:  Employee("Raj", -1)
Output: ValueError
```

### Think About

* Why is the constructor the ideal place to validate inputs? (Hint: no invalid object should ever exist.)
* Use `if not name:` to check for empty strings and `if salary < 0:` for negative values.
* `raise ValueError("message")` stops object creation immediately.

**File:** `02.py`

---

## 3. `__new__` vs `__init__` — Object Creation vs Initialization

Explore the two-phase object construction in Python. First, add `return 5` inside `__init__` and observe the `TypeError`. Then write a class `Demo` with both `__new__` and `__init__`, each printing when it runs. Observe the execution order and write comments explaining which one creates the object and which one initialises it.

### Example

```text
Input:  Demo()
Output:
  __new__ called
  __init__ called
```

### Think About

* `__new__` is a static method that **creates** and returns the new instance. It receives `cls` (the class itself).
* `__init__` is an instance method that **initialises** the already-created instance. It receives `self`.
* `__init__` must return `None`. Returning anything else raises `TypeError`.
* `__new__` runs first, `__init__` runs second — only if `__new__` returns an instance of the class.

**File:** `03.py`

---

# 🟢 LEVEL 2 — Common Traps & Pitfalls

## 4. Class Variable vs Instance Variable Trap

Create a class `Employee` with a **class-level** list `skills = []`. Create two objects `a` and `b`, append `"Python"` to `a.skills`, and observe that `b.skills` also contains `"Python"` (because class variables are shared). Fix the problem by initializing `self.skills = []` inside `__init__` so that each object gets its own independent list.

### Example

```text
Input:
  a = Employee("A", 1)
  b = Employee("B", 2)
  a.skills.append("Python")
Output (before fix): b.skills == ["Python"]   # Shared!
Output (after fix):  b.skills == []            # Independent
```

### Think About

* Class variables are shared across all instances — they live on the class object itself, not on `self`.
* Instance variables are created per object inside `__init__` using `self.variable = value`.
* To verify: check `id(a.skills) == id(b.skills)` before and after your fix.

**File:** `04.py`

---

## 5. Mutable Default Argument Trap

Write `__init__(self, name, skills=[])` and create two objects without passing `skills`. Append `"Python"` to the first object's skills and observe that the second object also has `"Python"`. Fix the bug using the `None` sentinel pattern: `skills=None` with `self.skills = skills if skills is not None else []`.

### Example

```text
Input:
  a = Employee("A")
  b = Employee("B")
  a.skills.append("Python")
Output (before fix): b.skills == ["Python"]  # Shared default list!
Output (after fix):  b.skills == []           # Independent
```

### Think About

* Default argument values in Python are evaluated **once** — at function definition time, not at each call.
* A mutable default (like `[]` or `{}`) is shared across all calls that don't provide an explicit argument.
* The idiomatic fix: use `None` as the default and create a fresh object inside the function body.

**File:** `05.py`

---

# 🟡 LEVEL 3 — Copying & Cloning Objects

## 6. Copy Constructor — Shallow vs Deep Copy

Add a `@classmethod` called `from_employee(cls, other)` that creates a new `Employee` with the same data as `other`. Then use `copy.copy` (shallow copy) and `copy.deepcopy` (deep copy) on an `Employee` that has a `skills` list. Observe which copy shares the inner list and which one is fully independent.

### Example

```text
Input:
  e1 = Employee("Raj", 10000)
  e1.skills.append("Python")
  e2 = copy.copy(e1);     e2.skills.append("SQL")
  e3 = copy.deepcopy(e1); e3.skills.append("Go")
Output:
  e1.skills == ["Python", "SQL"]   # shallow copy shares the inner list
  "Go" not in e1.skills            # deep copy is fully independent
```

### Think About

* `copy.copy()` creates a new object but **does not** recursively copy nested mutable objects — they remain shared references.
* `copy.deepcopy()` recursively copies everything, creating a fully independent clone.
* A `@classmethod` copy constructor gives you explicit control over how the new object is built.
* Use `id()` to verify whether two objects share the same inner list.

**File:** `06.py`

---

# 🟡 LEVEL 4 — Constructor Overloading & Factory Methods

## 7. Simulating Constructor Overloading

Python only allows **one** `__init__`. Simulate overloading by writing a single `__init__` that supports all of these calling patterns: `Employee()`, `Employee("Raj", 10000)`, and `Employee("Amit", 12000, "Python", "SQL", department="IT")`. Use default parameter values, `*args` for variable skills, and `**kwargs` for optional keyword arguments like `department`.

### Example

```text
Input:
  e1 = Employee()
  e2 = Employee("Raj", 10000)
  e3 = Employee("Amit", 12000, "Python", "SQL", department="IT")
Output:
  e1.name == "Unknown"
  e2.salary == 10000
  e3.skills == ["Python", "SQL"], e3.department == "IT"
```

### Think About

* Use `name="Unknown"` and `salary=0` as defaults so `Employee()` works without arguments.
* Use `*args` to capture any number of positional skill arguments after `salary`.
* Use `**kwargs` to capture keyword arguments like `department` and store them as attributes using `setattr(self, key, value)` or manual assignment.
* This is the Pythonic way to handle "multiple constructors" without language-level overloading.

**File:** `07.py`

---

## 8. Alternative Constructors with `@classmethod`

Add three `@classmethod` factory methods to `Employee`: `from_string("Neha, 15000")` that parses a comma-separated string, `from_dict({"name": "Raj", "salary": 100})` that builds from a dictionary, and `intern("Riya")` that creates an employee with salary `0`. All factory methods must return an instance through `cls(...)` (not hardcoded `Employee(...)`) so that subclasses inherit them correctly.

### Example

```text
Input:
  e1 = Employee.from_string("Neha, 15000")
  e2 = Employee.from_dict({"name": "Raj", "salary": 100})
  e3 = Employee.intern("Riya")
Output:
  e1.name == "Neha", e1.salary == 15000
  e2.name == "Raj",  e2.salary == 100
  e3.name == "Riya", e3.salary == 0
```

### Think About

* `@classmethod` receives `cls` as its first argument — it refers to the class the method is called on, not a fixed class.
* Using `cls(...)` instead of `Employee(...)` ensures subclasses that inherit these factory methods will create instances of the subclass, not the parent.
* Parse strings with `split(",")` and `strip()`. Unpack dicts with `cls(**data)` or manual key access.

**File:** `08.py`

---

# 🟠 LEVEL 5 — Inheritance & Constructor Chaining

## 9. Constructor Chaining with `super().__init__()`

Build a three-level inheritance hierarchy: `Person(name, age)`, `Student(Person)` that adds `roll_no`, and `GraduateStudent(Student)` that adds `thesis`. Each child class must call `super().__init__(...)` to chain the parent's constructor. After verifying it works, deliberately remove the `super().__init__(...)` call from `Student.__init__` and observe the resulting `AttributeError` when accessing `name` on a `GraduateStudent` instance.

### Example

```text
Input:  g = GraduateStudent("Rahul", 22, 101, "AI Safety")
Output: g.name == "Rahul", g.age == 22, g.roll_no == 101, g.thesis == "AI Safety"
```

### Think About

* A child's `__init__` completely **replaces** (does not extend) the parent's `__init__` unless you explicitly call `super().__init__(...)`.
* Without the `super()` call, the parent's attributes (`name`, `age`) are never assigned, causing `AttributeError`.
* `super()` returns a proxy object that delegates method calls to the next class in the MRO (Method Resolution Order).
* Always pass the required arguments up the chain: `super().__init__(name, age)`.

**File:** `09.py`

---

## 10. Multiple Inheritance, Diamond Problem & MRO

Build a diamond inheritance structure: `A` (base), `B(A)`, `C(A)`, and `D(B, C)`. Each class's `__init__` should print its own name and then call `super().__init__()`. Instantiate `D()` and observe the print order. Then print `D.__mro__` to see the Method Resolution Order. Before running, predict the order in a comment.

### Example

```text
Input:  D()
Output:
  D.__init__ called
  B.__init__ called
  C.__init__ called
  A.__init__ called

Input:  print(D.__mro__)
Output: (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

### Think About

* Python uses the **C3 linearization algorithm** to compute the MRO, ensuring each parent's `__init__` is called exactly once.
* `super()` doesn't always call the direct parent — it calls the next class in the MRO chain.
* In a diamond, without `super()`, `A.__init__` could run twice (once from `B` and once from `C`). With `super()`, it runs exactly once.
* Try swapping `D(B, C)` to `D(C, B)` and observe how the MRO and print order change.

**File:** `10.py`

---

## 11. Cooperative Multiple Inheritance with `**kwargs`

In multiple inheritance, different parent classes often require different constructor arguments. If any class in the MRO doesn't forward remaining arguments or hardcodes parameters, the chain breaks. Solve this using **cooperative multiple inheritance**:
* `Base`: `__init__(self, **kwargs)` that calls `super().__init__()`.
* `NamedEntity(Base)`: accepts `name` (default `"Unknown"`), sets `self.name = name`, and forwards remaining `kwargs` to `super().__init__(**kwargs)`.
* `TimestampedEntity(Base)`: accepts `created_at` (default `None`), sets `self.created_at = created_at`, and forwards remaining `kwargs` to `super().__init__(**kwargs)`.
* `User(NamedEntity, TimestampedEntity)`: accepts `role` (default `"Member"`), sets `self.role = role`, and forwards remaining `kwargs` to `super().__init__(**kwargs)`.

### Example

```text
Input:  u = User(name="Alice", created_at="2026-01-01", role="Admin")
Output: u.name == "Alice", u.created_at == "2026-01-01", u.role == "Admin"
```

### Think About

* In an MRO chain, you don't always know which class comes next at runtime.
* Using `**kwargs` allows each class to extract ("consume") only the parameters it needs and forward the rest via `super().__init__(**kwargs)`.
* The final base class before `object` terminates the kwargs forwarding to prevent `TypeError: object.__init__() takes exactly one argument`.
* This is the standard pattern recommended by Python core developer Raymond Hettinger for cooperative multiple inheritance.

**File:** `11.py`

---

## 12. Mixin Classes with Constructor Chaining

Mixins provide composable, reusable functionality across unrelated classes without forming a strict "is-a" taxonomy. A mixin should never be instantiated on its own, but its constructor must cooperate with the host class.
Create:
* `AuditMixin`: its `__init__` extracts `created_by` (default `"system"`), sets `self.created_by`, and chains `super().__init__(*args, **kwargs)`.
* `TagMixin`: its `__init__` extracts `tags` (default `None` -> empty list), sets `self.tags`, and chains `super().__init__(*args, **kwargs)`.
* `Document(AuditMixin, TagMixin)`: accepts `title` and `content`, sets `self.title = title`, `self.content = content`, and chains `super().__init__(**kwargs)`.

### Example

```text
Input:
  doc = Document(title="SRS", content="Specs...", created_by="Raj", tags=["v1", "draft"])
Output:
  doc.title == "SRS"
  doc.content == "Specs..."
  doc.created_by == "Raj"
  doc.tags == ["v1", "draft"]
```

### Think About

* Mixins are designed for horizontal feature sharing rather than vertical hierarchical taxonomy.
* A mixin's `__init__` should always call `super().__init__(*args, **kwargs)` so the next class in the MRO is not bypassed.
* Order in class definition matters: `class Document(AuditMixin, TagMixin)` places `AuditMixin` before `TagMixin` in `Document.__mro__`.

**File:** `12.py`

---

# 🔴 LEVEL 6 — Advanced Construction & Architecture Patterns

## 13. Abstract Base Class (`ABC`) with Constructor Invariants

Can an abstract class have an `__init__`? Yes! In fact, it is the best place to define common invariant state and enforce validation for all subclasses.
Create:
* An abstract class `PaymentProcessor(ABC)` with `__init__(self, api_key: str, currency: str = "USD")`. It validates that `api_key` is a non-empty string; if not, raise `ValueError("API key cannot be empty")`. It also declares `@abstractmethod def process_payment(self, amount: float) -> str`.
* Subclass `StripeProcessor(PaymentProcessor)`: `__init__` takes `api_key`, `currency`, and `webhook_secret`. It chains to `super().__init__(api_key, currency)`, sets `self.webhook_secret`, and implements `process_payment(amount)`.
* Subclass `PayPalProcessor(PaymentProcessor)`: `__init__` takes `api_key`, `currency`, and `client_id`. It chains to `super().__init__(api_key, currency)`, sets `self.client_id`, and implements `process_payment(amount)`.

### Example

```text
Input:  s = StripeProcessor("sk_test_123", "USD", "whsec_abc")
Output: s.api_key == "sk_test_123", s.currency == "USD", s.webhook_secret == "whsec_abc"

Input:  PaymentProcessor("key")
Output: TypeError: Can't instantiate abstract class PaymentProcessor with abstract method process_payment
```

### Think About

* An abstract class cannot be instantiated directly if it has at least one `@abstractmethod`.
* Subclasses **must** call `super().__init__(...)` to ensure the base state (`api_key`, `currency`) is properly initialized and validated.
* If a subclass forgets to implement any `@abstractmethod`, Python refuses to instantiate it at runtime.

**File:** `13.py`

---

## 14. Dataclass Inheritance & `__post_init__` Constructor Chaining

Modern Python uses `@dataclass` from the `dataclasses` module to auto-generate `__init__`. When inheriting dataclasses, Python orders parameters from base class to child class. Use `__post_init__` for custom validation and computed attributes:
* `@dataclass class Account`: fields `account_id: str`, `holder_name: str`, `balance: float = 0.0`.
  Inside `__post_init__(self)`: validate `balance >= 0`; if negative, raise `ValueError("Balance cannot be negative")`.
* `@dataclass class PremiumAccount(Account)`: adds `cashback_rate: float = 0.01` and `reward_points: int = 0`.
  Inside `__post_init__(self)`: MUST call `super().__post_init__()` to trigger the parent validation, and calculate `self.reward_points = int(self.balance * 0.1)`.

### Example

```text
Input:  p = PremiumAccount("A1", "Raj", balance=500.0, cashback_rate=0.02)
Output: p.account_id == "A1", p.balance == 500.0, p.reward_points == 50

Input:  PremiumAccount("A2", "Simran", balance=-50.0)
Output: ValueError: Balance cannot be negative
```

### Think About

* `@dataclass` automatically synthesizes `__init__` by combining base class fields and subclass fields.
* `__post_init__` runs immediately after the generated `__init__` completes.
* In child dataclasses, always call `super().__post_init__()` if the base dataclass defined `__post_init__`, otherwise base validation/computations are skipped!
* Notice field ordering rules in dataclasses: fields with default values cannot precede fields without default values.

**File:** `14.py`

---

## 15. Singleton Pattern via Controlled Construction (`__new__` + `__init__` Guard)

Implement a robust Singleton pattern for a `DatabaseConnection` class where only **one** instance can ever exist across the application:
1. Override `__new__(cls, *args, **kwargs)`: maintain a class variable `_instance = None`. If `_instance` is `None`, create it using `super().__new__(cls)` and store it. Otherwise, return the existing `_instance`.
2. Python automatically calls `__init__` every time `DatabaseConnection(...)` is invoked, even if `__new__` returned an existing instance! Guard against overwriting state by using an `_initialized` attribute on the instance: only initialize `db_name` and `host` the first time.
3. Test that two constructor calls return the exact same object (`db1 is db2`) and that subsequent calls do not overwrite existing connection settings.

### Example

```text
Input:
  db1 = DatabaseConnection("prod_db", "10.0.0.1")
  db2 = DatabaseConnection("dev_db", "localhost")
Output:
  db1 is db2 == True
  db2.db_name == "prod_db"
  db2.host == "10.0.0.1"
```

### Think About

* `__new__` controls **creation** of the instance (returning an existing one).
* `__init__` controls **initialization** of the instance — Python calls it unconditionally whenever `__new__` returns an instance of that class.
* Without an `if not hasattr(self, "_initialized"):` or `self._is_initialized` guard inside `__init__`, every subsequent "instantiation" would wipe out the singleton's attributes!
* Check identity with `is` keyword (`id(db1) == id(db2)`).

**File:** `15.py`