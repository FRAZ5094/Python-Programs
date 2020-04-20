import numpy as np 
import matplotlib.pyplot as plt
filename="SampleData.csv"
x,y,y2= np.loadtxt(filename, delimiter=",", unpack=True,skiprows=1)
#Var1,Var2=np.loadtxt(filename, delimiter=",", unpack=True,max_rows=1,dtype=str)

plt.plot(x,y,label="2x")
plt.plot(x,y2,label="3x")
#plt.plot(x,y3,label="4x")
#plt.xlabel(Var1)
#plt.ylabel(Var2)
#plt.title("{0} vs {1}".format(Var1,Var2))
plt.legend()
plt.show()