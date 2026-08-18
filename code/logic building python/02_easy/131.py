# Merge two arrays into a third array.
if (number := int(input("Enter the length of first array: "))) >= 1:

    array1 = []

    for i in range(number):
        value = int(input(f"Enter the number for first array at index {i}: "))
        array1.append(value)

    if (number2 := int(input("Enter the length of second array: "))) >= 1:

        array2 = []

        for i in range(number2):
            value = int(input(f"Enter the number for second array at index {i}: "))
            array2.append(value)

    array3 = array1 + array2
    print(array3)


else:
    print("Enter a valid length for the first array")