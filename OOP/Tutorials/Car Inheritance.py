class Vehicle():
    def __init__(self,price,gas,colour):
        self.price=price
        self.gas=gas
        self.colour=colour

    def fillUpTank(self):
        self.gas=100

    def emptyTank(self):
        self.gas=0

    def gasLeft(self):
        return self.gas

class Car(Vehicle):
    def __init__(self,price,gas,colour,speed):
        super().__init__(self,price,gas,colour)
        self.speed=speed
    
    def beep(self):
        print("Beep beep!")


class Truck(Vehicle):
    def __init__(self,price,gas,colour,tires):
        super().__init__(self,price,gas,tires)
        self.tires=tires
    
    def beep(self):
        print("Honk Honk!")
