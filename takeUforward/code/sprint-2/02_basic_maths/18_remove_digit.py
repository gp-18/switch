# Remove a Digit
# Remove all occurrences of a given digit d from a number n.
#
# Example 1:
# Input: n = 12234, d = 2
# Output: 134
#
# Example 2:
# Input: n = 5675, d = 5
# Output: 67
#
# Example 3 (Edge Case - All Digits Match):
# Input: n = 777, d = 7
# Output: 0  # If all digits removed, result is 0

number = input("Enter the number: ")
digit = input("Enter the digit: ")

ans = []

for n in number:
    if n == digit:
        continue

    ans.append(n)

final_answer = "".join(ans)

if final_answer == "":
    final_answer = "0"

print(final_answer)


# optimize 
number = input("Enter the number: ")
digit = input("Enter the digit: ")

final_answer = number.replace(digit, "")

print(final_answer if final_answer else "0")