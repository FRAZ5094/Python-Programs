import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
Fraser="LB10.csv"
Test="ThermoLabDataNotMine.csv"
Scott="LB04_07022020.csv"
Data=np.genfromtxt(Scott,delimiter=",",dtype=str,skip_header=3,filling_values="_")
DataValues=Data[3::,:]
Time=DataValues[:,0].astype(str)
Speed=DataValues[:,1].astype(float)
Thrust=DataValues[:,2].astype(float)
Throttle=DataValues[:,3].astype(float)
AirVolumeFlow=DataValues[:,4].astype(float)
AirMassFlow=DataValues[:,5].astype(float)
AirDensity=DataValues[:,6].astype(float)
FuelVolumeFlow=DataValues[:,7].astype(float)
FuelMassFlow=DataValues[:,8].astype(float)/1000
FuelDensity=DataValues[:,9].astype(float)
BarometricPressure=DataValues[:,10].astype(float)
OrificeDelta=DataValues[:,11].astype(float)
PsCompIn=DataValues[:,12].astype(float)
PsDiffIn=DataValues[:,13].astype(float)
PsDiffOut=DataValues[:,14].astype(float)
PtDiffOut=DataValues[:,15].astype(float)
PtNozzleIn=DataValues[:,16].astype(float)
PtExhaust=DataValues[:,17].astype(float)
TempAir=DataValues[:,18].astype(float)
TempFuel=DataValues[:,19].astype(float)
TempCompIn=DataValues[:,20].astype(float)
TempDiffIn=DataValues[:,21].astype(float)
TempDiffOut=DataValues[:,22].astype(float)
TempNozzleIn=DataValues[:,23].astype(float)
TempTurbineOut=DataValues[:,24].astype(float)
TempExhaust=DataValues[:,25].astype(float)
def sortSecond(val):
    return val[1]
plt.figure(1)
plt.scatter(Throttle,Thrust,marker="s",label="Thrust",s=4)
def Linearfunc(x,m,c):
    return m*x+c
Linearconstants, pcov=curve_fit(Linearfunc, Throttle, Thrust)
plt.plot(np.linspace(min(Throttle),max(Throttle),len(Throttle)), Linearfunc(np.linspace(min(Throttle),max(Throttle),len(Throttle)), *Linearconstants), 'r-',linestyle="--",dashes=(5, 3),label="Best Fit line: y={:.3f}x+{:.3f}".format(*Linearconstants))
plt.legend()
plt.ylabel("Thrust(N)")
plt.xlabel("Throttle (%)")
plt.tight_layout()
plt.savefig('Thrust against Throttle.png')

plt.figure(2)
ThrottleFuelMassFlowSort=list(zip(Throttle,FuelMassFlow))
ThrottleFuelMassFlowSort.sort(reverse = False)
plt.plot(*zip(*ThrottleFuelMassFlowSort),marker="s",label="Fuel mass flow rate",markersize=4)
#plt.plot(Throttle,FuelMassFlow,marker="s",label="Data",markersize=4)
def Quadfunc(x, a, b):
    return a*x**2+b
Quadconstants, pcov=curve_fit(Quadfunc, Throttle, FuelMassFlow)
plt.plot(np.linspace(min(Throttle),max(Throttle),len(Throttle)), Quadfunc(np.linspace(min(Throttle),max(Throttle),len(Throttle)), *Quadconstants), 'r-',linestyle="--",dashes=(5, 3),label="Best Fit line: y={:.2e}x^2+{:.2e}".format(Quadconstants[0],Quadconstants[1]))
plt.xlim(0,100)
plt.legend()
plt.ylabel("Fuel mass flow rate (kg/s)")
plt.xlabel("Throttle (%)")
plt.tight_layout()
plt.savefig('Fuel mass flow rate against Throttle')


plt.figure(3)
TSFC=(Quadconstants[0]*Throttle**2+Quadconstants[1])/(Linearconstants[0]*Throttle+Linearconstants[1])
ThrottleTSCFSort=list(zip(Throttle,TSFC))
ThrottleTSCFSort.sort(reverse = False)
plt.plot(*zip(*ThrottleTSCFSort),marker="s",label="TSFC",markersize=4)
#plt.plot(Throttle,TSFC,marker="s",markersize=3,label="TSFC")
plt.text(30,0.0003,"Min value of TSFC=({},{:.2e})".format(float(Throttle[np.where(TSFC == min(TSFC))]),float(min(TSFC))))
plt.legend()
plt.plot(Throttle[np.where(TSFC == min(TSFC))],min(TSFC),"r",marker="x",markersize=10)
plt.ylabel("TSFC (kg/Ns)")
plt.xlabel("Throttle (%)")
plt.tight_layout()
plt.savefig('TSFC against Throttle.png')
plt.show()