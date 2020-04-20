import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
%matplotlib inline
def func(x, a, b, c):
    return a * np.exp(-b * x)
x = np.linspace(0,100,1000)
y = 0.0073*np.exp(0.0174*x)
plt.figure(1)
plt.plot(x, y, 'b-',label='data')
plt.legend()
popt, pcov = curve_fit(func, x, y)
print("m={:g},c={:g}".format(popt[0],popt[1]))
plt.figure(2)
plt.plot(x, func(x, *popt), 'r-',label="fit: m={}, c={}".format(popt[0],popt[1]))
plt.legend()
plt.grid()
plt.show()