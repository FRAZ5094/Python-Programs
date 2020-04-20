import p5

class Planet:
    def __init__(self,x,y,m,v,d,trail=False):
        self.pos=p5.Vector(x,y)
        self.initpos=self.pos
        self.m=m
        self.d=d
        self.r=self.d/2
        self.vel=p5.Vector(v[0],v[1])
        self.initvel=self.vel
        self.trail=trail
        self.finished=False
        self.history=[]
        self.trailLength=100
        self.dontdoAgain=True

    def show(self):
        p5.circle((self.pos.x,self.pos.y),self.d,mode="CENTER")

    def relpos(self,other):
        return other.pos-self.pos

    def collide(self,other):
        if not self.finished:
            distance=abs(self.relpos(other))
            if distance<self.r+other.r:
                #print("Collide")
                self.finished=True
                other.finished=True
                print("finished")


    def update(self,other,Gravity):
        if not self.finished:
            pos=self.relpos(other)

            a_mag=(Gravity*other.m)/(abs(pos)**2)
            self.acc=pos.normalize()*a_mag
            self.vel+=self.acc

            if self.r<other.r:
                self.vel.limit(other.r*0.9)
            else:
                self.vel.limit(self.r*0.9)
        
            self.pos+=self.vel

    def drawTrails(self):
        if self.trail:
            if not self.finished:
                self.history.append(p5.Vector(self.pos.x,self.pos.y))
                if len(self.history)>self.trailLength:
                    self.history.pop(0)

            for i in range(len(self.history)):
                pos=self.history[i]
                p5.point(pos.x,pos.y)

    def toFinalDistance(self,other):
        pos=self.relpos(other)
        dist=abs(pos)
        newDist=abs(self.r-dist)
        pos=pos.normalize()*newDist
        return pos

