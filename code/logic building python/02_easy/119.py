# Count how many numbers in an array are divisible by both 3 and 5.
if (number := int(input("Enter the length of array: "))) >= 1:
    array = []

    for i in range(number):
        value = int(input(f"Enter the number at index {i}: "))
        array.append(value)

    count = 0
    for value in array : 
        if value % 3 == 0 and value % 5 == 0 :
            count = count + 1 


    print(count)

else:
    print("Enter the valid length")