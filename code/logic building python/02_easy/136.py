# Find the difference between the largest and smallest element in an array.
# Example 1: Input: 10, 20 -> Output: 20
# Example 2: Input: 5, 3, 9 -> Output: 9

if (number := int(input("Enter the length of array: "))) >= 1:
    array = []

    for i in range(number):
        value = int(input(f"Enter the number at index {i}: "))
        array.append(value)

    largest = float("-inf")
    smallest = float("inf")

    for value in array : 
        if value > largest : 
            largest = value

        if value < smallest : 
            smallest = value 

    print(largest - smallest)

else:
    print("Enter the valid length")
