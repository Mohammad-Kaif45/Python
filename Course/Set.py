# Set are mutable you can change the value
# Set does not allow duplicates elements
# Set are unordered in nature means you cannot access them by using index
# Set is semi-hetrogeneous in natute means it can store some data types like 
# string, numbers, tuples but not everything

# How Set stores value in python
# Each value in a set is hashed using a hash function (hash() in Python)
# The hash is used as an index to store the element in memory.
# Since hashing does not maintain order, sets are unordered
# Only immutable (hashable) objects can be stored in a set
# (e.g., numbers, strings, tuples). Mutable objects like lists and
# dictionaries are not allowed

s = {1,2,3,4}

s.add(4) # add an elements to the set

s.remove(2) # remove 2 (rises an error if not found)

s.discard(7) # remove 7 (no error if not found)

pop_element = s.pop() # remove a random element

s.clear()
print(s)

# Now these are some of the basic methods but sets also have
# some special methods for performing some special
# operations between 2 sets.

A = {1,2,3}
B = {3,4,5}

union = A.union(B)
print(union)

intersection = A.intersection(B)
print(intersection)

difference_set = A.difference(B)
print(difference_set)

