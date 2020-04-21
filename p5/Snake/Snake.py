import p5
from SnakeClass import *

global Snake,scl
Snake=Snake()
scl=20

def setup():

    p5.size(600,600)


def draw():
    p5.background(51)
    Snake.update(scl)
    Snake.show(scl)


def key_pressed():
    if key=="UP":
        Snake.vel=p5.Vector(0,-1)
    elif key=="DOWN":
        Snake.vel=p5.Vector(0,1)
    elif key=="LEFT":
        Snake.vel=p5.Vector(-1,0)
    elif key=="RIGHT":
        Snake.vel=p5.Vector(1,0)

p5.run(frame_rate=20)