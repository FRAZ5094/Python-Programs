import p5

class Ball:
    def __init__(self,x,y,d,veloctiyLoss,v,trail=False):
        self.pos=p5.Vector(x,y)
        self.vel=p5.Vector(v[0],v[1])
        self.d=d
        self.r=self.d/2
        self.gravity=p5.Vector(0,-2)
        self.veloctiyLoss=veloctiyLoss
        self.trail=trail
        self.ylist=[]
        self.xlist=[]
    
    def show(self):
        if self.trail:
            self.xlist.append(self.pos.x)
            self.ylist.append(self.pos.y)
            p5.stroke(255,255,30)
            numberfromlast=1000
            numberfromlast+=1
            for i in range(len(self.xlist[-numberfromlast:])):
                p5.point(self.xlist[-numberfromlast:][i],self.ylist[-numberfromlast:][i])
        p5.stroke(0)
        p5.circle((self.pos.x,self.pos.y),self.d,mode="CENTER")

    def update(self):
        self.vel+=self.gravity
        self.pos.x+=self.vel.x
        self.pos.y+=self.vel.y
    

    def hitOther(self,other):
        if self.pos.y-self.r<=other.pos.y+other.height and not(self.pos.x-self.r>=other.pos.y+other.width or self.pos.x-self.r<=other.pos.x):
            self.bounceOther(other)

    def hitWall(self):
        if self.pos.x-self.r<0 or self.pos.x+self.r>width:
            self.bounceWall()

    def hitCeiling(self):
        if self.pos.y+self.r>height:
            self.bounceCeiling()
    
    def bounceCeiling(self):
        self.pos.y=height-self.r-1
        self.vel.y*=-1*self.veloctiyLoss

    def bounceOther(self,other):
        self.pos.y=other.pos.y+other.height+self.r+1
        self.vel.y*=-1*self.veloctiyLoss

    def bounceWall(self):
        if self.pos.x-self.r<0:
            self.pos.x=self.r+1
        else:
            self.pos.x=width-self.r-1

        self.vel.x*=-1*self.veloctiyLoss


class Floor:
    def __init__(self,x,y,w,h):
        self.pos=p5.Vector(x,y)
        self.width=w
        self.height=h
        
    def show(self):
        p5.rect((self.pos.x,self.pos.y),self.width,self.height)