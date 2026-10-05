# Second Highest Occurring Element
# Given an array `nums`, find and return the element with the second highest frequency. If multiple elements have the same second highest frequency, return the smaller element (or -1 if no second highest exists).
#
# Example 1:
# Input: nums = [1, 2, 2, 3, 3, 3]
# Output: 2  # Frequencies: 3 -> 3, 2 -> 2, 1 -> 1
#
# Example 2:
# Input: nums = [4, 4, 5, 5, 5, 6]
# Output: 4  # Frequencies: 5 -> 3, 4 -> 2, 6 -> 1
#
# Example 3 (Edge Case - All Elements Have Same Frequency):
# Input: nums = [1, 2, 3]
# Output: -1  # All elements appear once; no second highest frequency

length = int(input("Enter the length of the array : "))
array = []

for i in range(0, length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

freq = {}

for value in array:
    freq[value] = freq.get(value, 0) + 1

second_highest = highest = float("-inf")
second_element = float("inf")
highest_element = float("inf")

for key, value in freq.items():

    if value > highest:
        second_highest = highest
        second_element = highest_element

        highest = value
        highest_element = key

    elif value > second_highest and value != highest:
        second_highest = value
        second_element = key

    elif value == second_highest and key < second_element:
        second_element = key

if second_highest == float("-inf"):
    print("-1")
else:
    print(f"The second highest occurring element is : {second_element}")
    