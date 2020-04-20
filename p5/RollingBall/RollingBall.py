import p5
from BallClass import *
def setup():
    global Ball
    p5.size(500,500)
    Ball=Ball(width/2,50,50)

def draw():
    global Ball
    p5.scale(1,-1)
    p5.translate(0,-height)
    p5.background(0)
    Ball.show()
    p5.stroke(255)
    p5.line((width/2+10,height),(width/2+10,0))
    p5.line((width/2-10,height),(width/2-10,0))

p5.run()