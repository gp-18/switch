# Find Missing Number
# Given an array nums containing N distinct numbers taken from the range [0, N] (or [1, N]),
# find the single number missing from the range.
#
# Example 1:
# Input:  nums = [3, 0, 1]
# Output: 2  # Range [0, 3], missing number is 2
#
# Example 2:
# Input:  nums = [1, 2, 4, 5], N = 5
# Output: 3  # Range [1, 5], missing number is 3
#
# Think About:
# - Approach 1 (Sum formula):
#   * Expected sum = N * (N + 1) // 2.
#   * Missing = Expected Sum - sum(nums).
# - Approach 2 (XOR property):
#   * XOR all numbers in the full range and XOR all numbers present in nums.
#   * Duplicates cancel out (a ^ a = 0), leaving only the missing number.
# - Time Complexity: O(N)
# - Space Complexity: O(1)
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

def find_missing_number_xor(nums, start_from_zero=True):
    """
    Finds the missing number using the XOR property.
    
    Why XOR?
    - Property 1: a ^ a = 0 (any number XORed with itself cancels out).
    - Property 2: a ^ 0 = a (any number XORed with 0 stays the same).
    - XORing all numbers in the full range [0..N] or [1..N] AND all numbers in `nums`:
      Every number present in `nums` appears twice and cancels out to 0,
      leaving ONLY the single missing number!
    - Advantage over Sum: Never causes integer overflow in languages with fixed-width integers.
    
    Time Complexity: O(N) (single pass)
    Space Complexity: O(1)
    """
    n = len(nums)
    xor_all = 0
    xor_nums = 0

    if start_from_zero:
        # Full range is [0, N], where N = len(nums)
        for i in range(n + 1):
            xor_all ^= i
        for num in nums:
            xor_nums ^= num
    else:
        # Full range is [1, N], where N = len(nums) + 1
        for i in range(1, n + 2):
            xor_all ^= i
        for num in nums:
            xor_nums ^= num

    return xor_all ^ xor_nums


def find_missing_number_sum(nums, start_from_zero=True):
    """
    Finds the missing number using the Gauss summation formula: N * (N + 1) // 2.
    
    Approach:
    Expected Sum of range minus actual sum of array elements gives the missing number.
    
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    n = len(nums)
    if start_from_zero:
        # Range is [0, N], total numbers expected = N + 1, sum = N * (N + 1) // 2
        expected_sum = n * (n + 1) // 2
    else:
        # Range is [1, N], where N = len(nums) + 1, sum = N * (N + 1) // 2
        N = n + 1
        expected_sum = N * (N + 1) // 2

    actual_sum = sum(nums)
    return expected_sum - actual_sum


# Determine whether the range is [0, N] or [1, N]
# If 0 is in the array, it's the [0, N] variant; otherwise [1, N]
is_zero_indexed = (0 in array)

ans_xor = find_missing_number_xor(array, start_from_zero=is_zero_indexed)
ans_sum = find_missing_number_sum(array, start_from_zero=is_zero_indexed)

range_str = f"[0, {len(array)}]" if is_zero_indexed else f"[1, {len(array) + 1}]"
print(f"Detected range: {range_str}")
print(f"Result (using XOR approach): Missing number is {ans_xor}")
print(f"Result (using Sum formula):  Missing number is {ans_sum}")


