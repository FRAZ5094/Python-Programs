import numpy as np


y=np.array([])
y=np.array([0.0274,0.0379,0.0586,0.0821,0.1126,0.1590,0.1920,0.2557])

x=np.array([0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])

if len(y)!=len(x):
    print("len of values is incorrect")

def trapezoidal_integration(x,y):
    """takes list x and y and returns the integral of y with respect to x according to the Trapezium Rule"""
    result={"total":0,"values":[]}
    
    for i in range(len(x)-1):
        value=(y[i]+y[i+1])*(x[i+1]-x[i])
        result["total"]+=value
        result["values"].append(value)

    result["total"]/=2
    return result


result=trapezoidal_integration(x,y)



print(result["total"])
print(result["values"])