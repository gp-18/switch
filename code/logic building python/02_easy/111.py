# Print only elements in an array that are greater than a given value k.


if (number := int(input("Enter the length of array: "))) >= 1:
    array = []

    for i in range(number):
        value = int(input(f"Enter the number at index {i}: "))
        array.append(value)

    key = int(input("Enter the value for the key: "))

    for value in array:
        if value > key:
            print(value)

else:
    print("Enter the valid length")