import p5
from PlanetClass import Planet
import numpy as np

global G
G=1000

def setup():
    global planet,moon
    p5.scale(1,-1)
    p5.size(1500,700)
    p5.translate(0,-height)
    planet=Planet(width/2,height/2,20,[0,0],500,trail=0)
    moon=Planet(width/2,planet.pos.y+planet.r+50,1,[0,0],10,trail=1)

    #0,1,2,5,7,7.5,7.7,7.8,7.82

    min_orbit_vx=np.sqrt(((G*planet.m)/(abs(moon.initpos.y-planet.initpos.y))))
    #moon.vel.x=min_orbit_vx

    print(min_orbit_vx)


def draw():

    global planet,moon

    p5.fill(255)
    if not moon.finished:
        p5.background(0)
        p5.scale(1,-1)
        p5.translate(0,-height)

        moon.collide(planet)
        
        moon.update(planet,G)

        #planet.update(moon,G)


        
        p5.no_fill()
        p5.stroke(255,60)
        #p5.circle((planet.pos.x,planet.pos.y),2*abs(moon.relpos(planet)))

    p5.fill(10, 173, 73)
    p5.stroke(0)
    planet.show()

    p5.fill(0,0,255)
    p5.stroke(0,0,255)
    moon.show()

p5.run(frame_rate=120)

