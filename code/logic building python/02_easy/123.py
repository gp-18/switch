# Replace every negative number in an array with 0.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

if (number := int(input("Enter the length of array: "))) >= 1:
    array = []

    for i in range(number):
        value = int(input(f"Enter the number at index {i}: "))
        array.append(value)

    for i in range(len(array)) : 
        if array[i] < 0 :
            array[i] = 0 

    print(array) 
            
else:
    print("Enter the valid length")
