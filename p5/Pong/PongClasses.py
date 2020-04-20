from p5 import *
import numpy as np
import random 

class Ball:
    def __init__(self,x,y,r):
        self.x=x
        self.initx=x
        self.y=y
        self.inity=y
        self.r=r
        self.paused=False

    def serve(self,servespeed,PaddleLeft,PaddleRight):
        self.x=self.initx
        self.y=self.inity
        self.servespeed=servespeed
        vx=random.randint(servespeed/5,servespeed)
        vy=np.sqrt(servespeed**2-vx**2)
        mult=[-1,1] 
        vy*=mult[random.randint(0,1)]
        vx*=mult[random.randint(0,1)]
        self.v=np.array([vx,vy])


    def show(self):
        circle((self.x,self.y),self.r,mode=CENTER)

    def update(self):
        if not self.paused:
            self.x+=self.v[0]
            self.y+=self.v[1]
            self.show()

    def hitWall(self,PaddleRight,PaddleLeft):
        if self.x+self.r>=width:
            PaddleRight.score+=1
            #print("Paddle Left scored")
            self.serve(self.servespeed,PaddleLeft,PaddleRight)
        elif self.x-self.r<=0:
            PaddleLeft.score+=1
            #print("Paddle Right scored")
            self.serve(self.servespeed,PaddleLeft,PaddleRight)

    def reverse_x(self):
        self.v[0]*=-1

    def reverse_y(self):
        self.v[1]*=-1
  


    def hitPaddleRight(self,PaddleRight):
        if self.x+self.r>=PaddleRight.x-PaddleRight.width and not PaddleRight.MissedBall(self):
            self.reverse_x()
            self.v*=1.1


    def hitPaddleLeft(self,PaddleLeft):
        if self.x-self.r<=PaddleLeft.x+PaddleLeft.width and not PaddleLeft.MissedBall(self):
            self.reverse_x()
            self.v*=1.1

    def hitVert(self):
        if self.y-self.r<=0 or self.y+self.r>=height:
            self.reverse_y()

class PaddleLeft:
    def __init__(self,x,y,w,fract,name):
        self.x=x
        self.initx=x
        self.inity=y
        self.y=y
        self.width=w
        self.height=height*fract
        self.name=name
        self.score=0

    def show(self):
      rect((self.x+self.width/2,self.y),self.width,self.height,mode=CENTER)  

    def MissedBall(self,Ball):
        if Ball.y-Ball.r>=self.y+self.height/2 or Ball.y+Ball.r<=self.y-self.height/2:
            return True
        else:
            return False

    def scoreUpdate(self):
        text(str(self.score),(int(width*3/4),int(height/7)))


    def cantMoveUp(self):
        if self.y-self.height/2<0:
            return True
        else:
            return False

    def cantMoveDown(self):
        if self.y+self.height/2>height:
            return True
        else:
            return False


class PaddleRight(PaddleLeft):
    
    def show(self):
        rect((self.x-self.width/2,self.y),self.width,self.height,mode=CENTER)

    def scoreUpdate(self):
        text(str(self.score),(int(width/4),int(height/7)))