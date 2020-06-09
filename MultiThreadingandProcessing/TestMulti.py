import multiprocessing
import threading
import time


class bruh:
    def __repr__(self):
        return "bruh"

class bruh2:
    def __repr__(self):
        return "bruh2"

def createMap(Class,q):
    q.put(Class())
    
def updateMapList():
    while True:
        Maps.append(q.get())


if __name__ == '__main__':
    #global q
    Maps=[]
    jobs=[]
    Classes=[bruh,bruh2]
    q=multiprocessing.Queue()
    for Class in Classes:
        p=multiprocessing.Process(target=createMap,args=(Class,q))
        p.start()

    t=threading.Thread(target=updateMapList)
    t.start()

    while True:
        print(Maps)
        time.sleep(0.1)
