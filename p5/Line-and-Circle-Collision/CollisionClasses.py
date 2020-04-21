import p5 

class Ball:

    def __init__(self,x,y,r):
        self.pos=p5.Vector(0,0)
        self.r=r
    
    def show(self):
        p5.stroke(255)
        p5.no_fill()
        p5.circle((self.pos.x,self.pos.y),self.r*2)

    def followMouse(self):
        self.pos=p5.Vector(mouse_x,mouse_y)

    def drawProjectionLine(self,line):
        posfromLine=self.pos-line.p1
        multiplier=(posfromLine.dot(line.Vector))/(abs(line.Vector)**2)
        proj=line.Vector*multiplier
        p5.stroke(255,0,0)
        p5.line((line.p1),(line.p1+proj))       

        




class Line:

    def __init__(self,p1,p2):
        self.p1=p5.Vector(p1[0],p1[0])
        self.p2=p5.Vector(p2[0],p2[1])
        self.Vector=p5.Vector(p2[0]-p1[0],p2[1]-p1[1])

    def show(self):
        p5.stroke(255)
        p5.line(self.p1,self.p2)
