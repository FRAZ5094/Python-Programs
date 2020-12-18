import numpy as np

V_max=np.array([75.83,74.83,73.83,72.83,73.33,73])

rho=1.225
s=12
C_D0=0.0255
P=85000
k=0.045
w=12000

for v in V_max:
    value=(1/2)*rho*((v)**4)*s*C_D0+((k*(w**2))/((1/2)*rho*s)) - P*v
    print(value)
