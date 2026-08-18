# Compare two arrays and check if they are equal
# (same elements and same order)

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

        is_equal = True

        if len(array1) != len(array2):
            is_equal = False
        else:
            for i in range(len(array1)):
                if array1[i] != array2[i]:
                    is_equal = False
                    break

        if is_equal:
            print("Arrays are equal")
        else:
            print("Arrays are not equal")

    else:
        print("Enter a valid length for the second array")

else:
    print("Enter a valid length for the first array")