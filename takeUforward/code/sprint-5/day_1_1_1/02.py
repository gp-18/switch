# Check if a Given Number is a Majority Element
# Given an array nums of size n and a target integer x, determine whether x is the
# majority element of nums (i.e. appears strictly more than n / 2 times).
# Return True or False.
#
# Example 1:
# Input:  nums = [1, 2, 3, 3, 3, 3, 10], x = 3
# Output: True
#
# Example 2:
# Input:  nums = [1, 1, 2, 2], x = 1
# Output: False
#
# Think About:
# - Count occurrences of x in nums.
# - Return count > len(nums) // 2.
# - Time Complexity: O(N)
# - Space Complexity: O(1)
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

target = int(input("Enter target number x to verify: "))

print(f"Your array has become : {array} and target is {target}.")

# Write your solution below:

# Time Complexity: O(N) | Space Complexity: O(1)
count = 0

for num in array:
    if num == target:
        count += 1

is_majority = count > length // 2

print(f"Is {target} a majority element? {is_majority}")

