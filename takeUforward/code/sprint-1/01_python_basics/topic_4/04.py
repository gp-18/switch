# Split a comma-separated string of names into a list, remove extra spaces from each name, and print each name.

# Example 1:
# Input: "Alice,  Bob , Charlie,David"
# Output:
# Alice
# Bob
# Charlie
# David

# Example 2:
# Input: " Apple , Banana , Mango "
# Output:
# Apple
# Banana
# Mango


names = input("Enter a comma-separated list of names: ").split(",")
for name in names:
    print(name.strip())