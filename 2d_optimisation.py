import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from mpl_toolkits.mplot3d.axes3d import get_test_data
%matplotlib qt

def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))
a=2
x = np.linspace(-a, a, 30)
y = np.linspace(-a, a, 30)


X, Y, Z = get_test_data(0.05)
#Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap='viridis',edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');