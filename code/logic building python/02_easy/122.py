# Create a new array containing only even elements from another array.

if (number := int(input("Enter the length of array: "))) >= 1:
    array = []

    for i in range(number):
        value = int(input(f"Enter the number at index {i}: "))
        array.append(value)

    new_array = [ x for x in array if x & 1 == 0 ]
    print(new_array)
else:
    print("Enter the valid length")