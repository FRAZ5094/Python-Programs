import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display
x = np.linspace(0, 100, 1000)
print(len(x))
print(x[-1])
#displayed in seperate window
#%matplotlib qt 
#default, displayed in interactive window
%matplotlib inline 
plt.plot(x, x*2,label="2x")
plt.plot(x, x*3,label="3x")
plt.plot(x, x*4,label="4x")
plt.title("Graph title:")
plt.legend()
plt.show()