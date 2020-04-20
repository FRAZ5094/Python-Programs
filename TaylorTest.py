import numpy as np 
import matplotlib.pyplot as plt
x=np.array(np.linspace(2,200,10))
y=x/3
plt.plot(x,y)
plt.plot(x,x)
plt.title("I have no idea about giving names")
plt.show()