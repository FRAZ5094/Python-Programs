from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
#%matplotlib qt
plt.gca(projection="3d")
t=np.linspace(0,4*np.pi,100)
x=t*np.sin(t)
y=t*np.cos(t)
z=2*t
plt.plot(x,y,z)
plt.show()