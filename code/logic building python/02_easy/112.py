# Check if a given element x exists in an array.

if (number := int(input("Enter the length of array: "))) >= 1:
    array = []

    for i in range(number):
        value = int(input(f"Enter the number at index {i}: "))
        array.append(value)

    key = int(input("Enter the value for the key: "))
    is_there = False

    for value in array:
        if value == key : 
            is_there = True 
            break

    print("yes") if is_there else print("no")
       

else:
    print("Enter the valid length")