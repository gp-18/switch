# Find the sum of even elements only in an array.

# # Filtering
# [x for x in array if condition]

# # Transformation with if/else
# [x if condition else y for x in array]

if (number := int(input("Enter the length of array: "))) >= 1:
    array = []

    for i in range(number):
        value = int(input(f"Enter the number at index {i}: "))
        array.append(value)

    value = sum(x for x in array if x % 2 == 0)

    print(value)

else:
    print("Enter the valid length")