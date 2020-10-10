import pandas as pd 
import numpy as np
from time import perf_counter

start=perf_counter()

V=30
V*=0.5144
D=0.6
T=250
J=0.25
n=102.7
omega=2*np.pi*n
c=5*10**-2
B=3
rho=1.225
alpha=3
C_L=0.7
L_to_D_ratio=22
solidity=(B*c)/(np.pi*D/2)

C_T=(T)/((rho)*(n**2)*(D**4))

a=(-1+np.sqrt(1+(8*C_T/np.pi*J**2)))/2

a=0.86

C_D=C_L/L_to_D_ratio

delta_x=0.1
starting_x=0.1
ending_x=1

data=pd.DataFrame({})

for x in np.arange(starting_x,ending_x+delta_x,delta_x):
    new_row={"x":round(x,2)}
    new_row["solidity"]=round(solidity,2)

    tan=(J*(1+a))/(np.pi*x)
    new_row["tan advance angle"]=round(tan,4)

    advance_angle=np.rad2deg(np.arctan(tan))
    new_row["advance angle"]=round(advance_angle,1)

    beta=advance_angle+alpha
    new_row["pitch angle"]=round(beta,1)
    new_row["coefficient of lift"]=C_L
    new_row["coefficient of drag"]=C_D

    C_T_D_X=(np.pi/8)*(solidity)*(J**2)*((1+a)**2)*((C_L*np.cos(np.deg2rad(advance_angle))-C_D*np.sin(np.deg2rad(advance_angle)))/((np.sin(np.deg2rad(advance_angle))**2)))
    new_row["thrust coefficient gradient"]=round(C_T_D_X,4)

    C_Q_D_X=(np.pi/16)*(solidity)*(J**2)*((1+a)**2)*x*((C_L*np.sin(np.deg2rad(advance_angle))+C_D*np.cos(np.deg2rad(advance_angle)))/((np.sin(np.deg2rad(advance_angle))**2)))
    new_row["torque coefficient gradient"]=round(C_Q_D_X,4)

    data=data.append(new_row,ignore_index=True)

data = data[["x","solidity","tan advance angle","advance angle","pitch angle","coefficient of lift","coefficient of drag","thrust coefficient gradient","torque coefficient gradient"]]

def trapezoidal_integration(x,y):
    """takes list x and y and returns the integral of y with respect to x according to the Trapezium Rule"""
    total=0
    for i in range(len(x)-1):
        total+=(y[i]+y[i+1])*(x[i+1]-x[i])
    return total/2

end=perf_counter()



Total_C_T=trapezoidal_integration(data["x"],data["thrust coefficient gradient"])
Total_C_Q=trapezoidal_integration(data["x"],data["torque coefficient gradient"])

display(data)

print(f"C_T={round(Total_C_T,3)}")
print(f"C_Q={round(Total_C_Q,3)}")

print(" ")
print(f"Calculated in: {round(end-start,3)} seconds")
    