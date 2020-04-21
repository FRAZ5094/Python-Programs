import p5
from CollisionClasses import *

global Lines
Lines=[]
Lines.append(Line((100,100),(200,400)))


def setup():
    global ball
    p5.size(600,600)
    ball=Ball(width/2,height/2,20)


def draw():
    global ball
    p5.background(0)
    ball.followMouse()
    ball.show()
    for i in range(len(Lines)):
        Lines[i].show()

    LinetoCircle=ball.pos-Lines[0].p1

    p5.line((Lines[0].p1),(Lines[0].p1+LinetoCircle))
    ball.drawProjectionLine(Lines[0])
p5.run()