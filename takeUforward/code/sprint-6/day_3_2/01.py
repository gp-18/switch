# Minimum Days to Make M Bouquets
# Given n roses and an array nums where nums[i] denotes that the 'ith' rose will bloom
# on the nums[i]th day, only adjacent bloomed roses can be picked to make a bouquet.
# Exactly k adjacent bloomed roses are required to make a single bouquet.
# Find the minimum number of days required to make at least m bouquets, each containing k roses.
# Return -1 if it is not possible.
#
# Example 1:
# Input:  nums = [7, 7, 7, 7, 13, 11, 12, 7], m = 2, k = 3
# Output: 12
# Explanation: On day 12, 2 bouquets of 3 adjacent roses can be formed.
#
# Example 2:
# Input:  nums = [1, 10, 3, 10, 2], m = 3, k = 2
# Output: -1
# Explanation: Total flowers needed = 3 * 2 = 6, but only 5 flowers available. Return -1.
#
# Example 3:
# Input:  nums = [1, 10, 3, 10, 2], m = 3, k = 1
# Output: 3
#
# Think About:
# - Edge case: If m * k > length, impossible, return -1.
# - Search space: low = min(nums), high = max(nums).
# - Monotonicity: As days increase, more roses bloom and remain bloomed.
# - If bouquets >= m: mid is a valid day, search left (high = mid - 1) to find earlier days.
# - Else: search right (low = mid + 1).
# - Greedy counting of adjacent roses: track consecutive bloomed roses. When consecutive == k,
#   increment bouquet count and reset consecutive to 0. An unbloomed rose resets consecutive to 0.
# - Time Complexity: O(N * log(max(nums) - min(nums) + 1))
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the number of roses (n) : "))
array = []

for i in range(length):
    value = int(input(f"Enter bloom day for rose {i} : "))
    array.append(value)

m = int(input("Enter number of bouquets required (m) : "))
k = int(input("Enter number of adjacent flowers per bouquet (k) : "))

print(f"Your roses : {array} with m = {m} bouquets and k = {k} roses/bouquet")

# Write your solution below:
# Optimal Approach: Binary Search on Answers [min(nums), max(nums)]
# Time Complexity: O(N * log(max(nums) - min(nums) + 1)) | Space Complexity: O(1)

if m * k > length:
    print("Not enough roses to make bouquets. Result : -1")
else:
    low = min(array)
    high = max(array)
    ans = -1

    while low <= high:
        mid = low + (high - low) // 2

        bouquets = 0
        consecutive = 0

        # Count how many adjacent bouquets of size k can be formed on day 'mid'
        for bloom_day in array:
            if bloom_day <= mid:
                consecutive += 1
                # When we have k adjacent bloomed roses, form 1 bouquet
                if consecutive == k:
                    bouquets += 1
                    consecutive = 0
            else:
                # Adjacent streak broken by an unbloomed flower
                consecutive = 0

        if bouquets >= m:
            ans = mid
            # Try to find an earlier day on the left
            high = mid - 1
        else:
            # Not enough bouquets, need more days for flowers to bloom
            low = mid + 1

    print(f"The minimum days required to make {m} bouquets is : {ans}")
