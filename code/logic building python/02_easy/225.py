# Sum the budgets from a list of person dictionaries.
# Example 1: Input: [{'name': 'John', 'budget': 21000}, {'name': 'Steve', 'budget': 32000}] -> Output: 53000
# Example 2: Input: [{'name': 'A', 'budget': 1000}, {'name': 'B', 'budget': 5000}] -> Output: 6000

people = [
    {"name": "John", "age": 21, "budget": 23000},
    {"name": "Steve", "age": 32, "budget": 40000},
    {"name": "Martin", "age": 16, "budget": 2700}
]

total_budget = sum(p["budget"] for p in people)
print("Total budget:", total_budget)
