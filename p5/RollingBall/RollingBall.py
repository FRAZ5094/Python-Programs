import p5
from BallClass import *

def setup():
    global smallBall,bigBall
    p5.size(500,500)
    bigBall=Ball(width/2,height/2,150,[0,0])
    smallBall=Ball(width/2,height/2-160,10,[0.01,0])

def draw():
    global smallBall,bigBall
    p5.background(0)
    smallBall.updatePos(bigBall)
    smallBall.collision(bigBall)


    smallBall.show()
    bigBall.show()
    p5.stroke(255,0,0)
    p5.line((smallBall.pos),(bigBall.pos))

p5.run(frame_rate=240)