import p5
from PlanetClass import Planet

global G
G=100000

def setup():
    global LeftPlanet,RightPlanet
    p5.scale(1,-1)
    p5.size(1500,700)
    p5.translate(0,-height)

    LeftPlanet=Planet(0,height/2,1,[10,0],25,trail=1)
    LeftPlanet.pos.x+=LeftPlanet.r
    RightPlanet=Planet(width,height/2,1,[-10,0],25,trail=1)
    RightPlanet.pos.x-=RightPlanet.r

def draw():
    global LeftPlanet,RightPlanet
    p5.scale(1,-1)
    p5.translate(0,-height)

    if not LeftPlanet.finished and not RightPlanet.finished:
        LeftPlanet.collide(RightPlanet)
        p5.stroke(255,0,0)
        LeftPlanet.update(RightPlanet,G)
        p5.stroke(0,0,255)

        RightPlanet.update(LeftPlanet,G)
        


        p5.background(0)
        
    p5.stroke(255,0,0)
    p5.fill(255,0,0)
    LeftPlanet.show()
    p5.stroke(0,0,255)
    p5.fill(0,0,255)
    RightPlanet.show()
    
p5.run(frame_rate=240)