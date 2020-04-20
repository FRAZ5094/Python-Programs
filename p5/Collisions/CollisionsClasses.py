from p5 import *

class Block():
    def __init__(self,x,w,m,v):
        self.x=x
        self.y=height-w
        self.w=w
        self.v=v
        self.m=m

    def hitWall(self):
        return self.x<=0

    def reverse(self):
        self.v*=-1

    def update(self):
        self.x+=self.v

    def collide(self,other):
        if self.x+self.w<other.x or self.x>other.x+other.w:
            return False
        else:
            return True

    def bounce(self,other):
        sumM=self.m+other.m
        newV=(self.m-other.m)/sumM * self.v
        newV+= ((2*other.m)/sumM)*other.v
        return newV

    def show(self):
        rect((self.x,self.y),self.w,self.w)
