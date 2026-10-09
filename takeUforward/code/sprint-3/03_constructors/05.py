# Mutable Default Argument Trap
# Write __init__(self, name, skills=[]) and create two objects WITHOUT passing skills.
# Append "Python" to the first object's skills and observe that the second object
# ALSO has "Python" — because the default list is shared across all calls.
# Fix it with the None sentinel pattern:
#   skills=None, then self.skills = skills if skills is not None else []
#
# Example (Before Fix):
# Input:
#   a = Employee("A")
#   b = Employee("B")
#   a.skills.append("Python")
# Output: b.skills == ["Python"]   # Shared default list!
#
# Example (After Fix):
# Input:
#   a = Employee("A")
#   b = Employee("B")
#   a.skills.append("Python")
# Output: b.skills == []            # Independent
#

# Write your solution below:

class Employee :
    def __init__(self , name , id , skills = None) -> None:
        self.name = name
        self.id = id
        if skills is None :
            self.skills = []
        else :
            self.skills = skills


a = Employee("A", 1)
b = Employee("B", 2)
a.skills.append("Python")
print(b.skills)
print(a.skills)