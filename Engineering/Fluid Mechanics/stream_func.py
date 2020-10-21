import numpy as np
import matplotlib.pyplot as plt
%matplotlib qt

class stream_func():
    def __init__(self):
        self.data=np.array([[0,0]])
        self.deleted_first=False

    def append(self,values):
        self.data=np.concatenate((self.data,[[values[0],values[1]]]))
        if len(self.data)==2 and not self.deleted_first:
            self.data=self.data[1:]
            self.deleted_first=True

a=1
stream_functions=[]
theta_values=np.linspace(00.01,np.pi-0.001,100)
b_list=np.arange(1,5,0.1)
for b in b_list:
    stream=stream_func()
    for theta in theta_values:
        r=np.sqrt(((a**2)*(b**2)/(2)+(a**2*(np.cos(theta)))/(2))/((np.sin(theta)**2)))
        stream.append([r*np.cos(theta),r*np.sin(theta)])
        
    stream_functions.append(stream)

fig = plt.figure()
ax = fig.add_subplot(111)

for func in stream_functions:
    plt.plot(func.data[:,0],func.data[:,1],color="blue")
    plt.plot(func.data[:,0],-func.data[:,1],color="blue")

circle_x=[]
circle_y=[]

for i in np.linspace(0,np.pi*2,100):
    circle_x.append(a/2*np.cos(i))
    circle_y.append(a/2*np.sin(i))

plt.plot(circle_x,circle_y,color="red")

ax.set_aspect('equal')

plt.xlim(-a,a)
plt.ylim(-a,a)
plt.show()


