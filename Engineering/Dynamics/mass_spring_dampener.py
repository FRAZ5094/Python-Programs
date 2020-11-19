import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def fraserq2(x,t):
    #x[1]=omega
    #x[0]=theta
    
    dx1dt=x[1]
    dx2dt=16-61*x[1]-210*x[0]

    dxdt=[dx1dt,dx2dt]
    return dxdt

def scottq2(x,t):
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

x_init=[0,21]

response=odeint(fraserq2,x_init,t)

theta=response[:,0]
omega=response[:,1]

A=0.05827243987
B=36.03012628
fraserq1_theta=A*np.exp(-12.3*t)*np.sin(B*t)

scottq1_theta=(0.95/np.sqrt(20.56))*np.exp(-0.8*t)*np.sin(np.sqrt(20.56)*t)
plt.plot(t,theta,label="simulation")
#plt.plot(t,fraserq1_theta,label="answer")
plt.legend()
#plt.ylim(0,1)

    