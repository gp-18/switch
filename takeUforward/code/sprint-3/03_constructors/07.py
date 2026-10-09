# Simulating Constructor Overloading
# Python only allows ONE __init__. Simulate overloading by writing a single __init__
# that supports ALL of these calling patterns:
#   Employee()
#   Employee("Raj", 10000)
#   Employee("Amit", 12000, "Python", "SQL", department="IT")
# Use default parameter values, *args for variable skills, and **kwargs for optional
# keyword arguments like department.
#
# Example 1:
# Input:  e1 = Employee()
# Output: e1.name == "Unknown"
#
# Example 2:
# Input:  e2 = Employee("Raj", 10000)
# Output: e2.name == "Raj", e2.salary == 10000
#
# Example 3:
# Input:  e3 = Employee("Amit", 12000, "Python", "SQL", department="IT")
# Output: e3.skills == ["Python", "SQL"], e3.department == "IT"
#

# Write your solution below:

class Employee : 
    def __init__(self , name = "Unknown" , salary = 0.0 , *args , **kwargs ) : 
        self.name = name 
        self.salary = salary 
        self.skills = list(args) 
        for key , value in kwargs.items() : 
            setattr(self , key , value)

e1 = Employee()
e2 = Employee("Raj", 10000)
e3 = Employee("Amit", 12000, "Python", "SQL", department="IT")

print("e1:", e1.name, e1.salary, e1.skills)
print("e2:", e2.name, e2.salary, e2.skills)
print("e3:", e3.name, e3.salary, e3.skills, e3.department)