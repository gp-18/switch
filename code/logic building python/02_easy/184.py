# Clone or copy a list using slice, list() constructor, or comprehension.
# Example 1: Input: [10, 20, 30] -> Output: [10, 20, 30]
# Example 2: Input: ['a', 'b'] -> Output: ['a', 'b']

original_list = [10, 20, 30, 40, 50]

# Method 1: Using Slicing [:]
cloned_list_1 = original_list[:]

# Method 2: Using list() constructor
cloned_list_2 = list(original_list)

# Method 3: Using List Comprehension
cloned_list_3 = [item for item in original_list]

# Method 4: Using .copy() method
cloned_list_4 = original_list.copy()

print("Original list:", original_list)
print("Cloned using slicing [:]:", cloned_list_1)
print("Cloned using list():", cloned_list_2)
print("Cloned using list comprehension:", cloned_list_3)
print("Cloned using .copy():", cloned_list_4)
