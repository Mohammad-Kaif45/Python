# Tuples are like lists, but they can’t be changed once created. They’re immutable (unchangeable) sequences.

# Empty tuple
empty = ()

# Tuple with items
point = (3, 5)
colors = ("red", "green", "blue")

# Single item tuple needs comma!
single = (42,)  # Note the comma
not_tuple = (42)  # This is just 42 in parentheses

# Without parentheses (implicit)
coordinates = 10, 20

# Accesing items in a tuple
point = (3,5)
print(point[0])  # Output: 3

# Tuples Unpacking
point = (4,7)
x,y = point # x = 4 and y = 7
print(x,y)
print(y,x)

a,b,c = 1,2,3
print(a)
print(b)
print(c)