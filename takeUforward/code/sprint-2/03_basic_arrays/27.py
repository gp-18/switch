# Check if Two Arrays are Equal
# Given two arrays `a` and `b`, determine if they contain the exact same elements with the same frequencies (irrespective of order).
#
# Example 1:
# Input: a = [1, 2, 5, 4, 0], b = [2, 4, 5, 0, 1]
# Output: True
#
# Example 2:
# Input: a = [1, 2, 3], b = [1, 2, 4]
# Output: False
#
# Example 3 (Edge Case - Negative Elements & Different Counts):
# Input: a = [-1, -2, -2], b = [-1, -1, -2]
# Output: False

def are_arrays_equal(a: list[int], b: list[int]) -> bool:
  # Arrays of different lengths can never contain the exact same elements
  if len(a) != len(b):
    return False

  freq = {}

  # Count element frequencies in the first array
  for val in a:
    freq[val] = freq.get(val, 0) + 1

  # Decrement frequencies using the second array
  for val in b:
    # If element was not in array 'a' or its count is already 0
    if val not in freq or freq[val] == 0:
      return False
    freq[val] -= 1

  # If all elements matched perfectly, the arrays are equal
  return True


# ==================== INPUT HANDLING ====================

# Input for Array 1
len1 = int(input("Enter the length of the first array : "))
array1 = []
for i in range(len1):
  val = int(input(f"Enter element at index {i} for Array 1: "))
  array1.append(val)

print(f"\nArray 1: {array1}\n")

# Input for Array 2
len2 = int(input("Enter the length of the second array: "))
array2 = []
for i in range(len2):
  val = int(input(f"Enter element at index {i} for Array 2: "))
  array2.append(val)

print(f"\nArray 2: {array2}\n")

# ==================== RESULT CHECK ====================

if are_arrays_equal(array1, array2):
  print("Result: The two arrays are EQUAL.")
else:
  print("Result: The two arrays are NOT EQUAL.")
