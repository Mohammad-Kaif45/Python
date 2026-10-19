# Sets are collections that only store unique values. They automatically remove duplicates.

# You can create sets two ways: with set() or with curly braces {} (but only when it has values).

empty_set = set()
numbers = {1,2,3,4,5,5,2,3,1,6}
print(numbers)

num = set([1,6,6])
print(num)

scores = [85,78,85,42,51]
unique_scores = set(scores)
print(scores)
print(unique_scores)

# Use set() for empty sets, not {}. Empty curly braces create a dictionary!

colors = {"red", "blue"}

# Add items
colors.add("green")
print(colors)  # {'red', 'blue', 'green'}

# Remove items
colors.remove("blue")    # Error if not found
colors.discard("yellow") # No error if not found

# Check membership
if "red" in colors:
    print("Red is available")

    # Order is not guaranteed!
numbers = {3, 1, 4, 1, 5}
print(numbers)  # Could be any order

# Use list if order matters
ordered = [3, 1, 4, 1, 5]