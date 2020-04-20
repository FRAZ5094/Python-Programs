import p5
from MoverClass import Mover

def setup():
    global mover
    p5.size(1000,1000)
    mover=Mover(width/2,height/2)

def draw():
    p5.background(0)
    global mover
    mover.update()
    mover.show()

p5.run()
 
