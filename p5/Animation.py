from p5 import *
import numpy as np


global x
x=0

def setup():
    size(500,500)


def draw():
    global x
    scale(1,-1)
    translate(0,-height)
    x+=1
    y=1/2*x
    stroke(0)
    point(x,y)




run()
 

