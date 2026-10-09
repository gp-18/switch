# __new__ vs __init__ — Object Creation vs Initialization
# Explore the two-phase object construction in Python.
# 1. First, add `return 5` inside __init__ and observe the TypeError.
# 2. Then write a class Demo with both __new__ and __init__, each printing when it runs.
# 3. Observe the execution order and write comments explaining which one creates
#    the object and which one initialises it.
#
# Example:
# Input:  Demo()
# Output:
#   __new__ called
#   __init__ called
#
# Key Point:
# __new__ CREATES the object (receives cls), __init__ INITIALISES it (receives self).
# __init__ must return None. Returning anything else raises TypeError.
#

# Write your solution below:


class Demo:
    def __new__(cls):
        print("__new__ called")
        return super().__new__(cls)

    def __init__(self):
        print("__init__ called")


d = Demo()