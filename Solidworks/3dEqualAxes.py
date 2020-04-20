from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
%matplotlib qt
fig = plt.figure()
ax = fig.gca(projection='3d')
filename="Cantilever-Static 1-Results-Displacement1-2.csv"
#filename="BikeFrame-FEA Default Config-Results-Displacement1-1.csv"

CSVData=np.genfromtxt(filename,delimiter=",",dtype=str,skip_header=8)
CSVFileInfo=np.genfromtxt(filename,delimiter=",",dtype=str,skip_header=1,max_rows=4)
X=CSVData[:,2].astype(float)
Z=-1*CSVData[:,1].astype(float)
Y=CSVData[:,4].astype(float)

scat = ax.scatter(X, Y, Z)

# Create cubic bounding box to simulate equal aspect ratio
max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max()
Xb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.5*(X.max()+X.min())
Yb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.5*(Y.max()+Y.min())
Zb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.5*(Z.max()+Z.min())
# Comment or uncomment following both lines to test the fake bounding box:
for xb, yb, zb in zip(Xb, Yb, Zb):
   ax.plot([xb], [yb], [zb], 'w')

plt.grid()
plt.show()