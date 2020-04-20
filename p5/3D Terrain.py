from p5 import *
import numpy as np
import time

def setup():
    size(640, 360)
    global counter
    counter=0


def draw():
    global counter
    background(0,255,0)
    rotate_x(counter)
    rotate_y(counter)
    stroke(255,0,0)
    circle((300,150),20)
    counter+=0.01

run(mode=P3D,frame_rate=60)
#mode="P3D"