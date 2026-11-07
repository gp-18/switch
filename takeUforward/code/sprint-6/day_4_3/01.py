# Painter's Partition Problem
# You are given A painters and an array C of N integers where C[i] denotes board lengths.
# Each painter takes B units of time to paint 1 unit of board length.
# Each painter paints only contiguous segments of boards without splitting.
# Minimize the maximum time to paint all boards modulo 10000003.
#
# Example 1:
# Input:  A = 2, B = 5, C = [1, 10]
# Output: 50
# Explanation: Painter 1 paints board 0 (time 5), Painter 2 paints board 1 (time 50).
# Max time = 50 % 10000003 = 50.
#
# Example 2:
# Input:  A = 10, B = 1, C = [1, 8, 11, 3]
# Output: 11
#
# Example 3:
# Input:  A = 3, B = 2, C = [5, 10, 30, 20]
# Output: 60
#
# Think About:
# - Minimize the maximum board length X assigned to any painter.
# - Search space: low = max(C), high = sum(C).
# - Feasibility check: greedily assign boards to painters; if sum > mid, use next painter.
# - If painters <= A: feasible, search left (high = mid - 1).
# - Else: search right (low = mid + 1).
# - Final result = (ans * B) % 10000003.
# - Time Complexity: O(N * log(sum(C)))
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter number of boards (N) : "))
array = []

for i in range(length):
    value = int(input(f"Enter length of board {i} : "))
    array.append(value)

A = int(input("Enter number of painters (A) : "))
B = int(input("Enter time per unit length (B) : "))

print(f"Your boards : {array} with painters A = {A} and time factor B = {B}")

# Write your solution below:
# Optimal Approach: Binary Search on Answers [max(C), sum(C)]
# Time Complexity: O(N * log(sum(C))) | Space Complexity: O(1)

MOD = 10000003

def can_paint(boards, painters_allowed, max_len):
    total = 0
    painters = 1

    for length_val in boards:
        if total + length_val > max_len:
            painters += 1
            total = length_val
            if painters > painters_allowed:
                return False
        else:
            total += length_val

    return True

low = max(array)
high = sum(array)
ans = high

while low <= high:
    mid = low + (high - low) // 2

    if can_paint(array, A, mid):
        ans = mid
        # Try to find a smaller maximum board length
        high = mid - 1
    else:
        # Requires too many painters, increase length limit
        low = mid + 1

result = (ans * B) % MOD

print(f"The minimum time required to paint all boards is : {result}")

