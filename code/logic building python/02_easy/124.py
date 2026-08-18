# Replace all even numbers in an array with 1 and all odd numbers with 0.

if (number := int(input("Enter the length of array: "))) >= 1:
    array = []

    for i in range(number):
        value = int(input(f"Enter the number at index {i}: "))
        array.append(value)

    for i in range(len(array)) : 
        if array[i] & 1 != 0 :
            array[i] = 0 
        else : 
            array[i] = 1

    print(array) 
            
else:
    print("Enter the valid length")