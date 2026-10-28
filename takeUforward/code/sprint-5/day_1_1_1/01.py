# Majority Element-I (> n/2)
# Given an array nums of size n, find the majority element that appears strictly
# more than n // 2 times. You may assume that the majority element always exists.
#
# Example 1:
# Input:  nums = [3, 2, 3]
# Output: 3
#
# Example 2:
# Input:  nums = [2, 2, 1, 1, 1, 2, 2]
# Output: 2
#
# Think About:
# - Initialize candidate = None and count = 0.
# - If count == 0: candidate = num.
# - If num == candidate: count += 1, else count -= 1.
# - Time Complexity: O(N)
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below:
value = 0 
count = 0 

for num in array:
    if count == 0:
        value = num 
    if num == value:
        count += 1 
    else:
        count -= 1 


count = 0 

for num in array : 
    if num == value: 
        count += 1 

if count > length // 2: 
    print(f"The majority element is : {value}")
else: 
    print("No majority element found.") 
        