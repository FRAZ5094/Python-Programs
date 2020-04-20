import p5
from BouncingBallClasses import Ball,Floor
def setup():
    global ball,ground
    p5.size(500,500)
    ball=Ball(width/2,height/2,25,1,[1,0],trail=1)
    ground=Floor(0,0,width,20)
def draw():
    global ball,ground
    p5.stroke(255)
    p5.scale(1,-1)
    p5.translate(0,-height)
    p5.background(0)


   
    ball.hitOther(ground)
    ball.hitWall()
    ball.hitCeiling()
    ball.update()
    ball.show()
   


    ground.show()

    p5.rect((0,0),2,height) #left
    p5.rect((width-2,0),2,height) #right
    p5.rect((0,height-2),width,2) #top

    #p5.stroke(255)
    #p5.line((0,ball.pos.y),(width,ball.pos.y))
    #p5.line((0,height/2),(width,height/2))

p5.run(frame_rate=240)