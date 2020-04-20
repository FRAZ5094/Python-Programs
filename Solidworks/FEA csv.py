import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import glob 
#%matplotlib qt
csvFiles=glob.glob("*.csv")
plt.gca(projection='3d')
n=1
for filename in csvFiles:
    CSVData=np.genfromtxt(filename,delimiter=",",dtype=str,skip_header=8)
    CSVFileInfo=np.genfromtxt(filename,delimiter=",",dtype=str,skip_header=1,max_rows=4)
    X=CSVData[:,2].astype(float)
    Z=CSVData[:,1].astype(float)
    Y=CSVData[:,4].astype(float)
    plt.figure(n)
    plt.plot(X,Y,-Z,c="b")
    n+=1
    plt.grid()
    plt.show()