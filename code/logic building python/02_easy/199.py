# Generate all sentences from given subjects, verbs, and objects.
# Example 1: Input: subjects=['I', 'You'], verbs=['love', 'like'], objects=['Python', 'Coding'] -> Output: I love Python...
# Example 2: Input: subjects=['He'], verbs=['plays'], objects=['Cricket'] -> Output: He plays Cricket

subjects = ["I", "You"]
verbs = ["love", "like"]
objects = ["Python", "Coding"]

for s in subjects:
    for v in verbs:
        for o in objects:
            print(f"{s} {v} {o}.")
