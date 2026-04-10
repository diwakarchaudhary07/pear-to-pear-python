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