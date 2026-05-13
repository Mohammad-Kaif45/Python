# OOPS (Object-Oriented Programming System) is a
# programming paradigm based on the concept of "objects",
# which can contain data (attributes) and code (methods)

# Class : A class is like a blueprint or template for creating objects.
# There are 2 types of things inside class Attributes and Methods.

# Attributes - Variables defined inside the class are Attribute
# Methods - Functions defined inside a class are Methods.

class Animal:
    species = "dog" # Attributes

    def make_sound(self): # methods
        print("bark")

obj = Animal() # Obkect of Animal class
obj.make_sound()
print(obj.species) # accessing object

# class Factory:
#     def __init__(self,material,zips,pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets

#     def show(self):
#         print(f'Material: {self.material}')
#         print(f'Zips: {self.zips}')
#         print(f'Pockets: {self.pockets}')

# bag1 = Factory('leather', 2, 4)
# bag1.show()

# campus = Factory('canvas', 1, 2)
# campus.show()

class Add:
    def __init__(self,a,b):
        print(a + b)

obj = Add(2,3)

# Constructor
# A constructor is a method that runs automatically when we call a class and 
# this constructor function will target the objects location

class Student:
    last_name = "Ansari" # class attribute
    def __init__(self,name): 
        self.name = name # instance attribute

s = Student("Kaif") # creating an object with value.
print(s.name,s.last_name) # accessing the attributes.

# To target the objects location we use self keyword.

# Type of attributes:
# Class Attributes : A normal variable created inside a class is a class attribute.
# Instance attribute : A attribute created using an instance like self.name, self.age etc. It is known as instance attribute


# Inheritance

# Inheritance allows a class (child class) to inherit properties and
# behaviors (attributes and methods) from another class (parent class)
# Benefits of using inheritance is : 
# Code reusability
# Organized structur
# Easy to maintain and extend

class Parent:
    def speak(self):
        print("i can speak")

class Child(Parent):
    pass

c = Child()
c.speak()

# Constructor in Inheritance 

# Lets say you have created a parent class with a constructor
# function inside it and then this class is inherited by another class
# then the constructor function of parent class will work for the
# child class as well. 

class Parent:
    def __init__(self,name):
        self.name = name

class Child(Parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

    def display(self):
        print(f"My name is {self.name}, and I am {self.age} years old")

c = Child("Kaif",21)
c.display()

class Demo:
    def __init__(self):
        self.name = "Kaif"
        self._age = 21
        self.__salary = 50000

    def show(self):
        print("Inside the class : ")
        print("Public attribute : ",self.name)
        print("Protected attribute : ",self._age)
        print("Private attribute : ",self.__salary)

d = Demo()
d.show()