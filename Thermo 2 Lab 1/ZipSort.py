import numpy as np
import matplotlib.pyplot as plt
from random import seed, randint
x=[]
def sortSecond(val):
    return val[1]
for i in range(10):
    x.append(randint(0,10))
x=np.asarray(x)
y=x**2
plt.plot(x,y)
sortedxy=list(zip(x,y))
sortedxy.sort(reverse = False)
#sortedxy.sort(key=sortSecond)
plt.plot(*zip(*sortedxy))
print(sortedxy[0])
plt.show()
