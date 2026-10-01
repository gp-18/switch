# ============================================================
# Problem: Book Information
# Difficulty: Easy
# ============================================================
#
# PROBLEM STATEMENT:
# Create a Book class with title, author, and price attributes.
# Add a get_details() method that returns the book details in
# readable format: "<title> by <author>: <price>".
# If price is negative, return "Invalid Price".
# Implement solution() to create a Book and return its details.
#
# INPUT:
# - title: string
# - author: string
# - price: integer
#
# OUTPUT:
# - Details string or "Invalid Price"
#
# EXAMPLE:
# Input:  ("Python Basics", "Rahul", 499)
# Output: "Python Basics by Rahul: 499"
#
# CONSTRAINTS:
# - title and author are non-empty strings
# ============================================================

class Book:
    def __init__(self, title, author, price):
        pass

    def get_details(self):
        pass


def solution(title, author, price):
    # Create Book and return details
    pass


# ---- TEST CASES ----
assert solution("Python Basics", "Rahul", 499) == "Python Basics by Rahul: 499", "Test 1 Failed"
assert solution("Data Structures", "Asha", 750) == "Data Structures by Asha: 750", "Test 2 Failed"
assert solution("Invalid Book", "Unknown", -50) == "Invalid Price", "Test 3 Failed"
assert solution("Free Guide", "Admin", 0) == "Free Guide by Admin: 0", "Test 4 Failed"

print("All test cases passed!")
