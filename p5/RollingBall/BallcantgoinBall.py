import p5
import numpy as np
from BallClass import *
def setup():
    global smallBall,bigBall
    p5.size(500,500)
    bigBall=Ball(width/2,height/2,200,[0,0])
    smallBall=Ball(width/2,250,20,[0,0])

def draw():
    global smallBall,bigBall
    p5.background(0)
    MousePos=p5.Vector(mouse_x,mouse_y)
    smallBall.pos=MousePos
    smallBall.collision(bigBall)
    smallBall.show()
    bigBall.show()
    p5.stroke(255,0,0)
    p5.line((smallBall.pos),(bigBall.pos))
    p5.line(())
    p5.stroke(255)
    print(np.rad2deg(smallBall.relativePos(bigBall).angle_between(p5.Vector(0,1))))
p5.run()