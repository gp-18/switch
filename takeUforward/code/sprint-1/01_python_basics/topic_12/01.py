# Print a 5-by-5 rectangle of stars.

# Example 1:
# Output:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# Example 2:
# Output dimension: 5 rows by 5 columns of stars

for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()
