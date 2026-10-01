# PRACTICE PROBLEMS

Solve these using Python. No solutions or hints are included.

## 🟢 Problem 1 — Easy

**Title:** Student Profile

**Difficulty:** Easy

### Problem

Create a `Student` class with `name` and `marks` attributes. Add a method that returns `"Pass"` if marks are at least 40; otherwise, return `"Fail"`.

**Input:** A student's name and integer marks.

**Output:** The student's name and result.

### Example

```text
Input:
Asha
75

Output:
Asha: Pass
```

---

## 🟢 Problem 2 — Easy

**Title:** Bank Account Operations

**Difficulty:** Easy

### Problem

Create a `BankAccount` class initialized with an account holder and starting balance. Implement `deposit(amount)` and `withdraw(amount)` methods. Reject non-positive amounts and withdrawals greater than the available balance.

**Input:** Starting balance followed by a sequence of deposit or withdrawal operations.

**Output:** The final balance after valid operations.

### Example

```text
Input:
1000
deposit 500
withdraw 200
withdraw 2000

Output:
1300
```

---

## 🟢 Problem 3 — Easy

**Title:** Book Information

**Difficulty:** Easy

### Problem

Create a `Book` class with `title`, `author`, and `price` attributes. Add a method that returns the book details in a readable format. If the price is negative, treat it as invalid.

**Input:** A book title, author, and price.

**Output:** The book details or an invalid price message.

### Example

```text
Input:
Python Basics
Rahul
499

Output:
Python Basics by Rahul: 499
```

---

## 🟢 Problem 4 — Easy

**Title:** Rectangle Calculator

**Difficulty:** Easy

### Problem

Create a `Rectangle` class with `length` and `width` attributes. Implement methods to calculate the area and perimeter of the rectangle. Reject non-positive dimensions.

**Input:** Length and width.

**Output:** The area and perimeter.

### Example

```text
Input:
10
5

Output:
Area: 50
Perimeter: 30
```

---

## 🟢 Problem 5 — Easy

**Title:** Temperature Converter

**Difficulty:** Easy

### Problem

Create a `Temperature` class with a Celsius value. Add methods to convert the temperature to Fahrenheit and Kelvin.

Use:
- Fahrenheit = `(Celsius × 9/5) + 32`
- Kelvin = `Celsius + 273.15`

**Input:** Temperature in Celsius.

**Output:** Temperature in Fahrenheit and Kelvin, rounded to two decimal places.

### Example

```text
Input:
25

Output:
Fahrenheit: 77.00
Kelvin: 298.15
```

---

## 🟡 Problem 6 — Medium

**Title:** Employee Salary Management

**Difficulty:** Medium

### Problem

Create an `Employee` class with a name and salary. Create a `Manager` class that inherits from `Employee` and adds a bonus. Implement a method that returns the total compensation for each employee type.

**Input:** An employee's name and salary, followed by a manager's name, salary, and bonus.

**Output:** Total compensation for both people.

### Example

```text
Input:
Asha 50000
Raj 70000 10000

Output:
Asha: 50000
Raj: 80000
```

---

## 🟡 Problem 7 — Medium

**Title:** Shape Area Calculator

**Difficulty:** Medium

### Problem

Create a common `Shape` interface or base class with an `area()` method. Implement `Rectangle` and `Circle` so each calculates its own area. Process a list of shapes and return their areas in input order.

**Input:** Shape types and their dimensions; use `π = 3.14`.

**Output:** The area of each shape, rounded to two decimal places.

### Example

```text
Input:
rectangle 4 5
circle 2

Output:
20.00
12.56
```

---

## 🟡 Problem 8 — Medium

**Title:** Library Borrowing System

**Difficulty:** Medium

### Problem

Create a `Book` class with a title and availability status. Create a `Library` class that manages multiple books. Implement methods to add a book, borrow a book, and return a book.

A book can only be borrowed if it is currently available. A book can only be returned if it is currently borrowed.

**Input:** A sequence of library operations.

**Output:** The result of each operation and the final availability of the requested books.

### Example

```text
Input:
add Python
add Django
borrow Python
borrow Python
return Python

Output:
Python: borrowed
Python: unavailable
Python: returned
```

---

## 🔴 Problem 9 — Hard

**Title:** Payment Processing System

**Difficulty:** Hard

### Problem

Design a payment system with a common payment interface and separate `CardPayment`, `UPIPayment`, and `WalletPayment` implementations. Each payment must validate its amount, reject invalid payments, and return a status. Process multiple payments through the same interface without checking each concrete payment type.

**Input:** A sequence of payment types and amounts, with any required test balance or validity data defined by your implementation.

**Output:** A success or failure status for each payment, in input order.

### Example

```text
Input:
card 500
upi 0
wallet 250

Output:
card: success
upi: failure
wallet: success
```

---

## 🔴 Problem 10 — Hard

**Title:** Notification System

**Difficulty:** Hard

### Problem

Design a notification system with a common notification interface and separate `EmailNotification`, `SMSNotification`, and `PushNotification` implementations.

Each notification type should validate its required data and provide a `send()` method. Process multiple notifications through the same interface without checking each concrete notification type.

For example, an email requires a valid email address, an SMS requires a phone number, and a push notification requires a device token.

**Input:** A sequence of notification types and their required data.

**Output:** A success or failure status for each notification, in input order.

### Example

```text
Input:
email user@example.com
sms 9876543210
push device123

Output:
email: success
sms: success
push: success
```

---

## General Instructions

For Problems 1–10, define your own class design where the statement leaves implementation details open. Preserve the required behavior and output.

Focus on practicing:

- Classes and objects
- Constructors
- Instance attributes
- Instance methods
- Encapsulation
- Inheritance
- Method overriding
- Polymorphism
- Common interfaces/base classes
- Processing multiple objects through a common interface
