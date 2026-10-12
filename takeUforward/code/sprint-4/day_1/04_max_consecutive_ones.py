# Maximum Consecutive Ones
# Given a binary array nums containing only 0s and 1s, return the maximum number of consecutive 1s present in the array.
#
# Example 1:
# Input:  nums = [1, 1, 0, 1, 1, 1]
# Output: 3
#
# Example 2:
# Input:  nums = [1, 0, 1, 1, 0, 1]
# Output: 2
#
# Think About:
# - Maintain a current streak count cnt = 0 and a maximum count max_cnt = 0.
# - Iterate through the array:
#   * If num == 1: increment cnt += 1 and update max_cnt = max(max_cnt, cnt).
#   * If num == 0: reset cnt = 0.
# - Time Complexity: O(N)
# - Space Complexity: O(1)
#

length = int(input("Enter the length of the binary array : "))
array = []

for i in range(length):
    value = int(input(f"Enter binary value (0 or 1) at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

def find_max_consecutive_ones(nums):
    """
    Find the maximum number of consecutive 1s in a binary array.
    
    Approach:
    - Maintain `current_streak` to track the ongoing streak of consecutive 1s.
    - Maintain `max_streak` to record the highest streak observed so far.
    - Whenever 1 is encountered: increment streak and update maximum.
    - Whenever 0 is encountered: reset the streak back to 0.
    
    Time Complexity: O(N) (we traverse the array once)
    Space Complexity: O(1) (only two integer counters used)
    """
    current_streak = 0
    max_streak = 0

    for num in nums:
        if num == 1:
            # We found a 1, so extend the current consecutive streak
            current_streak += 1
            # Update max_streak if current_streak is greater
            if current_streak > max_streak:
                max_streak = current_streak
        else:
            # We hit a 0, which breaks the consecutive streak of 1s
            current_streak = 0

    return max_streak


# Call the function and display the result
ans = find_max_consecutive_ones(array)
print(f"Result: Maximum consecutive 1s in the array is: {ans}")


