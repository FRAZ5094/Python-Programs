import p5

showGrid=True
gridW=320
gridH=320
gridScl=16
gridOffsetX=16
gridOffsetY=16
strokeWeight=1


def setup():
    p5.size(16*40,16*40)

def draw():
    p5.background(0)
    p5.stroke(255)
    p5.stroke_weight(strokeWeight)
    if showGrid:
        for x in range(int(gridW/gridScl)+1):
            x+=gridOffsetX/gridScl
            p5.line((x*gridScl,gridOffsetY),(x*gridScl,gridOffsetY+gridH))

        for y in range(int(gridH/gridScl)+1):
            y+=gridOffsetY/gridScl
            p5.line((gridOffsetX,y*gridScl),(gridOffsetX+gridW,y*gridScl))
            
    #print(strokeWeight)





def key_pressed():
    global strokeWeight
    if key=="]":
        if showGrid:
            showGrid=False
        else:
            showGrid=True
    if key=="UP":
        strokeWeight+=0.1

    if key=="DOWN":
        strokeWeight-=0.1