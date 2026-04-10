class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    # Area function
    def area(self):
        return self.length * self.breadth

    # Perimeter function
    def perimeter(self):
        return 2 * (self.length + self.breadth)


# Object create karna
r1 = Rectangle(10, 5)

# Output
print("Area:", r1.area())
print("Perimeter:", r1.perimeter())