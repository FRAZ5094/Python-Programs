import numpy as np
max=int(input("Enter max value: "))
min=int(input("Enter min value: "))
inc=int(input("Enter increment: "))
max+=inc
array=np.array(range(min,max,inc))
print(array)