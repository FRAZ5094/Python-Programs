import p5
from random import randint

def setup():
    p5.size(400,400)
    p5.background(0)

def draw():

    p5.translate(width/2,height/2)

    #v=p5.Vector(randint(-100,100),randint(-100,100))
    v=p5.Vector.random_2D() #random unit vector in 2d
    v*=100
    p5.stroke_weight(4)
    p5.stroke(255,50)
    p5.line((0,0),(v.x,v.y))


p5.run()