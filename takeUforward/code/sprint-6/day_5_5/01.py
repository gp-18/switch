# Minimize Max Distance to Gas Station
# Given a sorted array arr of size n containing coordinates of gas stations on X-axis,
# and an integer k, place k new gas stations to minimize the maximum distance between
# adjacent gas stations.
#
# Example 1:
# Input:  arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 10
# Output: 0.50000
#
# Example 2:
# Input:  arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 1
# Output: 1.00000
#
# Example 3:
# Input:  arr = [3, 6, 12, 19, 33, 44, 67, 72, 89, 95], k = 2
# Output: 14.00000
#
# Think About:
# - Binary search on continuous decimal space [0, max_gap].
# - Loop condition: while high - low > 1e-6.
# - Update bounds: low = mid or high = mid (no integer +1/-1).
# - Stations needed in gap: int(gap / dist) - (1 if gap == dist * int(gap / dist) else 0).
# - If stations_needed > k: mid is too small, search right (low = mid).
# - Else: search left (high = mid).
# - Time Complexity: O(N * log(max_gap / 1e-6))
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter number of gas stations (n) : "))
array = []

for i in range(length):
    value = int(input(f"Enter position of gas station {i} : "))
    array.append(value)

k = int(input("Enter number of new gas stations to place (k) : "))

print(f"Your gas stations : {array} with k = {k}")

# Write your solution below:
# Optimal Approach: Binary Search on Continuous Answer Space [0, max_gap]
# Time Complexity: O(N * log(max_gap / 1e-6)) | Space Complexity: O(1)

def number_of_gas_stations_required(dist, arr):
    cnt = 0
    for i in range(1, len(arr)):
        gap = arr[i] - arr[i - 1]
        number_in_between = int(gap / dist)

        # If gap is an exact multiple of dist, we need 1 fewer station
        if gap == dist * number_in_between:
            number_in_between -= 1

        cnt += number_in_between
    return cnt

# Find maximum initial gap between adjacent stations
max_gap = 0.0
for i in range(length - 1):
    max_gap = max(max_gap, float(array[i + 1] - array[i]))

low = 0.0
high = max_gap
diff = 1e-6

while high - low > diff:
    mid = (low + high) / 2.0
    cnt = number_of_gas_stations_required(mid, array)

    if cnt > k:
        # Distance mid is too small, requires too many stations
        low = mid
    else:
        # Distance mid is achievable, try for an even smaller distance
        high = mid

ans = high

print(f"The minimum possible maximum distance is : {ans:.5f}")

