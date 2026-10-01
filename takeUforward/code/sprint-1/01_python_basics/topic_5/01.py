# Print a three-line address using \n.

# Example 1:
# Input: Line 1: 123 Main St, Line 2: Apt 4B, Line 3: New York, NY
# Output:
# 123 Main St
# Apt 4B
# New York, NY

# Example 2:
# Input: Line 1: Flat 101, Line 2: Baker Street, Line 3: London
# Output:
# Flat 101
# Baker Street
# London

line1 = input("Enter Line 1 of the address: ")
line2 = input("Enter Line 2 of the address: ")
line3 = input("Enter Line 3 of the address: ")

# Print the address using \n to create new lines
address = f"{line1}\n{line2}\n{line3}"
print("The address is:")
print(address)
