# Count how many elements in an array are perfect squares.
# Example 1: Input: 1 2 2 3 3 3 -> Output: {1: 1, 2: 2, 3: 3}
# Example 2: Input: 5 5 5 -> Output: {5: 3}

if (number := int(input("Enter the length of array: "))) >= 1:
    array = []

    for i in range(number):
        value = int(input(f"Enter the number at index {i}: "))
        array.append(value)

    count = 0

    for value in array:
        if value >= 0:
            root = int(value ** 0.5)

            if root * root == value:
                count += 1

    print(count)

else:
    print("Enter the valid length")
