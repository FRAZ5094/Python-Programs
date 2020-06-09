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
        p5.stroke(255,0,0)
        p5.fill(255,0,0)

        if line.p1.x!=line.p2.x:
            #not a vertical line
            posfromLine=self.pos-line.p1
            multiplier=(posfromLine.dot(line.Vector))/(abs(line.Vector)**2)
            proj=line.Vector*multiplier
            closestPoint=proj+line.p1


            if closestPoint.x>line.p1.x and closestPoint.x<line.p2.x:
                p5.circle((closestPoint),10)
                p5.line((closestPoint),(self.pos))
            elif closestPoint.x<line.p1.x:
                p5.circle((line.p1),10)
                p5.line((line.p1),(self.pos))
            elif closestPoint.x>line.p2.x:
                p5.circle((line.p2),10)
                p5.line((line.p2),(self.pos))

        else:
            #a vertical line
            #print("Vertical")
            closestPoint=p5.Vector(line.p1.x,self.pos.y)

            if closestPoint.y>line.p1.y and closestPoint.y<line.p2.y:
                p5.circle((closestPoint),10)
                p5.line((closestPoint),(self.pos))
            elif closestPoint.y<line.p1.y:
                p5.circle((line.p1),10)
                p5.line((line.p1),(self.pos))
            elif closestPoint.y>line.p2.y:
                p5.circle((line.p2),10)
                p5.line((line.p2),(self.pos))






        




class Line:

    def __init__(self,p1,p2):

        if p1[0]<p2[0]:
            #p1 is the left most
            self.p1=p5.Vector(p1[0],p1[1])
            self.p2=p5.Vector(p2[0],p2[1])
            self.Vector=p5.Vector(p2[0]-p1[0],p2[1]-p1[1])
        elif p1[0]>p2[0]:
            #p2 is the left most
            #will swap the points so p1 is the left most
            self.p1=p5.Vector(p2[0],p2[1])
            self.p2=p5.Vector(p1[0],p1[1])
            self.Vector=p5.Vector(p1[0]-p2[0],p1[1]-p2[1])
        else:
            #if vertical p1 will always be the higher point
            if p1[1]<p2[1]:
                self.p1=p5.Vector(p1[0],p1[1])
                self.p2=p5.Vector(p2[0],p2[1])
                self.Vector=p5.Vector(p2[0]-p1[0],p2[1]-p1[1])

            elif p1[1]>p1[1]:
                self.p1=p5.Vector(p2[0],p2[1])
                self.p2=p5.Vector(p1[0],p1[1])
                self.Vector=p5.Vector(p1[0]-p2[0],p1[1]-p2[1])
            else:
                raise ValueError("Invalid Line")



    def show(self):
        p5.stroke(255)
        p5.line(self.p1,self.p2)
