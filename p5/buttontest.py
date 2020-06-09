import p5 
from pynput import keyboard
global up,down,left,right,newKey
newKey="none"
up=False
down=False
left=False
right=False


def on_release(Key):
    global newKey,up,down,right,left
    print(str(Key))
    if str(Key)=="Key."+ str(newKey).lower():
        print("bruh")
        up=False
        down=False
        left=False
        right=False





listener = keyboard.Listener(on_release=on_release)
listener.start()


def setup():
    pass

def draw():
    global up,down,left,right

    if up:
        print("up",frame_count)
    if down:
        print("down",frame_count)
    if left:
        print("left",frame_count)
    if right:
        print("right",frame_count)
    
        

def key_pressed():
    global up,down,right,left,newKey,lastKey
    up=False
    down=False
    left=False
    right=False
    newKey=key
    if newKey=="UP":
        up=True
    if newKey=="DOWN":
        down=True
    if newKey=="LEFT":
        left=True
    if newKey=="RIGHT":
        right=True



       



p5.run(frame_rate=60)