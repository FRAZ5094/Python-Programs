import p5
from SnakeClasses import *
from random import randint
import numpy as np

global Snake,scl
scl=20
Snake=Snake(scl)

def setup():
    global Food,scl
    p5.size(600,600)
    Food=Food(scl)


def draw():
    global Food
    p5.background(51)
    Snake.update()
    Snake.show()
    Food.show()
    Snake.eat(Food)




def key_pressed():
    global Food
    if key=="UP":
        Snake.vel=p5.Vector(0,-1)
    elif key=="DOWN":
        Snake.vel=p5.Vector(0,1)
    elif key=="LEFT":
        Snake.vel=p5.Vector(-1,0)
    elif key=="RIGHT":
        Snake.vel=p5.Vector(1,0)
    elif key=="ENTER":
        Food.pickLocation()
    else:
        print(key)

p5.run(frame_rate=10)