import p5
from WalkerClass import Walker

def setup():
    global walker
    p5.size(400,400)
    walker=Walker(width/2,height/2)

def draw():
    p5.background(0)
    global walker
    walker.update()
    walker.show()

p5.run()
 
