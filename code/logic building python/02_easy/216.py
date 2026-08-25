# Return the thickness of paper folded n times.
# Example 1: Input: 1 fold -> Output: 0.001 m
# Example 2: Input: 4 folds -> Output: 0.008 m

def paper_thickness(folds):
    initial_thickness = 0.0005  # in meters
    if folds >= 0:
        return initial_thickness * (2 ** folds)
    return "Folds must be non-negative"

n = int(input("Enter number of folds: "))
print(f"Thickness after {n} folds:", paper_thickness(n), "m")
