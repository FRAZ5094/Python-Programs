import numpy as np


y=np.array([])
y=np.array([-0.0142,-0.0126,-0.0081,-0.0011,0.0070,0.0017,0.0153,0])

x=np.array([0.376,0.472,0.568,0.664,0.760,0.856,0.952,1])

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