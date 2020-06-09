import p5
import threading
import time


first=True

def wait():
    print("started waiting")
    time.sleep(5)
    print("still waiting")
    time.sleep(5)


def setup():
    p5.size(600,600)


def draw():
    global first
    if first:
        first=False
        t=threading.Thread(target=wait)
        t.start()

    print(frame_count)

p5.run(frame_rate=10)