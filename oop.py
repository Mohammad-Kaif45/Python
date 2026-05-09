class Human:
    def __init__(self,n,o):
        self.name = n
        self.occupation = o

    def do_work(self):
        if(self.occupation == "cricket player"):
            print(self.name, "plays cricket")
        elif self.occupation == "actor":
            print(self.name,"shhots a film")

    def speak(self):
        print(self.name, "how are you")

    def personality(self):
        if(self.occupation == "actor"):
            print(self.name," is a professional actor who play a role in various film")
        elif self.occupation == "cricket player":
            print(self.name, " is a skill full cricket player")

obj1 = Human("Rohit Sharma","cricket player")
obj1.do_work()
obj1.speak()

obj2 = Human("Salman Khan","actor")
obj2.do_work()
obj2.speak()
obj2.personality()