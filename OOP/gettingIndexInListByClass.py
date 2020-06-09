
class bruh():
    
    def __repr__(self):
        return "bruh map"


class bruh2():

    def __repr__(self):
        return "bruh2 map"
Maps=[]
Maps.append(bruh())
Maps.append(bruh2())

for i,obj in enumerate(Maps):
    if obj.__class__==bruh2:
        print("class at {}".format(i))

