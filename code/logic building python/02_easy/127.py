# Rotate an array by one position to the left.
if (number := int(input("Enter the length of array: "))) >= 1:
    array = []

    for i in range(number):
        value = int(input(f"Enter the number at index {i}: "))
        array.append(value)

    start = array[0]

    for i in range(len(array) - 1):
        array[i] = array[i + 1]

    array[len(array) - 1] = start

    print(array)

else:
    print("Enter the valid length")