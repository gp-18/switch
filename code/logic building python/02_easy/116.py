# Check if all elements in an array are unique.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

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
