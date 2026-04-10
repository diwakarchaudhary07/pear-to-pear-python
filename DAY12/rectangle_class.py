class length:
    def __init__(self, hight,widht):
        self.hight = hight
        self.widht = widht

    # Area function
    def area(self):
        return self.hight * self.widht

    # Perimeter function
    def perimeter(self):
        return 2 * (self.hight + self.widht)


# Object create karna
r1 = length(10, 5)

# Output
print("Area:", r1.area())
print("Perimeter:", r1.perimeter())