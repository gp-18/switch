# Print a table-like line with tab-separated name, age, and city using \t.

# Example 1:
# Input: name = "Alice", age = 25, city = "New York"
# Output: Alice	25	New York

# Example 2:
# Input: name = "Bob", age = 30, city = "London"
# Output: Bob	30	London

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
# Print the information in a tab-separated format
print(f"{name}\t{age}\t{city}")