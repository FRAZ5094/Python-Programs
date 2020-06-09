import p5
from CollisionClasses import *

global Lines
Lines=[]
Lines.append(Line((100,100),(200,300)))
Lines.append(Line((330,550),(580,50)))
Lines.append(Line((500,300),(600,100)))
Lines.append(Line((0,50),(600,50)))

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
        ball.drawProjectionLine(Lines[i])

    #p5.line((Lines[0].p1),(Lines[0].p1+LinetoCircle))

    #ball.drawProjectionLine(Lines[0])

p5.run()