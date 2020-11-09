import matplotlib.pyplot as plt 
import numpy as np

#constants
c=20


F_0=25
k=2500
m=1
omega_n=np.sqrt(k/m)

zeta=c/(2*m*omega_n)


omega_d=omega_n*np.sqrt(1-(zeta**2))



t=np.linspace(0,0.5,1000)

x=(F_0/k)*(1-np.exp(-zeta*omega_n*t)*(np.cos(omega_d*t)+(zeta/np.sqrt(1-(zeta)**2)*np.sin(omega_d*t))))
x*=100
tp=np.pi/omega_d


plt.plot(t,x)
plt.plot([tr,tr],[0,1.6],"--")
plt.ylim(0,1.6)
plt.xlim(0,0.5)
plt.xlabel("time (s)")
plt.ylabel("x (cm)")