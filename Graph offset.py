import numpy as np 
import matplotlib.pyplot as plt
start=int(input("Enter the starting value:"))
end=int(input("Enter the ending value"))
inc=int(input("Enter the increment"))
Title="Graph offset by {} to {}".format(start,end)
end+=inc
x=np.array(range(start,end,inc))
for i in range(start,end,inc):
    y=x+i
    plt.plot(x,y,label="+ {}".format(i))
plt.legend()
plt.title(Title)
plt.show()
