# Class Variable vs Instance Variable Trap
# Create a class Employee with a CLASS-LEVEL list `skills = []`.
# Create two objects a and b, append "Python" to a.skills, and observe that
# b.skills ALSO contains "Python" (because class variables are shared).
# Fix the problem by initializing self.skills = [] inside __init__.
#
# Example (Before Fix):
# Input:
#   a = Employee("A", 1)
#   b = Employee("B", 2)
#   a.skills.append("Python")
# Output: b.skills == ["Python"]   # SHARED — both see the same list!
#
# Example (After Fix):
# Input:
#   a = Employee("A", 1)
#   b = Employee("B", 2)
#   a.skills.append("Python")
# Output: b.skills == []            # INDEPENDENT — each has its own list
#

# Write your solution below:

class Employee :
    def __init__(self , name , id) -> None:
        self.name = name
        self.id = id
        self.skills = []


a = Employee("A", 1)
b = Employee("B", 2)
a.skills.append("Python")
print(b.skills)
print(a.skills)