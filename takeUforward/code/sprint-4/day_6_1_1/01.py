# Q1. Library Book Management System (Practice - Encapsulation)
#
# Task:
# You are tasked to design a class Book to manage the book details in a library.
# The class should contain the following specifications:
#
# Attributes:
# - title (list[str]) : The title of the book (public).
# - author (list[str]) : The author of the book (public).
# - __isAvailable (list[bool]) : The availability status of the book (private).
#
# Methods:
# - __init__(self, title, author, isAvailable):
#     Parameterized constructor to initialize the title, author, isAvailable lists.
# - borrowBook(self, bookName: str):
#     If the availability status for book 'bookName' is True, borrow the book and mark status as False.
#     If availability status is False, print "Book is not available.".
#     If book does not exist, print "Book not found.".
# - returnBook(self, bookName: str):
#     The book with bookName is returned and should be marked as available by setting its available flag to True.
# - getAvailability(self, bookName: str):
#     Prints the availability status of the book with name 'bookName' (True for available, False for unavailable).
#
# Operation Codes:
# "1 <bookName>" - borrowBook(bookName)
# "2 <bookName>" - returnBook(bookName)
# "3 <bookName>" - getAvailability(bookName)
#
# Example 1:
# Input:
# title = ["Sherlock_Holmes", "Frankenstein", "King_Arthur", "Treasure_Island"]
# author = ["Arthur_Conan_Doyle", "Mary_Shelley", "Roger_Lancelyn_Green", "Robert_Louis_Stevenson"]
# isAvailable = [False, True, False, False]
# methodCalls = [["1", "Frankenstein"], ["1", "Sherlock_Holmes"], ["2", "King_Arthur"], ["3", "Sherlock_Holmes"], ["1", "Frankenstein"]]
# Output:
# Book is not available.
# False
# Book is not available.
#
# Example 2:
# Input:
# title = ["1984", "Animal_Farm"]
# author = ["George_Orwell", "George_Orwell"]
# isAvailable = [True, True]
# methodCalls = [["1", "1984"], ["3", "1984"], ["2", "1984"], ["3", "1984"]]
# Output:
# False
# True
#
# Example 3 (Edge Case):
# Input:
# title = ["Hamlet"]
# author = ["Shakespeare"]
# isAvailable = [False]
# methodCalls = [["1", "Macbeth"], ["3", "Macbeth"]]  # Book not in catalog
# Output:
# Book not found.
# Book not found.
#
# Think About:
# - Private attribute `__isAvailable` prevents direct external modification without borrowing/returning checks.
# - Use `self.title.index(bookName)` to find the index of the book. Handle ValueError gracefully.
# - Time Complexity: O(N) per operation where N is the catalog size.
# - Space Complexity: O(1) auxiliary space.

# Write your Book class below:

class Book:
    def __init__(self, title: list, author: list, isAvailable: list):
        # Write your code here
        pass

    def borrowBook(self, bookName: str):
        # Write your code here
        pass

    def returnBook(self, bookName: str):
        # Write your code here
        pass

    def getAvailability(self, bookName: str):
        # Write your code here
        pass
