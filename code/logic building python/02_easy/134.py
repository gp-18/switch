# Check if an array is sorted in ascending order.

if (number := int(input("Enter the length of array: "))) >= 1:
    array = []

    for i in range(number):
        value = int(input(f"Enter the number at index {i}: "))
        array.append(value)

    is_sorted = True
    for i in range(len(array)-1) :
        if array[i] > array[i + 1 ] :
            is_sorted = False 
            break 

    print("yes") if is_sorted else print("no")


else:
    print("Enter the valid length")