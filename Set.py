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