<<<<<<< HEAD
class parent:
    def __init__(self):
        self.fuels_types = input("Enter Fuels Types:")
        self.speed = input("Enter speed km/h:")
        self.brand = input("Enter Your Brand : ")


class child(parent):
    def __init__(self):
        super().__init__() 

class child2(child):
    def __init__(self):
        super().__init__() 

        print( "\nbrand=",self.brand , "\nspeed=",self.speed, "\nfuels_types=",self.fuels_types)     


obj = child2()
=======
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

>>>>>>> 60c60354f4a25ee940b0ed1d72e84be261749312
