import multiprocessing
import threading
from maps import *
import time

screenScale=5
scl=16*screenScale



def createMap(Class,q):
    q.put(Class(screenScale,scl))
    
def updateMapList():
    while True:
        Maps.append(q.get())

if __name__ == '__main__':
    Maps=[LittlerootTrainerTop(screenScale,scl)]
    MapClasses=[LittlerootTrainerBot,LittlerootOutside]
    q=multiprocessing.Queue()
    for Class in MapClasses:
        p=multiprocessing.Process(target=createMap,args=(Class,q))
        p.start()

    t=threading.Thread(target=updateMapList)
    t.start()
