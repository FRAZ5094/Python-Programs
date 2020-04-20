import matplotlib.pyplot as plt 
import numpy as np 
#%matplotlib qt
x=np.linspace(0,6*np.pi,100)
plt.figure(1)
plt.plot(x,x*2,label="2x")
plt.xlabel("x")
plt.ylabel("2x")
plt.legend()
plt.figure(2)
plt.plot(x,x*3,label="3x")
plt.xlabel("x")
plt.ylabel("3x")
plt.legend()
plt.show()
#k=input("press close to exit") 