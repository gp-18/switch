# Capacity to Ship Packages Within D Days
# You are given an array weights where weights[i] represents the weight of the i-th package.
# All packages must be shipped in the given order within days days.
# Find the minimum possible ship capacity so that all packages can be shipped within days days.
#
# Example 1:
# Input:  weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days = 5
# Output: 15
# Explanation: A ship capacity of 15 allows shipping all packages across 5 days.
#
# Example 2:
# Input:  weights = [3, 2, 2, 4, 1, 4], days = 3
# Output: 6
# Explanation: Day 1: [3, 2], Day 2: [2, 4], Day 3: [1, 4].
#
# Example 3:
# Input:  weights = [10, 50, 50, 10], days = 2
# Output: 60
#
# Think About:
# - Search space: low = max(weights), high = sum(weights).
# - Lower bound: The ship must at least carry the heaviest package.
# - Upper bound: Shipping all packages in 1 day requires sum(weights).
# - Monotonicity: Larger capacities require fewer or equal days.
# - If can_ship(mid) is True: search left (high = mid - 1) to find smaller feasible capacity.
# - Else: search right (low = mid + 1).
# - Time Complexity: O(N * log(sum(weights) - max(weights)))
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the number of packages (n) : "))
array = []

for i in range(length):
    value = int(input(f"Enter weight of package {i} : "))
    array.append(value)

days = int(input("Enter number of days allowed (days) : "))

print(f"Your packages : {array} with days = {days}")

# Write your solution below:
# Optimal Approach: Binary Search on Answers [max(weights), sum(weights)]
# Time Complexity: O(N * log(sum(weights) - max(weights))) | Space Complexity: O(1)

def can_ship(weights, allowed_days, capacity):
    required_days = 1
    curr_load = 0

    for w in weights:
        if curr_load + w > capacity:
            required_days += 1
            curr_load = w
        else:
            curr_load += w

    return required_days <= allowed_days

low = max(array)
high = sum(array)
ans = high

while low <= high:
    mid = low + (high - low) // 2

    if can_ship(array, days, mid):
        ans = mid
        # Try to find a smaller feasible capacity
        high = mid - 1
    else:
        # Capacity is too small, need a larger ship
        low = mid + 1

print(f"The minimum ship capacity is : {ans}")

