import p5
from random import randint
import numpy as np
class Snake:

    def __init__(self,scl):
        self.pos=p5.Vector(0,0)
        self.vel=p5.Vector(1,0)
        self.scl=scl
        self.length=0
        self.tail=[]

    def update(self):

        for i in range(self.length-1):
            self.tail[i]=self.tail[i+1]
        self.tail[self.length-1]=p5.Vector(self.pos.x,self.pos.y)

        self.pos+=self.vel*self.scl
        self.pos.x=p5.constrain(self.pos.x,0,width-self.scl)
        self.pos.y=p5.constrain(self.pos.y,0,height-self.scl)


    def show(self):
        p5.fill(255)
        p5.square((self.pos.x,self.pos.y),self.scl)



    def eat(self,food):
        d=p5.dist((self.pos.x,self.pos.y),(food.pos.x,food.pos.y))
        if d<1:
            Snake.length+=1
            food.pickLocation()

class Food:
    
    def __init__(self,scl):
        self.scl=scl
        self.pickLocation()



    def pickLocation(self):
        cols=np.floor(width/self.scl)
        rows=np.floor(height/self.scl)
        print(cols,rows)
        self.pos=p5.Vector(randint(0,cols-1),(randint(0,rows-1)))

        self.pos*=self.scl
        print(self.pos)

    def show(self):
        p5.fill(255,0,100)
        p5.square((self.pos.x,self.pos.y),self.scl)
