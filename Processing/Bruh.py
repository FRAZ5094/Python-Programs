global counter
counter=0

def setup():
    size(500,500,P3D)

    
def draw():
    global counter
    translate(width/2,height/2)
    background(0)
    rotateX(counter)
    rotateY(counter)
    box(50,50,50)
    counter+=0.01
    