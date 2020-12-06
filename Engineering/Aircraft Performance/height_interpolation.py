import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

h=[0,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000,13000,14000,15000]
rho=[1.255,1.1117,1.0065,0.9091,0.8191,0.7361,0.6597,0.5895,0.5252,0.4663,0.4127,0.3639,0.3108,0.2665,0.2268,0.1937]

def func(x, a, b,c):
    #print(a,"a")
    #print(b,"b")
    #print(c,"c")
    return a * x**2 + b*x + c


popt, pcov = curve_fit(func, h, rho)

h_new=np.linspace(min(h),max(h),10000)

rho_new=func(h_new,*popt)

bruh_rho=(popt[0]*(h_new**2))+(popt[1]*h_new)+popt[2]



idk_rho=(2.865*10**-9*(h_new**2))-(1.121*10**-4*h_new)+1.225

plt.plot(h_new,idk_rho,label="guessed")
#plt.plot(h_new,bruh_rho,label="actual")
plt.title(f"h={popt[0]:.2e}x^2 + {popt[1]:.2e}x + {popt[2]:.2e}")
plt.legend()