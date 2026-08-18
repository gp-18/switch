# Count how many elements in an array are perfect squares.
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