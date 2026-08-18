# Check if all elements in an array are unique.

if (number := int(input("Enter the length of array: "))) >= 1:
    array = []

    for i in range(number):
        value = int(input(f"Enter the number at index {i}: "))
        array.append(value)

    set_value = set()
    is_unique = True

    for value in array:
        if value in set_value:
            is_unique = False
            break
        else:
            set_value.add(value)

    print("All elements are unique") if is_unique else print("Elements are not unique")

else:
    print("Enter the valid length")