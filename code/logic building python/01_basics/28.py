# Input n integers into an array and print them.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

if (number := int(input("Enter the length of array : "))) >=1 :
    array = []
    for i in range(0,number) :
        array_value = int(input(f"Enter the number you want to insert at index {i} : "))
        array.append(array_value)

    print(array)
