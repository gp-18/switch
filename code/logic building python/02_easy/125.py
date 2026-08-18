# Swap the first and last elements of an array.

if (number := int(input("Enter the length of array: "))) >= 1:
    array = []

    for i in range(number):
        value = int(input(f"Enter the number at index {i}: "))
        array.append(value)

    array[0] , array[len(number) - 1] = array[len(number) - 1] , array[0]
    
    print(array) 
            
else:
    print("Enter the valid length")