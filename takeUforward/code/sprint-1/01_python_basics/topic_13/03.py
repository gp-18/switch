# Repeatedly ask for numbers until the user enters 0, then print their sum.

# Example 1:
# Input: 4, 6, 10, 0
# Output: Sum: 20

# Example 2:
# Input: 0
# Output: Sum: 0

total_sum = 0

while True:
    num = float(input("Enter a number (0 to finish): "))
    if num == 0:
        break
    total_sum += num

sum_val = int(total_sum) if total_sum.is_integer() else total_sum
print(f"Sum: {sum_val}")
