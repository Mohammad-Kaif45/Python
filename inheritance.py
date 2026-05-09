class vehicle:
    def general_usage(self):
        print("general usage : transportation")
    
class car(vehicle):
    def __init__(self):
        print("I am a car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print("specific use : commute to work, vacation with family")

class motorcycle(vehicle):
    def __init__(self):
        print("I am a bike")
        self.wheels = 2
        self.has_roof = False
    def specific_usage(self):
        print("Use to riding and racing")


obj1 = car()
obj1.general_usage()
obj1.specific_usage()

obj2 = motorcycle()
obj2.general_usage()
obj2.specific_usage()