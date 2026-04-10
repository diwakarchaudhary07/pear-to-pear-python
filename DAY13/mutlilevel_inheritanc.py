# Father (Parent) class
class Father:
    def show(self):
        print("This is father class")

# Child class 1
class Child1(Father):
    def display1(self):
        print("This is child1 class")

# Child class 2
class Child2(Father):
    def display2(self):
        print("This is child2 class")

# Objects
c1 = Child1()
c2 = Child2()

# Accessing methods
c1.show()       # from Father
c1.display1()   # from Child1

c2.show()       # from Father
c2.display2()   # from Child2