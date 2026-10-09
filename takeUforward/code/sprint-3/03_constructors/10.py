# Multiple Inheritance, Diamond Problem & MRO
# Build a diamond inheritance structure: A (base), B(A), C(A), and D(B, C).
# Each class's __init__ should print its own name and then call super().__init__().
# Instantiate D() and observe the print order.
# Then print D.__mro__ to see the Method Resolution Order.
# Before running, predict the order in a comment.
#
# Example 1:
# Input:  D()
# Output:
#   D.__init__ called
#   B.__init__ called
#   C.__init__ called
#   A.__init__ called
#
# Example 2:
# Input:  print(D.__mro__)
# Output: (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
#

# Write your solution below:

# Predicted order:
# D -> B -> C -> A
# Python follows the MRO when super().__init__() is called.

class A:
    def __init__(self):
        print("A.__init__ called")
        super().__init__()


class B(A):
    def __init__(self):
        print("B.__init__ called")
        super().__init__()


class C(A):
    def __init__(self):
        print("C.__init__ called")
        super().__init__()


class D(B, C):
    def __init__(self):
        print("D.__init__ called")
        super().__init__()


D()

print(D.__mro__)