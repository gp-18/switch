# Print a string in reverse using recursion
# Given a string `s`, print its characters in reverse order using recursion.
#
# Example 1:
# Input: s = "hello"
# Output: "olleh"
#
# Example 2:
# Input: s = "Python"
# Output: "nohtyP"
#
# Example 3 (Edge Case):
# Input: s = "a"
# Output: "a"
#

s = input("Enter the string : ")

print(f"Your string is : '{s}' and now doing the operations on it.")
def print_in_reverse(s):
    if len(s) == 0:
        return
    print_in_reverse(s[1:])
    print(s[0], end="")

print_in_reverse(s)
print()
