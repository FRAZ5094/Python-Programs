import p5
from random import randint
global cols,rows,scl,w,h,counter
counter=0
scl=20
w=600
h=600
cols=int(w/scl)
rows=int(h/scl)


def setup():
    p5.size(600,600)




def draw():
    p5.background(0)
    p5.stroke(255)
    p5.no_fill()
    p5.translate(width/2,height/2)
    p5.rotate_x(3.41459/3)
    p5.translate(-w/2,-h/2)
    for y in range(rows):
        p5.begin_shape("TRIANGLE_STRIP")
        for x in range(cols):
            p5.vertex(x*scl,y*scl,randint(-100,100))
            p5.vertex(x*scl,(y+1)*scl,randint(-100,100))
        p5.end_shape()


p5.run(mode="P3D")
