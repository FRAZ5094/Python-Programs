import p5
from BallClass import *

def setup():
    global smallBall,bigBall
    p5.size(500,500)
    bigBall=Ball(width/2,height,150,[0,0])
    smallBall=Ball(width/2,height-500,10,[0,0])

def draw():
    global smallBall,bigBall
    p5.background(0)
    smallBall.collision(bigBall)
    smallBall.updatePos(bigBall)

    smallBall.show()
    bigBall.show()
    p5.stroke(255,0,0)
    p5.line((smallBall.pos),(bigBall.pos))
    p5.stroke(255)

p5.run()