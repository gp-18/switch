# Default Constructor vs Custom __init__
# Create a class Employee with no __init__ (pass), make an object, and try to read e.salary
# (observe AttributeError). Then write a custom __init__ that takes no extra arguments
# and sets id = 0, salary = 0.0, name = None as default instance attributes.
#
# Example 1:
# Input:  e = Employee()
# Output: e.id == 0, e.salary == 0.0, e.name == None
#
# Example 2 (Without __init__):
# Input:  e = Employee(); print(e.salary)
# Output: AttributeError: 'Employee' object has no attribute 'salary'
#

# Write your solution below:

class Employee : 
    def __init__(self , id = 0 , salary = 0.0 , name = None) -> None:
        self.id = id
        self.salary = salary
        self.name = name 

e = Employee()
print(e.id)
print(e.salary)
print(e.name)