# Count how many times a given element appears in an array.
if (number := int(input("Enter the length of array: "))) >= 1:
    array = []

    for i in range(number):
        value = int(input(f"Enter the number at index {i}: "))
        array.append(value)

    key = int(input("Enter the value for the key: "))

    count = 0 
    for value in array:
        if value == key:
            count += 1 

    print(count)

else:
    print("Enter the valid length")