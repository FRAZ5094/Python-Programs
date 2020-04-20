class Car():
    Names=[]
    Makes=[]
    Models=[]
    Count = 0
    def __init__(self,make,model,variablename):
        self.make = make
        self.model = model
        self.tank_cap = 100
        self.tank = 0
        self.name = variablename
        Car.Names.append(variablename)
        Car.Makes.append(make)
        Car.Models.append(model)
        Car.Count+=1
        self.index=Car.Count-1
    def fillup(self):
        self.tank = self.tank_cap
        print(self.name +" is now full")
    def emptytank(self):
        self.tank= 0
        print(self.name +"is now empty")
    def remove(self):
        Car.Names.pop(self.index)
        Car.Makes.pop(self.index)
        Car.Models.pop(self.index)
        Car.Count-=1
        print(self.name +" has been removed")
        del self.make, self.model, self.tank_cap,self.tank,self.name



mycar=Car("VW","Up","mycar")
ScottsCar=Car("Suzuki","Swift","ScottsCar")