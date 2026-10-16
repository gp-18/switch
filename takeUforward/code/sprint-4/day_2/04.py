# Two Sum
# Given an array of integers nums and an integer target, return the 0-based indices
# of two elements in nums such that they add up to target.
# Each input will have exactly one solution, and the same element cannot be used twice.
#
# Example 1:
# Input:  nums = [1, 6, 2, 10, 3], target = 7
# Output: [0, 1]  # nums[0] + nums[1] = 1 + 6 = 7
#
# Example 2:
# Input:  nums = [1, 3, 5, -7, 6, -3], target = 0
# Output: [1, 5]  # nums[1] + nums[5] = 3 + (-3) = 0
#
# Example 3 (Edge Case):
# Input:  nums = [3, 3], target = 6
# Output: [0, 1]  # Identical duplicate elements forming the target sum
#
# Think About:
# Part A: If Array is Sorted -> Low-High (Two Pointer) Approach:
#   * low = 0, high = n - 1
#   * If nums[low] + nums[high] == target: return [low, high]
#   * If sum < target: low += 1 (need a larger sum)
#   * If sum > target: high -= 1 (need a smaller sum)
#   * Time Complexity: O(N) | Space Complexity: O(1)
#
# Part B: If Array is Unsorted -> Frequency / Hash Map Concept:
#   * seen = {value: index}
#   * For index i and number num:
#       complement = target - num
#       if complement in seen: return [seen[complement], i]
#       seen[num] = i
#   * Time Complexity: O(N) | Space Complexity: O(N)
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

target = int(input("Enter the target sum : "))

print(f"Your array has become : {array}, target is : {target} and now doing the operations on it.")

# Write your solution below

# ==============================================================================
# Part B: Frequency / Hash Map Concept (Optimal for Unsorted Arrays)
# Works for any array, preserving original indices in a single pass.
# Time Complexity: O(N) | Space Complexity: O(N)
# ==============================================================================
print("\n--- Part B: Frequency / Hash Map Concept (Unsorted Array) ---")
seen = {}  # Maps element value -> index
found_hash = False

for i in range(len(array)):
    complement = target - array[i]
    # Check if the needed complement was already seen
    if complement in seen:
        print(f"Indices found using Hash Map : [{seen[complement]}, {i}]")
        print(f"Values: array[{seen[complement]}] ({array[seen[complement]]}) + array[{i}] ({array[i]}) = {target}")
        found_hash = True
        break
    # Record current element's frequency/index in the hash map
    seen[array[i]] = i

if not found_hash:
    print("No two sum solution found using Hash Map.")


# ==============================================================================
# Part A: Two Pointer Low-High Approach (Optimal for Sorted Arrays)
# If the input array is sorted (or if we check pair existence), use low and high pointers.
# Time Complexity: O(N) | Space Complexity: O(1) auxiliary space
# ==============================================================================
print("\n--- Part A: Low-High Two Pointer Approach (Sorted Array) ---")

# Check if array is sorted
is_sorted = all(array[k] <= array[k + 1] for k in range(len(array) - 1))

if is_sorted:
    low = 0
    high = len(array) - 1
    found_two_pointer = False

    while low < high:
        current_sum = array[low] + array[high]

        if current_sum == target:
            print(f"Indices found using Two Pointers : [{low}, {high}]")
            print(f"Values: array[{low}] ({array[low]}) + array[{high}] ({array[high]}) = {target}")
            found_two_pointer = True
            break
        elif current_sum < target:
            # Current sum is too small, advance low pointer to get a larger value
            low += 1
        else:
            # Current sum is too large, move high pointer to get a smaller value
            high -= 1

    if not found_two_pointer:
        print("No two sum solution found using Two Pointers.")
else:
    print("Note: The array is not sorted. To apply the Low-High two-pointer approach,")
    print("we sort element-index pairs while preserving original indices:")

    indexed_array = [(array[k], k) for k in range(len(array))]
    indexed_array.sort(key=lambda x: x[0])  # Sort by value

    low = 0
    high = len(indexed_array) - 1
    found_sorted = False

    while low < high:
        current_sum = indexed_array[low][0] + indexed_array[high][0]

        if current_sum == target:
            orig_low_idx = indexed_array[low][1]
            orig_high_idx = indexed_array[high][1]
            print(f"Original indices found via Sorted Low-High : [{min(orig_low_idx, orig_high_idx)}, {max(orig_low_idx, orig_high_idx)}]")
            print(f"Values: {indexed_array[low][0]} + {indexed_array[high][0]} = {target}")
            found_sorted = True
            break
        elif current_sum < target:
            low += 1
        else:
            high -= 1

    if not found_sorted:
        print("No two sum solution found.")
