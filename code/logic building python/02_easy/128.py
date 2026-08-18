# Rotate an array by one position to the right.

if (number := int(input("Enter the length of array: "))) >= 1:
    array = []

    for i in range(number):
        value = int(input(f"Enter the number at index {i}: "))
        array.append(value)

    last = array[len(array) - 1]

    for i in range(len(array) - 1, 0, -1):
        array[i] = array[i - 1]

    array[0] = last

    print(array)

else:
    print("Enter the valid length")