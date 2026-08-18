# Find the first occurrence of a given number in an array.

if (number := int(input("Enter the length of array: "))) >= 1:
    array = []

    for i in range(number):
        value = int(input(f"Enter the number at index {i}: "))
        array.append(value)

    key = int(input("Enter the value for the key: "))

    index = -1 
    for i in range(len(array)) :
        if key == array[i] :
            index = i 
            break 

    print(index)

else:
    print("Enter the valid length")