# Return the product of a comma-space-separated string of numbers.
# Example 1: Input: '1, 2, 3, 4' -> Output: 24
# Example 2: Input: '10, 5, 2' -> Output: 100

text = input("Enter comma-separated numbers: ")

numbers = [int(n.strip()) for n in text.split(",") if n.strip()]

product = 1
for num in numbers:
    product *= num

print("Product:", product)
