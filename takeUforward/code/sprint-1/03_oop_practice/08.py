# ============================================================
# Problem: Library Borrowing System
# Difficulty: Medium
# ============================================================
#
# PROBLEM STATEMENT:
# Create a Book class with title and availability status.
# Create a Library class that manages multiple books with methods
# to add, borrow, and return books.
# - A book can only be borrowed if currently available.
# - A book can only be returned if currently borrowed.
# Implement solution() returning status messages for borrow/return ops.
#
# INPUT:
# - operations: list of tuples (action, book_title)
#   where action is "add", "borrow", or "return"
#
# OUTPUT:
# - List of status strings for borrow/return operations
#
# EXAMPLE:
# Input:  [("add", "Python"), ("add", "Django"), ("borrow", "Python"), ("borrow", "Python"), ("return", "Python")]
# Output: ["Python: borrowed", "Python: unavailable", "Python: returned"]
#
# CONSTRAINTS:
# - book titles are non-empty strings
# ============================================================

class Book:
    def __init__(self, title):
        pass

    def borrow(self):
        pass

    def return_book(self):
        pass


class Library:
    def __init__(self):
        pass

    def add_book(self, title):
        pass

    def borrow_book(self, title):
        pass

    def return_book(self, title):
        pass


def solution(operations):
    # Process library operations and return status list
    pass


# ---- TEST CASES ----
assert solution([
    ("add", "Python"),
    ("add", "Django"),
    ("borrow", "Python"),
    ("borrow", "Python"),
    ("return", "Python")
]) == [
    "Python: borrowed",
    "Python: unavailable",
    "Python: returned"
], "Test 1 Failed"

assert solution([
    ("add", "Flask"),
    ("borrow", "FastAPI"),
    ("borrow", "Flask"),
    ("return", "Flask"),
    ("borrow", "Flask")
]) == [
    "FastAPI: unavailable",
    "Flask: borrowed",
    "Flask: returned",
    "Flask: borrowed"
], "Test 2 Failed"

print("All test cases passed!")
