class vical :
    def __init__(self ,brand,speed):
        self.brand = brand
        self.speed = speed

    def show(self):
        print("brand name:",self.brand)
        print("speed:",self.speed)


class car(vical):
    def __init__(self,brand,speed,fuels_type):
        super().__init__(brand,speed)
        self.fuels_type=fuels_type

    def display(self):
        self.show()
        print("fuels types:",self.fuels_type)
brand=input("enter car brand:")
speed =input("enter car speed km/h:")
fuels_type =input("enter car fuels type:")

obj=car(brand,speed,fuels_type)
obj.display()

