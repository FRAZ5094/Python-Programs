import numpy as np


L=np.array([[2/np.sqrt(5),0,1/np.sqrt(5)],[0,1,0],[-1/np.sqrt(5),0,2/np.sqrt(5)]])
sigma=np.array([[77,0,0],[0,31,0],[0,0,-46]])

print("L\n\n",L)
print("\nsigma\n\n",sigma)
print("\nL_T\n\n",np.transpose(L))

print("\nsigma dash\n\n")

print(sigma*np.transpose(L))