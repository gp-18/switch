# Input n integers into an array and print them.

if (number := int(input("Enter the length of array : "))) >=1 :
    array = []
    for i in range(0,number) :
        array_value = int(input(f"Enter the number you want to insert at index {i} : "))
        array.append(array_value)

    print(array)
