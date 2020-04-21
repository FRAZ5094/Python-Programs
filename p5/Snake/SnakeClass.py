import p5

class Snake:

    def __init__(self):
        self.pos=p5.Vector(0,0)
        self.vel=p5.Vector(1,0)

    def update(self,scl):
        self.pos+=self.vel*scl
        self.pos.x=p5.constrain(self.pos.x,0,width-scl)
        self.pos.y=p5.constrain(self.pos.y,0,height-scl)
    def show(self,scl):
        p5.fill(255)
        p5.square((self.pos.x,self.pos.y),scl)

