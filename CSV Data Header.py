import numpy as np 
import matplotlib.pyplot as plt 
filename="SampleDataHeader.csv"
CSV=np.loadtxt(filename,delimiter=",",dtype=str)
XAxisName=CSV[0,0]
x=CSV[1:,0].astype(float)
for i in range(len(CSV[0])):
    y=CSV[1::,i].astype(float)
    LabelName=CSV[0,i]
    plt.plot(x,y,label=LabelName)
plt.xlabel(XAxisName)
plt.ylabel("y")
plt.title("Data from {}".format(filename))
plt.legend()
plt.show()

((()))