import p5


def setup():
    p5.size(400,400)


def draw():
    p5.background(0)
    pos=p5.Vector(200,200)
    mouse=p5.Vector(mouse_x,mouse_y)
    v=mouse-pos
    #m=abs(v)
    v=v.normalize()*100
    p5.translate(width/2,height/2)
    p5.stroke_weight(4)
    p5.stroke(255)
    p5.line((0,0),(v.x,v.y))
    #print(m)
p5.run()