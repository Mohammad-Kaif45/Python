class Mother:
    def cooking(self):
        print("I love cooking")

class Father:
    def gardening(self):
        print("I enjoy gardening")


class Child(Father,Mother): 
    def sports(self):
        print("I like to play cricket")


child = Child()

child.sports()
child.cooking()
child.gardening()
