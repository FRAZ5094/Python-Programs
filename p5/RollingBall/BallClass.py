import p5

class Ball:

    def __init__(self,x,y,r):
        self.pos=p5.Vector(x,y)
        self.r=r
        self.d=r*2

    def show(self):
        p5.circle((self.pos.x,self.pos.y),self.d)


