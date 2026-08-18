# Find the sum of odd elements only in an array.

if (number := int(input("Enter the length of array: "))) >= 1:
    array = []

    for i in range(number):
        value = int(input(f"Enter the number at index {i}: "))
        array.append(value)

    value = sum(x for x in array if x&1 !=0)

    print(value)

else:
    print("Enter the valid length")