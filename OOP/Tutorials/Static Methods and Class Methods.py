class Dog:
    dogs=[]

    def __init__(self,name):
        self.name=name
        self.dogs.append(self)


    # @ symbol means its at a decorator

    @classmethod #can be called using the name of the class
    def num_dogs(cls): #cls is name of the class
        return len(cls.dogs) #use when you need the name of the class
        #dont need to pass an object of that class

    @staticmethod #use for when you want to use a function but orginize in a class
    def bark(n): #dont need parameters
        """Barks n times"""
        for _ in range(n):
            print("Bark!")


tim=Dog("Tim")
fred= Dog("Fred")

print(Dog.dogs) #called using the class not the an instantce of dog
#means you dont have to have an instance of dog to use

print(Dog.num_dogs())

Dog.bark(5)