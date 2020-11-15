import numpy as np
import matplotlib.pyplot as plt

s=0
n=1
numbers=[]
for i in range(1,101):
    s+=n*(i**2)
    numbers.append((i,s))
    print(n*(i**2))
    n*=-1