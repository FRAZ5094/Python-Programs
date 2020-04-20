import numpy as np
import matplotlib.pyplot as plt

#Get all Values from CSV
FraserData="AeroLabExperiment1.csv"
JamieData="JamieAeroLabDataExp1.csv"
ScottData="ScottAeroLabDataExp1.csv"
Data=np.genfromtxt(ScottData,delimiter=",",dtype=str,filling_values="_")
AoA=Data[2:11,0].astype(float)
PositiveManometer=Data[2:11,1:11].astype(float)*0.001
NegativeManometer=Data[13:22,1:11].astype(float)*0.001
Velocity=Data[0,3].astype(float)
PositiveStaticPressure=Data[0,5].astype(float)*0.001
NegativeStaticPressure=Data[12,5].astype(float)*0.001
AngleofManometer=Data[0,7].astype(float)*(np.pi/180)
ChordLength=Data[0,9].astype(float)*0.01
x=np.array([0,0.003,0.005,0.008,0.014,0.021,0.028,0.035,0.042,0.05])

#If Static pressure needs to be taken away from the pressure
#PositiveManometer-=PositiveStaticPressure
#NegativeManometer-=NegativeStaticPressure

#Initial Calculations
PositivePressure=np.around(PositiveManometer*1000*9.81*np.sin(AngleofManometer),decimals=2)
NegativePressure=np.around(NegativeManometer*1000*9.81*np.sin(AngleofManometer),decimals=2)
ChordRatio=x/ChordLength



#Plot AoA graphs
for i in range(9):
    plt.figure(i)
    plt.title("Angle of Attack={:g}°".format(AoA[i]))
    plt.plot(PositivePressure[i,:],label="Upper",marker="^")
    plt.plot(NegativePressure[i,:],label="Lower",marker="D")
    plt.xlabel("x/c")
    plt.ylabel("ΔP (Pa)")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig("Graphs/Angle of Attack={:g} graph.png".format(AoA[i]))
    plt.show()


#Trapazoidal Rule for Area under pressure graph
n=len(ChordRatio)
NormalForce=[]
for AoAIndex in range(len(AoA)):
    UpperSum=0
    LowerSum=0
    for i in range(n-1):
        if i==0 or i==n:
            UpperSum+=PositivePressure[AoAIndex,i]
            LowerSum+=NegativePressure[AoAIndex,i]
        else:
            UpperSum+=2*PositivePressure[AoAIndex,i]
            LowerSum+=2*NegativePressure[AoAIndex,i]
    Deltax=(ChordRatio[-1]-ChordRatio[0])/(n)
    UpperArea=(Deltax/2)*UpperSum
    LowerArea=(Deltax/2)*LowerSum
    DeltaArea=UpperArea-LowerArea
    NormalForce.append(DeltaArea)

#Plot Normal Force 
plt.figure(9)
plt.grid()
plt.plot(AoA,NormalForce,label="Normal Force")
plt.xlabel("Angle of Attack (°)")
plt.ylabel("Normal Force (N)")
plt.title("Normal Force against Angle of Attack")
#plt.text(3,0,"fuck\nshit",fontsize=100,alpha=0.4)
plt.legend()
plt.tight_layout()
plt.savefig("Graphs/Normal Force against Angle of Attack.png")
plt.show()


#Calculate Lift Force
Lift=NormalForce*np.cos((AoA*(np.pi/180)))

#Plot Lift 
plt.figure(10)
plt.grid()
plt.plot(AoA,Lift,label="Lift Force")
plt.xlabel("Angle of Attack (°)")
plt.ylabel("Lift Force (N)")
plt.title("Lift Force against Angle of Attack")
plt.text(9.5,72,"Max Lift Force=\n{:.1f}N at {}°".format(max(Lift),float(AoA[np.where(Lift == max(Lift))])),fontsize=9,horizontalalignment='center')
#plt.text(11.5,56,"Max Lift Force=\n{:.2f}N at {}°".format(max(Lift),float(AoA[np.where(Lift == max(Lift))])),fontsize=9,horizontalalignment='center')
plt.plot(float(AoA[np.where(Lift == max(Lift))]),max(Lift),"r",marker="x",markersize=10)
plt.legend()
plt.tight_layout()
plt.savefig("Graphs/Lift Force against Angle of Attack.png")


#Calculate Drag Force
Drag=NormalForce*np.sin((AoA*(np.pi/180)))

#Plot Drag
plt.figure(11)
plt.grid()
plt.plot(AoA,Drag,label="Drag Force")
plt.xlabel("Angle of Attack (°)")
plt.ylabel("Drag Force (N)")
plt.title("Drag force against Angle of Attack")
plt.legend()
plt.tight_layout()
plt.savefig("Graphs/Drag Force against Angle of Attack.png")

#Save Positive and negative Pressure values to CSV
#Format Positive Pressure
OutputPositivePressure=np.c_[AoA,PositivePressure]
OutputPositivePressure=np.append([Data[1]],OutputPositivePressure,axis=0)
BlankSpace=np.array([[" "]*(len(OutputPositivePressure[0])-1)])
PositiveTitle=np.append(np.array(["Positive"]),BlankSpace)
OutputPositivePressure=np.append([PositiveTitle],OutputPositivePressure,axis=0)

#Format Negative Pressure
OutputNegativePressure=np.c_[AoA*-1,NegativePressure]
OutputNegativePressure=np.append([Data[1]],OutputNegativePressure,axis=0)
NegativeTitle=np.append(np.array(["Negative"]),BlankSpace)
OutputNegativePressure=np.append([NegativeTitle],OutputNegativePressure,axis=0)

#Combine Negative and Positive Pressure
CSVOutput=np.append(OutputPositivePressure,OutputNegativePressure,axis=0)

#Outut CSV
np.savetxt("PressureGraphsPa.csv",CSVOutput,delimiter=",",fmt="%s")


