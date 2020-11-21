import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def mymodel(x,t):
    #x[1]=omega
    #x[0]=theta
    #print(x,"x in model")
    dx1dt=x[1]
    dx2dt=16-61*x[1]-210*x[0]

    #print(dx1dt,"dx1")
    #print(dx2dt,"dx2")

    dxdt=np.array([dx1dt,dx2dt])
    return dxdt

def euler_int(xdot,h,x):
    #print(x,"x in euler int")
    return x+h*xdot

def calculate_response(model_name,x_init,time_array):
    x=x_init
    start_t=time_array[0]
    end_t=time_array[-1]
    delta_t=time_array[1]-time_array[0]
    for t in np.arange(t_start+delta_t,t_end+delta_t,delta_t):
        dxdt=model_name(x[-1],t)
        euler_resp=euler_int(dxdt,delta_t,x[-1])
        x=np.append(x,[euler_resp],axis=0)
    return x

t_start=0
t_end=2
t_delta=0.001

t=np.arange(t_start,t_end+t_delta,t_delta)

x_init=np.array([[0,21]])


response=odeint(mymodel,x_init[0],t)
theta=response[:,0]
omega=response[:,1]

x = calculate_response(mymodel,x_init,t)
custom_theta=[]

for array in x:
    custom_theta.append(array[0])






answer_theta = 0.076*(1+4.079*np.exp(-3.66*t)-5.079*np.exp(-57.337*t))

#plt.subplot(211)
plt.plot(t,theta,label="ode int")
#plt.subplot(212)
plt.plot(t,custom_theta,label="custom int")
print(f"peak theta = {max(theta)}")
print(f"peak t = {t[np.where(theta==max(theta))][0]}")
print(f"steady state theta = {theta[-1]}")
#plt.legend()

error=[]

for i in range(1,len(t)):
    error.append(((abs(theta[i]-custom_theta[i]))/custom_theta[i])*100)

avg_error=sum(error)/len(error)

print(avg_error)
