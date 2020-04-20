import p5 
from PlanetClass import Planet


def setup():
    global PlanetLeft,PlanetRight
    p5.size(500,500)
    PlanetLeft=Planet(width/2-100,height/2,1,[1,1],10,trail=1)
    PlanetRight=Planet(width/2+100,height/2,1,[-1,1],10,trail=1)

def draw():
    global PlanetLeft,PlanetRight
    p5.background(150)
    if not PlanetLeft.finished:
        PlanetLeft.collide(PlanetRight)
        PlanetLeft.update(PlanetRight,10)
        PlanetRight.update(PlanetLeft,10)
    PlanetLeft.show()
    PlanetLeft.drawTrails()
    PlanetRight.show()
    PlanetRight.drawTrails()
p5.run()