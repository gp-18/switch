# Second Largest Element
# Given an array nums of N integers, find and return the second largest distinct element without sorting.
# If no second largest distinct element exists, return -1.
#
# Example 1:
# Input:  nums = [1, 2, 4, 7, 7, 5]
# Output: 5
#
# Example 2:
# Input:  nums = [10, 10, 10]
# Output: -1
#
# Think About:
# - Single pass approach with two variables: largest = -float('inf') and second_largest = -float('inf').
# - For each num in nums:
#   * If num > largest: update second_largest = largest, then largest = num.
#   * Else if num < largest and num > second_largest: update second_largest = num.
# - Check if second_largest was updated; if not, return -1.
# - Time Complexity: O(N)
# - Space Complexity: O(1)
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

def find_second_largest(nums):
    """
    Find and return the second largest distinct element in nums in a single pass.
    If no second largest distinct element exists, return -1.
    
    Why single pass?
    - Two passes (find max, then find max < previous max) take 2N operations.
    - Single pass tracks both in 1N operations without sorting.
    
    Time Complexity: O(N) (we visit each element once)
    Space Complexity: O(1) (only two float/int variables used)
    """
    # Edge case: If array has fewer than 2 elements, second largest cannot exist
    if len(nums) < 2:
        return -1

    largest = -float('inf')
    second_largest = -float('inf')

    for num in nums:
        # Case 1: Found an element strictly greater than the current largest.
        # The previous largest now steps down to become the second_largest.
        if num > largest:
            second_largest = largest
            largest = num
        # Case 2: Found an element smaller than largest, but greater than second_largest.
        # This handles distinct elements strictly between largest and second_largest.
        elif num < largest and num > second_largest:
            second_largest = num
        # Note: If num == largest or num <= second_largest, we ignore it to maintain distinctness.

    # If second_largest was never updated from -inf (e.g., all elements were identical like [10, 10, 10]),
    # it means no distinct second largest element exists.
    if second_largest == -float('inf'):
        return -1

    return second_largest


# Call the function and display the result
result = find_second_largest(array)

if result != -1:
    print(f"Result: The second largest distinct element is: {result}")
else:
    print(f"Result: No second largest distinct element exists (returned {result}).")


