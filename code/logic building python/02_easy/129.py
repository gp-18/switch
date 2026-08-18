# Swap alternate elements of an array (1st↔2nd, 3rd↔4th, etc.).



if (number := int(input("Enter the length of array: "))) >= 1:
    array = []

    for i in range(number):
        value = int(input(f"Enter the number at index {i}: "))
        array.append(value)

    i = 0 
    while i < len(array) - 1 : 
        array[i] , array[i + 1] = array[i + 1] , array[i]
        i = i + 2 

    print(array)

else:
    print("Enter the valid length")