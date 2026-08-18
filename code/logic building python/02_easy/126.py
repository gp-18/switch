# Reverse an array without using built-in reverse.

if (number := int(input("Enter the length of array: "))) >= 1:
    array = []

    for i in range(number):
        value = int(input(f"Enter the number at index {i}: "))
        array.append(value)

    low = 0 
    high = len(array) - 1 

    while low <= high : 
        array[low] , array[high] = array[high] , array[low]
        low = low + 1 
        high = high - 1 

    print(array)
            
else:
    print("Enter the valid length")