# Find the second largest number in a list.
# Example 1: Input: 10, 20 -> Output: 20
# Example 2: Input: 5, 3, 9 -> Output: 9

array = list(map(int, input("Enter the numbers: ").split()))

largest = float("-inf")
second_largest = float("-inf")

for value in array:

    if value > largest:
        second_largest = largest
        largest = value

    elif value > second_largest and value != largest:
        second_largest = value

print(second_largest)
