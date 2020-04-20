import p5
import numpy as np

class Ball:

    def __init__(self,x,y,r,v):
        self.pos=p5.Vector(x,y)
        self.vel=p5.Vector(v[0],v[1])
        self.r=r
        self.gravity=p5.Vector(0,1)
        self.g=1


    def show(self):
        p5.circle((self.pos.x,self.pos.y),self.r*2)

    def relativePos(self,other):
        return other.pos-self.pos

    def updatePos(self,other):
        if self.touching:
            angle=self.relativePos(other).angle_between(p5.Vector(0,1))
            self.vel.y+=self.gravity.y*np.sin(angle)
 
        else:
            self.vel+=self.gravity
        self.pos+=self.vel

    def collision(self,other):
        rel=self.relativePos(other)
        mag=abs(rel)

        if mag<=self.r+other.r:
            self.touching=True
            distanceInside=other.r+self.r-mag
            rel.normalize()
            rel*=-1
            rel*=distanceInside
            self.pos+=rel
            print(rel)
            print("touching")
        else:
            self.touching=False
            print("not touching")