# Create a variable, reassign it to a value of a different type, and print type() before and after.

# Example 1:
# Input: my_variable = 42, then my_variable = "Hello, World!"
# Output:
# Before reassignment: my_variable = 42 , type = <class 'int'>
# After reassignment: my_variable = Hello, World! , type = <class 'str'>

# Example 2:
# Input: my_variable = 3.14, then my_variable = True
# Output:
# Before reassignment: my_variable = 3.14 , type = <class 'float'>
# After reassignment: my_variable = True , type = <class 'bool'>

my_variable = 42
print("Before reassignment: my_variable =", my_variable, ", type =", type(my_variable))
my_variable = 42.00
print("After reassignment: my_variable =", my_variable, ", type =", type(my_variable))
my_variable = True 
print("After reassignment: my_variable =", my_variable, ", type =", type(my_variable))
my_variable = "Hello, World!"
print("After reassignment: my_variable =", my_variable, ", type =", type(my_variable))
