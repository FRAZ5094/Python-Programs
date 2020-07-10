import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
import random
%matplotlib qt

plt.style.use("fivethirtyeight")

x_vals=[]
y_vals=[]
i=0

def animate(i):
    i+=1
    x_vals.append(i)
    y_vals.append(random.randint(0,100))
    plt.cla()
    plt.plot(x_vals,y_vals)
    if len(x_vals)>50:
        x_vals.pop(0)
        y_vals.pop(0)

ani=FuncAnimation(plt.gcf(),animate,interval=1)

plt.tight_layout()
plt.show()