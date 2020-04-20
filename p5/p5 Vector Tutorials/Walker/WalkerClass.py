import p5

class Walker:
    def __init__(self,x,y):
        self.pos=p5.Vector(x,y)
        #self.vel=p5.Vector(1,-1)
        self.vel=p5.Vector.random_2D()

    def update(self):
        self.pos+=self.vel

    def show(self):
        p5.stroke(255)
        p5.stroke_weight(2)
        p5.fill(255,100)
        p5.circle((self.pos.x,self.pos.y),32)


