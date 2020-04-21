import p5

global counter
counter=0

def setup():
    p5.size(600,600)

def draw():
    global counter
    counter+=0.01
    p5.background(0)
    p5.fill(0,255,0)
    p5.stroke(0)
    #p5.rotate_x(counter)
    p5.rotate_y(counter)
    #p5.sphere(300)
    p5.box(300,300,300)
    #print(counter)

p5.run(mode="P3D",frame_rate=240)