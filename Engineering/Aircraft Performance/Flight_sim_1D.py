import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from time import perf_counter


global m,S,C_D,C_L,g,D,A,C_T,V

V=50

W=15123
g=9.81
m=15123/g
#rho=1.225

C_L=1.41

D=2
C_T=0.1
A=np.pi*(D/2)**2
n=500


S=13.46
b=11.67
e=0.75666
Aspect_ratio=((11.67)**2)/(S)
k=1/(Aspect_ratio*e*np.pi)
C_D0=0.0251
C_D=C_D0+k*((C_L)**2)

def plane_model(s,t):
    global m,S,C_D,C_L,g,D,A,C_T,V

    #print(s)
    rho=(2.865*10**-9*s[0]**2)-(1.121*10**-4*s[0])+1.225
    #print(rho)

    mdot=rho*s[1]*A
    #J=(s[1])/(n*D)

    #b=-1+np.sqrt(1+((8*C_T)/(np.pi*J**2)))

    sdot=np.array([0,0])

    #sdot[0]=s[1]
    #sdot[1]=((mdot*b)/(m))*s[1]-((rho*S*C_D)/(2*m))*(s[1])**2
    sdot[0]=s[1]
    sdot[1]=((rho*S*C_L)/(2*m))*(V**2)-g

    return sdot

def euler_int(model_name,xdot,h,x):
    #print(x,"x in euler int")
    return x+h*xdot

def RK2(model_name,xdot,h,x):

    k1=h*model_name(x,0)
    k2=h*model_name(x+k1,0)

    return x+((k1+k2)/2)

def RK4(model_name,xdot,h,x):
    k1=h*model_name(x,0)
    k2=h*model_name(x+k1/2,0)
    k3=h*model_name(x+k2/2,0)
    k4=h*model_name(x+k3,0)

    return x+((k1+2*k2+2*k3+k4)/6)

def calculate_response(model_name,integration,x_init,time_array):
    x=x_init
    start_t=time_array[0]
    end_t=time_array[-1]
    delta_t=time_array[1]-time_array[0]
    for t in np.arange(t_start+delta_t,t_end+delta_t,delta_t):
        dxdt=model_name(x[-1],t)
        resp=integration(model_name,dxdt,delta_t,x[-1])
        x=np.append(x,[resp],axis=0)
    return x


t_start=0
t_delta=0.1
t_end=500


t=np.arange(t_start,t_end+t_delta,t_delta)


s_init=np.array([[4000,0]])

start=perf_counter()
results = calculate_response(plane_model,RK4,s_init,t)
end=perf_counter()

x=[]
dx_dt=[]
z=[]
dz_dt=[]

for array in results:
    z.append(array[0])
    dz_dt.append(array[1])

plt.subplot(211)
plt.plot(t,z)
plt.subplot(212)
plt.plot(t,dz_dt)
