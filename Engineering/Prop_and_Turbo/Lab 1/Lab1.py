import pandas as pd 
import matplotlib.pyplot as plt
from numpy.fft import fft,fftfreq,ifft
%matplotlib qt


data=pd.read_csv("testhigh.dat",sep="\t",header=None)
data=data.T
data=data.drop(columns=[1])
data.columns=["microphone signal","square wave","time"]

n=len(data)
freqs=fftfreq(n)
mask=freqs>0

fft_vals=fft(data["square wave"])

plt.plot(freqs,fft_vals)


"""
plt.plot(data["time"],data["square wave"])
plt.xlim(0,0.01)
"""
plt.show()

