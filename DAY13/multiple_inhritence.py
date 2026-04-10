class father:
    def __init__(self, car ,home):
        self.car = car
        self.home = home

    def show(self):
        print("car name:",self.car)
        print("home prize :",self.home)

class mother:
    def __init__(self ,salary,saving):
        self.salary = salary
        self.saving = saving


    def show1(self):
        print("salary", self.salary)
        print("saving:",self.saving)

class child(father,mother):
    def __init__(self , car ,home ,salary,saving):
        father.__init__(self ,car,home)
        mother.__init__(self,salary,saving)

    def show2(self):
        self.show()
        self.show1()
        
obj = child("punch" ,"50L",50000,100000)
obj.show2()