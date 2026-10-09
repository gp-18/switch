# Constructor Chaining with super().__init__()
# Build a three-level inheritance hierarchy:
#   Person(name, age)
#   Student(Person)    — adds roll_no
#   GraduateStudent(Student) — adds thesis
# Each child class must call super().__init__(...) to chain the parent's constructor.
#
# After verifying it works, deliberately remove the super().__init__(...) call
# from Student.__init__ and observe the resulting AttributeError when accessing
# `name` on a GraduateStudent instance.
#
# Example 1:
# Input:  g = GraduateStudent("Rahul", 22, 101, "AI Safety")
# Output: g.name == "Rahul", g.age == 22, g.roll_no == 101, g.thesis == "AI Safety"
#
# Example 2 (Without super() in Student):
# Input:  g = GraduateStudent("Rahul", 22, 101, "AI Safety")
#         print(g.name)
# Output: AttributeError: 'GraduateStudent' object has no attribute 'name'
#

# Write your solution below:
class Person :
    def __init__(self , name , age) :
        self.name = name 
        self.age = age 

class Student(Person) : 
    def __init__(self , name , age , roll_no ) :
        super().__init__(name, age)
        self.roll_no = roll_no 

class GraduateStudent(Student) :
    def __init__(self , name , age , roll_no , thesis) :
        super().__init__(name, age, roll_no)
        self.thesis = thesis 

g = GraduateStudent("Rahul", 22, 101, "AI Safety")
print(g.name, g.age, g.roll_no, g.thesis)