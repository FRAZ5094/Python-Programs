import numpy as np
import matplotlib.pyplot as plt
filename="AeroLabExperiment2.csv"

Data=np.genfromtxt(filename,delimiter=",",dtype=str,filling_values="_")
FanSpeed=Data[2:5,0].astype(float)
SmoothTunnelVelocity1=Data[2:5,1].astype(float)
SmoothTunnelVeloctiy2=Data[8:11,1].astype(float)
SmoothDrag1=Data[2:5,2].astype(float)
SmoothDrag2=Data[8:11,2].astype(float)
GolfTunnelVelocity1=Data[2:5,3].astype(float)
GolfTunnelVelocity2=Data[8:11,3].astype(float)
GolfDrag1=Data[2:5,4].astype(float)
GolfDrag2=Data[8:11,4].astype(float)

plt.figure(1)
plt.plot(SmoothTunnelVelocity1,SmoothDrag1,label="Smooth Sphere")
plt.plot(GolfTunnelVelocity1,GolfDrag1,label="Golf ball")
plt.xlabel("Tunnel Velocity (m/s)")
plt.ylabel("Drag (N)")
plt.xlim(left=0)
plt.minorticks_on()
plt.grid(which="both")
plt.legend()
plt.tight_layout()
plt.savefig("Graphs/Drag against velocity.png")
plt.show()