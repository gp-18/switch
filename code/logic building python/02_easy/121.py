# Create a new array containing squares of all elements.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

if (number := int(input("Enter the length of array: "))) >= 1:
    array = []

    for i in range(number):
        value = int(input(f"Enter the number at index {i}: "))
        array.append(value)

    new_array = [ x * x  for x in array]
    print(new_array)
else:
    print("Enter the valid length")
