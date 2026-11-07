# Aggressive Cows
# Given an array nums of size n, which denotes the positions of stalls,
# and an integer k, which denotes the number of aggressive cows.
# Assign stalls to k cows such that the minimum distance between any two cows
# is the maximum possible. Find the maximum possible minimum distance.
#
# Example 1:
# Input:  nums = [0, 3, 4, 7, 10, 9], k = 4
# Output: 3
# Explanation: Sorted stalls: [0, 3, 4, 7, 9, 10]. Placing cows at [0, 3, 7, 10]
# yields distances 3, 4, 3 with minimum distance 3.
#
# Example 2:
# Input:  nums = [4, 2, 1, 3, 6], k = 2
# Output: 5
# Explanation: Sorted stalls: [1, 2, 3, 4, 6]. Place cows at [1, 6] -> distance 5.
#
# Example 3:
# Input:  nums = [10, 1, 2, 7, 5], k = 3
# Output: 4
#
# Think About:
# - Sort the stalls to enable greedy left-to-right placement.
# - Search space: low = 1, high = nums[-1] - nums[0].
# - Monotonicity: If distance mid is feasible, try larger distance (low = mid + 1).
# - Else: distance is too large, search smaller (high = mid - 1).
# - When low > high, high holds the maximum feasible minimum distance.
# - Time Complexity: O(N log N + N * log(max - min))
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter number of stalls (n) : "))
array = []

for i in range(length):
    value = int(input(f"Enter position of stall {i} : "))
    array.append(value)

k = int(input("Enter number of cows (k) : "))

print(f"Your stalls : {array} with k = {k} cows")

# Write your solution below:
# Optimal Approach: Binary Search on Answers [1, nums[-1] - nums[0]] with Greedy Check
# Time Complexity: O(N log N + N * log(max - min)) | Space Complexity: O(1)

def can_we_place(stalls, dist, cows):
    cnt_cows = 1
    last = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - last >= dist:
            cnt_cows += 1
            last = stalls[i]
        if cnt_cows >= cows:
            return True

    return False

# Sort stall coordinates to allow greedy placement
array.sort()

low = 1
high = array[-1] - array[0]
ans = 1

while low <= high:
    mid = low + (high - low) // 2

    if can_we_place(array, mid, k):
        ans = mid
        # Feasible to place cows with at least mid distance; try for larger distance
        low = mid + 1
    else:
        # Distance too large, cows cannot be placed
        high = mid - 1

print(f"The maximum possible minimum distance is : {ans}")

