# Count the vowels in a string using a for loop.

# Example 1:
# Input: "education"
# Output: 5

# Example 2:
# Input: "python"
# Output: 1

text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print(f"Number of vowels: {count}")
