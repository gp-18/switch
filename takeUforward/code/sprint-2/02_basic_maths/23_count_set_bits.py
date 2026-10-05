# Count Set Bits
# Count the number of set bits (1s) in the binary representation of an integer n.
#
# Example 1:
# Input: n = 5
# Output: 2  # Binary representation: 101
#
# Example 2:
# Input: n = 15
# Output: 4  # Binary representation: 1111
#
# Example 3 (Edge Case - Zero):
# Input: n = 0
# Output: 0  # Binary representation: 0

number = int(input("Enter the number: "))

number = abs(number)

count = 0

while number > 0:
    number &= (number - 1)
    count += 1

print(count)