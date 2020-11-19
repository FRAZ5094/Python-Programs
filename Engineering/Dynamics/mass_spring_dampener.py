import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def mysystem(x,t):
    #x[1]=omega
    #x[0]=theta
    
    dx1dt=x[1]
    dx2dt=23-20*x[1]-90*x[0]

    dxdt=[dx1dt,dx2dt]
    return dxdt

t_start=0
t_end=2
t_delta=0.00001

t=np.arange(t_start,t_end+t_delta,t_delta)

x_init=[0,14]

response=odeint(mysystem,x_init,t)

theta=response[:,0]
omega=response[:,1]

#scott_theta=(7/6)+(1/12)*np.exp(-3*t)-(5/4)*np.exp(-t)

plt.plot(t,theta)
#plt.plot(t,scott_theta)
#plt.ylim(0,1)

    