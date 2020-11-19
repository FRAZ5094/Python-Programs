import numpy as np
import matplotlib.pyplot as plt
from math import factorial
#%matplotlib qt

x_array=np.linspace(0,6*np.pi,1000)

actual_sin=np.sin(x_array)

approx_sin=[]
order=10

for x in x_array:
    sum=0
    for n in range(order):
        sum+=((-1)**n)*((x**((2*n)+1))/(factorial((2*n+1))))
    approx_sin.append(sum)
    


#print(x_array)
plt.plot(x_array,actual_sin)
plt.plot(x_array,approx_sin)
plt.show()