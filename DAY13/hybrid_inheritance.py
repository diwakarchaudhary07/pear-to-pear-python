class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

class C(A):
    def showC(self):
        print("Class C")

class D(B, C):   # Multiple inheritance
    def showD(self):
        print("Class D")

# Object
obj = D()

obj.showA()  # from A
obj.showB()  # from B
obj.showC()  # from C
obj.showD()  # from D