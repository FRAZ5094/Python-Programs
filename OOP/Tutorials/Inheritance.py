class Dog(object):

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def speak(self):
        print("Hi I am", self.name, "and I am",self.age,"years old")

    def talk(self):
        print("Bark!")




class Cat(Dog): #dont have to remake class if similar to dog
#cat is inheriting from dog
# therefore dog is Parent class
# and cat is child class   

    def __init__(self,name,age,colour):
        super().__init__(name,age) #brings the code over from __init__ of dog
        #super class is Dog
        self.colour=colour
        self.name="Tech" #overridden from Dog
    def talk(self): #talk function is overridden from Dog to be for the cat object
        print("Meow!")

jim=Dog("jim",70)
tim=Cat("Tim",5,"Blue")
tim.talk()
jim.talk()