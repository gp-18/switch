# Add a number to the end of a list and remove the first element.
# Example 1: Input: lst=[1, 2, 3, 4], new_elem=5 -> Output: [2, 3, 4, 5]
# Example 2: Input: lst=[10, 20], new_elem=30 -> Output: [20, 30]

lst = [1, 2, 3, 4]
new_item = 5

if len(lst) > 0:
    lst.append(new_item)
    lst.pop(0)
    print("Updated list:", lst)
else:
    print("List is empty")
