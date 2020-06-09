class Map:
    def __init__(self,w,h):
        self.width=w
        self.height=h

class Littleroot(Map):
    def __init__(self,w,h,d):
        super().__init__(w,h)
        self.depth=d
maps=[]

maps.append(Map(10,20))
maps.append(Littleroot(30,50,50))
