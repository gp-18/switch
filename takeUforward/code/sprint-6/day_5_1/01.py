# Book Allocation Problem
# Given an array nums of n integers representing pages in books,
# and an integer m representing the number of students.
# Allocate books contiguously such that each student gets at least one book,
# and the maximum number of pages assigned to a student is minimized.
# Return -1 if allocation is impossible.
#
# Example 1:
# Input:  nums = [12, 34, 67, 90], m = 2
# Output: 113
# Explanation: Optimal allocation [12, 34, 67] | [90] gives max pages = 113.
#
# Example 2:
# Input:  nums = [25, 46, 28, 49, 24], m = 4
# Output: 71
# Explanation: Allocation [25, 46] | [28] | [49] | [24] gives max pages = 71.
#
# Example 3:
# Input:  nums = [15, 17, 20], m = 2
# Output: 32
#
# Think About:
# - Edge case: If m > n (more students than books), impossible, return -1.
# - Search space: low = max(nums), high = sum(nums).
# - Monotonicity: As page limit increases, fewer or equal students are required.
# - If count_students(mid) <= m: feasible, search left (high = mid - 1) to minimize.
# - Else: search right (low = mid + 1).
# - Time Complexity: O(N * log(sum(nums) - max(nums)))
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter number of books (n) : "))
array = []

for i in range(length):
    value = int(input(f"Enter pages in book {i} : "))
    array.append(value)

m = int(input("Enter number of students (m) : "))

print(f"Your books : {array} with m = {m} students")

# Write your solution below:
# Optimal Approach: Binary Search on Answers [max(nums), sum(nums)]
# Time Complexity: O(N * log(sum(nums) - max(nums))) | Space Complexity: O(1)

def count_students(books, max_pages):
    students = 1
    pages = 0

    for book in books:
        if pages + book <= max_pages:
            pages += book
        else:
            students += 1
            pages = book

    return students

if m > length:
    print("Allocation impossible (m > n). Result : -1")
else:
    low = max(array)
    high = sum(array)
    ans = high

    while low <= high:
        mid = low + (high - low) // 2

        if count_students(array, mid) <= m:
            ans = mid
            # Try to find a smaller maximum page limit
            high = mid - 1
        else:
            # Requires more than m students, increase page limit
            low = mid + 1

    print(f"The minimum possible maximum pages is : {ans}")

