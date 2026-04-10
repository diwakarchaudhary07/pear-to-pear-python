class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):   # Inheritance
    def _init_(self, name, age, roll_no):
        super()._init_(name, age)   # Parent constructor call
        self.roll_no = roll_no

    def display(self):
        self.show()
        print("Roll No:", self.roll_no)


# Object
s1 = Student("Ashish", 20, 101)
s1.display()