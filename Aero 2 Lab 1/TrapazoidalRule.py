import numpy as np
import matplotlib.pyplot as plt
lengthofdata=100
k=5
x=np.linspace(0,100,lengthofdata)
n=lengthofdata
y=k*x
plt.plot(x,y)
plt.show()
height=max(x)*k
ActualArea=(1/2)*max(x)*height
print(ActualArea)
#TrapSum=(2*sum(y[1:-1]))+y[0]+y[-1]
TrapSum=0
for i in range(n):
    if i==0 or i==n:
        TrapSum+=y[i]
    else:
        TrapSum+=2*y[i]
Deltax=(max(x)-min(x))/(n)
TrapArea=(Deltax/2)*TrapSum
print(TrapArea)
print(Deltax)