# Dictionary.py
# This file demonstrates Python dictionaries and how they work.

# A dictionary is an unordered collection of key-value pairs.
# Each key must be unique and immutable, while values can be of any type.

person = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# Access values by key
print('Name:', person['name'])
print('Age:', person['age'])
print('City:', person['city'])

# Add a new key-value pair
person['occupation'] = 'Engineer'
print('Occupation:', person['occupation'])

# Iterate through keys and values
for key, value in person.items():
    print(f'{key}: {value}')

# Dictionaries are useful for mapping and lookups
scores = {
    'math': 95,
    'science': 88,
    'history': 76
}
print('Math score:', scores.get('math'))
print('Biology score (default):', scores.get('biology', 'not available'))

d = {10:100,20:200,30:300}
sum = 0
for key in d:
    sum += d[key]

print('Sum of values:', sum)

    

