import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from time import perf_counter

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

def custom_model(x,t):
    k=1000
    c=200
    m=100

    dx1dt=x[1]
    dx2dt=(1/m)*(-c*x[1]-k*x[0])

    dxdt=np.array([dx1dt,dx2dt])
    return dxdt

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
t_end=4
t_delta=0.01

t=np.arange(t_start,t_end+t_delta,t_delta)

x_init=np.array([[0,21]])


#response=odeint(mymodel,x_init[0],t)
#theta=response[:,0]
#omega=response[:,1]

start=perf_counter()
x = calculate_response(mymodel,RK4,x_init,t)
end=perf_counter()

custom_theta=[]

for array in x:
    custom_theta.append(array[0])

good_delta_t=0.001
good_t=np.arange(t_start,t_end+good_delta_t,good_delta_t)

answer_theta = 0.076*(1+4.079*np.exp(-3.66*good_t)-5.079*np.exp(-57.337*good_t))

plt.subplot(211)
plt.title("actual result")
plt.plot(good_t,answer_theta,label="actual answer")
plt.subplot(212)
plt.title("simulation")
plt.plot(t,custom_theta,label="simulation")
plt.legend()
plt.tight_layout()
plt.show()

print(f"simulation took {round(end-start,3)} seconds")
print(f"peak theta = {round(max(answer_theta),3)}")
print(f"peak t = {round(good_t[np.where(answer_theta==max(answer_theta))[0][0]],3)}")
print(f"steady state theta = {round(answer_theta[-1],3)}")



error=[]

for i in range(1,len(t)):
    if good_t[i] in t:
        where=np.where(t==good_t[i])[0]
        if len(where)>1:
            print("duplicate values")
        else:
            where=where[0]
            error.append(((abs(answer_theta[i]-custom_theta[where]))/abs(answer_theta[i]))*100)

avg_error=sum(error)/len(error)

print(f"Error from actual answer = {round(avg_error,3)}%")
