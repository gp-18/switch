# Count how many times the inner statement executes in a loop with 4 outer iterations and 3 inner iterations.

# Example 1:
# Scenario: Outer loop runs 4 times, inner loop runs 3 times for each outer loop
# Output: Total executions = 4 * 3 = 12 times

# Example 2:
# Scenario: Outer runs 5 times, inner runs 2 times -> 5 * 2 = 10 executions

outer_iterations = 4
inner_iterations = 3
total_executions = 0

for i in range(outer_iterations):
    for j in range(inner_iterations):
        total_executions += 1

print(f"Total executions = {outer_iterations} * {inner_iterations} = {total_executions} times")
