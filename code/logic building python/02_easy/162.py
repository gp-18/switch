# Find the sum of all elements at odd indices in an array.
# Example 1: Input: 5 -> Output: 15
# Example 2: Input: 10 -> Output: 55

if (number := int(input("Enter the length of array: "))) >= 1:

    array = []

    for i in range(number):
        value = int(input(f"Enter the number at index {i}: "))
        array.append(value)

    total = 0

    for i in range(1, len(array), 2):
        total += array[i]

    print("Sum:", total)

else:
    print("Enter a valid length")
