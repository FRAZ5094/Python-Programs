from p5 import *
from CollisionsClasses import Block

global count
count=0



def setup():
    global timestep,placesofPI
    placesofPI=5
    timestep=100000
    size(600,200)
    global block1,block2
    block1=Block(100,20,1,0)
    block2=Block(200,150,100**placesofPI,-5/timestep)

def draw():
    global block1,block2,count,timestep,placesofPI
    background(200)

    for _ in range(timestep):
        if block1.collide(block2):
            v1=block1.bounce(block2)
            v2=block2.bounce(block1)
            block1.v=v1
            block2.v=v2
            count+=1
            print("Pi approximation:{}".format(count/10**placesofPI))

        if block1.hitWall():
            block1.reverse()
            count+=1
            print("Pi approximation:{}".format(count/10**placesofPI))
        block1.update()
        block2.update()

        
    block1.show()
    block2.show()

run()
