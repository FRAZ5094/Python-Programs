import numpy as np
import matplotlib.pyplot as plt
#print("Pi to different dp's:\n1: {0:.1f}\n2: {0:.2f}\n3: {0:.3f}".format(np.pi))
print("Rouding value program")
#n=float(input("Enter the number to round:"))
n=np.pi
start=int(input("Enter the starting value of rounding:"))
end=int(input("Enter the ending value of rounding:"))
print("Value of {0} from {1} to {2} d.p.:".format(n,start,end))
end+=1
for i in range(start,end):
    print("{1} d.p. {0:.{1}f}".format(n,i))
k=input("press close to exit") 


