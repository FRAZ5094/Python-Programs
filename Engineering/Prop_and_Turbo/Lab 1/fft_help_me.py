from scipy.fft import fft
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib qt

if 'data148' not in locals():
    data148=pd.read_csv("testhigh.dat",sep="\t",header=None)
    data148=data148.T
    data148=data148.drop(columns=[1])
    data148.columns=["microphone signal","square wave","time"]

voltage=np.array(data148["microphone signal"])

pressure=voltage/0.0495

N = 40000

T = 1/N

yf = fft(pressure)
xf = np.linspace(0.0, 1/(2*T), N//2)

plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]),linewidth=1)

estimate=1646
number_of_lines=int(xf[-1]/estimate)

for i in range(1,number_of_lines+1):
        #plt.plot([i*estimate,i*estimate],[0,100],'r--',alpha=0.3)
        pass
#plt.grid()
plt.ylim(0,5)
plt.xlim(0,20000)
plt.title("Fourier Transform of microphone signal")
plt.xlabel("frequency (Hz)")
plt.ylabel("|Pressure (Pa)|")
plt.tight_layout()
plt.show()
plt.grid()
plt.savefig("2388083M_Fourier")