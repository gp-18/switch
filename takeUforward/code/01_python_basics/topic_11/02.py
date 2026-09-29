# Count how many numbers in a list are positive.

# Example 1:
# Input: [-2, 5, 0, 7, -1, 8]
# Output: 3 (positive numbers: 5, 7, 8)

# Example 2:
# Input: [-1, -4, -6]
# Output: 0

raw_input = input("Enter numbers separated by spaces: ")
numbers = [float(x) for x in raw_input.split()] if raw_input.strip() else []

positive_count = 0
for num in numbers:
    if num > 0:
        positive_count += 1

print(f"Positive numbers count: {positive_count}")
