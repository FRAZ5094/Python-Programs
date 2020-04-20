from p5 import *
import numpy as np
import time 
from PongClasses import Ball,PaddleLeft,PaddleRight

def setup():
    global ball,Player1,Player2,f
    size(1000,500)
    title("Pong Game")
    f=create_font("arial.ttf",64)
    text_font(f,64)
    Player1=PaddleRight(width,height/2,30,0.3,"Player 1")
    Player2=PaddleLeft(0,height/2,30,0.3,"Player 2")
    Player1.scoreUpdate()
    Player2.scoreUpdate()
    ball=Ball(width/2,height/2,25)
    ball.serve(25,PaddleLeft,PaddleRight)


def draw():
    rect((width/2,height/2),10,height,mode=CENTER)
    global ball,Player1,Player2
    background(0)
    ball.hitVert()
    ball.hitPaddleRight(Player1)
    ball.hitPaddleLeft(Player2)
    ball.hitWall(Player1,Player2)
    ball.update()
    Player1.show()
    Player2.show()
    Player1.scoreUpdate()
    Player2.scoreUpdate()
    if key_is_pressed:
        if key=="W":
            if not Player2.cantMoveUp():
                Player2.y-=20
        elif key=="S":
            if not Player2.cantMoveDown():
                Player2.y+=20
        elif key=="UP":
            if not Player1.cantMoveUp():
                Player1.y-=20
        elif key=="DOWN":
            if not Player1.cantMoveDown():
                Player1.y+=20

run(frame_rate=240)