# Dictionaries store data in key-value pairs. Think of them like a real dictionary where you look up a word (key) to find its definition (value).

# Empty dictionary
my_dict = {}

# Dictionary with data
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print(person.get("name"))

person["age"] = 28
print(person.get("age"))

person["email"] = "alice@gmail.com"
print(person)

person.clear()

person = {"name": "Alice", "age": 30, "city": "New York"}

# Get all keys, values, or items
print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Alice', 30, 'New York'])
print(person.items())   # dict_items([('name', 'Alice'), ...])

# Check if key exists
if "name" in person:
    print("Name found!")

# Update multiple values
person.update({"age": 31, "job": "Engineer"})

# Dictionary of dictionaries
students = {
    "alice": {"age": 20, "grade": "A"},
    "bob": {"age": 21, "grade": "B"},
    "charlie": {"age": 19, "grade": "A"}
}

# Access nested data
print(students["bob"]["age"])

obj = {
    "name":"Virat",
    "age":34
}

# print(obj["age"])

print(obj.get("age","Age not found"))

