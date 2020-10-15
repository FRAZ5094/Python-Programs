import matplotlib.pyplot as plt 
import numpy as np

beta=np.linspace(0,5,1000)
zeta_list=[1,0.5,0.375,0.25,0.15,0.1,0.05]
for zeta in zeta_list:
    TR=(np.sqrt(1+(2*zeta*beta)**2))/(np.sqrt((1-beta**2)**(2)+(2*zeta*beta)**2))
    plt.plot(beta,TR,label=str(zeta))
plt.legend()
plt.ylim(0,3.5)
plt.show()