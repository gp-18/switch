# Multiply all numbers in a list.
# Example 1: Input: 1 2 3 4 5 -> Output: Product of all numbers in the list: 120
# Example 2: Input: 2 5 10 -> Output: Product of all numbers in the list: 100

numbers = list(map(int, input("Enter space-separated numbers: ").split()))

if len(numbers) > 0:
    product = 1
    for num in numbers:
        product *= num
    print("Product of all numbers in the list:", product)
else:
    print("The list is empty")
