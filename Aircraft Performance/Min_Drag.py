import numpy as np
import matplotlib.pyplot as plt 

C_D_0=0.0251
C_L=1.41
rho=1.225
S=13.46
A=10.12
e=0.7566
W=15123
P_engine=228000
propulsive_efficency=0.85
k=1/(np.pi*A*e)

V_max=100
#V_min=10
V_max=((2*P_engine*propulsive_efficency)/(rho*S*C_D_0))**(1/3)
V_min=np.sqrt((2*W)/(rho*C_L*S))
n=1000
step=(V_max-V_min)/n

V=np.array(np.arange(V_min,V_max+step,step))



p_drag=(C_D_0*1/2)*(rho)*(V**2)*S
i_drag=[]
for velocity in V:
    C_L_current=W/((1/2)*rho*(velocity**2)*S)
    i_drag.append((k*C_L_current**2)*(1/2)*(rho)*(velocity**2)*S)

t_drag=i_drag+p_drag

V_md=np.sqrt((2*W)/(rho*S))*(k/C_D_0)**(1/4)
C_L_at_V_md=W/((1/2)*rho*(V_md**2)*S)

"""
p_drag_at_V_md=(C_D_0*1/2)*(rho)*(V_md**2)*S
i_drag_at_V_md=(k*C_L_at_V_md**2)*(1/2)*(rho)*(V_md**2)*S

D_at_V_md=i_drag_at_V_md+p_drag_at_V_md
"""

C_D_at_V_md=C_D_0+k*C_L_at_V_md**2
D_at_V_md=(C_D_at_V_md)*((1/2)*(rho)*(V_md**2)*S)



plt.plot(V,t_drag,label="total drag")
plt.plot(V,p_drag,label="profile drag",linestyle="--")
plt.plot(V,i_drag,label="induced drag",linestyle="--")
plt.plot(V_md,D_at_V_md,"ro",markersize=5)
plt.axvline(x=V_min, ymin=0, ymax=10000,color="red")
plt.axvline(x=V_max, ymin=0, ymax=10000,color="red")
#plt.ylim(0,2000)
plt.legend()
plt.show()

plt.plot(V,t_drag*V,label="total power")
plt.plot(V,p_drag*V,label="profile power",linestyle="--")
plt.plot(V,i_drag*V,label="induced power",linestyle="--")
plt.axvline(x=V_min, ymin=0, ymax=10000,color="red")
plt.axvline(x=V_max, ymin=0, ymax=10000,color="red")
#plt.ylim(0,200000)
plt.legend()
plt.show()