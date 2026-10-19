def greet(name):
    print(f"hello, {name}")

greet("Kaif")
greet("John")

def add(a,b):
    return a + b

result = add(5,6)
print(result)

def get_min_max(numbers):
    return min(numbers), max(numbers)

# Get both values
minimum, maximum = get_min_max([5, 2, 8, 1, 9])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9

# Or as a tuple
result = get_min_max([5, 2, 8, 1, 9])
print(result)  # (1, 9)